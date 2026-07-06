from models.database import get_connection


class Employee:

    # =====================================================
    # DASHBOARD
    # =====================================================

    @staticmethod
    def get_dashboard(employee_id):

        conn = get_connection()

        data = {}

        # ================= TOTAL SALES =================

        data["total_sales"] = conn.execute("""

            SELECT COUNT(*)

            FROM sales

            WHERE employee_id=?

        """, (employee_id,)).fetchone()[0]

        # ================= TOTAL QUANTITY =================

        data["total_quantity"] = conn.execute("""

            SELECT IFNULL(SUM(quantity),0)

            FROM sales

            WHERE employee_id=?

        """, (employee_id,)).fetchone()[0]

        # ================= TOTAL REVENUE =================

        data["total_revenue"] = conn.execute("""

            SELECT IFNULL(SUM(total_amount),0)

            FROM sales

            WHERE employee_id=?

        """, (employee_id,)).fetchone()[0]

        # ================= THIS MONTH =================

        data["this_month_sales"] = conn.execute("""

            SELECT COUNT(*)

            FROM sales

            WHERE employee_id=?

            AND strftime('%m',sale_date)=strftime('%m','now')

        """, (employee_id,)).fetchone()[0]

        # ================= LAST MONTH =================

        data["last_month_sales"] = conn.execute("""

            SELECT COUNT(*)

            FROM sales

            WHERE employee_id=?

            AND strftime('%m',sale_date)=strftime('%m','now','-1 month')

        """, (employee_id,)).fetchone()[0]

        last = data["last_month_sales"]

        current = data["this_month_sales"]

        if last == 0:

            growth = 100 if current > 0 else 0

        else:

            growth = round(

                ((current-last)/last)*100,

                2

            )

        data["growth"] = growth

        if growth >= 20:

            data["performance"] = "Excellent"

        elif growth >= 5:

            data["performance"] = "Good"

        elif growth >= 0:

            data["performance"] = "Average"

        else:

            data["performance"] = "Needs Improvement"

        # ================= BEST FERTILIZER =================

        best = conn.execute("""

            SELECT

                fertilizers.fertilizer_name,

                SUM(quantity) total

            FROM sales

            JOIN fertilizers

            ON sales.fertilizer_id=fertilizers.id

            WHERE employee_id=?

            GROUP BY fertilizers.fertilizer_name

            ORDER BY total DESC

            LIMIT 1

        """, (employee_id,)).fetchone()

        data["best_fertilizer"] = (

            best["fertilizer_name"]

            if best else "--"

        )

        # ================= TARGET =================

        data["target"] = 500

        data["achievement"] = round(

            (data["total_quantity"]/500)*100,

            2

        ) if data["total_quantity"] else 0
        # ================= MONTHLY SALES CHART =================

        chart = conn.execute("""

            SELECT

                strftime('%m',sale_date) AS month,

                SUM(quantity) AS qty

            FROM sales

            WHERE employee_id=?

            GROUP BY month

            ORDER BY month

        """, (employee_id,)).fetchall()

        month_names = [

            "Jan","Feb","Mar","Apr",
            "May","Jun","Jul","Aug",
            "Sep","Oct","Nov","Dec"

        ]

        labels = []

        values = []

        for row in chart:

            labels.append(

                month_names[int(row["month"])-1]

            )

            values.append(

                row["qty"]

            )

        data["chart_labels"] = labels

        data["chart_values"] = values

        conn.close()

        return data


    # =====================================================
    # GET PROFILE
    # =====================================================

    @staticmethod
    def get_profile(employee_id):

        conn = get_connection()

        profile = conn.execute("""

            SELECT *

            FROM employees

            WHERE employee_id=?

        """, (employee_id,)).fetchone()

        conn.close()

        return profile


    # =====================================================
    # UPDATE PROFILE
    # =====================================================

    @staticmethod
    def update_profile(

        employee_id,

        phone,

        email,

        address,

        state,

        district

    ):

        conn = get_connection()

        conn.execute("""

            UPDATE employees

            SET

                phone=?,

                email=?,

                address=?,

                state=?,

                district=?

            WHERE employee_id=?

        """,(

            phone,

            email,

            address,

            state,

            district,

            employee_id

        ))

        conn.commit()

        conn.close()


    # =====================================================
    # SAVE SALE
    # =====================================================

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

        total = int(quantity) * float(price)

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

        """,(

            employee_id,

            state_id,

            district_id,

            fertilizer_id,

            quantity,

            total

        ))

        conn.commit()

        conn.close()
            # =====================================================
    # SALES HISTORY
    # =====================================================

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
            ON sales.state_id = states.id

            JOIN districts
            ON sales.district_id = districts.id

            JOIN fertilizers
            ON sales.fertilizer_id = fertilizers.id

            WHERE sales.employee_id=?

            ORDER BY sales.id DESC

        """, (employee_id,)).fetchall()

        conn.close()

        return history


    # =====================================================
    # DELETE SALE
    # =====================================================

    @staticmethod
    def delete_sale(sale_id):

        conn = get_connection()

        conn.execute("""

            DELETE FROM sales

            WHERE id=?

        """, (sale_id,))

        conn.commit()

        conn.close()


    # =====================================================
    # EMPLOYEE DETAILS
    # =====================================================

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