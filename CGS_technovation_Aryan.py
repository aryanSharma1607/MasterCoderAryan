# Using two libraries:
import pandas as pd  # Used to import csv file
import csv  # Used to manage csv file

filepath = r"C:\Users\sharm\Downloads\unemploymentrateinindia\Unemployment_Rate_M_Total.csv"  # My computers filepath to downloaded csv
df = pd.read_csv(filepath)

print("Find the unemployment rate and number of people employed in any state in India from 2020 Jan, to 2023 Jan.")

state = input("Enter the state's name: ")
year = int(input("Enter the year (2020 to 2023): "))
month = int(input("Enter the month number (1 to 12): "))

# arrays to be appended on
row_num = []
yearMonths = []
csv_file = []

# arrays separately for finding only India's
row_num_India = []
yearMonths_India = []

# Formatting month for end result
month_name = ""
# Format the year and month to fit my csv file, such as if year = 2020, month = 03, year_month = 202003
if int(month/10) == 0:
    year_month = int(str(year) + "0" + str(month))
else:
    year_month = int(str(year) + str(month))


# Binary search, unchanged
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Using the filepath to fill up arrays with information
with open(filepath) as fd:
    reader = csv.reader(fd)
    for row in reader:
        csv_file.append(row)
        if state == row[1]:  # Only fill up in rows whos state is the one entered by user
            yearMonths.append(int(row[4]))
            row_num.append(int(row[0]))
        if "India" == row[1]:
            yearMonths_India.append(int(row[4]))
            row_num_India.append(int(row[0]))

# Using the binary search function to get the line
final_year_month = binary_search(yearMonths, year_month)
final_year_month_India = binary_search(yearMonths_India, year_month)

# Getting our employment data
final_data_line = int(row_num[0] + final_year_month)
final_unemp_rate = csv_file[final_data_line][7]

final_data_row_India = int(row_num_India[0] + final_year_month_India)
final_unemp_rate_India = csv_file[final_data_row_India][7]

difference = float(final_unemp_rate_India) - float(final_unemp_rate)
difference = difference

if month == 1:
    month_name = "January"
elif month == 2:
    month_name = "February"
elif month == 3:
    month_name = "March"
elif month == 4:
    month_name = "April"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "June"
elif month == 7:
    month_name = "July"
elif month == 8:
    month_name = "August"
elif month == 9:
    month_name = "September"
elif month == 10:
    month_name = "October"
elif month == 11:
    month_name = "November"
elif month == 12:
    month_name = "December"

# Printing out final data
print(f"\nThe estimated unemployment rate in {state} in the month of {month_name}, {year} is {final_unemp_rate}%.")

print(f"The estimated unemployment rate in India for the same month and year is {final_unemp_rate_India}%.")

if difference > 0:
    difference = abs(difference)
    print(f"\n{state}'s unemployment rate is %.2f" %difference + "% less than that of the average in India.")
elif difference < 0:
    difference = abs(difference)
    print(f"\n{state}'s unemployment rate is %.2f" %difference + "% greater than that of the average in India.")
else:
    print(f"{state}'s unemployment rate is the same as the average in India, ie. {final_unemp_rate}")