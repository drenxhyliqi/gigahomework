import psycopg
from queries import (
    create_mentee, list_mentees, update_mentee, delete_mentee,
    average_score_per_mentee, mentees_below_threshold, assessment_summary
)
import argparse


def handle_create():
    try:
        full_name = input("Sheno emrin e plote te intern-it: ")
        email = input("Email: ")
        cohort = input("Sheno batch-in: ")
        mentee_id = create_mentee(full_name, email, cohort)
        print("Intern-i u shtua me sukses!")
    except psycopg.errors.UniqueViolation:
        print(f"Gabim: Ky email ekzsiton!")
    except psycopg.errors.ForeignKeyViolation:
        print(f"Gabim: Kjo ID nuk ekzsiton!")
    except Exception as e:
        print(f"Gabim {e}")


def handle_list():
    try:
        mentees = list_mentees()
        for m in mentees:
            print(m)
    except Exception as e:
        print(f"Gabim: {e}")


def handle_update():
    try:
        mentee_id = int(input(
            "Sheno id-n e internit qe deshironi t'ia ndryshoni batch-in: "))
        new_cohort = input("Sheno batch-in e ri: ")
        update_mentee(mentee_id, new_cohort)
        print("Perditesimi u krye me sukses")
    except ValueError:
        print(f"Gabim: ID duhet te jete numer")
    except Exception as e:
        print(f"Gabim gjate perditesimit: {e}")


def handle_delete():
    try:
        mentee_id = int(input(
            "Sheno id e internit qe deshironi ta largoni nga batch-i: "))
        delete_mentee(mentee_id)
        print("U fshi me sukses!")
    except ValueError:
        print(f"Gabim ID duhet te jete numer")
    except Exception as e:
        print(f"Gabim gjate fshirjes: {e}")


def print_menu() -> None:
    print()
    print("GigaAcademy Mentees Tracker")
    print("  1) Add mentee")
    print("  2) List mentees")
    print("  3) Update cohort")
    print("  4) Delete mentee")
    print("  0) Quit")


def run_menu() -> None:
    while True:
        print_menu()
        zgjedh = input("Zgjedh: ")
        if zgjedh == "0":
            break
        elif zgjedh == "1":
            handle_create()
        elif zgjedh == "2":
            handle_list()
        elif zgjedh == "3":
            handle_update()
        elif zgjedh == "4":
            handle_delete()
        else:
            print("Ky inputt nuk pranohet provo perseri!")


def run_cli():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Per krijim te mentee
    mentee = subparsers.add_parser("mentee")
    mentee_sub = mentee.add_subparsers()

    # Per listim te mentees
    mentee_list = mentee_sub.add_parser("list")
    mentee_list.set_defaults(func=lambda args: handle_list())

    # mentee add
    mentee_add = mentee_sub.add_parser("add")
    mentee_add.add_argument("--name", required=True)
    mentee_add.add_argument("--email", required=True)
    mentee_add.add_argument("--cohort", required=True)
    mentee_add.set_defaults(func=lambda args: create_mentee(
        args.name, args.email, args.cohort))

    # mentee update
    mentee_update = mentee_sub.add_parser("update")
    mentee_update.add_argument("--id", required=True, type=int)
    mentee_update.add_argument("--cohort", required=True)
    mentee_update.set_defaults(
        func=lambda args: update_mentee(args.id, args.cohort))

    # mentee delete
    mentee_delete = mentee_sub.add_parser("delete")
    mentee_delete.add_argument("--id", required=True, type=int)
    mentee_delete.set_defaults(func=lambda args: delete_mentee(args.id))

    # -- report --
    report = subparsers.add_parser("report")
    report_sub = report.add_subparsers()

    # report averages
    report_avg = report_sub.add_parser("averages")
    report_avg.set_defaults(
        func=lambda args: [print(r) for r in average_score_per_mentee()])

    # report below
    report_below = report_sub.add_parser("below")
    report_below.add_argument("--threshold", required=True, type=float)
    report_below.set_defaults(func=lambda args: [print(
        r) for r in mentees_below_threshold(args.threshold)])

    # report assessments
    report_assess = report_sub.add_parser("assessments")
    report_assess.set_defaults(
        func=lambda args: [print(r) for r in assessment_summary()])

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
