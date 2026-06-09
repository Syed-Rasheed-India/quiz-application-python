#Student Grade Calculator

try:
    mark = int(input("Enter mark: "))

except Exception as e:
    print(e)

else:
    if mark >= 90:
        print("Your Grade Is O")
    elif mark >= 80:
        print("Your Grade Is A")
    elif mark >= 70:
        print("Your Grade Is B")
    elif mark >= 60:
        print("Your Grade Is C")
    elif mark >= 50:
        print("Your Grade Is D")
    elif mark <=20:
        print("Your Grade Is F")
    else:
        print("Your Grade Is E")
