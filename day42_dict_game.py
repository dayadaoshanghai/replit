def get_input(prompt):
    return input(prompt).strip().title()

def print_with_color(text, type_color):
    color_codes = {"Earth": "\033[32m", "Air": "\033[37m", "Fire": "\033[31m", "Water": "\033[34m"}
    color_code = color_codes.get(type_color, "\033[33m")
    print(f"{color_code}{text}")

mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast\n")

for name in mokedex:
    mokedex[name] = get_input(f"{name}:\t")

print_with_color("MokéBeast Details:", mokedex["Type"])
for name, value in mokedex.items():
    print(f"{name:<19}: {value}")
