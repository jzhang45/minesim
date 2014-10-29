""" Oilsands Mining Operations Simulator (Minesim) v0.7.5.2 based on the thesis of Rezsa Farahani Copyright 2014 titled:
    Design, simulation, and evaluation of effective industrial information systems: case of machine condition monitoring
    and maintenance management information systems

    Thesis available on www.rezsa.com
    rfarahani@ualberta.ca

    Operation of several assets with several random failure and incident events with different distributions.
    Using SimPy 2.3:

    Assets operate for the duration of their scheduled total operation time. Once an event occurs, which
    can be of several types including machine faults and failures, and safety/environmental incidents,
    the asset's operation is halted until the event is addressed, then the asset resumes operation.

    While operating, the asset operator can make the decision to continue operating, call for inspection,
    or take to maintenance based on the condition of the asset and his subjective belief.

    The inspection and maintenance resources are also limited, therefore assets have to queue until the resources
    become available and in order to receive service.

    The casedata file linked to the simulator is intended to simulate four different operations strategies and
    Industrial Information Systems (IIS):

    1. Breakdown maintenance operations: assets operate till they fail or an incident happens
    2. Planned maintenance operations: assets are inspected at specific schedules to catch faults prior to failures/incidents
    3. The operations employs and offline Condition Monitoring System (CMS) for detecting machine faults and predicting events
    4. The operations employs and realtime Condition Monitoring System for detecting machine faults and predicting events
    """
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# make fault events reoccuring and reactivate them after each releveant maintenance
# failures and incidents should be one time occurring processes that should be cancelled/removed/started in case of maintenance or fault
#!!!!!!!!!!!!!!!!!!!!!!!!

#for when run from command line in debug mode
#if __debug__:
#    from SimPy.SimulationTrace import *
#    SimulationMode = "SimulationTrace"
#else:
#    from SimPy.Simulation import *
#    SimulationMode = "Simulation"

Trace = False
Prints = False
PRINTOUT = True
PRINTOUT_FINAL = True
PLOTS = True
if Trace:
    from SimPy.SimulationTrace import *
    SimulationMode = "SimulationTrace"
else:
    from SimPy.Simulation import *
    SimulationMode = "Simulation"

import gc
from random import *
from time import time
import csv
import matplotlib.pyplot as plt
import numpy as np
# select which case data file to use
import casedata4 as cdata

## Model components ...........................................


def inspector_diagnosis(condition_true):
    """ inspector's assessment model of the machine condition based on assessment
     condition probabilities and the true condition of the machine. """
    assert condition_true == 'healthy' or condition_true == 'faulty'

    roll = random()
    if condition_true == 'healthy':
        if roll >= 0.: diagnosis = 'healthy'
        else: diagnosis = 'faulty'
    else:
        if roll >= 0.1: diagnosis = 'faulty'
        else: diagnosis = 'healthy'

    return diagnosis


def mtech_diagnosis(condition_true):
    """ maintenance tech's assessment model of the machine condition based on assessment
     condition probabilities and the true condition of the machine. """
    assert condition_true == 'healthy' or condition_true == 'faulty'

    roll = random()
    if condition_true == 'healthy':
        if roll >= 0.: diagnosis = 'healthy'
        else: diagnosis = 'faulty'
    else:
        if roll >= 0.1: diagnosis = 'faulty'
        else: diagnosis = 'healthy'

    return diagnosis


class Asset(Process):
    """ Class representing a truck object. contains the main PEM: operating() """

    def __init__(self, name, sim, output_rate, cost_rate, optime_scheduled, inspection_proc, maintenance_proc, operator=None, cms=False):
        Process.__init__(self, name, sim)
        self.output = 0.
        self.cost = 0.
        self.opcost = 0.
        self.output_rate = output_rate
        self.cost_rate = cost_rate
        self.events = []
        self.faults_num = 0
        self.failures_num = 0
        self.incidents_saf_num = 0
        self.incidents_env_num = 0
        self.optime_scheduled = optime_scheduled
        self.optime_remaining = self.optime_scheduled
        self.events_occured = []
        self.events_cost = 0.
        self.total_event_time = 0.
        self.time_operating = 0.
        self.state = 'production'
        self.condition_known = ['healthy', 0.]
        self.condition_true = 'healthy'
        self.cms = cms
        self.faults_existing = []
        self.events_existing = []
        self.faults_detected_num = 0
        self.past_states = (('production-healthy',),)
        self.distributions = {'failure':{}, 'fault':{}, 'incident':{}}
        self.operator = operator
        self.do_maint = False
        self.do_inspect = False
        self.inspection_proc = inspection_proc
        self.maintenance_proc = maintenance_proc

    def cms_model(self):
        """ Model of the asset's condition monitoring system. """
        if self.cms:
            roll = random()
            if self.condition_true == 'healthy':
                if roll >= 0.3: diagnosis = 'healthy'
                else: diagnosis = 'faulty'
            else:
                if roll >= 0.4: diagnosis = 'faulty'
                else: diagnosis = 'healthy'

            self.condition_known = [diagnosis, self.sim.now()]
            return diagnosis
        else: return False

    def operating(self):
        """ Main operation method of an asset and it's process execution method (PEM). """

        # initially set the total operated time of the asset to the schedule runtime.
        self.time_operating = self.optime_scheduled
        if Prints: print "%0.1f: asset %s starts the beginning of its operation period." %(self.sim.now(), self.name)
        #the main PEM condition
        while self.optime_remaining > 0 and self.sim.now() < self.optime_scheduled:
            yield hold, self, self.optime_remaining
            # check if the asset has been interrupted
            if self.interrupted():
                if Prints: print "%.1f: asset %s process is interrupted by %s process. The interruption is reset"\
                                 % (self.sim.now(), self.name, self.interruptCause.name)

                self.interruptReset()
                if self.interruptCause.name != self.operator.name:
                    self.events_occured.append([self.interruptCause.name, self.sim.now()])

                # check for conditions that take the asset into an inspection or maintenance state
                if self.do_maint is True or self.do_inspect is True or self.interruptCause.event_type in ['failure', 'incident', 'routine service']:
                    # set asset state name based on event
                    if self.interruptCause.event_type == 'failure':
                        self.state = 'failure'
                        self.condition_true = 'faulty'
                    elif self.interruptCause.event_type == 'incident':
                        self.state = 'incident'
                    elif self.do_inspect is True or (self.interruptCause.event_type == 'routine service' and self.interruptCause.mode == 'inspection'):
                        self.state = 'inspection'
                    elif self.do_maint is True or (self.interruptCause.event_type == 'routine service' and self.interruptCause.mode == 'maintenance'):
                        self.state = 'maintenance'

                    if Prints: print '%.1f: the state is %s, inspection flag is %s and maintenance flag is %s'\
                                     % (self.sim.now(), self.state, self.do_inspect, self.do_maint)
                    #hold for a notification period, this has to be changed to a state change delay value later
