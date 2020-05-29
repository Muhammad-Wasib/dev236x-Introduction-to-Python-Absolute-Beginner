
# Module #1 Introduction  To Python:


# Programe :


# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
# owner =input("enter name for contact person for training group : ")
# rsn_to_come=input("Enter why you are here : ")
# num_people =input("enter the total number attending the class : ")
# training_time = input("enter the training time selected : ")
# [ ] create a integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
# min_early = 10
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting
# print("Reminder you are here for : ",rsn_to_come,"owner name is : ",owner,"Number of people attending",num_people,
 #     "Training time is : ",training_time,"please arrive at : ",min_early," for the class")

# end

# print method concatenation with comma of integer and string :
# print("I am", 17, "years old")

# end


# Taking input check boolean values with methods
# a=input(" Enter alphabet ")
# print(a.isalpha())
# b=input(" Enter alnum ")
# print(b.isalnum())
# c=input(" Enter title ")
# print(c.istitle())
# d=input(" Enter integers only ")
# print(d.isdigit())
# e=input("Enter only lower case")
# print(e.islower())
# f=input(" Enter uper case ")
# print(f.isupper())
# g=input('S')
# print(g.startswith())
# b=input(" Enter string ")
# print(b.isalpha())

# end

# programe
# fav_color=input('What is fav color : ' ).upper()
# print(fav_color)
# print(fav_color.swapcase())
# end

# progrmae
# menu = "salad, pasta, sandwich, pizza, drinks, dessert"
# print('pizza' in menu)
# greeting="Hello World"
# print("'hello in greeting'=",'Hello World' in greeting)
# print("'Hello World in Greeting'=", 'hello' in  greeting)
# greeting = "Hello World!"
# print("'hello' in greeting = ",'hello' in greeting)
# print("'Hello' in greeting = ", 'Hello' in greeting)

# Greeting="Hello World"
# print("'hello wolrd in greeting = ", 'hello' in Greeting)
# print("'Hello world in greeting = ", 'Hello' in Greeting)
# print("'Hello World in greetinG if lower used ",'Hello'.lower() in Greeting.lower())
# en

# create a programe where a user can check if an item is on the menu
# menu_ask = "salad, Pasta, Sandwich, pizza, drinks, dessert, Briyani, sajji, broast,"
# ainput=input("'What's your order sir Enter any food item to check in the list it's available or not : ")
# print("item availability is = ",ainput.lower() in menu_ask.lower())
# print("item availability is = ",menu_ask.lower() in ainput.lower()) "its wrong statement"

# [ ] fix the error
# paint_colors = "red, blue, green, black, orange, pink"
# print('Red in paint colors = ','red' in paint_colors)
# end

# challange
# [ ] Challenge: Add to the menu
# print the current menu
# get user input for add_item variable
# new_menu use string addition to add add_item to menu
# print the new_menu
# testing

# check if an item is on the menu, check for previous items and the item you added
# add to menu
# Testing Add to Menu - create user input to search for an item on the new menu

# menu='Briyani,broast,sajji,karhai,kabab,chinese rice,pizza,'
# print(menu)
# add_item=input("add items :")
# new_menu=menu+add_item
# print(new_menu)
# user_input=input('check item on the new menu enter item : ')
# print('item = ',user_input.lower() in new_menu.lower())

# PROGRAME
# a=' GREEN'.lower()
# b=a.isupper()
# print(a,b)

# PROGRAME
# name = "skye homsi"
# name_1 = name.title()
# name_2 = name_1.swapcase()
# print(name_2)


# Final coding assignment module 1
# Allergy check

# 1[ ] get input for test
# input_test=input("Enter What have you eaten in last 24 hours: ")

# 2/3[ ] print True if "dairy" is in the input or False if not

# print('It is ','Dairy'.lower() in input_test.lower(),"that Dairy is in user input")
# 4[ ] Check if "nuts" are in the input
# print("It is",'NUTS'.lower() in input_test.lower(),"that nuts are in the user input")
# 4+[ ] Challenge: Check if "seafood" is in the input
# print("It is",'SEAFOOD'.lower() in input_test.lower(),"that seafood are in the user input")
# 4+[ ] Challenge: Check if "chocolate" is in the input
# print("It is: ",'CHOCOLATE'.lower() in input_test.lower(),"that chocalate are in the user input")



# [ ] get input for input_test variable
# input_test=input("Enter What have you eaten in last 24 hours: ")

# [ ] print "True" message if "dairy" is in the input or False message if not

# print('It is ','Dairy'.lower() in input_test.lower(),"that Dairy is in user input")

# [ ] print True message if "nuts" is in the input or False if not

# print("It is",'NUTS'.lower() in input_test.lower(),"that nuts are in the user input")

# [ ] Challenge: Check if "seafood" is in the input - print message


# print("It is",'SEAFOOD'.lower() in input_test.lower(),"that seafood are in the user input")

# [ ] Challenge: Check if "chocolate" is in the input - print message
# print("It is: ",'CHOCOLATE'.lower() in input_test.lower(),"that chocalate are in the user input")

# x          #End of Module #1                    x#


                                                  # Module 2  Concept function

#Print is an bulit in function by python its also takes 0 arguments examples are here:

# print("line 1")
# print(#python print function also takes zero argumemts)
# print("line 3")

#def simple_calculator(num1,num2):
#    print("This calculator can only do Subtraction")
#    num1=int(num1)
#    num2 = int(num2)
#    return num1-num2
#a=num1=input("Enter num 1: ")
#b=num2=input("Enter num 2: ")
#print(simple_calculator(a,b),": Your Answer.")

