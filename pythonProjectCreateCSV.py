import csv
import random
import string
from pathlib import Path


# Generate sample data using random function and concatenating strings of random characters
def generate_random_string(length=7):
    letters = string.ascii_letters
    first_name = "".join(random.choice(letters) for i in range(length))
    last_name = "".join(random.choice(letters) for i in range(length))
    return (first_name + " " + last_name).title()



data = [{"username": f"user{i}", "full_name": generate_random_string()} for i in range(1, 101)]

# get the currenty working directory
cwd = Path.cwd()

# Define the CSV file name
csv_file = (cwd/"user_datatest_100.csv")

# Define the CSV column headers
headers = ["username", "full_name", "password"]

# Write the data to the CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write the header
    writer.writeheader()

    # Write the data rows
    for row in data:
        # Add an empty password field
        row["password"] = ""
        writer.writerow(row)

csv_file