#                    yield hold, self, 0.5

                    # inspection state
                    if self.do_inspect is True or (self.interruptCause.event_type == 'routine service' and self.interruptCause.mode == 'inspection'):
                        # constant for now, change based on fault type later.
                        if Prints: print '%.1f: performing inspection on %s' %(self.sim.now(), self.name)
                        # check if resources needed, if so, request
                        priority = 1 if self.do_inspect else 0
                        t_req_i = False
                        t_req_it = False
                        if self.sim.inspect_staff_num:
                            t_req_i = self.sim.now()
                            yield request, self, self.sim.inspectors, priority
                        if self.sim.inspection_tools_qty:
                            t_req_it = self.sim.now()
                            yield request, self, self.sim.inspect_tools, priority

                        if t_req_it is False: t_req_it = self.sim.now()
                        if t_req_i is False: t_req_i = self.sim.now()
                        if t_req_it <= t_req_i:
                            req_t = t_req_it
                        else:
                            req_t = t_req_i
                        # go through inspection
                        # calculate downtime
                        if Prints: print 'Total event time (recorded before this process): ', self.total_event_time
                        downtime = self.inspection_proc[0] + (self.sim.now() - req_t)
                        if Prints: print "downtime: ", downtime

                        diagnosis = inspector_diagnosis(self.condition_true)
                        if Prints: print "true condition of machine was: ", self.condition_true
                        if Prints: print "inspector diagnosis was: ", diagnosis
                        self.condition_known = [diagnosis, self.sim.now()]
                        if self.condition_true == 'faulty' and diagnosis == 'faulty':
                            self.faults_detected_num += 1

#                        if self.condition_true == 'faulty':
#                            self.condition_known = ['faulty', self.sim.now()]
#                        else:
#                            self.condition_known = ['healthy', self.sim.now()]

                        self.cost_time_calc(downtime, self.inspection_proc[1])

                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        # this decision interrupts the asset, but is there a better way with signals?
                        # operator decides about inspection results
                        self.state = 'production'
                        self.do_inspect = False
                        if self.interruptCause.event_type == 'routine service':
                            if Prints: print "%.1f: routine inspection done. Setting up next schedule inspection in %.1f from now."\
                                             % (self.sim.now(), self.inspection_proc[0])
                            self.sim.reactivate(self.interruptCause, delay=self.inspection_proc[0])
                        # !! activating the operator flag process should be after reactivating the routine inspection process for its interruption to be detected
                        decision = self.operator.cm_decision(self.condition_known, self.condition_true)
                        self.events_occured.append([self.operator.name+'_'+decision, self.sim.now()+self.inspection_proc[0]])
                        if Prints: print "%.1f: after inspection, operator makes decision and decides to %s" % (self.sim.now(), decision)
                        opx = Operator(name=self.operator.name, asset=self, sim=self.sim)
                        if decision == 'maintenance':
                            if Prints: print "activating: ", opx.name
                            self.do_maint = True
                        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        #TEST: which one is correct? the second one is more elegant. if a process class can have activated more than
                        # one of its methods as a PEM, that resembles the reality and conforms better with OO programming method
                        # it doesn't seem to be passing tests though, could be explored more.
                            self.sim.activate(opx, opx.flag_asset(), delay=self.inspection_proc[0])