# {}                           (simple_calculator() Function Working)


# [ ] define yell_this()
# []  get user input in variable words_to_yel
# [ ] call yell_this function with words_to_yell as argument
# def function_type_1():
#    a="This is how we define function in Python"
#    print(a.upper)
# function_type_1()


# def function_type_2(b):
#    print(b.upper() + '!')
# function_type_2("Another method to define function in python put variable when defining a function in parameters and "
#                "when calling a function you can add the thing what type of function you want to define")


# def function_type_3(c="You can also define a function like this where variable and work can define together in parameter"):
#    print(c)
# calling a functiom
# function_type_3()
# function_type_3("bye")
# in this case we change the functionality of function at this time if you call fac7this function again it will remain same"
# function_type_3()


# function with multi-parameters
# def make_schedule(a, b):
#    schedule = ("[1st] " + a.title() + ", [2nd] " + b.title())
#    return schedule

# student_schedule = make_schedule(a=input("Enter subject 1: "),b=input("Enter subject 2: "))
# print("SCHEDULE:", student_schedule)


# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
# def make_6thclass_Schedule(period_1,period_2,period_3,period_4,period_5,period_6,period_7,period_8):
#    return "1st " + period_1 + "/n2nd " + period_2 + "/n3rd " + period_3 + "/n4th " + period_4 + "/n5th " + period_5 + "/n6th " + period_6 + "/n6th " + period_7 + "/n7th " + period_8 + "/n8th "
# Taking user input to select subject and periods
# Six_class_schedule=make_6thclass_Schedule(period_1=input("Enter subject of period 1: "),period_2=input("/nEnter subject of period 2: "),period_3=input("/nEnter subject of period 3: "),
#                                          period_4=input("/nEnter subject of period 4: "),period_5=input("/nEnter subject of period 5: "),period_6=input("/nEnter subject of period 6: "),
#                                          period_7=input("/nEnter subject of period 7: "),period_8=input("/nEnter subject of period 8: "),)
# print(Six_class_schedule)
# progrmae end /

# practice

# def add_num(num_1=10):
#   return num_1+num_1
# print(add_num(100))

# def low_case(words_in):
#    return words_in.lower()
# words_lower = low_case("Return THIS lower")
# print(words_lower)

# Sequence in python


# def hat_available(color):
#    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
#    return(color.lower() in hat_colors)
#
# have_hat = hat_available('green')

# print('hat available is', have_hat)


# Task 2

# Program: bird_available
# The program should ask for user to "input a bird name to check for availability"
# and print a statement informing of availability view video

# create this program with a Boolean function bird_available()
# has parameter that takes the name of a type of bird
# for this exercise the variable bird_types = 'crow robin parrot eagle sandpiper hawk piegon'
# return True or False (we are making a Boolean function)
# call the function using the name of a bird type from user input
# print a sentence that indicates the availablity of the type of bird checked

# [ ] create function bird_available
# def bird_available(bird):
    # [ ] user input
#    bird_types='crow robin parrot eagle sandpiper hawk piegon'
#    return bird.lower() in bird_types.lower()


# [ ] call bird_available
# name_bird=input("input a bird name to check for availability: ")
# have_bird=bird_available(name_bird)
# [ ] print availbility status
# print(name_bird.capitalize(),'availability is: ' ,have_bird)

# function
# name = input("enter your name: ")
# def greet(person):
#   print("Hi,", person)


# Practice module 2:

# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case

# def title_it(msg):
#    return (msg.title())
# Print=("this function contain title function")
# (title_it(Print))


##
# [ ] define title_it_rtn() which returns a titled string instead of printing
# def title_it_rtn(a):
#    return a.title()
# [ ] call title_it_rtn() using input for the string argumetnt and print the result
# taking_input=input("Enter input: ")
# output=title_it_rtn(taking_input)
# print(output)

##### Programe bookstore() Create and Test Book Store:
# bookstore() takes 2 string arguments: book & price
# bookstore returns a string in sentence form
# bookstore() should call title_it_rtn() with book parameter
# ather input for book_entry and price_entry to use in calling bookstore()
# print the return value of bookstore()


# def bookstore(book,price):
#    sentence='Title: ' + book , 'Cost:  $' + price
#    return sentence
# book_entry=input("Enter Book Name: ")
# price_entry=input("Enter Cost: ")
# output2=bookstore(book_entry,price_entry)
# print(output2)

# def book_store(book, price):

#    sentence= "Title: " + book + ", costs " + price
#    return sentence

# book_choice = input("Enter books title: ")
# book_price = input("Enter books price: ")

# print (book_store(book_choice, book_price))


# fix the error


# def get_name():
#    name_entry = input("enter a name: ")
#    return name_entry

# def get_greeting():
#    greeting_entry = input("enter a greeting: ")
#    return greeting_entry


# def make_greeting(name, greeting = "Hello"):
#    return (greeting + " " + name + "!")

# get name and greeting, send to make_greeting
# print(make_greeting(get_name(), get_greeting()))

# Final Submission Code of Module 2:

# Program: fishstore()¶
# create and test fishstore()

# fishstore() takes 2 string arguments: fish & price
# fishstore returns a string in sentence form
# gather input for fish_entry and price_entry to use in calling fishstore()
# print the return value of fishstore()
# example of output: Fish Type: Guppy costs $1


# def fishstore(fish,price):
#    sentence="Fish type: "+ fish.title() +  " Cost: $" + price
#    return sentence

# fish_entry=input("Enter fish name: ")
# price_entry=input("Enter the fish price: ")
# output_fishstore=fishstore(fish_entry,price_entry)
# print(output_fishstore)

