List = []
try:
  f = open("game.exe","r")
  List = eval(f.read())
  f.close()
except:
  print("File not found, using a blank file")

def add_game():
  item = input("Input the item to add:>")
  List.append(item)
  print(f"{item} has been added to your inventory")
  f = open("game.exe", "w")
  f.write(str(List))
  f.close()

def view_game():
  item = input("Input the item to view:>")
  if item in List:
    List.count(item)
    print(f"{item} has been found {List.count(item)} times")
  else:
    print(f"{item} is not in your inventory")

def remove_game(): 
  item = input("Input the item to remove:>")
  if item in List:
    List.remove(item)
    print(f"{item} has been removed from your inventory")

print("🌟RPG Inventory🌟")
while True:
    choice = input("1: ADD 2: Remove 3:View >")
    if choice == "1":
        add_game()
    elif choice == "2":
        remove_game()
    elif choice == "3":
     view_game()
    else:
     print("Invalid choice") 