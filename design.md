# Design - CR05: Shift-Swap Approval

## 1. Proposed Approach

CR05 requests an approval process for shift swaps in FleetDesk. The proposed design separates submitting a swap request from approving or rejecting it.

A request should record the relevant shifts, the requesting user, the request status, and the approval decision. Only an authorized user should be able to approve or reject a request. The existing roster should be updated only after a valid approval.

This is a proposed design. The existing database schema, role permissions, and roster-update implementation must be inspected before the design can be finalized.

## 2. Proposed Workflow

1. An authorized user submits a shift-swap request.
2. The system validates the request and checks for conflicting shifts.
3. The request is stored with a pending status.
4. An authorized approver reviews the request.
5. The approver approves or rejects it.
6. If approved, the system validates the roster again and updates the shift assignments.
7. The system records the outcome and displays the updated status.

## 3. Test Cases

### Test Case 1: Valid Approval

**Input:** A valid shift-swap request is submitted and approved by an authorized approver.

**Expected result:** The request status becomes approved, and the roster is updated consistently.

### Test Case 2: Unauthorized Approval

**Input:** A user without approval permission attempts to approve a pending request.

**Expected result:** The system rejects the action and leaves the request and roster unchanged.

### Test Case 3: Conflicting Shift

**Input:** A request would assign a driver to overlapping shifts.

**Expected result:** The system prevents the conflicting swap and explains that the request cannot proceed.

### Test Case 4: Rejected Request

**Input:** An authorized approver rejects a pending shift-swap request.

**Expected result:** The request status becomes rejected, and the roster remains unchanged.

### Test Case 5: Regression Test - Existing Roster

**Input:** An existing driver roster is viewed and printed after the approval feature is introduced.

**Expected result:** Existing roster entries remain correct, and the roster-printing behavior continues to work as before.

## 4. Design Risks and Open Questions

- Which user roles can approve requests?
- Can an approver approve their own request?
- Are notifications required?
- What happens if a shift changes after a request is submitted?
- How will simultaneous approvals be prevented from creating conflicting roster assignments?

These questions should be resolved with the system requirements and existing implementation before development.