###        End of Module 2.

#                            Module #3 Start
# ..Conditionals
# if, else, pass
# Conditionals using Boolean String Methods
# Comparison operators
# String comparisons


# if else statements:

# sunny_today=True
# if sunny_today:
#    print("It's a sunny day ")
# else:
#    print("It's not a sunny day ")

# sunny_today=False
# if sunny_today:
#    print("It's a sunny day ")
# else:
#    print("It's not a sunny day")

# code1:
# favourite_book=input("Enter book title: ")
# if favourite_book.istitle():
#    print("Nice capatilizationn ")
# else:
#    print("Each word of title have to be capitalize ")

# code2:
# a_number=input("Enter a positive integer: ")
# if a_number.isdigit():
#    print(a_number,"You have entered a positive integer. ")
# else:
#    print(a_number,"is not a positive integer. ")
# if a_number.isalpha():
#    print(a_number,"it's not a positive integer it should not contain alpha character positive intergers starts witn 1")
# else:
#    pass

# Code3:
# vehicle_type=input("Enter a type of vehicle starts witr 'P' : ")
# if vehicle_type.upper().startswith('P'):
#    print(vehicle_type, "Starts with P : ")
# else:
#    print(vehicle_type," Does not starts with P : ")


# Task
# test_string_1 = "welcome"
# test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
# if test_string_1.islower():
#    print(test_string_1,": is in lower case")
# else:
#    print(test_string_2, ": its not in lower case. ")
# if test_string_2.islower():
#    print(test_string_2,": is in lower case")
# else:
#    print(test_string_2, ": its not in lower case. ")

##  End

# Task
# create a functions using startswith('w')
# w_start_test() tests if starts with "w"
# function should have a parameter for test_string and print the test result

# test_string_1 = "welcome"
# test_string_2 = "I have $3"
# test_string_3 = "With a function it's efficient to repeat code"

# [ ] create a function w_start_test() use if & else to test with startswith('w')
# def w_start_test(test_string):
#     if test_string.upper().startswith("W"):
#         print(test_string, ": It's starts with 'w' ")
#     else:
#         print(test_string, ": It's not starts with 'w' ")
#     return test_string


# [ ] Test the 3 string variables provided by calling w_start_test()
# w_start_test(test_string_1)
# w_start_test(test_string_2)
# w_start_test(test_string_3)
# end of programe




                                    # Examples :
# review code and run code
# x = 22
# if x > 25:
#    print("x is already bigger than 25")
# else:
#    print("x was", x)
#    x = 25
#    print("now x is", x)


# review code and run code
# x = 18
# if x + 18 == x + x :
#    print("Pass: x + 18 is equal to", x + x)
# else:
#    print("Fail: x + 18 is not equal to", x + x)

# review code and run cell. "!" means "not"
# x = 19
# test_value = 18
# if x != test_value:
#    print('x is not', test_value)
# else:
#    print('x is', test_value)


# game:
# x =  input("Enter any number: ")
# test_value = '18'
# if x != test_value:
#    print("keep playing")
# else:
#    print('game over the x is', test_value,"same as you entered :D ")


# Task
# [ ] create an if/else statement that tests if y is greater than or equal x + x
# [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output
# x = 3
# y = x + 8
# if y >= x + x:
#    print("y value is : ",y,' True:"y is greater than or equal x+x "',"x+x value is : ",x+x)
# else:
#    print("y value is : ",y,'False:"y is not greater than or eual to x + x'"x+x value is : ",x+x)

# code
# id = 3556
# if id > 2999:
#    print(id, "is a new student")
# else:
#    print(id, "is an existing student")

##     Task:

# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# answer = input("Enter What is 8 + 13? : ")
# answer=int(answer)
# addition = 8 + 13
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# if answer == addition:
#    print(addition, " is correct answer.")
# else:
#    print("incorrect answer: ", answer)
#                                           note: input returns a "string" done with jugaar :D

# Practice prgrame:
# msg=input("Enter input: ").lower()
# if msg == "save the notebook":
#    print("Message as expected")
# else:
#    print("Message not as expected")


# Samjh nae aya
# name=input("Enter input: ")
# if name.lower() <="c":
#    print(" Welcome to the a, b, c line")
# else:
#     print("sorry this is the a, b, c line")

#def tf_quiz(question,answer):
#    question="Oct have green blood"
#    return question
#tf_quiz()

                                              #programe:
#Call the tf_quiz function with 2 arguments
#1: T/F  question string
#2: answer key string like "T"
#return a string correct or incorrect

#def tz_quiz(question,answer):
#    if answer=="f":
#     print("Correct answer")
#    else:
#        print("incorrect answer")
#quiz_eval="Oct have green blood"
#print(quiz_eval)
#a=input("Enter t or f")
#answer=a
#(tz_quiz(quiz_eval,a))
                                 #reddit lean python code
#def tf_quiz(correct_ans):
#    question = input("Should save your notebook after edit?").lower()
#    correct_ans = "t"
#    print(question)
#    if question==correct_ans:
#     print("You answer is correct")
#     tf_quiz = "Should save your notebook after edit?(T/F): ", correct_ans
#     return tf_quiz
#    else:
#     print("Incorrect answer")
#(tf_quiz(correct_ans="t"))






#Define and use tf_quiz() function
#tf_quiz() has 2 parameters which are both string arguments
#question: a string containg a T/F question like "Should save your notebook after edit?(T/F): "
#correct_ans: a string indicating the correct answer, either "T" or "F"
#tf_quiz() returns a string: "correct" or "incorrect"
#Test tf_quiz(): create a T/F question (or several!) to call tf_quiz()

