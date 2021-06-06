count = 0
name = str(input("What is your name? "))

while count < 5:
    print(name, "is awesome!")
    count += 1

for me in range(51):
    print(me)

for me in range(0, 51, 2):
    print(me)

animals = ["bull", "boar", "swan"]

for animal in animals:
    print(animal)

for me in range(101):
    print(me)
    if me == 20:
        break
       
for me in range(20):
    if me == 5:
        continue
    print(me) 

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i*j)

