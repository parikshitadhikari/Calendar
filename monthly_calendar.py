import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the months in digit (like January as 1, February as 2 and so on): "))

print("The calendar of month " + str(month)+ " of " + str(year)+ " is")
print(calendar.month(year, month))