#def tf_quiz(question,correct_ans="t"):
#    if a==correct_ans:
#        return print("Correct answer")
#    else:
#        print("Incorrect answer")
#question = "Should save your notebook after edit?(T/F): "
#print(question)
#a=input("Enter your answer: ").lower()
#tf_quiz(question,a)

                                          #using string elif
#def weather(type):
#    if type=="sunny":
#        print("Wear a t-shirt it's a sunny day")
#    elif type=="rainy":
#        print("bring an umbrella and boots")
#    elif type=="snowy":
#        print("Wear a warm coat and hat")
#    else:
#        print("Sorry not sure what to suggest for",type)
#weather_input=input("Enter weather sunny, rainy, snowy").lower()
#weather(weather_input)

                                         #guess game
#def guess_game(guess):
#    secret_num="2"
#    if guess.isdigit()==False:
#        print("invalid guess should only use digits")
#    elif guess=="1":
#        print("guess is too low")
#    elif guess=="2":
#        print("guess is right")
#    elif guess=="3":
#     print("guess is too high")
 #   else:
 #    print("it's not a valid guess 1-3")
#guess_input=input("Enter a guess for a secret number (1, 2, 3): ")
#guess_game(guess_input)
#guess_game(guess_input)

#                                    Task 1
#Program: Shirt Sale
#Complete program using   if, elif, else
#Get user input for variable size (S, M, L)
#reply with each shirt size and price (Small = $ 6, Medium = $ 7, Large = $ 8)
#if the reply is other than S, M, L, give a message for not available
#optional: add additional sizes


#def shirt_size(size):
 #if size.isalpha()==False:
 #   print("Please enter valid input S for small, M for medium, L for large: ")
 #elif size=="s":
 #   print("Small = $ 6 ")
 #elif size=="m":
 #   print("Medium = $ 7 ")
 #elif size=="l" :
 #   print("Large = $ 8 ")
 #else:
 #   print("You have entered wrong value please enter small=s, medium=m, large=l: ")
#Calling function
#size=input("Enter size S, M, L")
#shirt_size(size)

                                      # Self task  Simp-le Calculator perform all four functions:

#def Calculator(function,input1,input2,input3):
#    if function=="+":
#        print(input1+input2+input3)
#    elif function=="-":
#        print(input1-input2)
#    elif function== "*":
#      print(input1*input2)
#    elif function=="/":
#        print(input1/input2)
#    else:
#        print("You have enter invalid function")
#sign=input("Enter which function you want to perform +, -, *, /,")
#num1=input("Enter num1: ")
#num2=input("Enter num2: ")
#num3=input("Enter num3 is only for addtion: ")
#Calculator(sign,int(num1),int(num2),int(num3))



                                         #Task 2

#Program: Multiplying Calculator Function
#define function multiply(), and within the function:
#gets user input() of 2 strings made of whole numbers
#cast the input to int()
#multiply the integers and return the equation with result as a str()
#return example
#9 * 13 = 117



#def multiply():
#    a=int(input("Enter input 1: "))
#    b=int(input("Enter input 2: "))
#    multiplay=a*b
#    return str(multiplay)


#print(multiply())


###              TASK 3

#Project: Improved Multiplying Calculator Function¶
#putting together conditionals, input casting and math
#update the multiply() function to multiply or divide
#single parameter is operator with arguments of * or / operator
#default operator is "*" (multiply)
#return the result of multiplication or division
## Review, run, fix

#def multidiv(operation):
#    ainput = int(input("Enter number: "))
#    binput = int(input("Enter number: "))
#    if operation=="*":
#        return (ainput*binput)
#    elif operation=="/":
#        return (ainput/binput)
#    else:
#        return(ainput*binput," is your answer You have not enter a valid operation default operator is '*' ")


#operator=input('Enter operation "* or "/: ')
#print(multidiv(operator))


                                              #1-4.3 Intro Python Practice

#Conditionals
#Student will be able to

#control code flow with if... else conditional logic
#using Boolean string methods (.isupper(), .isalpha(), .startswith()...)
#using comparision (>, <, >=, <=, ==, !=)
#using Strings in comparisons



#Task 1:
# [ ] input avariable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years
# or else print message "It is good to be" age



#age=int(input("Enter age: "))
#if age>=12:
#    print(" on age in 10 years ")
#else:
#    print("it is good to be",age)




#Task 2 if else
# [ ] input a number
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"



#anumber=input("Enter digit: ")
#if anumber.isdigit():
#    eval=int(anumber)
#    if eval > 100:
#        print(anumber,"anumber greater than 100")
#    else:
#     print(anumber,"not grater than 100")
#else:
#    print("only int is accepted ")





#solved....
#Task 3
#Guessing a letter A-Z¶
#check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)

#- if guess is not an alpha character print invalid and return False
#- test and print if guess is "high" or "low" and return False
#- test and print if guess is "correct" and return True


#function()
#def check_guess(letter,guess):
#    if not guess.isalpha():
#      print ( "False enter valid alphabet")
#    else:
#      print(guess,"Entered")
#      if guess > letter:
#        print ("Your guess is High")
#      else:
#       print ("Your guess is Low")
#    if guess == letter:
#     print("Your answer is correct")
#     return True
#    else:
#     print("Your answer is not correct")
#     return False

#Calling function

#ainput=input("Enter alphabet: ")
#aletter="L"
#check_guess(aletter,ainput)

#                OR

