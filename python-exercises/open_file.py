
file = open("teams.txt", "w")
clubs = ['Arsenal', 'Crystal Palace', 'Chelsea', 'Fulham', 'Brighton']


for name in clubs:
    file.write(name + "\n")
file.close()


file = open("teams.txt", "r")
lines_to_read = [0,3]


for position, line in enumerate(file):
    if position in lines_to_read:
        print(line)