#                            self.sim.activate(self.operator, self.operator.flag_asset())
                        else:
                            self.do_maint = False

                        yield hold, self, self.inspection_proc[0]
                        if self.sim.inspection_tools_qty: yield release, self, self.sim.inspect_tools
                        if self.sim.inspect_staff_num: yield release, self, self.sim.inspectors
                    # maintenance state
                    else:
                        self.state = 'maintenance'
                        if Prints: print '%.1f: performing maintenance. State should be maintenance. The state is: %s'\
                                         % (self.sim.now(), self.state)
                        # check if resources needed, if so, request
                        if self.interruptCause.event_type == 'incident':
                            priority = 3
                        elif self.interruptCause.event_type == 'failure':
                            priority = 2
                        elif self.do_maint:
                            priority = 1
                        else:
                            priority = 0

                        t_req_m = False
                        t_req_mt = False
                        if self.sim.maint_staff_num:
                            t_req_m = self.sim.now()
                            yield request, self, self.sim.mtechs, priority
                        if self.sim.maintenance_tools_qty:
                            t_req_mt = self.sim.now()
                            yield request, self, self.sim.maint_tools, priority
                        if t_req_mt is False: t_req_mt = self.sim.now()
                        if t_req_m is False: t_req_m = self.sim.now()
                        if t_req_mt <= t_req_m:
                            req_t = t_req_mt
                        else:
                            req_t = t_req_m
                        # if maintenance was due to a failure or incident:
                        if self.interruptCause.event_type in ['failure', 'incident']:
                            if Prints: print "maintenance due to: ", self.interruptCause.event_type
                            if self.interruptCause.event_type == 'failure':
                                self.failures_num += 1
                            elif self.interruptCause.mode[:3] == 'saf':
                                self.incidents_saf_num += 1
                            elif self.interruptCause.mode[:3] == 'env':
                                self.incidents_env_num += 1
                            maint_duration = self.interruptCause.duration
                            cost = self.interruptCause.cost
                            #####!!!!!!!!!!!!!!!!
                            # This needs to also update Faults!! make a procedure for updating probabilities and removing old events...

                            failure_data = self.distributions[self.interruptCause.event_type][self.interruptCause.mode]
                            # only if the failure process is a failure that wasn't triggered due to fault will be reactivated.
                            #  If the mode of the failure has "_fault" tagged to its end,
                            # this means that it was generated by a fault and so the fault should be reactivated not a failure of that mode.
                            if self.interruptCause.mode[-5:] != 'fault':
                                self.sim.events.append(Event(event_type=self.interruptCause.event_type, mode=self.interruptCause.mode,
                                                             asset=self, sim=self.sim, randfunc=failure_data[0], duration=failure_data[1], cost=failure_data[2]))
                                self.sim.activate(self.sim.events[-1], self.sim.events[-1].halt_routine(), delay=maint_duration)
                                self.events.append(self.sim.events[-1])
                                if Prints: print 'activated new failure or incident event with updated distribution: ', self.sim.events[-1].name
                            self.cancel(self.interruptCause)
                            self.events.remove(self.interruptCause)
                            if Prints: print 'cancelled and removed old failure or incident event: ', self.interruptCause.name
                            #!!! MAKE INTO PROCEDURE: should cancel and remove all faults and repair and calculate downtime for
                            # all fault repairs. This is taking an 'opportunity based maintenance'
                            ## approach where at the opportunity of dealing with events and incidents,
                            # all the faults are dealt with. When fixing a fault, the conditional probability of the
                            ## maintenance tech in detecting the the fault should be also accounted for...
                            newevent_objects = []
                            newevents = []
                            oldevents = []
                            for event in self.events:
                                if event.event_type == 'fault':
                                    ## if the fault in the list is the cause of the failure, restart that fault,
                                    #  but the cost and time of fixing that fault doesn't count
                                    ## because its failure was dealt with

                                    if event.mode == self.interruptCause.mode.split('_')[0]:
                                        if Prints: print "this fault not counted in cost calculations: ", event.name
                                        fault_restart = True
                                    elif event in self.faults_existing:
                                        ## calculate the cost and duration of fixing all the other found faults
                                        if mtech_diagnosis('faulty') == 'faulty':
                                            if Prints: print "while servicing machine in response to event, maintenance" \
                                                             " tech detects a true fault, this fault counted in cost calculations: ", event.name
                                            self.faults_detected_num += 1
                                            maint_duration += event.duration
                                            cost += event.cost
                                            fault_restart = True
                                        else:
                                            if Prints: print "while servicing machine in response to event, maintenance" \
                                                             " tech fails to detect a true fault: ", event.name
                                            fault_restart = False
                                    else:
                                        fault_restart = False
                                    if fault_restart is True and [event.event_type, event.mode] not in newevents:
                                        oldevents.append(event)
                                        fault_data = self.distributions['fault'][event.mode]
                                        newevents.append([event.event_type, event.mode])
                                        self.sim.events.append(Event(event_type='fault', mode=event.mode, asset=self,
                                                                     sim=self.sim, randfunc=fault_data[0], duration=fault_data[5], cost=fault_data[6]))
                                        self.sim.activate(self.sim.events[-1], self.sim.events[-1].fault_routine(), delay=maint_duration)
                                        newevent_objects.append(self.sim.events[-1])

                            for event in oldevents:
                                self.cancel(event)
                                self.events.remove(event)
                                if event in self.faults_existing: self.faults_existing.remove(event)
                                if Prints: print "cancelled and removed old fault: ", event.name
                            if newevent_objects:
                                self.events.extend(newevent_objects)
                                if Prints: print "activated new fault with reset probabilities: ", newevents

                        # if maintenance was due to regular maintenance intervals
                        # !!!!!!!
                        # mantenance times should be different if a fault is detected and known, vs. unknown general maintenance: SHOULD BE ADDRESSED NOW BUT CHECK
                        else:
#                            if Prints: print 'Total event time: ', self.total_event_time
                            if self.interruptCause.event_type == 'routine service':
                                if Prints: print "%0.1f: maintenance due to regular maintenance routine" % (self.sim.now())
                                maint_duration = self.maintenance_proc[0]
                                cost = self.maintenance_proc[1]
                                if Prints: print "reactivating regular maintenance"
                                self.sim.reactivate(self.interruptCause, delay=maint_duration)
                            else:
                                if Prints: print "%0.1f: maintenance at operator's request." % (self.sim.now())
                                maint_duration = 0.
                                cost = 0.
                                self.events_occured.append(['requested_maintenance_'+self.name, self.sim.now()])

                            newevents = []
                            newevent_objects = []
                            old_faults = []
                            old_events = []
                            if not self.faults_existing:
                                maint_duration = self.maintenance_proc[0]
                                cost = self.maintenance_proc[1]
                            else:
                                for event in self.faults_existing:
                                    if self.cms:
                                        if Prints: print "maintenance tech performed maintenance because CMS indicated" \
                                                         " to operator that machine is faulty. fixed: ", event.name
                                        maint_do = True
                                    elif mtech_diagnosis('faulty') == 'faulty':
                                        if Prints: print 'maintenance tech detects true fault as part of maintenance,' \
                                                         ' restores asset to healthy, and event probability is reset, of:', event.name
                                        self.faults_detected_num += 1
                                        maint_do = True
                                    else:
                                        if Prints: print 'maintenance tech fails to detect true fault as part of regular maintenance:', event.name
                                        maint_do = False
                                    if maint_do:
                                        dist_data = self.distributions[event.event_type][event.mode]
                                        maint_duration += event.duration
                                        cost += event.cost
                                        for non_fault_event in self.events:
                                            if non_fault_event.event_type in ['incident', 'failure'] and non_fault_event.mode[:3] == event.mode[:3]:
                                                old_events.append(non_fault_event)
                                        if [event.event_type, event.mode] not in newevents:
                                            self.sim.events.append(Event(event_type=event.event_type, mode=event.mode, asset=self, sim=self.sim,
                                                                         randfunc=dist_data[0], duration=dist_data[2], cost=dist_data[3]))
                                            self.sim.activate(self.sim.events[-1], self.sim.events[-1].fault_routine(), delay=maint_duration)

                                            old_faults.append(event)
                                            newevent_objects.append(self.sim.events[-1])
                                            newevents.append([event.event_type, event.mode])
                                            if Prints: print 'activated new event with updated distribution'


                            for event in old_faults:
                                self.cancel(event)
                                self.events.remove(event)
                                self.faults_existing.remove(event)
                                if Prints: print 'cancelled old fault: ', event.name
                            for event in old_events:
                                self.cancel(event)
                                self.events.remove(event)
                                if Prints: print 'cancelled old event: ', event.name

                            self.events.extend(newevent_objects)
                            if Prints: print "the new events added were: ", newevents

                        downtime = maint_duration + (self.sim.now() - req_t)
                        if Prints: print "end of maintenance process: true and known machine conditions set to healthy, state is production. downtime: ", downtime
                        self.cost_time_calc(downtime, cost)
                        self.condition_true = 'healthy'
                        self.condition_known = ['healthy', self.sim.now()]
                        self.do_maint = False
                        self.state = 'production'

                        yield hold, self, maint_duration

                        if self.sim.maintenance_tools_qty: yield release, self, self.sim.maint_tools
                        if self.sim.maint_staff_num: yield release, self, self.sim.mtechs

                # interruption because of an operator's decision moment
## Operator section --------
                elif self.interruptCause.event_type == 'operator decision' and self.interruptCause.mode == 'decision moment':
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                # this decision interrupts the asset, but is there a better way with signals?
                    if self.cms: self.cms_model()
                    decision = self.operator.cmi_decision(self.condition_known, self.condition_true)
                    if Prints: print "Suddenly, operator makes decision at %.2f and decides to %s" %(self.sim.now(), decision)
                    opy = Operator(name=self.operator.name, asset=self, sim=self.sim)
                    if decision == 'maintenance':
                        self.do_maint = True
                        self.do_inspect = False
                        self.sim.activate(opy, opy.flag_asset(), delay=0.)
                    elif decision == 'inspection':
                        self.do_maint = False
                        self.do_inspect = True
                        self.sim.activate(opy, opy.flag_asset(), delay=0.)
                    else:
                        self.do_maint = False
                        self.do_inspect = False
                    self.events_occured.append([self.operator.name+'_'+decision, self.sim.now()])
                    self.cost_time_calc(0., 0.)
                # interruption because a fault occurred. probabilities of relevant failures and incident modes get updated.
## FAULT section --------
                elif self.interruptCause.event_type == 'fault':
                    self.faults_num += 1
                    #this has two situations: faulty in reality, and faulty that has been registered and is know by the driver from fault detection or from inspection
                    if Prints: print 'simulation going through fault handling procedure'
                    self.condition_true = 'faulty'
                    self.faults_existing.append(self.interruptCause)
                    if self.cms:
                        diagnosis = self.cms_model()
                        if Prints: print "%.1f: The asset is faulty: %s. The CMS of machine %s makes diagnosis: %s"\
                                         % (self.sim.now(), self.interruptCause.name, self.name, diagnosis)
                        ## CAN MAKE THIS INTO ROUTINE
                        if diagnosis == 'faulty':
                            self.faults_detected_num += 1
                            decision = self.operator.cm_decision(self.condition_known, self.condition_true)
                            self.events_occured.append([self.operator.name+'_'+decision, self.sim.now()+self.inspection_proc[0]])
                            if Prints: print "%.1f: after CMS detection of fault, operator makes decision and decides to %s" %(self.sim.now(), decision)
                            opx = Operator(name=self.operator.name, asset=self, sim=self.sim)
                            if decision == 'maintenance':
                                if Prints: print "activating: ", opx.name
                                self.do_maint = True
                                self.sim.activate(opx, opx.flag_asset(), delay=0.01)
                            else:
                                self.do_maint = False

                    self.cost_time_calc(0., 0.)
                    newevents = []
                    pre_existing = False
                    for event in self.events:
                        if (event.event_type == 'failure' or event.event_type == 'incident') and event.mode == self.interruptCause.mode:
                            pre_existing = True
                            fault_data = self.distributions['fault'][event.mode]
                            event_data = self.distributions[event.event_type][event.mode]
                            if fault_data[1]:
                                if Prints: print 'this fault results in adjusting probabilities associated with:', event.name

                                self.sim.events.append(Event(event_type=event.event_type, mode=event.mode, asset=self,
                                                             sim=self.sim, randfunc=fault_data[1], duration=event_data[1], cost=event_data[2]))
                                self.sim.activate(self.sim.events[-1], self.sim.events[-1].halt_routine())

                                newevents.append(self.sim.events[-1])
                                if Prints: print 'activated new event with updated distribution:', event.name
                                self.cancel(event)
                                self.events.remove(event)
                                if Prints: print 'cancelled old event: ', event.name
                    if pre_existing is False:
                        if Prints: print "no pre-failure of this fault type found in the event list..."
                        fault_data = self.distributions['fault'][self.interruptCause.mode]
                        ## if the fault results in a failure (by checking for the failure distribution in fault_data...
                        if fault_data[1]:
                            ## creates data for a failure event resulting from the fault, but assigns False to it's distribution so later on it can be
                            ## determined that this failure was generated from a fault and should not be restarted as a process e.g. after going through a serivce
                            if self.interruptCause.mode in self.distributions['failure']:
                                event_type = 'failure'
                                mode = self.interruptCause.mode
                                data = self.distributions['failure'][mode]
                            elif self.interruptCause.mode in self.distributions['incident']:
                                event_type = 'incident'
                                mode = self.interruptCause.mode
                                data = self.distributions['incident'][mode]
                            else:
                                data = fault_data[1:4]
                                self.distributions[fault_data[4]][self.interruptCause.mode+'_fault'] = data
                                event_type = fault_data[4]
                                mode = self.interruptCause.mode+'_fault'
                            self.sim.events.append(Event(event_type=event_type, mode=mode, asset=self, sim=self.sim,
                                                         randfunc=data[0], duration=data[1], cost=data[2]))
                            self.sim.activate(self.sim.events[-1], self.sim.events[-1].halt_routine())
                            if Prints: print "activated new event: ", self.sim.events[-1].name
                            newevents.append(self.sim.events[-1])
                        else:
                            if Prints: "causing all the effects from the fault..."
                            ## do what this fault that doesn't lead to a failure does
                            pass
                    self.events.extend(newevents)
                else:
                    if Prints: print "%.1f asset interrupted, but cause not in main condition list." % (self.sim.now())
            self.sim.monitor.observe(self.sim.total_output, self.sim.now())

            # calculate asset metrics during its runtime
            self.output = self.output_rate * self.time_operating
            self.opcost = self.cost_rate * self.time_operating
            self.cost = self.opcost + self.events_cost

    def cost_time_calc(self, duration, cost):
        """ calculates total runtime remaining after an interruption to the asset. Updates the asset variables: total_event_time,
            time_operating, and events_cost. Caution in using this function, it's not a pure function and has side effects. """

        assert duration >= 0.
        assert cost >= 0.

        self.optime_remaining = self.interruptLeft - duration
        self.total_event_time += duration
        self.time_operating -= duration
        self.events_cost += cost
        return True