#def chcek_guess(letter,guess):
#    if guess > letter:
#        print("guess is high")
#    else:
#        print("guess is low")
#    if guess.isalpha()!=True:
#        return "False invalid input "
#    else:
#        if guess.startswith(letter):
#            return "True answer is correct"
#        else:
#            return "answer is not correct"


#calling function

#aletter="L"
#aguess=input()
#print(chcek_guess(aletter,aguess))


#Q
#Task
#Letter Guess¶
#create letter_guess() function that gives user 3 guesses

#takes a letter character argument for the answer letter
#gets user input for letter guess
#calls check_guess() with answer and guess
#End letter_guess if
#check_guess() equals True, return True
#or after 3 failed attempts, return False


#function()
#def letter_guess(letter,guess):
#    if letter == guess.upper():
#        print("You win first attempt")
#        return True
#    else:
#        guess = input("Enter letter again: ")
#        if letter == guess.upper():
#            print("You win 2nd attempt")
#            return True
#        else:
#            guess = input("Enter letter again last chance")
#            if letter == guess.upper():
#                print("You win 3rd attempt")
#                return True
#            else:
#                print("You lose 3 tries over")
#                return False


#calling function

#aletter=("P")
#bguess=input("Enter letter: ")
#print((letter_guess(aletter,bguess)))

#Calling two function comboine:

#def chcek_guess(letter,guess):
#    if guess > letter:
#        print("guess is high")
#    else:
#        print("guess is low")
#    if guess.isalpha()!=True:
#        return "False invalid input "
#    else:
#        if guess.startswith(letter):
#            return "True answer is correct"
#        else:
#            return "answer is not correct"


######UNSOLVED:
#def letter_guess(letter,guess):
#   if letter == guess:
#       print("You win first attempt")
#       return True
#   else:
#       guess = input("Enter letter again: ")
#       if letter == guess:
#           print("You win 2nd attempt")
#           return True
#       else:
#           guess = input("Enter letter again last chance")
#           if letter == guess:
#               print("You win 3rd attempt")
#               return True
#           else:
#               print("You lose 3 tries over")
#               return False


#def check_guess(letter,guess):
#   if guess > letter:
#       print("guess is high")
#   else:
#       print("guess is low")
#   if guess.isalpha()!=True:
#       return "False invalid input "
#   else:
#       if guess=="L":
#           return "True answer is correct"
#       else:
#        return "False your answer is not correct"

#CALLING TWO FUNCTION
#ainput=input("Enter alphabet: ")
#aletter=str("L")
#print(check_guess(aletter,ainput))
#print(letter_guess(aletter,ainput))


#Pet Conversation¶
#ask the user for a sentence about a pet and then reply

#get user input in variable: about_pet
#using a series of if statements respond with appropriate conversation
#check if "dog" is in the string about_pet (sample reply "Ah, a dog")
#check if "cat" is in the string about_pet
#check if 1 or more animal is in string about_pet
#no need for else's
#finish with thanking for the story

#about_pet = input("Enter a sentence about a pet: ")

#if 'dog' in about_pet.lower():
#    print ("Ah, a dog")
#if 'cat' in about_pet.lower():
#    print ("Ah, a cat")
#elif 'dog, cat' in about_pet.lower():
#      print ("Ah, there is one or more pet")

#print("Thank you for your story")

#End Practice 1-4




                                 #1-5 Intro Python Practice :



#conditionals, type, and mathematics extended

#Task 1:
#Tasks
#Rainbow colors
#ask for input of a favorite rainbow color first letter: ROYGBIV

#Using if, elif, and else:

#print the color matching the letter
#R = Red
#O = Orange
#Y = Yellow
#G = Green
#B = Blue
#I = Indigo
#V = Violet
#else print "no match"

#favorite_color=input("Enter favorite Color First Letter: R, O, Y, G, B, I, V: ").upper()
#if favorite_color=="R":
#    print("Its Red")
#elif favorite_color=="O":
#    print("its Orange")
#elif favorite_color =="Y":
#    print("its Yellow")
#elif favorite_color =="G":
#    print("its Green")
#elif favorite_color =="B":
#    print("its Blue")
#elif favorite_color =="I":
#    print("its Indigo")
#elif favorite_color =="V":
#    print("its Violet")
#else:
#    print("No Match")


#Task 2:
# [ ] make the code above into a function rainbow_color() that has a string parameter,
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.


#def rainbow_color(favorite_color):
#    if favorite_color == "R":
#        print("Its Red")
#    elif favorite_color == "O":
#        print("its Orange")
#    elif favorite_color == "Y":
#        print("its Yellow")
#    elif favorite_color == "G":
#        print("its Green")
#    elif favorite_color == "B":
#        print("its Blue")
#    elif favorite_color == "I":
#        print("its Indigo")
#    elif favorite_color == "V":
#        print("its Violet")
#    else:
#        print("No Match")


#favorite_color=input("Enter favorite Color First Letter: R, O, Y, G, B, I, V: ").upper()
#rainbow_color(favorite_color)


#Task 3
#Create function age_20() that adds or subtracts 20 from your age for a return value based on current age
# (use if)
#call the funtion with user input and then use the return value in a sentence
#example age_20(25) returns 5:

#def age_20(age,function):

#    if function==0:
#        age=age+20
#        return 'Your age after 20 years is:'+ str(age)
#    elif function==1:
#        age=age-20
#        return 'Your age before 20 years was: '+ str(age)

#Your_age=int(input('Enter your age: '))
#fun=int(input("Press 0 for addition and 1 for Subtraction: "))
#print(age_20(Your_age,fun))

