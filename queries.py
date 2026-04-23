from db import get_connection


def create_mentee(full_name: str, email: str, cohort: str) -> int:
    with get_connection() as connection:  # thirret funksioni qe ben lidhjen me databaze(perdoret with pasi qe mbyllja behet automatikisht)
        with connection.cursor() as cur:  # me cursor iu qasemi tabelave ne databaze
            cur.execute("INSERT INTO mentees (full_name, email, cohort) VALUES (%s, %s, %s) RETURNING id",
                        # me execute e kemi dergu sql query-n ne databaze per run
                        (full_name, email, cohort)
                        )
            row = cur.fetchone()  # me fetch merren te dhenat qe kthehn prej databazes
            return row[0]


def list_mentees() -> list[tuple]:
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute(
                "SELECT id, full_name, email, cohort, enrolled_on FROM mentees ORDER BY full_name")
            return cur.fetchall()


def update_mentee(mentee_id: int, new_cohort: str) -> bool:
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute("UPDATE mentees SET cohort = %s WHERE id = %s",
                        (new_cohort, mentee_id)
                        )
            return cur.rowcount == 1


def delete_mentee(mentee_id: int) -> bool:
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute("DELETE from mentees WHERE id = %s", (mentee_id,))
            return cur.rowcount == 1


def average_score_per_mentee():
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute("""
                SELECT mentees.full_name,
                       AVG(assessment_scores.score * 100.0 / assessments.max_score) AS average_pct
                FROM mentees
                JOIN assessment_scores ON mentees.id = assessment_scores.mentee_id
                JOIN assessments ON assessment_scores.assessment_id = assessments.id
                GROUP BY mentees.full_name
                ORDER BY mentees.full_name
            """)
            return cur.fetchall()


def mentees_below_threshold(threshold_pct):
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute("""
                SELECT mentees.full_name,
                       AVG(assessment_scores.score * 100.0 / assessments.max_score) AS average_pct
                FROM mentees
                JOIN assessment_scores ON mentees.id = assessment_scores.mentee_id
                JOIN assessments ON assessment_scores.assessment_id = assessments.id
                GROUP BY mentees.full_name
                HAVING AVG(assessment_scores.score * 100.0 / assessments.max_score) < %s
            """, (threshold_pct,))
            return cur.fetchall()


def assessment_summary():
    with get_connection() as connection:
        with connection.cursor() as cur:
            cur.execute("""
                SELECT assessments.title,
                       COUNT(assessment_scores.mentee_id),
                       MAX(assessment_scores.score),
                       MIN(assessment_scores.score),
                       AVG(assessment_scores.score)
                FROM assessments
                JOIN assessment_scores ON assessments.id = assessment_scores.assessment_id
                GROUP BY assessments.title
            """)
            return cur.fetchall()
