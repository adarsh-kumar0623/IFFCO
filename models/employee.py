# ================= DASHBOARD =================

@staticmethod
def get_dashboard(employee_id):

    conn = get_connection()

    data = {}

    # ==========================================
    # TOTAL SALES
    # ==========================================

    data["total_sales"] = conn.execute("""

        SELECT COUNT(*)

        FROM sales

        WHERE employee_id=?

    """, (employee_id,)).fetchone()[0]

    # ==========================================
    # TOTAL QUANTITY
    # ==========================================

    data["total_quantity"] = conn.execute("""

        SELECT IFNULL(SUM(quantity),0)

        FROM sales

        WHERE employee_id=?

    """, (employee_id,)).fetchone()[0]

    # ==========================================
    # TOTAL REVENUE
    # ==========================================

    data["total_revenue"] = conn.execute("""

        SELECT IFNULL(SUM(total_amount),0)

        FROM sales

        WHERE employee_id=?

    """, (employee_id,)).fetchone()[0]

    # ==========================================
    # THIS MONTH SALES
    # ==========================================

    data["this_month_sales"] = conn.execute("""

        SELECT COUNT(*)

        FROM sales

        WHERE employee_id=?

        AND strftime('%m',sale_date)=strftime('%m','now')

    """, (employee_id,)).fetchone()[0]

    # ==========================================
    # LAST MONTH SALES
    # ==========================================

    data["last_month_sales"] = conn.execute("""

        SELECT COUNT(*)

        FROM sales

        WHERE employee_id=?

        AND strftime('%m',sale_date)=strftime('%m','now','-1 month')

    """, (employee_id,)).fetchone()[0]

    # ==========================================
    # GROWTH %
    # ==========================================

    last = data["last_month_sales"]

    current = data["this_month_sales"]

    if last == 0:

        growth = 100 if current > 0 else 0

    else:

        growth = round(((current-last)/last)*100,2)

    data["growth"] = growth
        # ==========================================
    # PERFORMANCE
    # ==========================================

    if growth >= 20:

        data["performance"] = "Excellent"

    elif growth >= 5:

        data["performance"] = "Good"

    elif growth >= 0:

        data["performance"] = "Average"

    else:

        data["performance"] = "Needs Improvement"

    # ==========================================
    # BEST SELLING FERTILIZER
    # ==========================================

    best = conn.execute("""

        SELECT

            fertilizers.fertilizer_name,

            SUM(quantity) AS total

        FROM sales

        JOIN fertilizers

        ON sales.fertilizer_id = fertilizers.id

        WHERE employee_id=?

        GROUP BY fertilizers.fertilizer_name

        ORDER BY total DESC

        LIMIT 1

    """, (employee_id,)).fetchone()

    if best:

        data["best_fertilizer"] = best["fertilizer_name"]

    else:

        data["best_fertilizer"] = "--"

    # ==========================================
    # MONTHLY TARGET
    # ==========================================

    target = 500

    data["target"] = target

    achieved = data["total_quantity"]

    data["achievement"] = round(

        (achieved / target) * 100,

        2

    ) if target else 0

    conn.close()

    return data