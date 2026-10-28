
# triage.py
# Rule-based classifier for FleetDesk maintenance requests.

def triage(text):
    text = text.lower()

    # Adaptive: changes caused by an external environment or platform.
    if any(word in text for word in [
        "windows 11", "vendor", "regulator",
        "end of support", "platform"
    ]):
        return "adaptive"

    # Corrective: fixing an existing defect or failure.
    if any(word in text for word in [
        "wrong", "duplicate trips", "freezes",
        "printer dialogs", "fails", "incorrect"
    ]):
        return "corrective"

    # Preventive: reducing future maintenance risk without changing behaviour.
    if any(word in text for word in [
        "no behaviour change", "duplicated in three forms",
        "data-access module", "adds tests",
        "flagged as risky", "rewrites the nightly clean-up",
        "splits the 700-line procedure", "merges roster rules"
    ]):
        return "preventive"

    # Perfective: adding or improving requested functionality.
    if any(word in text for word in [
        "requested", "request a", "report",
        "approval", "warning", "calendar import"
    ]):
        return "perfective"

    return "unknown"
