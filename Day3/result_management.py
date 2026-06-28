# List of student marks
marks= [78, 45, 92, 34, 67, 88, 29]

while True:
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
                elif marks>=75:
                    print("Grade: B")
                elif marks>=60:
                    print("Grade: C")
                elif marks>40:
                    print("Grade: D")
                else:        
                    print("Result: Fail") 
                    
        case 2:
            print("\nStudents Marks:")
            for mark in marks:
                print(mark)
            
        case 3:
            highest= marks[0]
            for mark in marks:
                if mark>highest:
                    highest= mark
            
            print("Highest Mark= ",highest)
            
        case 4:
            print("\nPassed Students Marks: ")
            for mark in marks:
                if mark < 40:
                    continue  # Skip failed students
                print(mark)
                
        case 5:
            print("Future Feature Coming Soon...")
            pass
            
        case 6:
            # Find highest mark
            highest = marks[0]
            for mark in marks:
                if mark > highest:
                    highest = mark

            # Count passed and failed students
            passed_students = 0
            failed_students = 0

            for mark in marks:
                if mark >= 40:
                    passed_students += 1
                else:
                    failed_students += 1

            print("\n====== SUMMARY ======")
            print("Total Students:", len(marks))
            print("Highest Mark:", highest)
            print("Passed Students:", passed_students)
            print("Failed Students:", failed_students)

            print("\nThank You For Using Student Result System")
            break

        # Invalid Choice
        case _:
            print("Invalid Choice! Please select a valid option.")
    
    
    
