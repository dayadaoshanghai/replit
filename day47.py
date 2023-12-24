card = {
  "Mr.Morgan": {
    "intelligence": 120,
    "handsomeness": 7,
    "l33t_coding_skiiz": 80,
    "baldness_level": 8
  },
  "Mr.Colley": {
    "intelligence": 80,
    "handsomeness": 5,
    "l33t_coding_skiiz": 90,
    "baldness_level": 6
  }
}


def card_game():
  print(
    "Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
  for name, value in card.items():
    print(name)
  choice1_name = input("player1 choose name card:")
  choice2_name = input("player2 choose name card:")

  choice_state = input("player1 choose your state:")

  if choice_state == "handsomeness":
    choice1_state = card[choice1_name][choice_state]
    choice2_state = card[choice2_name][choice_state]
    if choice1_state > choice2_state:
      print("player1 win")
    elif choice1_state < choice2_state:
      print("player2 win")
    else:
      print("draw")
  elif choice_state == "intelligence":
    choice1_state = card[choice1_name][choice_state]
    choice2_state = card[choice2_name][choice_state]
    if choice1_state > choice2_state:
      print("player1 win")
    elif choice1_state < choice2_state:
      print("player2 win")
    else:
      print("draw")
  elif choice_state == "l33t_coding_skiiz":
    choice1_state = card[choice1_name][choice_state]
    choice2_state = card[choice2_name][choice_state]
    if choice1_state > choice2_state:
      print("player1 win")
    elif choice1_state:
      print("player2 win")
    else:
      print("draw")
  elif choice_state == "baldness_level":
    choice1_state = card[choice1_name][choice_state]
    choice2_state = card[choice2_name][choice_state]
    if choice1_state > choice2_state:
      print("player1 win")
    elif choice1_state < choice2_state:
      print("player2 win")
    else:
      print("draw")

  else:
    print("wrong state")


def add_card():
  while True:
    print("plase add some rule to the card")
    name = input("name:")
    intelligence = int(input("intelligence:"))
    handsomeness = int(input("handsomeness:"))
    l33t_coding_skiiz = int(input("l33t_coding_skiiz:"))
    baldness_level = int(input("baldneess_level:"))
    card[name] = {
      intelligence, handsomeness, l33t_coding_skiiz, baldness_level
    }
    print(card)
    judge = input("add success,do you want to add more?")
    if judge.capitalize() == "Y":
      continue
    else:
      return card
      break


card_game()
add_card()
