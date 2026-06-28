from datetime import datetime


def format_currency(amount):
    try:
        return f"₹ {float(amount):,.2f}"
    except:
        return "₹ 0.00"


def format_date(date_string):
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return date.strftime("%d-%m-%Y")
    except:
        return date_string


def calculate_total(quantity, price):
    try:
        return float(quantity) * float(price)
    except:
        return 0


def success_response(message, data=None):
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def error_response(message):
    return {
        "status": "error",
        "message": message
    }