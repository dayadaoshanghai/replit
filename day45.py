def editList(List):
  ori_info = input("Enter the info you want to edit: ")
  for row in List:
    new_info = input("Enter the new info: ")
    index = row.index(ori_info)
    row[index] = new_info
    print("The new list is: ", List)
  return List

def viewList(List):
  option = input("1:view all, 2:view by priority")
  if option == "1":
    for row in List:
      print("|".join(row))
  else:
    priority = input("Enter priority: ")
    for row in List:
      if priority in row:
        print("|".join(row))
        print()


def addList(List):
  name = input("what to do? >")
  due = input("When it is due? >")
  priority = input("What priority? >")
  row = [name, due, priority]
  List.append(row)
  return List

def removeList(List):
  remove_item = input("What to remove? >")
  # for row in List:
  #   if item in row:
  #     List.remove(row)
  #     print("The item has been removed")
  #     return List
  List[:] = [row for row in List if remove_item not in row]
  print("The item has been removed")
  print(List)
  return List


List = []
while True:
  print("🌟Life Organizer🌟")
  choice = input("Welcome to he life organizer. Do you want to add, view, edit or remove a task?")
  if choice == "add":
    addList(List)

  elif choice == "view":
    viewList(List)
  elif choice == "edit":
    editList(List)

  elif choice == "remove":
    removeList(List)

