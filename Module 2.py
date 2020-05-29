
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
