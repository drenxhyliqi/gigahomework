"""
app.py — GigaAcademy Mentees Tracker

Level 1: Implement the four CRUD functions below, then wire up the menu loop.
Level 2: See hints at the bottom of this file and in the brief.

Rules (non-negotiable):
  - Use psycopg v3 for the database driver.
  - Use parameterised queries (%s placeholders). NEVER f-strings or concatenation.
  - Read connection details from environment variables (see .env.example).
  - Commit your inserts/updates/deletes.
"""

import os
import sys

import psycopg
from dotenv import load_dotenv

load_dotenv()


# ---------------------------------------------------------------------------
# Connection helper
# ---------------------------------------------------------------------------

def get_connection():
    """Open a new connection using environment variables.

    Returns a psycopg.Connection. Caller is responsible for closing it,
    or use it as a context manager: `with get_connection() as conn: ...`
    """
    return psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


# ---------------------------------------------------------------------------
# Level 1 — CRUD functions (YOU implement these)
# ---------------------------------------------------------------------------

def create_mentee(full_name: str, email: str, cohort: str) -> int:
    """Insert a new mentee. Return the new mentee's id.

    TODO: Implement using a parameterised INSERT ... RETURNING id.
    """
    with get_connection() as connection:  # thirret funksioni qe ben lidhjen me databaze(perdoret with pasi qe mbyllja behet automatikisht)
        with connection.cursor() as cur:  # me cursor iu qasemi tabelave ne databaze
            cur.execute("INSERT INTO mentees (full_name, email, cohort) VALUES (%s, %s, %s) RETURNING id",
                        # me execute e kemi dergu sql query-n ne databaze per run
                        (full_name, email, cohort)
                        )
            row = cur.fetchone()  # me fetch merren te dhenat qe kthehn prej databazes
            return row[0]


def list_mentees() -> list[tuple]:
    """Return all mentees as a list of tuples, sorted by full_name.

    TODO: Implement using SELECT. Each row should contain
    (id, full_name, email, cohort, enrolled_on).
    """
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute(
                "SELECT id, full_name, email, cohort, enrolled_on FROM mentees ORDER BY full_name")
            return cur.fetchall()


def update_mentee(mentee_id: int, new_cohort: str) -> bool:
    """Update a mentee's cohort. Return True if a row was updated, False otherwise.

    TODO: Implement using UPDATE. Check cursor.rowcount.
    """
    raise NotImplementedError("Implement update_mentee")


def delete_mentee(mentee_id: int) -> bool:
    """Delete a mentee by id. Return True if a row was deleted, False otherwise.

    TODO: Implement using DELETE. Check cursor.rowcount.
    """
    raise NotImplementedError("Implement delete_mentee")


# ---------------------------------------------------------------------------
# Menu loop (YOU implement this for Level 1)
# ---------------------------------------------------------------------------

def print_menu() -> None:
    print()
    print("GigaAcademy Mentees Tracker")
    print("  1) Add mentee")
    print("  2) List mentees")
    print("  3) Update cohort")
    print("  4) Delete mentee")
    print("  0) Quit")


def run_menu() -> None:
    """Run the interactive CLI menu.

    TODO: Loop until the user picks 0. Handle bad input gracefully — no
    tracebacks should ever be shown to the user. Wrap DB calls in try/except
    and print friendly error messages.
    """
    raise NotImplementedError("Implement run_menu")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        run_menu()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)


# ===========================================================================
# LEVEL 2 HINTS (ignore if you're on Level 1)
# ===========================================================================
#
# 1. Split this file. Create a package with:
#       db.py     -> get_connection()
#       queries.py -> all the SQL functions
#       cli.py     -> argparse subparsers that call into queries.py
#       app.py    -> just the entry point
#
# 2. For Part B (transactions), the pattern is:
#
#       with get_connection() as conn:
#           with conn.cursor() as cur:
#               cur.execute(...)  # insert assessment
#               for email, score in scores_by_email.items():
#                   cur.execute(...)  # insert score
#       # psycopg commits on successful __exit__ of the connection context,
#       # and rolls back if any exception propagated out.
#
# 3. For Part C, start with `argparse.ArgumentParser` and use `.add_subparsers()`
#    for the `mentee`, `report`, and `assessment` command groups.
