def prettyPrint():
  for name, value in mokedex.items():
        print(f"{name:<19}")
        for subkey, subvalue in value.items():
            print(f"{subkey}: {subvalue}")
        print()

# mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}
mokedex = {}
while True:
    Beast_Name = input("Enter the name of the beast: ")
    Type = input("Enter the type of the beast: ")
    Move = input("Enter the special move of the beast: ")
    HP = input("Enter the HP of the beast: ")
    MP = input(f"Enter the MP of the beast: ")
    mokedex[Beast_Name] = {"Type": Type, "Special Move": Move, "HP": HP, "MP": MP} 


    prettyPrint()
    