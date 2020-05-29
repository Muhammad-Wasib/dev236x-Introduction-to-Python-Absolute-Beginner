
#Start 1-6 Intro Python Practice
#Nested Conditionals
#Student will be able to
#create nested conditional logic in code
#3print format print using escape sequence(/)


#Task: 1
# [ ] print a string that outputs the following exactly: The new line character is "\n"

#print(' The new line character is "\\n"')


#Task: 2
# [ ] print output that is exactly (with quotes): "That's how we escape!"

#print('"That\'s how we escape!"')

#Task: 3
# [ ] with only 1 print statement and using No Space Characters, output the text commented below

# 1       one
# 22      two
# 333     three
#print("1\tone\n"
#      "22\tthree\n"
#      "333\tthree")





#Task: 5
#Program: quote_me() Function
#quote_me takes a string argument and returns a string that will display surrounded with added double quotes if printed

#check if passed string starts with a double quote ("\""), then surround string with single quotations
#if the passed string starts with single quote, or if doesn't start with a quotation mark, then surround with double quotations
#Test the function code passing string input as the argument to quote_me()

#my programe
#def quote_me(argument1):
#    if argument1.startswith("\""):
#        a = "'"+argument1[1:-1]+"'"
#        return a
#    elif argument1.startswith("\'") or argument1.isalpha():
#        b = '"'+argument1[1:-1]+'"'
#        return b
#function1=input("Enter something with single quotation double quotation or with quotation: ")
#ha=(quote_me(function1))
#print(ha)

#net programe
#def quote_me(phrase):
#    if phrase.startswith("\""):
#        print('\'' + phrase[1:-1] + '\'')
#    elif phrase.startswith('\''):
#        print("\"" + phrase[1:-1] + "\"")
#    elif phrase.isalpha()
#        print("\"" + phrase[0:-0] + "\"")


# game=input("Enter input")
#quote_me(game)


#Task: 6
#Program: shirt order
#First get input for color and size

#White has sizes L, M
#Blue has sizes M, S
#print available or unavailable, then
#print the order confirmation of color and size

#hint: set a variable "available = False" before nested if statements and
#change to True if color and size are avaliable

#color=input("Enter color: ")
#size=input("Enter size: ")
#if color.lower()=="white":
#    if size.lower()=="l" or size.lower()=="m":
#        print("Available ","Color: ",color,", Size",size,"Order Confirmed")
#    else:
#        print("Only Large and Medium size available in white color")
#elif color.lower()=="blue":
#    if size.lower()=="m" or size.lower()=="s":
#        print("Available ","Color: ",color,", Size",size,"Order Confirmed")
#    else:
#        print("Only Medium and Small size is available in blue color.")
#else:
#    print("Color is not available")


#Program: str_analysis() Function
#Create the str_analysis() function that takes a string argument. In the body of the function:



#Task: 7
#Check if string is digits
#if digits: convert to int and check if greater than 99
#if greater than 99, print a message about a "big number"
#if not greater than 99, print message about "small number"
#if not digits: check if string isalpha
#if isalpha print message about being all alpha
#if not isalpha print a message about being neither all alpha nor all digit
#call the function with a string from user input


#def str_analysis(argument):
#    if argument.isdigit():
#        argument=int(argument)
#        if argument > 99:
#            print("Big Number ")
#        else:
#            print("Small Number ")
#    elif argument.isalpha():
#        print("All Alpha")
#    else:
#        print("Neither all alpha nor or all digits")

#ainput=input("Enter something: ")
#str_analysis(ainput)



#Task: 8
#Program: ticket_check() - finds out if a seat is available
#Call ticket_check() function with 2 arguments: section and seats requested and return True or False

#section is a string and expects: general, floor
#seats is an integer and expects: 1 - 10
#Check for valid section and seats

#if section is general (or use startswith "g")
#if seats is 1-10 return True
#if section is floor (or use starts with "f")
#if seats is 1-4 return True
#otherwise return False

