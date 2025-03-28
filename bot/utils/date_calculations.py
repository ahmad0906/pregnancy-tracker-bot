from datetime import datetime, timedelta

def calculate_due_date(lmp_date: str):
    """Calculate the due date (LMP + 280 days)."""
    lmp = datetime.strptime(lmp_date, "%Y-%m-%d")
    due_date = lmp + timedelta(days=280)
    return due_date.strftime("%Y-%m-%d")

def get_pregnancy_week(lmp_date: str):
    """Calculate current pregnancy week."""
    lmp = datetime.strptime(lmp_date, "%Y-%m-%d")
    today = datetime.today()
    weeks_pregnant = (today - lmp).days // 7
    return weeks_pregnant
