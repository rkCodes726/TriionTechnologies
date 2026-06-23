S_number= 10

while True:
    num= int(input("Guess the number: "))
    if num>S_number:
        print("Too High!")
    elif num<S_number:
        print("Too low!")
    else:
        print("Correct Guess!")
        break
        