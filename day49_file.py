f = open("high.score", "r")
print("🌟Current Leader🌟")
contents = f.read().split()
print(contents)

highscore = 0 
name = None 

for i in contents:
    data = i.split(":")
    print(data[1])
    if data != []:
        if int(data[1]) > highscore:
            highscore = int(data[1])
            name = data[0]

print(f"The winner is {name} with {highscore}")