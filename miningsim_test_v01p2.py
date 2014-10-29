# Test suite v0.1.2 for mining simulator v0.7.5.2
# TURNOFF PLOTS IN MAIN CODE
import mining_07p5p2 as simcode
import unittest


class TestCases:

    cases = {
            'case_00':{'rnd_seed': 12345,
                      'max_time': 0.0,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 0.0, 'cost_rate': 0.0, 'maint_t_gen': 0.0, 'maint_cost_gen': 0.0, 'insp_t_gen': 0.0, 'insp_cost_gen': 0.0,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ''},
                        },
                       ],
                      'assets_schedule': {'DeathStar': 0.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False,},
                      'results':{'events': {'DeathStar': []}, 'total_cost_avg': 0.0, 'total_output_avg': 0.0, 'total_lost_output_avg': 0.0, 'total_event_time': 0.0}
                      },
            'case_0':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 0.0, 'cost_rate': 0.0, 'maint_t_gen': 0.0, 'maint_cost_gen': 0.0, 'insp_t_gen': 0.0, 'insp_cost_gen': 0.0,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': []}, 'total_cost_avg': 0.0, 'total_output_avg': 0.0, 'total_lost_output_avg': 0.0, 'total_event_time': 0.0}
                      },
            'case_1':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 2000.0, 'cost_rate': 500.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False, 'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': []}, 'total_cost_avg': 500000.0, 'total_output_avg': 2000000.0, 'total_lost_output_avg': 0.0, 'total_event_time': 0.0}
                      },
            'case_2':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 50,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 2000.0, 'cost_rate': 500.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': []}, 'total_cost_avg': 500000.0, 'total_output_avg': 2000000.0, 'total_lost_output_avg': 0.0, 'total_event_time': 0.0}
                      },
            'case_3':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 2000.0, 'cost_rate': 500.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 500.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': []}, 'total_cost_avg': 250000.0, 'total_output_avg': 1000000.0, 'total_lost_output_avg': 0.0, 'total_event_time': 0.0}
                      },
            'case_4':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':200.,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': [['routine_maintenance_DeathStar', 200.0], ['routine_maintenance_DeathStar', 405.0],
                                                          ['routine_maintenance_DeathStar', 610.0], ['routine_maintenance_DeathStar', 815.0]]},
                                 'total_cost_avg': 204000.0, 'total_output_avg': 980000.0, 'total_lost_output_avg': 20000.0, 'total_event_time': 20.0}
                      },
            'case_5':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 15.0, 'maint_cost_gen': 10000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':400.,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': [['routine_maintenance_DeathStar', 400.0], ['routine_maintenance_DeathStar', 815.0]]},
                                 'total_cost_avg': 214000.0, 'total_output_avg': 970000.0, 'total_lost_output_avg': 30000.0, 'total_event_time': 30.0}
                      },
            'case_6':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{},
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':300., 'inspect_staff_num':False, 'maint_intervals':400,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': [['routine_inspection_DeathStar', 300.0], ['Darth_maintenance', 302.0], ['requested_maintenance_DeathStar', 302.0],
                                                          ['routine_maintenance_DeathStar', 400], ['routine_inspection_DeathStar', 602.0], ['Darth_continue', 604.0],
                                                          ['routine_maintenance_DeathStar', 805.0], ['routine_inspection_DeathStar', 904.0], ['Darth_continue', 906.0]]},
                                 'total_cost_avg': 203300.0, 'total_output_avg': 979000.0, 'total_lost_output_avg': 21000.0, 'total_event_time': 21.0}
                      },
            'case_7':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400.0, 'inspect_staff_num':False, 'maint_intervals':500.0,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405.0], ['Luke_continue', 407.0], ['routine_maintenance_XWing1', 500.0],
                                                       ['routine_inspection_XWing1', 807.0], ['Luke_continue', 809.0]],
                                            'DeathStar': [['routine_inspection_DeathStar', 400.0], ['Darth_maintenance', 402.0], ['requested_maintenance_DeathStar', 402.0],
                                                          ['routine_maintenance_DeathStar', 500.0], ['routine_inspection_DeathStar', 802.0], ['Darth_continue', 804.0]]},
                                 'total_cost_avg': 303300.0, 'total_output_avg': 1481500.0, 'total_lost_output_avg': 18500.0, 'total_event_time': 23.0}
                      },
            'case_8':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400.0, 'inspect_staff_num':False, 'maint_intervals':500.0,
                                         'maint_staff_num':1, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 400.0], ['Luke_continue', 402.0], ['routine_maintenance_XWing1', 500.0], ['routine_inspection_XWing1', 802.0],
                                                       ['Luke_continue', 804.0]],
                                            'DeathStar': [['routine_inspection_DeathStar', 400.0], ['Darth_maintenance', 402.0], ['requested_maintenance_DeathStar', 402.0],
                                                          ['routine_maintenance_DeathStar', 500.0], ['routine_inspection_DeathStar', 802.0], ['Darth_continue', 804.0]]},
                                 'total_cost_avg': 302800.0, 'total_output_avg': 1479000.0, 'total_lost_output_avg': 21000.0, 'total_event_time': 28.0}
                      },
            'case_9':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400.0, 'inspect_staff_num': 1, 'maint_intervals': False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty':False},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405.0], ['Luke_continue', 407.0], ['routine_inspection_XWing1', 807.0],
                                                       ['Luke_continue', 809.0]],
                                            'DeathStar': [['routine_inspection_DeathStar', 400.0], ['Darth_maintenance', 402.0], ['requested_maintenance_DeathStar', 402.0],
                                                          ['routine_inspection_DeathStar', 802.0], ['Darth_continue', 804.0]]},
                                 'total_cost_avg': 301800.0, 'total_output_avg': 1489000.0, 'total_lost_output_avg': 11000.0, 'total_event_time': 13.0}
                      },
            'case_10':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400.0, 'inspect_staff_num': 1, 'maint_intervals': 500.0,
                                         'maint_staff_num':False, 'inspection_tools_qty':False,'maintenance_tools_qty': 1},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405.0], ['Luke_continue', 407.0], ['routine_maintenance_XWing1', 500.0],
                                                       ['routine_inspection_XWing1', 807.0], ['Luke_continue', 809.0]],
                                            'DeathStar': [['routine_inspection_DeathStar', 400.0], ['Darth_maintenance', 402.0], ['requested_maintenance_DeathStar', 402.0],
                                                          ['routine_maintenance_DeathStar', 500.0], ['routine_inspection_DeathStar', 802.0], ['Darth_continue', 804.0]]},
                                 'total_cost_avg': 302800.0, 'total_output_avg': 1479000.0, 'total_lost_output_avg': 21000.0, 'total_event_time': 28.0}
                      },
            'case_11':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400.0, 'inspect_staff_num': 1, 'maint_intervals': 500.0,
                                         'maint_staff_num': 1, 'inspection_tools_qty': 1,'maintenance_tools_qty': 1},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405.0], ['Luke_continue', 407.0], ['routine_maintenance_XWing1', 500.0],
                                                       ['routine_inspection_XWing1', 807.0], ['Luke_continue', 809.0]],
                                            'DeathStar': [['routine_inspection_DeathStar', 400.0], ['Darth_maintenance', 402.0], ['requested_maintenance_DeathStar', 402.0],
                                                          ['routine_maintenance_DeathStar', 500.0], ['routine_inspection_DeathStar', 802.0], ['Darth_continue', 804.0]]},
                                 'total_cost_avg': 302800.0, 'total_output_avg': 1479000.0, 'total_lost_output_avg': 21000.0, 'total_event_time': 28.0}
                      },
            'case_12':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{
                         'failures':{"tire": ("300.", 5.0, 5000.0)},
                         },
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False, 'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': [['tire_failure_DeathStar', 300.0], ['tire_failure_DeathStar', 605.0], ['tire_failure_DeathStar', 910.0]]},
                                 'total_cost_avg': 212000.0, 'total_output_avg': 985000.0, 'total_lost_output_avg': 15000.0, 'total_event_time': 15.0}
                      },
            'case_13':{'rnd_seed': 12345,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                        'events':{
                         'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0)},
                         },
                        'cms': False,
                        'operator': {'name': "Darth", 'dist': ""}
                        },
                       ],
                      'assets_schedule': {'DeathStar': 1000.0},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num':False, 'maint_intervals':False,
                                         'maint_staff_num':False, 'inspection_tools_qty':False, 'maintenance_tools_qty':False},
                      'results':{'events': {'DeathStar': [['tire_failure_DeathStar', 323.34977127379045],
                                                          ['tire_failure_DeathStar', 334.48250849037896]]},
                                 'total_cost_avg': 208000.0, 'total_output_avg': 990000.0, 'total_lost_output_avg': 10000.0, 'total_event_time': 10.0}

                      },
            'case_14':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                  'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0)},
                                                  'faults':{"tire": ("expovariate(1.0 / 200.0)", "expovariate(1.0 / 300.0)", 5.0, 5000.0, "failure", 9.25, 2000.0),
                                                           },
                                                  },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 700.},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['tire_failure_XWing1', 502.3409461333749]],
                                            'DeathStar': [['tire_fault_DeathStar', 269.1078563634206], ['tire_failure_DeathStar', 679.4199895619179]]},
                                 'total_cost_avg': 275600.0, 'total_output_avg': 1343000.0, 'total_lost_output_avg': 7000.0, 'total_event_time': 9.0}

                      },
            'case_15':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                  'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0)},
                                                  'faults':{"tire": ("expovariate(1.0 / 200.0)", "expovariate(1.0 / 300.0)", 5.0, 5000.0, "failure", 2.0, 2000.0),
                                                           },
                                                  },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num': False, 'maint_intervals': 400,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['routine_maintenance_XWing1', 400], ['tire_failure_XWing1', 502.3409461333749],
                                                       ['routine_maintenance_XWing1', 805.0]],
                                            'DeathStar': [['tire_fault_DeathStar', 269.1078563634206], ['routine_maintenance_DeathStar', 400],
                                                          ['routine_maintenance_DeathStar', 805.0]]},
                                 'total_cost_avg': 306200.0, 'total_output_avg': 1481000.0, 'total_lost_output_avg': 19000.0, 'total_event_time': 26.0}

                      },
            'case_16':{'rnd_seed': 12347,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                  'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0)},
                                                  'faults':{"tire": ("expovariate(1.0 / 200.0)", "expovariate(1.0 / 300.0)", 5.0, 5000.0, "failure", 9.25, 2000.0),
                                                           },
                                                  },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400, 'inspect_staff_num': False, 'maint_intervals': 450,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405], ['Luke_continue', 407.0], ['routine_maintenance_XWing1', 450],
                                                       ['tire_failure_XWing1', 691.1414323549119], ['routine_inspection_XWing1', 807.0], ['Luke_continue', 809.0],
                                                       ['routine_maintenance_XWing1', 905.0]],
                                            'DeathStar': [['tire_failure_DeathStar', 261.9479852548444], ['routine_inspection_DeathStar', 400],
                                                          ['Darth_continue', 402.0], ['routine_maintenance_DeathStar', 450],
                                                          ['tire_failure_DeathStar', 473.4500148693784], ['routine_inspection_DeathStar', 802.0],
                                                          ['Darth_continue', 804.0], ['tire_fault_DeathStar', 847.6834977301769],
                                                          ['routine_maintenance_DeathStar', 905.0]]},
                                 'total_cost_avg': 313550.0, 'total_output_avg': 1457750.0, 'total_lost_output_avg': 42250.0, 'total_event_time': 51.25}

                      },
            'case_17':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                 'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0), "struss": ("expovariate(1.0 / 800.0)", 10.0, 8000.0)},
                                                 'faults':{"tire": ("expovariate(1.0 / 400.0)", "expovariate(1.0 / 300.0)", 5.0, 5000.0, "failure", 2.0, 2000.0),
                                                           "struss": ("expovariate(1.0 / 500.0)", "expovariate(1.0 / 300.0)", 10.0, 8000.0, "failure", 2.0, 2000.0)}
                                                 },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['routine_inspection_XWing1', 405], ['Luke_continue', 407.0], ['routine_inspection_XWing1', 807.0],
                                                       ['Luke_continue', 809.0], ['tire_failure_XWing1', 865.8002987840183]],
                                            'DeathStar': [['struss_fault_DeathStar', 245.33750160262585], ['routine_inspection_DeathStar', 400], ['Darth_maintenance', 402.0],
                                                          ['requested_maintenance_DeathStar', 402.0], ['tire_fault_DeathStar', 492.15867967592175],
                                                          ['tire_failure_DeathStar', 589.7407819804682], ['tire_fault_DeathStar', 710.9036138788077],
                                                          ['routine_inspection_DeathStar', 802.0], ['Darth_maintenance', 804.0], ['requested_maintenance_DeathStar', 804.0]]},
                                 'total_cost_avg': 309600.0, 'total_output_avg': 1483000.0, 'total_lost_output_avg': 17000.0, 'total_event_time': 21.0}

                      },
            'case_18':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                 'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0), "struss": ("expovariate(1.0 / 800.0)", 10.0, 8000.0)},
                                                 'faults':{"tire": ("expovariate(1.0 / 400.0)", "expovariate(1.0 / 300.0)", 0., 5000.0, "failure", 9.25, 2000.0),
                                                           "struss": ("expovariate(1.0 / 500.0)", "expovariate(1.0 / 300.0)", 0., 8000.0, "failure", 9.25, 2000.0)}
                                                 },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': "uniform(0.5, self.asset.optime_scheduled)"}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': "uniform(0.5, self.asset.optime_scheduled)"},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['Luke_continue', 238.91830563938788], ['tire_failure_XWing1', 770.3586164341622]],
                                            'DeathStar': [['tire_failure_DeathStar', 294.405001923151], ['tire_fault_DeathStar', 429.51447166254627],
                                                          ['Darth_continue', 463.45221288417747], ['tire_failure_DeathStar', 496.9211999027785],
                                                          ['struss_fault_DeathStar', 615.1983495949022], ['tire_fault_DeathStar', 649.2534863416157],
                                                          ['struss_failure_DeathStar', 712.0760326095491], ['Darth_continue', 792.3614991513929],
                                                          ['tire_fault_DeathStar', 833.9888527627214], ['struss_fault_DeathStar', 892.7470834541089],
                                                          ['struss_failure_DeathStar', 928.1092999806308], ['tire_failure_DeathStar', 971.5020710551611]]},
                                 'total_cost_avg': 325750.0, 'total_output_avg': 1453750.0, 'total_lost_output_avg': 46250.0, 'total_event_time': 48.25}

                      },
            'case_19':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                 'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0), "struss": ("expovariate(1.0 / 800.0)", 10.0, 8000.0)},
                                                 'faults':{"tire": ("expovariate(1.0 / 400.0)", "expovariate(1.0 / 300.0)", 0., 5000.0, "failure", 9.25, 2000.0),
                                                           "struss": ("expovariate(1.0 / 500.0)", "expovariate(1.0 / 300.0)", 0., 8000.0, "failure", 9.25, 2000.0)}
                                                 },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': "uniform(0.5, self.asset.optime_scheduled)"}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': "uniform(0.5, self.asset.optime_scheduled)"},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.},
                      'operation_vars':{'inspect_intervals':400, 'inspect_staff_num': False, 'maint_intervals': 450,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['Luke_continue', 238.91830563938788], ['routine_inspection_XWing1', 405], ['Luke_continue', 407.0],
                                                       ['routine_maintenance_XWing1', 450], ['tire_failure_XWing1', 770.3586164341622], ['routine_inspection_XWing1', 807.0],
                                                       ['Luke_continue', 809.0], ['routine_maintenance_XWing1', 905.0]],
                                            'DeathStar': [['tire_failure_DeathStar', 294.405001923151], ['routine_inspection_DeathStar', 400], ['Darth_continue', 402.0],
                                                          ['tire_fault_DeathStar', 429.51447166254627], ['routine_maintenance_DeathStar', 450], ['Darth_continue', 463.45221288417747],
                                                          ['tire_fault_DeathStar', 495.8812873175912], ['struss_fault_DeathStar', 615.1983495949022], ['struss_failure_DeathStar', 717.600980101638],
                                                          ['struss_fault_DeathStar', 727.8528172834609], ['tire_fault_DeathStar', 763.2150952952965], ['routine_inspection_DeathStar', 802.0],
                                                          ['Darth_maintenance', 804.0], ['requested_maintenance_DeathStar', 804.0], ['tire_failure_DeathStar', 828.2029370283416],
                                                          ['routine_maintenance_DeathStar', 905.0]]},
                                 'total_cost_avg': 324700.0, 'total_output_avg': 1438500.0, 'total_lost_output_avg': 61500.0, 'total_event_time': 70.5}

                      },
            'case_20':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                 'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0), "struss": ("expovariate(1.0 / 800.0)", 10.0, 8000.0)},
                                                 'faults':{"tire": ("expovariate(1.0 / 400.0)", "expovariate(1.0 / 300.0)", 0., 5000.0, "failure", 9.25, 2000.0),
                                                           "struss": ("expovariate(1.0 / 500.0)", "expovariate(1.0 / 300.0)", 0., 8000.0, "failure", 9.25, 2000.0)}
                                                 },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': "uniform(0.5, self.asset.optime_scheduled)"}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': "uniform(0.5, self.asset.optime_scheduled)"},
                                        },
                                       {'name': 'XWing2', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                         'failures':{"tire": ("normalvariate(600.0, 300.0)", 4.0, 2000.0), "struss": ("expovariate(1.0 / 900.0)", 15.0, 10000.0)}
                                         },
                                        'cms': False,
                                        'operator': {'name': "R2D2", 'dist': "uniform(0.5, self.asset.optime_scheduled)"}
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 1000.0, 'XWing2': 1000.0},
                      'operation_vars':{'inspect_intervals':400, 'inspect_staff_num': 2, 'maint_intervals': 450,
                                         'maint_staff_num': 1, 'inspection_tools_qty': 2,'maintenance_tools_qty': 1},
                      'results':{'events': {'XWing2': [['struss_failure_XWing2', 289.9839162583577], ['routine_inspection_XWing2', 410], ['R2D2_continue', 412.0],
                                                       ['routine_maintenance_XWing2', 450], ['tire_failure_XWing2', 533.0967750870777], ['tire_failure_XWing2', 668.2032786914697],
                                                       ['struss_failure_XWing2', 777.4121774359072], ['routine_inspection_XWing2', 812.0], ['R2D2_continue', 814.0], ['R2D2_continue', 884.3471347161761],
                                                       ['routine_maintenance_XWing2', 918.4522128841775]],
                                            'XWing1': [['Luke_continue', 238.91830563938788], ['routine_inspection_XWing1', 405], ['Luke_continue', 407.0], ['Luke_continue', 440.5531671666847],
                                                       ['routine_maintenance_XWing1', 450], ['Luke_continue', 667.3064983264288], ['tire_failure_XWing1', 770.3586164341622],
                                                       ['routine_inspection_XWing1', 807.0], ['Luke_continue', 809.0], ['routine_maintenance_XWing1', 910.0]],
                                            'DeathStar': [['tire_failure_DeathStar', 294.405001923151], ['routine_inspection_DeathStar', 400], ['Darth_continue', 402.0],
                                                          ['routine_maintenance_DeathStar', 450], ['tire_fault_DeathStar', 457.3162026971949], ['tire_failure_DeathStar', 457.46730500628865],
                                                          ['Darth_continue', 549.0963284417705], ['tire_fault_DeathStar', 551.6504556440602], ['tire_failure_DeathStar', 587.0126721705822],
                                                          ['struss_fault_DeathStar', 615.1983495949022], ['tire_failure_DeathStar', 635.1462469766235], ['tire_fault_DeathStar', 784.7701601718371],
                                                          ['routine_inspection_DeathStar', 802.0], ['Darth_maintenance', 804.0], ['requested_maintenance_DeathStar', 804.0],
                                                          ['routine_maintenance_DeathStar', 905.0]]}, 'total_cost_avg': 441032.4568457986, 'total_output_avg': 1890162.284228993,
                                 'total_lost_output_avg': 109837.71577100674, 'total_event_time': 154.06382221309548}

                      },
             'case_21':{'rnd_seed': 12346,
                      'max_time': 1000.,
                      'simulation_num': 1,
                      'assets_data':[
                                       {'name': 'DeathStar', 'output_rate': 1000.0, 'cost_rate': 200.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 2000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{
                                                  'failures':{"tire": ("expovariate(1.0 / 600.0)", 5.0, 5000.0)},
                                                  'faults':{"tire": ("expovariate(1.0 / 200.0)", None, 5.0, 5000.0, "failure", 9.25, 2000.0),
                                                           },
                                                  },
                                        'cms': False,
                                        'operator': {'name': "Darth", 'dist': ""}
                                        },
                                       {'name': 'XWing1', 'output_rate': 500.0, 'cost_rate': 100.0, 'maint_t_gen': 5.0, 'maint_cost_gen': 1000.0, 'insp_t_gen': 2.0, 'insp_cost_gen': 500.,
                                        'events':{'failures':{"tire": ("normalvariate(700.0, 300.0)", 4.0, 2000.0)}},
                                        'cms': False,
                                        'operator': {'name': "Luke", 'dist': ""},
                                        }
                                      ],
                      'assets_schedule': {'DeathStar': 1000.0, 'XWing1': 700.},
                      'operation_vars':{'inspect_intervals':False, 'inspect_staff_num': False, 'maint_intervals': False,
                                         'maint_staff_num': False, 'inspection_tools_qty': False,'maintenance_tools_qty': False},
                      'results':{'events': {'XWing1': [['tire_failure_XWing1', 502.3409461333749]],
                                            'DeathStar': [['tire_fault_DeathStar', 269.1078563634206], ['tire_failure_DeathStar', 373.2597143154435],
                                                          ['tire_fault_DeathStar', 432.7626044179445]]},
                                 'total_cost_avg': 275600.0, 'total_output_avg': 1343000.0, 'total_lost_output_avg': 7000.0, 'total_event_time': 9.0}

                      },

             }

