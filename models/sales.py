from models.database import get_connection


def save_sale(
    employee_id,
    state_id,
    district_id,
    fertilizer_id,
    quantity,
    total_amount,
    sale_date
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO sales
        (
            employee_id,
            state_id,
            district_id,
            fertilizer_id,
            quantity,
            total_amount,
            sale_date
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            employee_id,
            state_id,
            district_id,
            fertilizer_id,
            quantity,
            total_amount,
            sale_date
        )
    )

    conn.commit()
    conn.close()