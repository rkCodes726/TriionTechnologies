print("1. Calculate Grade")
print("2. View Marks")
print("3. Find Highest Marks")
print("4. Show Passed Students")
print("5. Future Feature")
print("6. Exit")
choice= int(input("Enter Your Choice: "))
match choice:
    case 1:
        marks= int(input("Enter your Marks(0-100): "))
        if marks<0 or marks>100:
            print("Invalid marks! Please enter a value between 0 and 100.")
        else:
            if marks>=90:
                print("Grade: A")
            elif marks>=75 and marks<=89:
                print("Grade: B")
            elif marks>=60 and marks<=74:
                print("Grade: C")
            elif marks>=40 and marks<=59:
                print("Grade: D")
            else:        
                print("Fail") 
                
    case 2:
        marks= [78, 45, 92, 34, 67, 88, 29]
        for i in marks:
            print("marks: ",  i)
        
    case 3:
        
    case 4:
        marks= [78, 45, 92, 34, 67, 88, 29]
        for i in marks:
            if i>=40:
                print("passed mark: ",i)
            else:
                continue
    case 5:
        
    case 6:
        break
    
    
    