# THIS WORKS TOO!
#class SimCases(unittest.TestCase):

#    def tests(self):

#        for case_name in TestCases.cases:
#            case = TestCases.cases[case_name]
#            results = simcode.main(rnd_seed=case['rnd_seed'], max_time=case['max_time'], optime_scheduled=case['max_time'], simulation_num=case['simulation_num'],
#                                   assets_data=case['assets_data'], assets_schedule=case['assets_schedule'], operation_vars=case['operation_vars'])
#            self.assertEqual(results, (case['results']['total_profit_avg'], case['results']['total_cost_avg']), 'key metrics not all equal for %s'%(case_name))


class SimCases(unittest.TestCase):

    def test_case_00(self):

        case = TestCases.cases['case_00']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'financial metrics not all equal for case 00')

    def test_case_0(self):

        case = TestCases.cases['case_0']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'financial metrics not all equal for case 0')

    def test_case_1(self):

        case = TestCases.cases['case_1']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'financial metrics not all equal for case 1')

    def test_case_2(self):

        case = TestCases.cases['case_2']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'financial metrics not all equal for case 2')

    def test_case_3(self):

        case = TestCases.cases['case_3']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 3')

    def test_case_4(self):

        case = TestCases.cases['case_4']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 4')

    def test_case_5(self):

        case = TestCases.cases['case_5']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 5')

    def test_case_6(self):

        case = TestCases.cases['case_6']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 6')

    def test_case_7(self):

        case = TestCases.cases['case_7']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 7')

    def test_case_8(self):

        case = TestCases.cases['case_1']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 8')

    def test_case_9(self):

        case = TestCases.cases['case_9']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 9')

    def test_case_10(self):

        case = TestCases.cases['case_10']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 10')

    def test_case_11(self):

        case = TestCases.cases['case_11']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 11')

    def test_case_12(self):

        case = TestCases.cases['case_12']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 12')

    def test_case_13(self):

        case = TestCases.cases['case_13']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 13')

    def test_case_14(self):

        case = TestCases.cases['case_14']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 14')

    def test_case_15(self):

        case = TestCases.cases['case_15']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 15')

    def test_case_16(self):

        case = TestCases.cases['case_16']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 16')

    def test_case_17(self):

        case = TestCases.cases['case_17']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 17')

    def test_case_18(self):

        case = TestCases.cases['case_18']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 18')

    def test_case_19(self):

        case = TestCases.cases['case_19']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 19')

    def test_case_20(self):

        case = TestCases.cases['case_20']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 20')

    def test_case_21(self):

        case = TestCases.cases['case_21']
        results = self.sim(case)
        self.assertEqual(results, case['results'], 'metrics not all equal for case 21')

    def sim(self, case):

        results = simcode.main(rnd_seed=case['rnd_seed'], max_time=case['max_time'], optime_scheduled=case['max_time'], simulation_num=case['simulation_num'],
                               assets_data=case['assets_data'], assets_schedule=case['assets_schedule'], operation_vars=case['operation_vars'])
        print results
        return results


#TURNOFF PLOTS IN MAIN CODE
suite = unittest.TestLoader().loadTestsFromTestCase(SimCases)
unittest.TextTestRunner(verbosity=2).run(suite)