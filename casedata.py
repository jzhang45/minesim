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

asset_type_1 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("uniform(1.0, 9408.0)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[1] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 400000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[1]['assets_data'], E.cases[1]['assets_schedule'] = asset_gen(**asset_type_1)

asset_type_2 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("normalvariate(4704.0, 2053.0)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[2] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 400000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[2]['assets_data'], E.cases[2]['assets_schedule'] = asset_gen(**asset_type_2)

asset_type_3 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 10800.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[3] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 400000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[3]['assets_data'], E.cases[3]['assets_schedule'] = asset_gen(**asset_type_3)

asset_type_4 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("uniform(1.0, 9408.0)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[4] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 1000000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals':168., 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[4]['assets_data'], E.cases[4]['assets_schedule'] = asset_gen(**asset_type_4)

asset_type_5 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("normalvariate(4704.0, 2053.0)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 43800.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[5] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 1000000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': 168., 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[5]['assets_data'], E.cases[5]['assets_schedule'] = asset_gen(**asset_type_5)

asset_type_6 = {'number': 10, 'name_base': 'Machine', 'output_rate': 30000.0, 'cost_rate': 0.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.0, 
                'events':{'faults':{"tire": ("weibullvariate(5399.0, 2.5)", "uniform(1.0, 48.0)", 9.25, 6000.0, "failure", 5., 1000.0),
                                    "safety": ("uniform(1.0, 17520.0)", "uniform(1.0, 48.0)", 15.25, 1005000.0, "incident", 5., 5000.0),
                                    "environmental": ("uniform(1.0, 10800.0)", "uniform(1.0, 48.0)", 15.25, 105000.0, "incident", 5., 5000.0)},
                     },
            'cms': False,    
            'operator_dist': "",
            'optime': 8760.0
            }

E.cases[6] = {'rnd_seed': 12347,
                      'max_time': 8760.,
                      'simulation_num': 1000000,
                      'assets_data': [],
                      'assets_schedule': None,
                      'operation_vars':{'inspect_intervals': 168., 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False}, 
                      'results':{}  
                      }
E.cases[6]['assets_data'], E.cases[6]['assets_schedule'] = asset_gen(**asset_type_6)