path = []

path.append("Bedroom")
path.append("Gas Station")
path.append("The Office")
path.append("The Library")
path.append("Restaurant")

while(len(path) > 1):
    popped_value = path.pop()
    if (popped_value == "The Library"):
        print(path.pop())
        break

