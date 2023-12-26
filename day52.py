List = [] 
try:
    f = open("order.txt", "r")
    List = eval(f.read())
    f.close()
except:
    print("File not found")

def add_list():
  name = input("What's your name:")
  while True:
    try:
      quantity = int(input("How many pizzas do you want:"))
      break 
    except:
      print("invalid input,please input a number")
  
  size = int(input("What size do you want:"))
  cost = size * quantity
  row = [name, cost]
  List.append(row)

def view_list():
  print(List)

while True:
  print("🌟Dave's Dodgy Pizzas🌟")
  choice = input("1. Add pizza to order, 2. View order, 3. Exit")

  if choice == "1":
    add_list()
    f = open("order.txt", "w")
    f.write(str(List))
    f.close()
  elif choice == "2":
    view_list()
  else:
    break
  
