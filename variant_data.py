# variant_data.py - VARIANT B (last digit 1, 5 or 9): FleetDesk
REG_NO = "B23F0399SE015"

# (id, release, hours, description)
CHANGES = [
    ("CR01", "R1", 42, "Depot managers request a driver-rest warning on the roster screen (REQ-12)"),
    ("CR02", "R1", 34, "Developer, with no ticket or request, merges roster rules duplicated in three forms; no behaviour change"),
    ("CR03", "R1", 26, "Roster printout shows duplicate trips after a bus swap (ticket B -207)"),
    ("CR04", "R2", 28, "Windows 11 rollout breaks the client's printer dialogs; client updated (IT notice N-5)"),
    ("CR05", "R2", 48, "Depot managers request shift-swap approval (REQ-19)"),
    ("CR06", "R2", 30, "Team lead, with no ticket or request, replaces SQL strings in the client with one data-access module; no behaviour change"),
    ("CR07", "R3", 20, "Overtime total is wrong for night shifts that cross midnight (ticket B-231)"),
    ("CR08", "R3", 48, "Planners request a route-wise fuel-use report (REQ-27)"),
    ("CR09", "R3", 38, "Developer, with no ticket or request, splits the 700-line procedure sp_build_roster and adds tests; no behaviour change"),
    ("CR10", "R4", 32, "Labour regulator requires overtime records kept for seven years; archive routine added (notice in file LAB-3)"),
    ("CR11", "R4", 50, "Planners request holiday-calendar import (REQ-35); the date code had to be cleaned up first because it was too tangled to extend"),
    ("CR12", "R4", 20, "Client freezes when the depot list is empty (ticket B-260)"),
    ("CR13", "R5", 46, "Database vendor ends support for version 12; procedures re-tested and ported to version 15"),
    ("CR14", "R5", 44, "Developer, with no ticket or request, rewrites the nightly clean-up scripts that a code review flagged as risky; no behaviour change"),
]

MY_CLASS = {
    "CR01": "perfective",
    "CR02": "preventive",
    "CR03": "corrective",
    "CR04": "adaptive",
    "CR05": "perfective",
    "CR06": "preventive",
    "CR07": "corrective",
    "CR08": "perfective",
    "CR09": "preventive",
    "CR10": "adaptive",
    "CR11": "perfective",
    "CR12": "corrective",
    "CR13": "adaptive",
    "CR14": "preventive",
}

RELEASES = { # kloc = thousand lines of code, cc = average cyclomatic complexity per routine
    "R1": dict(kloc=80, cc=17.4, defects=9),
    "R2": dict(kloc=86, cc=17.1, defects=9),
    "R3": dict(kloc=93, cc=16.9, defects=10),
    "R4": dict(kloc=99, cc=16.8, defects=10),
    "R5": dict(kloc=106, cc=16.6, defects=10),
}

PROFILE = { # scores 1 (worst) to 5 (best) for every factor
    "name": "FleetDesk", "years_in_production": 12,
    "facts": [
        "F1 A thick Delphi client on 38 depot PCs talks straight to one shared database server.",
        "F2 Rules are split between client forms, 64 stored procedures and 9 triggers; no map exists.",
        "F3 Three staff built it; two left. The last, sole expert on sp_build_roster, retires in 9 months.",
        "F4 It builds the daily duty roster for 1,200 drivers; if it is down, buses do not leave.",
        "F5 The manual describes the original screens; 21 of the 33 screens have changed since.",
        "F6 No incident in 2 years, but every release needs 3 weeks of manual testing.",
        "F7 Payroll and the depot managers' daily bus allocation both read the roster file it produces.",
    ],
    "quality": {"complexity": 2, "modularity": 1, "test_coverage": 2,
                "documentation_accuracy": 1, "change_safety": 2},
    "value": {"central_to_daily_operations": 5, "people_who_depend_on_it": 4, "cost_of_absence": 5},
    "rules_still_valid_pct": 85, "alternative_fit_pct": 40,
    "platform_end_of_support_months": None, "key_expert_leaving_months": 9,
}
