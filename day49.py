f = open("savedFile.txt", "r+")
contents = f.readline().strip()
f.close()



print(contents)