#Task 4
#create a function rainbow_or_age that takes a string argument

#if argument is a digit return the value of calling age_20() with the str value cast as int
#if argument is an alphabetical character return the value of calling rainbow_color() with the str
#if neither return FALSE



#def age_20(age,function):

#    if function==0:
#        age=age+20
#        return 'Your age after 20 years is:'+ str(age)
#    elif function==1:
#        age=age-20
#        return 'Your age before 20 years was: '+ str(age)
#    else:
#        return "Enter invalid input"

#def rainbow_color(favorite_color):
#    if favorite_color.upper() == "R":
#        return ("Its Red")
#    elif favorite_color.upper()  == "O":
#        return ("its Orange")
#    elif favorite_color.upper()  == "Y":
#        return ("its Yellow")
#    elif favorite_color.upper() == "G":
#        return ("its Green")
#    elif favorite_color.upper() == "B":
#        return ("its Blue")
#    elif favorite_color.upper() == "I":
#        return ("its Indigo")
#    elif favorite_color.upper() == "V":
#        return ("its Violet")
#    else:
#        return ("No Match")



#def rainbow_or_age(argument):
#    if argument.isdigit():
#      aage=int(argument)
#      afunction=int(input("Press 0 for addition and 1 for Subtraction: "))
#      return age_20(aage,afunction)
#    elif argument.isalpha():
#       return rainbow_color(favorite_color=argument)
#    else:
#        invalid="Invalid input please enter age or color name first letter."
#        return False,invalid

#argument=input("Enter age for age function or color first letter for rainbow function: ")
#print(rainbow_or_age(argument))

##Additional Practice

#num1=int(input("Enter input 1: "))
#num2=int(input("Enter input 2: "))
#average=(num1+num2)/2
#print("Your answer is"+average)


#mul1=int(input("Enter input 1: "))
#mul2=int(input("Enter input 2: "))
#multiplication=mul1*mul2
#print("Your answer is ",str(multiplication))

#add1=int(input("Enter input 1: "))
#add2=int(input("Enter input 2: "))
#addition=add1+add2
#print("your answer is ",str(addition) )



# [ ] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer
#numone=int(input("Enter input 1: "))
#numtwo=int(input("Enter input 2: "))
#if numone ==numtwo:
#    print(numone - numtwo)
#elif numone > numtwo:
#    print(numone - numtwo)
#else:
#    print(numtwo - numone)



# [ ] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [ ] cast the answer to an integer to cut off the decimals and print the result


#numone=float(input("Enter input 1: "))
#numtwo=float(input("Enter input 2: "))
#if numone and numtwo ==0:
#    print("Can't divided by zero error")
#elif numone > numtwo:
#    div=numone / numtwo
#    print(int(div))
#else:
#    div=numtwo / numone3

#    print(int(div))

#End of Pracrice



#Module 3 Required Coding Activity
#Program: Cheese Order¶
#set values for maximum and minimum order variables
#set value for price variable
#get order_amount input and cast to a number
#check order_amount and give message checking against
#over maximum
#under minimum
#else within maximum and minimum give message with calculated price

#print("Programe Cheese Order: ")
#max_value=101
#min_value=0.25
#price_variable=7.5
#order_amount=float(input("Enter cheese order weight (numeric value): "))
#if order_amount >=max_value:
#    print(order_amount,"is more than currently available stock")
#elif order_amount<min_value:
#    print(order_amount,"is below minimum order amount")
#else:
#    ans=price_variable*order_amount
#    print(order_amount,"Costs $",ans)

##           End of Module#3 code submitted.





##                                            ##Start Module #4 (6.1 Intro Python)



#Module 4- Section 1: Nested Conditionals
#Bookmark this page

#programe:
#ab=int(input("Enter number 1 to 3"))
#if ab>=2:
#    if ab>2:
#        print("its number 3")
#    else:
#        print("its number 2")
#else:
#    print("its number 1")

#sandwhich programe:
#sandwhich_type=input('"c" for Cheese or "v" for Veggie Special: ')
#if sandwhich_type.lower()=="c":
#    cheese_type=input('"c" for Cheddar or "m" for Manchego: ')
#    if cheese_type.lower()=="c":
#        print("Here is your Cheddar Cheese sandwich")
#    else:
#        print("Here is your Manchego Cheese sandwich")
#else:
#    print("Here is your Veggie Special")


#programe:
#print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
#sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
#if sandwich_type.lower()=="c":
#    print("Please select a cheese.")
#    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
#    if cheese_type.lower()=="c":
#        print("Here is your Cheddar Cheese sandwich.  Thank you.")
#    elif cheese_type.lower()=="m":
#        print("Here is your Manchego Cheese sandwich.  Thank you.")
#    else:
#        print("Sorry, we don't have", cheese_type, "choice today.")
#elif sandwich_type.lower()=="v":
#    print("Here is your Veggie Special. Thank you.")
#else:
#    print("Sorry, we don't have", sandwich_type, "choice today.")
#print("Goodbye!")


#Task 1
#print("say hello")
#a=input("Enter input yes or no y/n")
#if a.lower()=="y":
#    b=input("full hello y/n")
#    if b.lower()=="y":
#        print("Hello")
#    else:
#        print("hi")
#else:
#    print("friendly nod")

#Task 2
#Nested if - testing for False
#Program: [ ] 3 Guesses
#use nested if statements complete the flowchart code
#create a birds string variable with the names of 1, 2, 3 or more birds to make it easier
#get bird_guess input and use bird_guess in bird_names to generate Boolean True/False
#if the the guess is wrong (False) create a sub test until the user has had 3 guesses

