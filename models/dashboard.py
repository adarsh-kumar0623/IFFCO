from models.database import get_connection


# =====================================================
# DASHBOARD SUMMARY
# =====================================================

def get_dashboard_summary():

    conn = get_connection()

    data = {}

    data["total_sales"] = conn.execute("""
        SELECT COUNT(*)
        FROM sales
    """).fetchone()[0]

    data["total_revenue"] = conn.execute("""
        SELECT IFNULL(SUM(total_amount),0)
        FROM sales
    """).fetchone()[0]

    data["total_employees"] = conn.execute("""
        SELECT COUNT(*)
        FROM employees
        WHERE role='employee'
    """).fetchone()[0]

    data["total_states"] = conn.execute("""
        SELECT COUNT(*)
        FROM states
    """).fetchone()[0]

    data["total_districts"] = conn.execute("""
        SELECT COUNT(*)
        FROM districts
    """).fetchone()[0]

    data["total_fertilizers"] = conn.execute("""
        SELECT COUNT(*)
        FROM fertilizers
    """).fetchone()[0]

    data["top_state"] = conn.execute("""
        SELECT
            states.state_name,
            SUM(total_amount) total
        FROM sales
        JOIN states
        ON sales.state_id=states.id
        GROUP BY states.state_name
        ORDER BY total DESC
        LIMIT 1
    """).fetchone()

    data["top_employee"] = conn.execute("""
        SELECT
            employees.name,
            SUM(total_amount) total
        FROM sales
        JOIN employees
        ON sales.employee_id=employees.employee_id
        GROUP BY employees.name
        ORDER BY total DESC
        LIMIT 1
    """).fetchone()

    data["top_fertilizer"] = conn.execute("""
        SELECT
            fertilizers.fertilizer_name,
            SUM(quantity) total
        FROM sales
        JOIN fertilizers
        ON sales.fertilizer_id=fertilizers.id
        GROUP BY fertilizers.fertilizer_name
        ORDER BY total DESC
        LIMIT 1
    """).fetchone()

    data["average_sale"] = conn.execute("""
        SELECT
            IFNULL(AVG(total_amount),0)
        FROM sales
    """).fetchone()[0]

    conn.close()

    return data


# =====================================================
# MONTHLY SALES CHART
# =====================================================

def monthly_sales_chart():

    conn = get_connection()

    rows = conn.execute("""

        SELECT

            strftime('%m',sale_date) month,

            SUM(total_amount) total

        FROM sales

        GROUP BY month

        ORDER BY month

    """).fetchall()

    conn.close()

    labels = [

        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"

    ]

    values = [0]*12

    for row in rows:

        values[int(row["month"])-1] = row["total"]

    return labels, values
# =====================================================
# STATE SALES CHART
# =====================================================

def state_sales_chart():

    conn = get_connection()

    rows = conn.execute("""

        SELECT

            states.state_name,

            SUM(total_amount) total

        FROM sales

        JOIN states

        ON sales.state_id = states.id

        GROUP BY states.state_name

        ORDER BY total DESC

        LIMIT 5

    """).fetchall()

    conn.close()

    labels = [row["state_name"] for row in rows]

    values = [row["total"] for row in rows]

    return labels, values


# =====================================================
# TOP FERTILIZER CHART
# =====================================================

def fertilizer_sales_chart():

    conn = get_connection()

    rows = conn.execute("""

        SELECT

            fertilizers.fertilizer_name,

            SUM(quantity) total

        FROM sales

        JOIN fertilizers

        ON sales.fertilizer_id = fertilizers.id

        GROUP BY fertilizers.fertilizer_name

        ORDER BY total DESC

        LIMIT 5

    """).fetchall()

    conn.close()

    labels = [row["fertilizer_name"] for row in rows]

    values = [row["total"] for row in rows]

    return labels, values


# =====================================================
# TOP EMPLOYEE CHART
# =====================================================

def employee_sales_chart():

    conn = get_connection()

    rows = conn.execute("""

        SELECT

            employees.name,

            COUNT(*) total

        FROM sales

        JOIN employees

        ON sales.employee_id = employees.employee_id

        GROUP BY employees.name

        ORDER BY total DESC

        LIMIT 5

    """).fetchall()

    conn.close()

    labels = [row["name"] for row in rows]

    values = [row["total"] for row in rows]

    return labels, values


# =====================================================
# RECENT SALES
# =====================================================

def recent_sales(limit=10):

    conn = get_connection()

    rows = conn.execute("""

        SELECT

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

    return rows
