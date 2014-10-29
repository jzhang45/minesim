# All the cases for the simulation work PhD thesis

def asset_gen(number, name_base, output_rate, cost_rate, maint_t_gen, maint_cost_gen, insp_t_gen, insp_cost_gen, events, operator_dist, optime, cms=False):
    
    assets_data = []
    assets_schedule = {}
    for i in range(number):
        asset = {}
        asset['name'] = name_base + '-' + str(i+1)
        asset['output_rate'] = output_rate
        asset['cost_rate'] = cost_rate
        asset['maint_t_gen'] = maint_t_gen
        asset['maint_cost_gen'] = maint_cost_gen
        asset['insp_t_gen'] = insp_t_gen
        asset['insp_cost_gen'] = insp_cost_gen
        asset['events'] = events
        asset['operator'] = {}
        asset['operator']['name'] = 'operator' + '-' + str(i+1)
        asset['operator']['dist'] = operator_dist
        asset['cms'] = cms
        assets_data.append(asset)
        assets_schedule[asset['name']] = optime
    return assets_data, assets_schedule

class E:    
  
    cases = {}

asset_type_1 = {'number': 100, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 8.0, 'maint_cost_gen': 5000.0, 'insp_t_gen': 5.0, 'insp_cost_gen': 2000.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 10.25, 60000.0, "failure", 6., 50000.0),
                                    "strut": ("normalvariate(4380.0, 8760.0)", "uniform(1.0, 96.0)", 28.25, 8000.0, "failure", 24., 5000.0),
                                    "engine": ("uniform(8760.0, 17520.0)", "uniform(1.0, 72.0)", 100.25, 503000.0, "failure", 96., 500000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 28.25, 1005000.0, "incident", 24., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 16.25, 15000.0, "incident", 12., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "uniform(.1, 72.0)",
            'optime': 8760.0
            }

E.cases[1] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 20000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': False, 'inspect_staff_num': 10, 'maint_intervals': False,
                                         'maint_staff_num': 10, 'inspection_tools_qty': 12,'maintenance_tools_qty':12}, 
                      'results':{}  
                      }
E.cases[1]['assets_data'], E.cases[1]['assets_schedule'] = asset_gen(**asset_type_1)


asset_type_2 = {'number': 100, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 8.0, 'maint_cost_gen': 5000.0, 'insp_t_gen': 5.0, 'insp_cost_gen': 2000.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 10.25, 60000.0, "failure", 6., 50000.0),
                                    "strut": ("normalvariate(4380.0, 8760.0)", "uniform(1.0, 96.0)", 28.25, 8000.0, "failure", 24., 5000.0),
                                    "engine": ("uniform(8760.0, 17520.0)", "uniform(1.0, 72.0)", 100.25, 503000.0, "failure", 96., 500000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 28.25, 1005000.0, "incident", 24., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 16.25, 15000.0, "incident", 12., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "uniform(.1, 72.0)",
            'optime': 8760.0
            }

E.cases[2] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 20000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': 168., 'inspect_staff_num': 10, 'maint_intervals': False,
                                         'maint_staff_num': 10, 'inspection_tools_qty': 12,'maintenance_tools_qty':12}, 
                      'results':{}  
                      }
E.cases[2]['assets_data'], E.cases[2]['assets_schedule'] = asset_gen(**asset_type_2)

## case 3 is the same as the case 2, their difference is in the inspector and maintenance tech model hardcoded in the code and inspection time and costs


asset_type_3 = {'number': 100, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 8.0, 'maint_cost_gen': 5000.0, 'insp_t_gen': 0.5, 'insp_cost_gen': 50.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 10.25, 60000.0, "failure", 6., 50000.0),
                                    "strut": ("normalvariate(4380.0, 8760.0)", "uniform(1.0, 96.0)", 28.25, 8000.0, "failure", 24., 5000.0),
                                    "engine": ("uniform(8760.0, 17520.0)", "uniform(1.0, 72.0)", 100.25, 503000.0, "failure", 96., 500000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 28.25, 1005000.0, "incident", 24., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 16.25, 15000.0, "incident", 12., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "uniform(.1, 72.0)",
            'optime': 8760.0
            }

E.cases[3] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 20000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': 168., 'inspect_staff_num': 10, 'maint_intervals': False,
                                         'maint_staff_num': 10, 'inspection_tools_qty': 12,'maintenance_tools_qty':12}, 
                      'results':{}  
                      }
E.cases[3]['assets_data'], E.cases[3]['assets_schedule'] = asset_gen(**asset_type_3)


asset_type_4 = {'number': 100, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 8.0, 'maint_cost_gen': 5000.0, 'insp_t_gen': 0.5, 'insp_cost_gen': 50.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 10., 60000.0, "failure", 6., 50000.0),
                                    "strut": ("normalvariate(4380.0, 8760.0)", "uniform(1.0, 96.0)", 28., 8000.0, "failure", 24., 5000.0),
                                    "engine": ("uniform(8760.0, 17520.0)", "uniform(1.0, 72.0)", 100., 503000.0, "failure", 96., 500000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 28., 1005000.0, "incident", 24., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 16., 15000.0, "incident", 12., 5000.0)},
                     },
            'cms': True,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[4] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 20000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': False, 'inspect_staff_num': 5, 'maint_intervals': False,
                                         'maint_staff_num': 5, 'inspection_tools_qty': 6,'maintenance_tools_qty':6}, 
                      'results':{}  
                      }
E.cases[4]['assets_data'], E.cases[4]['assets_schedule'] = asset_gen(**asset_type_4)