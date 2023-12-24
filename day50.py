import random 

def add_idea():
    f = open("idea.txt", "a+")
    idea = input("What is your idea? ")
    f.write(idea + "\n")
    f.close()

def show_idea():
    f = open("idea.txt", "r")
    content = f.read().split("\n")
    content = content.remove("")
    print(content)

def random_idea():
    f = open("idea.txt", "r")
    content = f.read().split("\n")
    f.close()
    content.remove("")
    print(random.choice(content))
    


print("🌟Idea Storage🌟")  
while True:
    judge = input("Add an idea or see a random idea? (a/r) ")
    if judge.capitalize() == "A":
        add_idea()
    elif judge.capitalize() == "R":
        random_idea()
    else:
        print("Please enter a valid command.")

