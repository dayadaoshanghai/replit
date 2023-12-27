import csv  # Imports the csv library

with open("Day54Totals.csv") as file:  # Opens the csv file
  reader = csv.DictReader(
    file)  # reads the contents of the csv file into the 'reader' variable
  line = 0
  total = 0

  for row in reader: 
    print (row)

    cost = float(row["Cost"])
    quantity = float(row["Quantity"])
    total +=  (cost * quantity)
  print(total)

