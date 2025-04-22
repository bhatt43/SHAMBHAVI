class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.date == other.date
        return False

    def __str__(self):
        return f"{self.date[0]:02d}/{self.date[1]:02d}/{self.date[2]}"

# Example usage
if __name__ == "__main__":
    date1 = Date(22, 4, 2025)
    date2 = Date(22, 4, 2025)
    date3 = Date(1, 1, 2024)

    print("Date 1:", date1)
    print("Date 2:", date2)
    print("Date 3:", date3)

    print("Date 1 == Date 2?", date1 == date2)  # True
    print("Date 1 == Date 3?", date1 == date3)  # False
