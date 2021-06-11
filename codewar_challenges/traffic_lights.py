def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."

print(update_light("red"))
print(update_light("yellow"))
print(update_light("green"))
