minesim
=======

Oilsands Mining Operations Simulator v0.7.5.2 based on the thesis of Rezsa Farahani titled: 
Design, simulation, and evaluation of effective industrial information systems: case of machine condition monitoring
and maintenance management information systems

Thesis available on www.rezsa.com


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