#def ticket_check(section,seats):
#    if section.lower().startswith("g"):
#        if seats<=10:
#            return True
#        else:
#            return False
#    elif section.lower().startswith("f") :
#        if seats<=4:
#            return True
#        else:
#            return False
#    else:
#        print("Enter valid input ")


#call_fuction1=input("Enter section: ")
#call_fuction2=(input)("Enter seats: ")
#print(ticket_check(call_fuction1,int(call_fuction2)))



#end of pratice 1-6





# Start 1-7.2 Intro Python Practice
#while() loops & increments
#Student will be able to
#create forever loops using while and break
#use incrementing variables in a while loop
#control while loops using Boolean operators

#Task: 1
# [ ] use a "forever" while loop to get user input of integers to add to sum,
# until a non-digit is entered, then break the loop and print sum
#sum = 0
#q=str(input("Enter y to sum and e for exit the programe: "))
#if q.lower()==("y") or q.lower().startswith("yes"):
#    while True:
#        add_sum = str(input("Enter Integer To Sum: "))
#        if add_sum.isdigit():
#         add_sum=int(add_sum)
#         sum+=add_sum
#        elif add_sum.lower()=="exit" or add_sum.lower().startswith("e"):
#          print("programe end ",str(sum))
#          break


#else:
#    print("invalid input ")

#Task: 2
# [ ] use a while True loop (forever loop) to give 4 chances for input of a correct color in a rainbow
# rainbow = "red orange yellow green blue indigo violet"
#chances=0
#while chances<4:
#    rainbow_color=str(input("Input rainbow color: ").lower())
#    chances+=1
#    if rainbow_color in "red, orange, yellow, green, blue, indigo, violet":
#        print(rainbow_color,"Your color is a rainbow color. ")
#    else:
#        print("Your color is not in rainbow color ")


#Task: 3
# [ ] Get input for a book title, keep looping while input is Not in title format (title is every word capitalized)
#title = ""
#while True:
#   title=input("Enter Book Title: ")
#   if title.istitle():
#       print("Programe end")
#       break
#   else:
#       print("Enter in title format every word should capitalized: ")

#Task: 4
# [ ] create a math quiz question and ask for the solution until the input is correct

#ans=288
#quiz = int(input("Math Quiz \n Answer the question (22+44+68-122*24)= "))
#while quiz!=ans:
#    quiz = int(input(" Enter Again! "))
#else:
#    print("Your answer is correct")

#Task: 5

#Fix the error:
# [ ] review the code, run, fix the error
#tickets = int(input("enter tickets remaining (0 to quit): "))

#while tickets > 0:
    # if tickets are multiple of 3 then "winner"
#    if int(tickets / 3) == tickets / 3:
#        print("you win!")
#    else:
#        print("sorry, not a winner.")
#    tickets = int(input("enter tickets remaining (0 to quit): "))

#print("Game ended")



#Task: 6

#create a function: quiz_item() that asks a question and tests if input is correct
#quiz_item()has 2 parameter strings: question and solution
#shows question, gets answer input
#returns True if answer == solution or continues to ask question until correct answer is provided
#use a while loop
#create 2 or more quiz questions that call quiz_item()
#Hint: provide multiple choice or T/F answers


#My programe:
#def quiz_item(question,solution):
#    while True:
#        if question==solution:
#            return True
#        else:
#            print("Wrong Answer. . . ")
#            ask_again=int(input("Try again: "))
#            if ask_again==solution:
#                return True
#q1a=4
#q2a=0
#q3a=4
#q4a=2
#print(quiz_item(int(input("What is 2+2= ")),q1a))
#print(quiz_item(int(input("What is 2-2= ")),q2a))
#print(quiz_item(int(input("What is 2*2= ")),q3a))
#print(quiz_item(int(input("What is 6/3= ")),q4a))



