while True:
  f = open("high.score", "a+")
  name = input("> ")
  score = input(">")
  f.write(f"{name}:{score}\n")
  f.close()
  judge = input("add more? (y/n) ")
  if judge.capitalize() == "Y":
    continue
  else:
    break
  