class Event(Process):
    """ This is a class for events produced by assets which includes
        faults, failures, safety and environmental incidents, inspection
        and maintenance calls. """

    def __init__(self, event_type, mode, asset, sim, randfunc, duration, cost):
        Process.__init__(self, name="%s_%s_%s" % (mode, event_type, asset.name), sim=sim)
        self.asset = asset
        self.randfunc = randfunc
        self.duration = duration
        self.cost = cost
        self.event_type = event_type
        self.mode = mode

    def halt_routine(self):
        """ a routine that generates events and the PEM for the Event. """
#        if self.asset.optime_remaining < 0:
#            break
        event_time = eval(self.randfunc)
        assert event_time > 0.
        yield hold, self, event_time
#        if self.asset.terminated():
#            break
        self.interrupt(self.asset)

    def fault_routine(self):
#        if self.asset.optime_remaining < 0:
#            break
        event_time = eval(self.randfunc)
        while event_time < 0.:
            event_time = eval(self.randfunc)
        assert event_time > 0.
        yield hold, self, event_time
#        if self.asset.terminated():
#            break
        self.interrupt(self.asset)
#        yield passivate, self

class Operator(Process):
    """ main class for the operator of an asset. it contains three methods: decision_moment,
        and two decision models, cm_decision and cmi_decision. """

    def __init__(self, name='an_operator', asset=None, sim=None, belief=None, duration=0., cost=0.):
        Process.__init__(self, name=name, sim=sim)
        self.name = name
        self.belief = belief
        self.asset = asset
        self.duration = duration
        self.cost = cost
        self.event_type = 'operator decision'
        self.mode = None
        self.decisions = []

    def decision_moment(self):
        """ The PEM for the operator for stochastically sending interrupts to the asset."""

        while True:
            if self.asset.optime_remaining < 0 or not self.belief:
                break
            decision_time = eval(self.belief)
            assert decision_time > 0.
            yield hold, self, decision_time
            if self.asset.terminated():
                break
            self.interrupt(self.asset)
            self.mode = 'decision moment'

    # these are the operator's decision models, they have to be generalized and included in a data structure
    def cm_decision(self, condition_known, condition_true):
        """ method that is a decision model for the operator. takes two asset variables, condition_known and condition_true and
            returns two outcomes: the operator's stochastic decision to continue asset operation or request maintenance as strings. """

        # !!! WARNING: this variable means whether there's an offline cms or not. it's hardcoded now but should be
        # in the data structure and as part of the asset object
        cms_offline = False
        roll = random()
        if condition_known[0] == 'faulty':
            if cms_offline or self.asset.cms:
                if roll < 0.9:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
            else:
                if roll < 0.7:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
        elif (self.sim.now() - condition_known[1]) < 48.:
            if cms_offline or self.asset.cms:
                if roll < 0.0:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
            else:
                if roll < 0.05:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
        else:
            if cms_offline or self.asset.cms:
                if roll < 0.05:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
            else:
                if roll < 0.1:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
        return self.decisions[-1]