#net programe:
#def quiz_item_a(a_question, a_solution):
#  while True:
#    if a_question.lower() == a_solution:
#      return True
#    else:
#      print("Wrong.")
#      ask_again = input("Try again: ")
#      if ask_again.lower() == a_solution:
#        return True

#print(quiz_item_a(input("Is Kermit a frog? Y/N answer please: "), "y"))
#print(quiz_item_a(input("Do cows drink milk? Y/N answer please: "), "n"))
#print(quiz_item_a(input("Does the sun rise in the east? Y/N answer please: "), "y"))


#End of practice and module 4








                                       #Module 4 Required Coding Activity:


#Program: str_analysis() Function
#Create the str_analysis() function that takes 1 string argument and returns a string message.
# The message will be an analysis of a test string that is passed as an argument to str_analysis().
# The function should respond with messages such as:

#"big number"
#"small number"
#"all alphabetic"
#"multiple character types"
#The program will call str_analysis() with a string argument from input collected within a while loop.
# The while loop will test if input is empty (an empty string "") and continue to loop and gather input until the user
# submits at least 1 character (input cannot be empty).

#The program then calls the str_analysis() function and prints the return message.

#Sample input and output:
#enter nothing (twice) then enter a word

#enter word or integer:
#enter word or integer:
#enter word or integer: Hello
#"Hello" is all alphabetical characters!

#alphabetical word input

#enter word or integer: carbonization
#"carbonization" is all alphabetical characters!

#numeric inputs

#enter word or integer: 30
#30 is a smaller number than expected

#enter word or integer: 1024
#1024 is a pretty big number
#loop until non-empty input is submitted
#This diagram represents the input part of the assignment -
# it is the loop to keep prompting the user for input until they submit some input (non-empty).


#Additional Details
#In the body of the str_analysis() function:

#Check if string is digits
#if digits: convert to int and check if greater than 99
#if greater than 99 print a message about a "big number"
#if not greater than 99 print message about "small number"
#check if string isalpha then (since not digits)
#if isalpha print message about being all alpha
#if not isalpha print a message about being neither all alpha nor all digit
#call the function with a string from user input

#Run and test your code before submitting


#def str_analysis(argument):
#    if argument.isdigit():
#        if int(argument) > 200:
#            return (str(argument) + " Pretty Big Number")
#        else:
#            if int(argument) > 99:
#                return (str(argument) + " Big Number")
#            else:
#                if int(argument) < 99 and int(argument) > 50:
#                    return (str(argument) + " Small Number")
#                else:
#                    return (str(argument) + " Small Number then expected")
#    elif argument.isalpha():
#        return ( "\"" + argument + "\"" + " is all alphabetical characters")
#    elif argument.isalnum():
#        return ( "\"" + argument + "\""+ " Neither all alpha nor or all digit")
#    else:
#        return ("Invalid input please enter integer or word ")


#str_input = input("Enter word or integer: ")
#while str_input=="":
#    str_input = input("Enter word or integer: ")
#print(str_analysis(str_input))


#End of Module 4 and Required Code Activity.




#Final Code Submission:

#Program: adding_report() function
#This program calls the adding_report() function which repeatedly takes positive integer
#input until the user quits and then sums the integers and prints a "report".
#The adding_report() function has 1 string parameter which indicates the type of report:

#"A" used as the argument to adding_report() results in printing of all of the input integers and the total
#"T" used as the argument results in printing only the total
#Sample input and output:
#call adding_report() with "A" as argument (print all the integers entered and the total)

#Input an integer to add to the total or "Q" to quit
#Enter an integer or "Q": 3
#Enter an integer or "Q": 6
#Enter an integer or "Q": 24
#Enter an integer or "Q": 17
#Enter an integer or "Q": 61
#Enter an integer or "Q": nine
#nine is invalid input
#Enter an integer or "Q": q

#Items
#3
#6
#24
#17
#61

#Total
# 111
#call with "T"(print only the total)