#birds=input("Guess Bird:\n1:Chicken\n2:Crane\n3:Dove\n4:Duck\n5:Eagle\n6:Falcon\n7:Goose\nEnter input: ")
#if birds=="3":
#    print(True,"You win 1st try!")
#else:
#    birds = input("Guess Bird:\n1:Chicken\n2:Crane\n3:Dove\n4:Duck\n5:Eagle\n6:Falcon\n7:Goose\n False Enter input again: ")
#    if birds=="3":
#        print(True,"You win 2nd try!")
#    else:
#        birds = input("Guess Bird:\n1:Chicken\n2:Crane\n3:Dove\n4:Duck\n5:Eagle\n6:Falcon\n7:Goose\n False Enter input last try")
#        if birds=="3":
#            print(True,"You win 3rd try!")
#        else:
#            print("Sorry out of tries")


#Program: pre_word() Function
#Function has a single string parameter that it checks s is a single word starting with "pre"

#Check if word starts with "pre"
#Check if word .isalpha()
#if all checks pass: return True
#if any checks fail: return False
#Test
#get input using the directions: enter a word that starts with "pre":
#call pre_word() with the input string
#test if return value is False and print message explaining not a "pre" word
#else print message explaining is a valid "pre" word


#def pre_word(parameter):
#    if parameter.lower().startswith("pre"):
#        if parameter.isalpha():
#            return True
#        else:
#            return False
#    else:
#        return False
#parameter=input("Enter a word starts with pre")
#print(pre_word(parameter))
#if pre_word(parameter)==False:
#    print("not a pre word")
#else:
#    print("Valid pre word")

#7.1 While loop and Increment:


#while True:
#    weather = input("Enter weather (sunny, rainy, snowy, or quit): ")
#    print()

#    if weather.lower() == "sunny":
#        print("Wear a t-shirt and sunscreen")
#        break
#    elif weather.lower() == "rainy":
#        print("Bring an umbrella and boots")
#        break
#    elif weather.lower() == "snowy":
#        print("Wear a warm coat and hat")
#        break
#    elif weather.lower().startswith("q"):
#        print('"quit" detected, exiting')
#        break
#    else:
#        print("Sorry, not sure what to suggest for", weather +"\n")

#Task 1

#while True
#[ ] Program: Get a name forever ...or until done
#create variable, familar_name, and assign it an empty string ("")
#use while True:
#ask for user input for familar_name (common name friends/family use)
#keep asking until given a non-blank/non-space alphabetical name is received (Hint: Boolean string test)
#break loop and print a greeting using familar_name

#familar_name=""
#while True:
#    familar_name=input("common name friends/family use: ")
#    if familar_name.isalpha():
#        print("Hello",familar_name)
#        break
#else:
#    print("Enter common name friends/family use: ")

#Seat_Count
#seat_count=0
#while True:
#    seat_count=seat_count + 1
#    print("seat occupied",seat_count)
#    if seat_count>=100:
#     break
#     print("Seats finished",seat_count)



# [ ] review the SEAT TYPE COUNT code then run entering: hard, soft, medium and exit

#My programe:
#initialize variable:
#hard_seat=0
#soft_seat=0
#seat_counter=0
#total_seat=10


#while True:
#    seat = input("Enter seat Type=Hard,Soft,Medium and e for exit: ")
#    if seat.lower()=="hard":
#        hard_seat+=1
#        seat_counter+=1
#    elif seat.lower()=="soft":
#        soft_seat+=1
#        seat_counter += 1
#    elif seat.lower()=="medium":
#        print("Enter valid input medium counted as hard")
#        hard_seat+=1
#        seat_counter += 1
#        print("Enter valid input")
#    elif seat.lower().startswith("e"):
#        print("Total Seats:",total_seat,"\nHard seat:",hard_seat,"\nSoft Seat:",soft_seat)
#        break
#    else:
#        print("Input is invalid")
#    if seat_counter==total_seat:
#        print('"Total Seats:" ',total_seat,'"Hard seat:"',hard_seat,'"Soft Seat:"',soft_seat)
#        break

#or

#Same
#Microsoft_programe:

#hard_seats=0
#soft_seats=0
#seat_count=0
#num_seats=4


#while True:
#    seat_type = input('enter seat type of "hard","soft" or "exit" (to finish): ')

#   if seat_type.lower().startswith("e"):
#        print()
#        break
#    elif seat_type.lower() == "hard":
#        hard_seats += 1
#    elif seat_type.lower() == "soft":
#        soft_seats += 1
#    else:
#        print("invalid entry: counted as hard")
#        hard_seats += 1
#    seat_count += 1
#    if seat_count >= num_seats:
#        print("\nseats are full")
#        break

#print(seat_count, "Seats Total: ", hard_seats, "hard and", soft_seats, "soft")


#Task 2:
#Task 2

#incrementing in a while() loop
#Program: Shirt Count
#enter a sizes (S, M, L)
#tally the count of each size
#input "exit" when finished
#report out the purchase of each shirt size

#shirt_count=0
#small=0
#medium=0
#large=0

#while True:
#    shirt=input("Enter shirt size 's' for small, 'm' for medium, 'l' for large and 'e' (exit) for finish the progrmae: ")
#    if shirt.lower().startswith("e") or shirt.lower()=="exit":
#        print(" Total Shirt",shirt_count,"\n Small Size:",small,"\n Medium Size:",medium,"\n Large Size:",large)
#        break
#    elif shirt.lower().startswith("s"):
#        small+=1
#        shirt_count+=1
#    elif shirt.lower().startswith("m"):
#        medium+=1
#        shirt_count+=1
#    elif shirt.lower().startswith("l"):
#        large+=1
#        shirt_count+=1
#    else:
#        print("You have entered invalid input please enter valid input")


