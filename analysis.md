# Analysis - CR05: Shift-Swap Approval

## 1. Change Request

- **Request ID:** CR05
- **Release:** R2
- **Effort estimate:** 48 hours
- **Description:** Shift-swap approval requested
- **Maintenance category:** Perfective

## 2. Classification and Reason

CR05 is classified as perfective maintenance because it introduces a requested capability for FleetDesk users. The request adds an approval process for shift swaps rather than correcting an existing defect or adapting the system to a new external environment.

## 3. Parts of the System Potentially Affected

The following areas may need changes:

- Shift-swap request interface
- Approval and rejection workflow
- User permissions and role checks
- Database records for swap requests and approval status
- Notifications or status messages, if supported by the existing system

These are potential impact areas based on the request, not verified source-code locations.

## 4. Effort Estimate

The supplied maintenance ledger estimates 48 hours for CR05. This is the recorded estimate, not a newly measured implementation time.

## 5. Risk Assessment

**Risk level: Medium (initial assessment).**

The change may affect shift assignments and approval permissions. Incorrect handling could result in unauthorized or inconsistent changes to the roster. Before implementation, the existing approval rules, user roles, and roster-update process should be inspected.

## 6. Information Still Required

The request description does not specify approval roles, notification requirements, or rules for conflicting shifts. These details must be confirmed before the design is finalized.