#Input an integer to add to the total or "Q" to quit
#Enter an integer or "Q": 5
#Enter an integer or "Q": 7
#Enter an integer or "Q": Quit

#Total
# 12
#The forever (while True) loop diagram
#This diagram represents only part of the assignment - it is the loop and nested if statements inside the function. The code will enter at the while True loop after initializing variables.

#image of while True Loop with nested if statements described in bulleted text above

#Additional Details
#initialize total variable which will sum integer values entered

#initialize items variable which will build a string of the integer inputs separated with a new line character

#define the adding_report function with one parameter report that will be a string with default of "T"

#inside the function build a forever loop (infinite while loop) and inside the loop complete the following

#use a variable to gather input (integer or "Q")
#check if the input string is a digit (integer) and if it is...
#add input iteger to total
#if report type is "A" add the numeric character(s) to the item string seperated by a new line
#if not a digit, check if the input string is "Q" or starts with a "Q", if "Q" then...
#if the report type is "A" print out all the integer items entered and the sum total
#if report type is "T" then print out the sum total only
#break out of while loop to end the function after printing the report ("A" or "T")
#if not a digit and if not a "Q" then print a message that the "input is invalid"
#Call the adding_report function with "A" and then with "T" report parameters

#Run and test your code before submitting

#def  adding_report(parameter):
#        t_total=0
#        a_total=0
#        items=""
#        print(" Report Types  include  All Items (\"A\") or Total Only(\"T\") ")
#        if parameter.lower()=="t":
#            while True:
#              ain=input(" Input an Integer to add to the total or \"Q\"  to Quit ")
#              if ain.isdigit() == True:
#               ain=int(ain)
#               t_total+=ain
#              elif ain.lower()!="q":
#                  print("\"",str(ain),"\"",("is a Invalid input"))
#              else:
#                  print("Total "+str(t_total) +(" \"Programe end\""))
#                  break

#        elif parameter.lower()=="a":
#            while True:
#             bin=input(" Input an Integer to add to the total or \"Q\"  to Quit ")
#             if bin.isdigit()==True:
#                bin=int(bin)
#                a_total+=bin
#                items = items + str(bin) + "\n"
#             elif bin.lower()!="q":
#                 print("\"",str(bin),"\"",("is a Invalid input"))
#             else:
#                 print("\nItems\n" + str(items))
#                 print("Total "+str(a_total)+(" \"Programe end\" "))
#                 break
#        else:
#            print(" Choose Report Type (\"A\" or \"T\") input only \'A\' and \'T\'")



#rept_type=input(" Choose Report Type (\"A\" or \"T\"): ")
#adding_report(rept_type)


#net code
#def adding_report(report_type):
#    total = 0
#    items = ""

#    string = input('Input an integer to add to the total or "Q" to quit: ')
#    while True:
#        if string.isdigit():
#            total += int(string)
#            if report_type == "A":
#                items = items + string + "\n"
#        elif string.startswith("Q"):
#            if report_type == "A":
#                print("\nItems\n" + items + "\n" + "\nTotal\n" + str(total))
#            elif report_type == "T":
#                print("\nTotal\n" + str(total))
#            break
#        else:
#            print("Invalid input")

#        string = input('Enter an integer or "Q" to quit: ')


#print("This program adds a sequence of integers and produces two types of reports.")
#print("Report A: Prompts for a sequence of integers and outputs the concatenated sequence and total.")
#print("Report B: Prompts for a sequence of integers and output only the total.\n")

#report_type = input("Which report type do you prefer [A, T, or Q to quit]? ")
#while report_type != "Q":
#    if report_type in "A T":
#        adding_report(report_type)
#    else:
#        print("ERROR: Try again!\n")
#    report_type = input("\nWhich report type do you prefer [A, T, or Q to quit]? ")

#print("Bye!")

#Microsoft: DEV236x
#Introduction to Python: Absolute Beginner

