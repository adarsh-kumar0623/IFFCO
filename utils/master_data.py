import sqlite3

DB_PATH = "database/iffco.db"


def get_states():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    data = conn.execute("""
        SELECT id, state_name
        FROM states
        ORDER BY state_name
    """).fetchall()

    conn.close()

    return data


def get_districts(state_id):

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    data = conn.execute("""
        SELECT
            id,
            district_name
        FROM districts
        WHERE state_id = ?
        ORDER BY district_name
    """, (state_id,)).fetchall()

    conn.close()

    return data


def get_fertilizers():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    data = conn.execute("""
        SELECT
            id,
            fertilizer_name,
            price_per_bag
        FROM fertilizers
        ORDER BY fertilizer_name
    """).fetchall()

    conn.close()

    return data


def get_price(fertilizer_id):

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    data = conn.execute("""
        SELECT price_per_bag
        FROM fertilizers
        WHERE id=?
    """, (fertilizer_id,)).fetchone()

    conn.close()

    return data