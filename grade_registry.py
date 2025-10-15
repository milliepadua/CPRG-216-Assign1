"""
grade_registry.py
Author: Vitor De Oliveira Peixoto (group member)
Date: 2025-10-09
Description:
    Grade Registry Program using only constructs from Modules 1 & 2.
    Inputs: interactive console prompts asking whether to add students, their names, and GPAs per subject.
    Processing: for each student, collect GPA values (until -1), compute an average (0 if none),
                and store name->average in a dictionary (in insertion order).  Loop until user exits.
    Output: final list of students with their accumulative average GPAs, formatted to match the test plan.
"""

from collections import OrderedDict

def format_gpa(value):
    """Format a float to match examples: up to 2 decimals, drop trailing zeros and dot."""
    # Round to 2 decimals as per examples
    rounded = round(value + 1e-12, 2)
    s = f"{rounded:.2f}".rstrip("0").rstrip(".")
    return s

def main():
    students = OrderedDict()

    print("Welcome to the Grade Registry Program")
    while True:
        print("Would you like to add a new student? y(yes),n(no)")
        ans = input()

        # Normalize input
        low = ans.strip().lower()
        if low in ("y", "yes"):
            # Ask for student name
            print("Enter the student's name:")
            name = input().strip()

            # Ask for GPAs
            print("Enter student GPA for each subject. Enter -1 to stop entering GPA.")
            gpas = []

            while True:
                entry = input().strip()
                # Sentinel
                if entry == "-1":
                    break
                # Accept only valid numeric entries
                try:
                    gpa = float(entry)
                    gpas.append(gpa)
                except ValueError:
                    # If it's not -1 and not a number, prompt again silently (stay close to basic constructs)
                    # Alternatively, we could print a message, but the test plan doesn't specify one here.
                    continue

            # Compute and store average (or 0 if none)
            if len(gpas) == 0:
                avg = 0.0
            else:
                avg = sum(gpas) / len(gpas)

            students[name] = avg

        elif low in ("n", "no"):
            break
        else:
            print("Incorrect Input, please enter y(yes)/n(no).")
            # Loop continues

    print("This is the list of students in the system, and their corresponding accumulative GPA")
    for name, avg in students.items():
        # If there were no GPAs, show 0 as in the example, not 0.0
        if isinstance(avg, float) and abs(avg) < 1e-12:
            print(f"{name} 0")
        else:
            print(f"{name} {format_gpa(avg)}")

if __name__ == "__main__":
    main()
