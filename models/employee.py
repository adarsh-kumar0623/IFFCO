from models.database import get_connection


class Employee:

    # ================= DASHBOARD =================

    @staticmethod
    def get_dashboard(employee_id):

        conn = get_connection()

        data = {}

        data["total_sales"] = conn.execute("""
            SELECT COUNT(*)
            FROM sales
            WHERE employee_id=?
        """,(employee_id,)).fetchone()[0]

        data["total_quantity"] = conn.execute("""
            SELECT IFNULL(SUM(quantity),0)
            FROM sales
            WHERE employee_id=?
        """,(employee_id,)).fetchone()[0]

        data["total_revenue"] = conn.execute("""
            SELECT IFNULL(SUM(total_amount),0)
            FROM sales
            WHERE employee_id=?
        """,(employee_id,)).fetchone()[0]

        conn.close()

        return data


    # ================= SAVE SALES =================

    @staticmethod
    def save_sale(
        employee_id,
        state_id,
        district_id,
        fertilizer_id,
        quantity
    ):

        conn = get_connection()

        price = conn.execute("""

            SELECT price_per_bag

            FROM fertilizers

            WHERE id=?

        """,(fertilizer_id,)).fetchone()[0]

        total = price * int(quantity)

        conn.execute("""

            INSERT INTO sales(

                employee_id,
                state_id,
                district_id,
                fertilizer_id,
                quantity,
                total_amount,
                sale_date

            )

            VALUES(

                ?,?,?,?,?,?,
                DATE('now')

            )

        """,
        (
            employee_id,
            state_id,
            district_id,
            fertilizer_id,
            quantity,
            total
        ))

        conn.commit()

        conn.close()


    # ================= HISTORY =================

    @staticmethod
    def get_sales_history(employee_id):

        conn = get_connection()

        history = conn.execute("""

            SELECT

                sales.id,
                sales.sale_date,
                states.state_name,
                districts.district_name,
                fertilizers.fertilizer_name,
                sales.quantity,
                sales.total_amount

            FROM sales

            JOIN states
            ON sales.state_id=states.id

            JOIN districts
            ON sales.district_id=districts.id

            JOIN fertilizers
            ON sales.fertilizer_id=fertilizers.id

            WHERE sales.employee_id=?

            ORDER BY sales.id DESC

        """,(employee_id,)).fetchall()

        conn.close()

        return history


    # ================= DELETE =================

    @staticmethod
    def delete_sale(sale_id):

        conn = get_connection()

        conn.execute("""

            DELETE FROM sales

            WHERE id=?

        """,(sale_id,))

        conn.commit()

        conn.close()