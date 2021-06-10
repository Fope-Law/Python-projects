file = open("teams.txt", "w")
list = ["Arsenal", "Crystal Palace", "Chelsea", "Fulham", "Brighton"]

for nt in list:
     file.write(nt +"\n")
file.close()

file = open("teams.txt", "r")
print("teams.txt")