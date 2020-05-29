Module #3 Start
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

