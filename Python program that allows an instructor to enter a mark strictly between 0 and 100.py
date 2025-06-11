while True:
    try:
        mark = int(input("Enter a mark between 0 and 100: "))

        if 0 <= mark <= 100:
            if 91 <= mark <= 100:
                grade = "A"
            elif 80 <= mark <= 90:
                grade = "B"
            elif 70 <= mark <= 79:
                grade = "C"
            elif 60 <= mark <= 69:
                grade = "D" 
            elif 50 <= mark <= 59:
                grade = "E" 
            elif 40 <= mark <= 49:
                grade = "O"
            elif 0 <= mark <= 39:
                grade = "F" 

            print(f"Mark: {mark}, Grade: {grade}") 
            break 
        else:
            print("Mark must be between 0 and 100. Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
                
                
                
                                 


        
