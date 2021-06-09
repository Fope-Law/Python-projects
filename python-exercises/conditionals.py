mark = int(input("Enter your mark here: "))

if mark > 85:
    print("Distinction")
if mark > 65 and mark <= 85: 
    print("Pass")
if mark <= 65: 
    print("Fail")