def raibow_text(string):
  for letter in myString:
    if letter.lower() == "r":
      print('\033[31m', end='') #red
    elif letter.lower() == "b" or letter.lower() == "g" or letter.lower() == "p" or letter.lower() == "y":
      print('\033[32m', end='') #bule
    elif letter.lower() == "c":
      print('\033[36m', end='') #cyan
    elif letter.lower() == "m":
      print('\033[35m', end='') #magenta
    elif letter.lower() == "w":
      print('\033[37m', end='') #white
    elif letter.lower() == "k":
      print('\033[30m', end='') #black
  
    print(letter, end = '')
    print('\033[0m', end='') #back to default

myString = input("please input a sentence:")
raibow_text(myString)