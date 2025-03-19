from datetime import datetime, timedelta

def display_welcome_message():
    print("==========================================")
    print(" Welcome to the Menstrual Cycle App ")
    print("==========================================\n")

def get_last_period_start_date():
    return input("Enter the start date of your last period (YYYY-MM-DD): ")

def get_cycle_length():
    return int(input("Enter your average cycle length (in days): "))

def get_period_duration():
    return int(input("Enter your average period duration (in days): "))

def calculate_next_period(last_period_start_date, cycle_length):
    last_period_start_date = datetime.strptime(last_period_start_date, "%Y-%m-%d")
    next_period_start_date = last_period_start_date + timedelta(days=cycle_length)
    return next_period_start_date.strftime("%Y-%m-%d")

def calculate_ovulation(last_period_start_date, cycle_length):
    last_period_start_date = datetime.strptime(last_period_start_date, "%Y-%m-%d")
    ovulation_date = last_period_start_date + timedelta(days=cycle_length-14)
    return ovulation_date.strftime("%Y-%m-%d")

def display_safe_and_fertile_periods(last_period_start_date, cycle_length, period_duration):
    ovulation_date = calculate_ovulation(last_period_start_date, cycle_length)
    ovulation_date = datetime.strptime(ovulation_date, "%Y-%m-%d")
    fertile_start = ovulation_date - timedelta(days=5)
    fertile_end = ovulation_date + timedelta(days=1)
    safe_start_before = datetime.strptime(last_period_start_date, "%Y-%m-%d") + timedelta(days=period_duration)
    safe_end_before = fertile_start - timedelta(days=1)
    safe_start_after = fertile_end + timedelta(days=1)
    safe_end_after = datetime.strptime(calculate_next_period(last_period_start_date, cycle_length), "%Y-%m-%d")
    print("Safe Periods:")
    print("Before Fertile Window: " + safe_start_before.strftime("%Y-%m-%d") + " to " + safe_end_before.strftime("%Y-%m-%d"))
    print("After Fertile Window: " + safe_start_after.strftime("%Y-%m-%d") + " to " + safe_end_after.strftime("%Y-%m-%d"))
    print("\nFertile Periods:")
    print("From " + fertile_start.strftime("%Y-%m-%d") + " to " + fertile_end.strftime("%Y-%m-%d"))

def display_goodbye_message():
    print("\n==========================================")
    print(" Thank you for using the Menstrual App! ")
    print(" Stay healthy and take care! ")
    print("==========================================")

def main():
    display_welcome_message()
    last_period_start_date = get_last_period_start_date()
    cycle_length = get_cycle_length()
    period_duration = get_period_duration()
    next_period_start_date = calculate_next_period(last_period_start_date, cycle_length)
    ovulation_date = calculate_ovulation(last_period_start_date, cycle_length)
    print("\nCalculations:")
    print("Next Period Start Date: " + next_period_start_date)
    print("Estimated Ovulation Date: " + ovulation_date)
    print("\nSafe and Fertile Periods:")
    display_safe_and_fertile_periods(last_period_start_date, cycle_length, period_duration)
    display_goodbye_message()

main()