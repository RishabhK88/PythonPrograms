# CSV stands for comma seperate value which is like a simplified spreadsheet
# stored as plain text
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["TransactionId", "ProductId", "Price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 10])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
