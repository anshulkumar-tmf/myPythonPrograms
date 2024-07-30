import csv
import secrets
from pathlib import Path   # to locate the data files

cwd = Path.cwd()

with open(cwd / "user_datatest_100.csv", "r") as file_input, open(cwd / "user_outtest.csv", "w") as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output,fieldnames=reader.fieldnames)
    writer.writeheader()
    for user in reader:
        user["password"] = secrets.token_hex(8)
        writer.writerow(user)