#    def cm_decision(self, condition_known, condition_true):
#        """ method that is a decision model for the operator. takes two asset variables, condition_known and condition_true and
#            returns two outcomes: the operator's stochastic decision to continue asset operation or request maintenance as strings. """
#
#        if condition_known[0] == 'faulty':
#            decision = 'maintenance'
#        else:
#            decision = 'continue'
#        self.decisions.append(decision)
#        return decision

    def cmi_decision(self, condition_known, condition_true):
        """ method that is a decision model for the operator. takes two asset variables, condition_known and condition_true and
            returns three outcomes: the operator's stochastic decision to continue asset operation, request maintenance,
             or request inspection as strings. """

        # !!! WARNING: this variable means whether there's an offline cms or not. it's hardcoded now but should be
        # in the data structre and as part of the asset object
        cms_offline = False
        roll = random()
        if condition_known[0] == 'faulty':
            if cms_offline or self.asset.cms:
                if roll < 0.9:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
            else:
                if roll < 0.7:
                    self.decisions.append('maintenance')
                else:
                    self.decisions.append('continue')
        elif (self.sim.now() - condition_known[1]) < 48.:
            if cms_offline or self.asset.cms:
                if roll <= 0.0:
                    self.decisions.append('maintenance')
                elif  0.0 < roll < 0.05:
                    self.decisions.append('inspection')
                else:
                    self.decisions.append('continue')
            else:
                if roll <= 0.05:
                    self.decisions.append('maintenance')
                elif  0.05 < roll < 0.1:
                    self.decisions.append('inspection')
                else:
                    self.decisions.append('continue')
        else:
            if cms_offline or self.asset.cms:
                if roll <= 0.05:
                    self.decisions.append('maintenance')
                elif  0.05 < roll < 0.15:
                    self.decisions.append('inspection')
                else:
                    self.decisions.append('continue')
            else:
                if roll <= 0.1:
                    self.decisions.append('maintenance')
                elif  0.1 < roll < 0.2:
                    self.decisions.append('inspection')
                else:
                    self.decisions.append('continue')
        return self.decisions[-1]

#     def cmi_decision(self, condition_known, condition_true):
#        """ method that is a decision model for the operator. takes two asset variables, condition_known and condition_true and
#            returns two outcomes: the operator's stochastic decision to continue asset operation or request maintenance as strings. """
#
#        if condition_known[0] == 'faulty':
#           decision = 'maintenance'
#        else:
#            decision = 'continue'
#        self.decisions.append(decision)
#        return decision

    def flag_asset(self):
        """ method that is a PEM for the operator that sends an interruption to the asset at the moment it's called
            and updates the asset's mode variable to 'flag asset'. """
        #flag_time is the time for the operator to flag the asset with his decision after receiving inspection results
        flag_time = 0.0
        yield hold, self, flag_time
        self.interrupt(self.asset)
        self.mode = 'flag asset'


class Service(Process):
    """ main class for service procedures such as inspection and maintenance. contains the PEM service_routine. """

    def __init__(self,mode, asset, sim, intervals, duration, cost):
        Process.__init__(self, name="routine_%s_%s" %(mode, asset.name), sim=sim)
        self.asset = asset
        self.intervals = intervals
        self.duration = duration
        self.cost = cost
        self.event_type = 'routine service'
        self.mode = mode

    def service_routine(self):
        """ main PEM for a service object. sends interruptions to the asset at regular intervals. """

        while True:
            if self.asset.optime_remaining < 0:
                break
            assert self.intervals > 0.
            yield hold, self, self.intervals
            if self.asset.terminated():
                break
            self.interrupt(self.asset)


