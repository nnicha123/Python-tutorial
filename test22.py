# string = "make a wish Simon says"
# print(string.endswith("Simon says"))
instructions = input()
if (instructions.endswith("Simon says")):
    idx = instructions.find("Simon says")
    return "I " + instructions[0:idx]
elif (instructions.startswith("Simon says")):
    return "I " + instructions[11:len(instructions)]
else:
    return "I won't do it!"