#CHALLENGE: Shirt Register (optional)
#Update the Shirt Count program to calculate cost

#use shirt cost (S = 6, M = 7, L = 8)
#to calculate and report the subtotal cost for each size
#to calculate and report the total cost of all shirts

#shirt_count=0
#small=0
#medium=0
#large=0
#total_price=0
#small_price=0
#medium_price=0
#large_price=0
#while True:
#    shirt=input("Enter shirt size 's' for small, 'm' for medium, 'l' for large and 'e' (exit) for finish the progrmae: ")
#    if shirt.lower().startswith("e") or shirt.lower()=="exit":
#        total_price=small_price+medium_price+large_price
#        print(" Small Size:",small,", Total Small price: $",small_price,"\n Medium Size:",medium,", Total Medium price: $",medium_price,"\n Large Size:",large,
#        ", Total Large price: $" ,large_price," \n Total Shirts:",shirt_count,", Total Price: $",total_price,)
#        break
#    elif shirt.lower().startswith("s"):
#        small+=1
#        shirt_count+=1
#        small_price+=6
#    elif shirt.lower().startswith("m"):
#        medium+=1
#        shirt_count+=1
#        medium_price+=7
#    elif shirt.lower().startswith("l"):
#        large+=1
#        shirt_count+=1
#        large_price+=8
#    else:
#        print("You have entered invalid input please enter valid input")

#quiz question
#num_1 = ""
#num_temp = ""
#num_final = ""

#while True:
#    num_1 = input("Enter an integer: ")
#    if num_1.isdigit():
#        num_final = num_temp + num_1
#        num_temp = num_final
#    else:
#        print(num_final)
#        break


#7.2 intro python while loops and increments


#Task 1

#while with comparison operator
#Program: Animal Names
#Use while to get the user input, animal_name, of 4 animals
#use a counter, num_animals, in the while loop condition
#append the names to a string variable, all_animals
#User can exit early by typing "exit" (check if animal_name is "exit" and break)
#when the loop finishes, print the names of all_animals
#-bonus: print "no animals" if animal_name is empty after exiting the loop

#Tip: Think about Sequence and variables that need to be initialized before the while loop
#all_animals=""
#animal_counter=0
#while animal_counter<4:
#    animal_name=input("Enter animal name: ")
#    if animal_name=="exit":
#        print("programe end")
#        break
#    else:
#        animal_counter+=1
#        all_animals+=animal_name+"\n"
#if all_animals.isspace():
#    print("no animal")
#else:
#    print(all_animals)




#Using while with a Boolean String
#Program: Long Number
#Create variables
#int_num and get user input string of only digits
#long_num and initialize it as an empty string
#Create a while loop that runs as long as the input is all digits
#Inside the while loop
#add int_num to the end of long_num
#get user input for int_num again (inside while loop this time)
#After the loop exits
#print the value of long_num


#int_num=input("Enter string digit: ")
#long_num=""
#while int_num.isdigit()==True:
#    int_num=input("Enter string digit or type enter to exit: ")
#    long_num+=int_num
#else:
#    print("programe end",long_num)


#table of 2:
#count = 1
#mul=2
#loop 5 times
#while count < 100:
#    print(mul, "x", count, "=", mul * count)
#    count+=1


#quiz question
#while 3<5:
#    print("wasib")

#x = 0

#while x < 5:
#    x += 1
#    print('loop')

#def ignore_case(name):
#    answer = ""
#    while answer.isalpha() == False:
#        answer = input("enter last name: ")
#    return answer.lower() == name.lower()
#print(ignore_case("Wasib"))
#count = 1

#while count >=1:
#    print("loop")
#    count +=1
#    break


#End of Module 4.

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





                                    #Microsoft: DEV274x  #Intrduction to Python: Fundamentals

#Module 1 Section 1: String Index
#2-1.1 Intro Python
#Sequence: String
#Accessing String Characters with index *
#Accessing sub-strings with index slicing
#Iterating through Characters of a String
#More String Methods


#Student will be able to
#Work with String Characters by index


#String Index
#Accessing a single String Character

#student_name="Wasib"
#print(student_name[0])
#print(student_name[1])
#print(student_name[2])
#print(student_name[3])
#print(student_name[4])


#student_name=input("Enter name: ")
#if student_name[0].lower()=="w":
#   print("Name start with w",student_name)
#elif student_name[0].lower()=="s":
#    print("name start with s",student_name)
#else:
#    print("Not a match try again",student_name)

#student_name="Wasib pervez"
#print(student_name[4])
#print(student_name[5])
#print(student_name[6])

#Task 1:
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
#street_name="Askari 4 House no: Su-80"
#print(street_name[0])
#print(street_name[3])
#print(street_name[5])


# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else

#team_name=input('Enter input: ')
#if team_name[2].lower()=="i":
#    print("There is 'i' ",team_name)
#elif team_name[2].lower()=="o":
#    print("There is 'o' ",team_name)
#elif team_name[2].lower()=="u":
#    print("There is 'u' ",team_name)
#else:
#   print("input has no similar character")

##Concept of Using a negative box:

#Task:2
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name

#street_name="Elephant"
#print(street_name[5])
#print(street_name[6])
#print(street_name[7])



# [ ] create and assign string variable: first_name

# [ ] print the first and last letters of name


#first_name="Wasib Pervez"
#print(first_name[0])
#print(first_name[-1])
















