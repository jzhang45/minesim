import csv
import matplotlib.pyplot as plt
import numpy as np

datafile = '../results.csv'
rows_to_read = 400001
simulation_num = rows_to_read - 1
print "Processing..."
with open(datafile, 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    results = []
    first_row = True
    for row in data:
        if first_row is False:
            row = ','.join(row)
            row = row.rsplit(',')
            results.append([float(item) for item in row])
        else:
            first_row = False
    results = np.array(results)
    if simulation_num <= len(results):
        results_arr = results[:simulation_num]
    else:
        print "Number of rows to read is more than available rows in file."

total_output_avg = np.average(results_arr[:,0])
total_lost_output_avg = np.average(results_arr[:,1])
total_cost_avg = np.average(results_arr[:,2])
uptime_total_avg = np.average(results_arr[:,3])
uptime_avg_avg = np.average(results_arr[:,4])
faults_avg = np.average(results_arr[:,5])
faults_detected_avg = np.average(results_arr[:,6])
failures_avg = np.average(results_arr[:,7])
incidents_saf_avg = np.average(results_arr[:,8])
incidents_env_avg = np.average(results_arr[:,9])
        
with open(r'../results_avg.csv', 'wb') as csvfile:
    reswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    reswriter.writerow(['Revenue', 'Lost Revenue', 'Cost', 'Total Uptime', 'Average Uptime',
                        'Faults', 'Detected Faults', 'Failures', 'Safety Incidents', 'Environmental Incidents'])
    results_avg = [total_output_avg, total_lost_output_avg, total_cost_avg, uptime_total_avg, uptime_avg_avg,
                   faults_avg, faults_detected_avg, failures_avg, incidents_saf_avg, incidents_env_avg]
    reswriter.writerow(results_avg)

print "....................................."
print "Average operations total uptime for %d simulations: %.2f" %(simulation_num, uptime_total_avg)
print "Average operations average uptime for %d simulations: %.2f" %(simulation_num, uptime_avg_avg)
print "Average total fault events for %d simulations: %.2f" %(simulation_num, faults_avg)
print "Average total detected faults for %d simulations: %.2f" %(simulation_num, faults_detected_avg)
print "Average total failure events for %d simulations: %.2f" %(simulation_num, failures_avg)
print "Average total safety events for %d simulations: %.2f" %(simulation_num, incidents_saf_avg)
print "Average total environmental events for %d simulations: %.2f" %(simulation_num, incidents_env_avg)
print "Average total revenue of the operation for %d simulations: %.2f" %(simulation_num, total_output_avg)
print "Average total cost of the operation for %d simulations: %.2f" %(simulation_num, total_cost_avg)
print "Average total lost revenue of the operation for %d simulations: %.2f" %(simulation_num, total_lost_output_avg)
print "Average total net profit of the operation for %d simulations: %.2f" %(simulation_num, total_output_avg - total_cost_avg)


def hist_plot(data, x_label, file_name):
    plt.figure()
    plt.hist(data)
    plt.xlabel(x_label)
    plt.ylabel('Count')
    plt.tick_params(axis='both', size=15)
    plt.xticks(rotation=60)
    plt.tight_layout()
    plt.savefig('../'+file_name)


font = {'size': 20}
plt.rc('font', **font)

revenue_mils = results_arr[:, 0]/1000000.
hist_plot(revenue_mils, 'Revenue ($M)', 'fig1')

revenue_loss_mils = results_arr[:, 1]/1000000.
hist_plot(revenue_loss_mils, 'Revenue Loss ($M)', 'fig2')

cost_mils = results_arr[:, 2]/1000000.
hist_plot(cost_mils, 'Cost ($M)', 'fig3')

fig_info = [['Revenue', 'fig1'], ['Revenue Loss', 'fig2'], ['Cost', 'fig3'], ['Total uptime', 'fig4'],
            ['Average uptime', 'fig5'], ['Faults', 'fig6'], ['Detected faults', 'fig7'],
            ['Failures', 'fig8'], ['Safety incidents', 'fig9'], ['Environmental incidents', 'fig10']]

# number of items from fig_info list to skip
skip = 3
for i, item in enumerate(fig_info):
    if i >= skip:
        hist_plot(results_arr[:, i], *fig_info[i])

plt.show()