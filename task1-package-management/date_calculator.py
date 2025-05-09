import datetime
def difference_dates(date1: str, date2: str) -> int :
    """
    calculates the difference between two dates to display the number of days between two dates

    Parameters:
    date1: first date of format YYYY-MM-DD with string datatype
    date2: second date of format YYYY-MM-DD with string datatype

    This function will calculate the difference by subtacting date1 from date2
    Raise:
    ValueError: parameters are in incorrect format

    Example:
    difference_dates("2025-06-01", "2025-06-15") returns 15
    difference_dates("2025-06-01", "2025-15-06") returns valueError
    """
    return abs((date2 - date1).days)
def main():
    try:
        d1 = input("Enter the first date of format YYYY-MM-DD: ")
        d2 = input("Enter the second date of format YYYY-MM-DD: ")
    
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()

        difference = difference_dates(date1, date2)
        print("Days between two dates are: ", difference)

    except ValueError:
        print("ValueError: Parameters are in incorrect format. Please use YYYY-MM-DD format.")
main()