class Operation(eval(SimulationMode)):
    """ The operation simulation object class. Each operation of assets is an instance of this object.
        Each operation instance is a simulation instance. """

    def __init__(self, max_time, optime_scheduled, assets_schedule, assets_data,
                 inspect_intervals=None, inspect_staff_num=False, maint_intervals=None,
                 maint_staff_num=False, inspection_tools_qty=False, maintenance_tools_qty=False):
        if Trace:
            SimulationTrace.__init__(self)
        else:
            Simulation.__init__(self)

        self.name = "a_simulation"
        self.max_time = max_time
        self.optime_scheduled = optime_scheduled
        self.assets_schedule = assets_schedule
        self.total_output = 0.
        self.total_cost = 0.
        self.total_lost_output = 0.
        self.assets_data = assets_data
        self.assets = []
        self.events = []
        self.events_occurred = {}
        self.total_event_time = 0.
        self.time_operating = 0.
        self.failures_num = 0
        self.faults_num = 0
        self.incidents_saf_num = 0
        self.incidents_env_num = 0
        self.faults_detected_num = 0
        self.operators = []
        self.services = []
        self.inspect_intervals = inspect_intervals
        self.inspect_staff_num = inspect_staff_num
        self.maint_intervals = maint_intervals
        self.maint_staff_num = maint_staff_num
        self.inspectors = False
        self.mtechs = False
        self.inspection_tools_qty = inspection_tools_qty
        self.inspect_tools = False
        self.maintenance_tools_qty = maintenance_tools_qty
        self.maint_tools = False

    def run(self):
        """ The main execution method of the operation simulation object that
            creates and activates processes and resources for each operation simulation. """

        self.initialize()
        self.monitor = Monitor('Time operating', sim=self)

        if self.maint_staff_num:
            self.mtechs = Resource(capacity=self.maint_staff_num, sim=self, name='maintenance techs', qType=PriorityQ, monitored=True)

        if self.inspect_staff_num:
            self.inspectors = Resource(capacity=self.inspect_staff_num, sim=self, name='inspectors', qType=PriorityQ, monitored=True)

        if self.inspection_tools_qty:
            self.inspect_tools = Resource(capacity=self.inspection_tools_qty, sim=self, name='inspection tools', qType=PriorityQ, monitored=True)

        if self.maintenance_tools_qty:
            self.maint_tools = Resource(capacity=self.maintenance_tools_qty, sim=self, name='maintenance tools', qType=PriorityQ, monitored=True)

        # this variable is for when the machines are spread out over the service time and not serviced all at one time, can have two values 0 or 1
        spread_inspection = 1
        # !!! WARNING hardcoded here, average inspection time, should be calculated from averaging the insp_t_general variable of all assets
        # OR, this can be simply taken as an inspection job period, i.e. each job takes 5 h, with machines evenly distributed over sessions
        inspection_duration_avg = 5
        inspect_per_session = 1
        if self.inspect_intervals:
            inspect_per_session = int(round((len(self.assets_data)/(self.inspect_intervals/inspection_duration_avg))))
            if inspect_per_session < 1: inspect_per_session = 1

        asset_count = 0
        for asset in self.assets_data:
            inspect_delay = spread_inspection * int(asset_count/inspect_per_session) * inspection_duration_avg
            asset_count += 1
            # create and activate the assets and their operators
            self.operators.append(Operator(name=asset['operator']['name'], sim=self, belief=asset['operator']['dist']))
            self.activate(self.operators[-1], self.operators[-1].decision_moment())

            self.assets.append(Asset(name=asset['name'], sim=self, output_rate=asset['output_rate'], cost_rate=asset['cost_rate'],
                                          optime_scheduled=self.assets_schedule[asset['name']], inspection_proc=(asset['insp_t_gen'], asset['insp_cost_gen']),
                                          maintenance_proc=(asset['maint_t_gen'], asset['maint_cost_gen']), operator=self.operators[-1], cms=asset['cms']))
            self.activate(self.assets[-1], self.assets[-1].operating())

            self.operators[-1].asset = self.assets[-1]

            # create and assign simulation resources
            if self.maint_intervals:
                self.services.append(Service(mode = 'maintenance', asset=self.assets[-1], sim=self,intervals=self.maint_intervals,
                                                  duration=asset['maint_t_gen'], cost=asset['maint_cost_gen']))
                self.activate(self.services[-1], self.services[-1].service_routine())

            if self.inspect_intervals:
                self.services.append(Service(mode = 'inspection', asset=self.assets[-1], sim=self, intervals=self.inspect_intervals,
                                                  duration=asset['insp_t_gen'], cost=asset['insp_cost_gen']))
                self.activate(self.services[-1], self.services[-1].service_routine(), delay=inspect_delay)

            # create and activate the event process. Should DRY
            if 'failures' in asset['events']:
                for mode, data in asset['events']['failures'].iteritems():
                    self.events.append(Event(event_type='failure', mode = mode, asset=self.assets[-1], sim=self,
                                             randfunc=data[0], duration=data[1], cost=data[2]))
                    self.activate(self.events[-1], self.events[-1].halt_routine())
                    self.assets[-1].events.append(self.events[-1])
                    self.assets[-1].distributions['failure'][mode] = data
            if 'faults' in asset['events']:
                for mode, data in asset['events']['faults'].iteritems():
                    self.events.append(Event(event_type='fault', mode = mode, asset=self.assets[-1], sim=self,
                                             randfunc=data[0], duration=data[5], cost=data[6]))
                    self.activate(self.events[-1], self.events[-1].fault_routine())
                    self.assets[-1].events.append(self.events[-1])
                    self.assets[-1].distributions['fault'][mode] = data
            if 'incidents' in asset['events']:
                for mode, data in asset['events']['incidents'].iteritems():
                    self.events.append(Event(event_type='incident', mode = mode, asset=self.assets[-1], sim=self,
                                             randfunc=data[0], duration=data[1], cost=data[2]))
                    self.activate(self.events[-1], self.events[-1].halt_routine())
                    self.assets[-1].events.append(self.events[-1])
                    self.assets[-1].distributions['incident'][mode] = data

        self.simulate(until=self.max_time)

        # Output results
        if PRINTOUT:
            print "-------------------------------------"
            print "Results of simulation %s:" % (self.name)
            print "....................................."
            print "num of assets: ", len(self.assets)
        for asset in self.assets:
            self.total_output += asset.output
            self.total_cost += asset.cost
            self.total_lost_output += asset.total_event_time * asset.output_rate
            self.events_occurred[asset.name] = asset.events_occured
            self.total_event_time += asset.total_event_time
            self.time_operating += asset.time_operating
            self.failures_num += asset.failures_num
            self.faults_num += asset.faults_num
            self.incidents_env_num += asset.incidents_env_num
            self.incidents_saf_num += asset.incidents_saf_num
            self.faults_detected_num += asset.faults_detected_num

            if PRINTOUT:
                print "Process of asset %s:" % asset.name
                print "Total event time: ", asset.total_event_time
                print "Uptime: ", asset.time_operating
                print "Events:", [event_name for event_name in asset.events_occured]
                print "total revenue: %.2f" % asset.output
                print "total lost revenue: %.2f" % (asset.total_event_time*asset.output_rate)
                print "total cost: %.2f" % asset.cost
                print ".........................................."

## Experiment variables (Global vars) ........................

## Simulation ................................................

