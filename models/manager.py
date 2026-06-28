from models.database import get_connection
import sqlite3


class Manager:

    # ================= DASHBOARD =================

    @staticmethod
    def get_recent_sales(limit=10):

        conn = get_connection()

        sales = conn.execute("""

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
            ON sales.state_id = states.id

            JOIN districts
            ON sales.district_id = districts.id

            JOIN fertilizers
            ON sales.fertilizer_id = fertilizers.id

            ORDER BY sales.id DESC

            LIMIT ?

        """, (limit,)).fetchall()

        conn.close()

        return sales


    # ================= EMPLOYEES =================

    @staticmethod
    def get_all_employees():

        conn = get_connection()

        employees = conn.execute("""

            SELECT *

            FROM employees

            WHERE role='employee'

            ORDER BY name

        """).fetchall()

        conn.close()

        return employees


    # ================= ADD EMPLOYEE =================

    @staticmethod
    def add_employee(
        employee_id,
        name,
        email,
        designation,
        password
    ):

        conn = get_connection()

        try:

            check = conn.execute("""

                SELECT employee_id

                FROM employees

                WHERE employee_id=?
                OR email=?

            """, (
                employee_id,
                email
            )).fetchone()

            if check:

                return False

            conn.execute("""

                INSERT INTO employees(

                    employee_id,
                    name,
                    email,
                    designation,
                    password,
                    role

                )

                VALUES(

                    ?,?,?,?,?,?

                )

            """, (

                employee_id,
                name,
                email,
                designation,
                password,
                "employee"

            ))

            conn.commit()

            return True

        except sqlite3.Error:

            return False

        finally:

            conn.close()


    # ================= UPDATE =================

    @staticmethod
    def update_employee(
        employee_id,
        name,
        email,
        designation
    ):

        conn = get_connection()

        try:

            conn.execute("""

                UPDATE employees

                SET

                    name=?,

                    email=?,

                    designation=?

                WHERE employee_id=?

            """, (

                name,

                email,

                designation,

                employee_id

            ))

            conn.commit()

            return True

        except sqlite3.Error:

            return False

        finally:

            conn.close()


    # ================= DELETE =================

    @staticmethod
    def delete_employee(employee_id):

        conn = get_connection()

        try:

            conn.execute("""

                DELETE FROM employees

                WHERE employee_id=?

            """, (employee_id,))

            conn.commit()

            return True

        except sqlite3.Error:

            return False

        finally:

            conn.close()


    # ================= SINGLE EMPLOYEE =================

    @staticmethod
    def get_employee(employee_id):

        conn = get_connection()

        employee = conn.execute("""

            SELECT *

            FROM employees

            WHERE employee_id=?

        """, (employee_id,)).fetchone()

        conn.close()

        return employee