# FleetDesk Maintenance Log

**Registration Number:** B23F0399SE015  
**Selected Change Request:** CR05  
**Change Request:** Shift-swap approval requested  
**Release:** R2  
**Estimated Effort:** 48 hours  
**Maintenance Category:** Perfective

## 1. Identification

Recorded CR05 in `requests.csv`. The request concerns adding shift-swap approval functionality to FleetDesk.

## 2. Analysis

Reviewed the change request and classified it as perfective maintenance because it requests an enhancement to the existing system. Documented the potential affected areas, initial risk assessment, and questions requiring clarification in `analysis.md`.

## 3. Design

Documented the proposed workflow and five test cases in `design.md`. The cases cover valid approval, unauthorized approval, conflicting shifts, rejected requests, and regression testing of the existing roster.

## 4. Implementation and Testing

Implemented a rule-based maintenance-request classifier in `triage.py` and added automated tests in `test_triage.py`. The reference classifications are defined in `variant_data.py`.

The initial test run reported five failing change-request classifications. After revising the classification rules, the subsequent test run completed successfully:

- Test method executed: 1
- Change requests checked: 14
- Classification mismatches in the final run: 0
- Final test status: OK

Command used:

`python -m unittest -v test_triage`

## 5. Release

The release stage records the completed maintenance workflow and its verification evidence. The release commit and annotated Git tag are to be created after the release files and repository history are checked.

## Git Commit History

1. `852db9a` - CR05 Identification
2. `e5c62b8` - CR05 Analysis
3. `100f5ed` - CR05 Design
4. `5e45ee3` - CR05 Implementation and Test

**Release status:** Pending final release commit and tag.