def main(rnd_seed=12345, max_time=0.,optime_scheduled=0., simulation_num=None, assets_data=None, assets_schedule=None, operation_vars=None):
    #write try except for the function inputs

    t_start = time()

    seed(rnd_seed)

    # global variables for the collection of all simulations
    simulations= []
    total_cost_avg = 0.
    total_output_avg = 0.
    total_lost_output_avg = 0.
    uptime_total_avg = 0.
    uptime_avg_avg = 0.
    failures_avg = 0.
    faults_avg = 0.
    incidents_saf_avg = 0.
    incidents_env_avg = 0.
    faults_detected_avg = 0.
    out_results = []
    revenues = []
    costs = []
    lost_revenues = []
    faults_detected = []
    failures = []
    incidents_saf = []
    incidents_env = []
    uptime_avg = []
    # initializing and running each simulation
    first_write = True
    batch = 10000
    batches = simulation_num / batch
    if batches < 1.:
        batches = 1
        batch = simulation_num
    # only for when simulation_num % batch = 0, if that's not the case, should modify the loop
    for i in range(batches):
        for j in range (batch):
            if PRINTOUT_FINAL:
                print "Running simulation: ", i*batch+j+1
                print "......................................"
            simulation = Operation(max_time, optime_scheduled, assets_schedule, assets_data, **operation_vars)
            simulation.name = "sim_"+str(i*batch+j+1)
            simulation.run()

            # output of a single simulation
            if PRINTOUT:
                print 'Operation events: ', simulation.events_occurred
                print 'Operation total event time: ', simulation.total_event_time
                print 'Operation total uptime: ', simulation.time_operating
                print 'Operation average uptime: ', simulation.time_operating/len(simulation.assets)
                print 'Operation total fault events: ', simulation.faults_num
                print 'Operation total detected faults: ', simulation.faults_detected_num
                print 'Operation total failure events: ', simulation.failures_num
                print 'Operation total safety incident events: ', simulation.incidents_saf_num
                print 'Operation total environmental incident events: ', simulation.incidents_env_num
                print 'Total revenue of the operation in simulation "%s": %.2f' %(simulation.name, simulation.total_output)
                print 'Total cost of the operation in simulation "%s": %.2f' %(simulation.name, simulation.total_cost)
                print 'Total lost revenue of the operation in simulation "%s": %.2f' %(simulation.name, simulation.total_lost_output)
                print 'Net profit of the operation in simulation "%s": %.2f' %(simulation.name, simulation.total_output - simulation.total_cost)
                print "....................................."


            costs.append(simulation.total_cost)
            revenues.append(simulation.total_output)
            failures.append(simulation.failures_num)
            incidents_saf.append(simulation.incidents_saf_num)
            incidents_env.append(simulation.incidents_env_num)
            faults_detected.append(simulation.faults_detected_num)
            uptime_avg.append(simulation.time_operating/len(simulation.assets))
            lost_revenues.append(simulation.total_lost_output)
            out_results.append([simulation.total_output, simulation.total_lost_output, simulation.total_cost, simulation.time_operating,
                                simulation.time_operating/len(simulation.assets),simulation.faults_num, simulation.faults_detected_num,
                                simulation.failures_num, simulation.incidents_saf_num, simulation.incidents_env_num])

            total_cost_avg += simulation.total_cost
            total_output_avg += simulation.total_output
            total_lost_output_avg += simulation.total_lost_output
            faults_avg += simulation.faults_num
            failures_avg += simulation.failures_num
            incidents_saf_avg += simulation.incidents_saf_num
            incidents_env_avg += simulation.incidents_env_num
            faults_detected_avg += simulation.faults_detected_num
            uptime_total_avg += simulation.time_operating
            uptime_avg_avg += simulation.time_operating/len(simulation.assets)

        if first_write is True:
            # tip: use raw strings for hardwired file paths, so that things like /t and /n don't get interpreted incorrectly
            with open(r'../results.csv', 'wb') as csvfile:
                reswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                reswriter.writerow(['Revenue', 'Lost Revenue', 'Cost', 'Total Uptime', 'Average Uptime', 'Faults',
                                    'Detected Faults', 'Failures', 'Safety Incidents', 'Environmental Incidents'])
                for row in out_results:
                    reswriter.writerow(row)
            if PLOTS:
                results_arr = np.array(out_results)
            first_write = False
        else:
            with open(r'../results.csv', 'a+b') as csvfile:
                reswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in out_results:
                    reswriter.writerow(row)
            if PLOTS:
                results_arr = np.append(results_arr, out_results, 0)

        out_results = []
        revenues = []
        costs = []
        lost_revenues = []
        faults_detected = []
        failures = []
        incidents_saf = []
        incidents_env = []
        uptime_avg = []
    # get rid of garbage
        gc.collect()


    total_cost_avg /= simulation_num
    total_output_avg /= simulation_num
    total_lost_output_avg /= simulation_num
    failures_avg /= simulation_num
    faults_avg /= simulation_num
    incidents_saf_avg /= simulation_num
    incidents_env_avg /= simulation_num
    faults_detected_avg /= simulation_num
    uptime_total_avg /= simulation_num
    uptime_avg_avg /= simulation_num

    t_end = time()
    t_sim = t_end - t_start

    results = {'total_output_avg': total_output_avg, 'total_lost_output_avg': total_lost_output_avg,
               'total_cost_avg': total_cost_avg, 'total_event_time':  simulation.total_event_time, 'events': simulation.events_occurred}


    # output of all simulations
    with open(r'../results_avg.csv', 'wb') as csvfile:
        reswriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        reswriter.writerow(['Revenue', 'Lost Revenue', 'Cost', 'Total Uptime', 'Average Uptime',
                            'Faults', 'Detected Faults', 'Failures', 'Safety Incidents', 'Environmental Incidents'])
        results_avg = [total_output_avg, total_lost_output_avg, total_cost_avg, uptime_total_avg,
                       uptime_avg_avg, faults_avg, faults_detected_avg, failures_avg, incidents_saf_avg, incidents_env_avg]
        reswriter.writerow(results_avg)

    if PRINTOUT_FINAL:
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
        print "Total computation time: %0.3fs" %(t_sim)

    if PLOTS:

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

        revenue_mils = results_arr[:,0]/1000000.
        hist_plot(revenue_mils, 'Revenue ($M)', 'fig1')

        revenue_loss_mils = results_arr[:,1]/1000000.
        hist_plot(revenue_loss_mils, 'Revenue Loss ($M)', 'fig2')

        cost_mils = results_arr[:,2]/1000000.
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

    if PRINTOUT:
        print "Simulation results data (total event time and list of occurred events is for the last simulation): ", results

    print "End of run."

    return results

if __name__ == "__main__":

    import doctest
    doctest.testmod()
    #select which case from the imported casedata file to simulate
    case_num = 1
    case = cdata.E.cases[case_num]
    main(rnd_seed=case['rnd_seed'], max_time=case['max_time'], optime_scheduled=case['max_time'], simulation_num=case['simulation_num'],
             assets_data=case['assets_data'], assets_schedule=case['assets_schedule'], operation_vars=case['operation_vars'])