from queries import create_mentee, list_mentees, update_mentee, delete_mentee


def handle_create():
    try:
        full_name = input("Sheno emrin e plote te intern-it: ")
        email = input("Email: ")
        cohort = input("Sheno batch-in: ")
        mentee_id = create_mentee(full_name, email, cohort)
        print("Intern-i u shtua me sukses!")
    except Exception as e:
        print(f"Gabim: {e}")


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
    except Exception as e:
        print(f"Gabim: {e}")


def handle_delete():
    try:
        mentee_id = int(input(
            "Sheno id e internit qe deshironi ta largoni nga batch-i: "))
        delete_mentee(mentee_id)
        print("U fshi me sukses!")
    except Exception as e:
        print(f"Gabim: {e}")


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
