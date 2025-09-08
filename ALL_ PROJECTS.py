#text Styler
user_sentence= input("Enter a Sentence: ")
valid=True
for check in user_sentence:
    if not check.isalpha() and not check.isspace():
        valid=False
        print("Invalid Input! Alphabetic Sentences Only")
        break
if valid:
    print("Choose an operation out of the following:")
    list_operation= {1:"UpperCase", 2:"LowerCase", 3:"ReverseOrder", 4:"Modified Version: Insert Underscores in place of every space in sentence"}
    for key,value in list_operation.items():   # To access items in a list for is simple, for item in list_op..  but for dictionary if we do the same as list, it only prints the keys, to print values too, we need to write two variables key,value and .items() with dict name
        print(key,value)
    op_key=int(input("Enter the operation key number:"))
    if op_key not in list_operation.keys():   # I used op_key is not   but it is wrong   use    op_key not in
        print("Invalid Key!")
    else:
        if op_key==1:
            print(user_sentence.upper())
        elif op_key==2:
            print(user_sentence.lower()) 
        elif op_key==3:
            print(user_sentence[::-1])
        elif op_key==4:
            print(user_sentence.replace(" ","_"))




#Calculator

print("Choose the type of Calculator to use from the following: ")
print("1: Basic Calculator, To use enter 1")
print("2: Exponent Calculator 'Integer Only', To use enter 2")
print("\n")
calc_type=int(input("Enter Calculator type key: "))
if calc_type==1:
            print("""Calculator Operation Description:
        '+' for Addition
        '-' for Subtraction
        '*' for Multiplication
        '/' for Division
        '%' for Modulus, Positive Numbers Only
        '//'for Integer Division, Positive Numbers Only
Note: Both Integer and Floating point input supported""")
            try:
                num1= float(input("Enter first number= "))
            except ValueError:
                print("Invalid Input!, Restart Calculator")
            else:
                operator= (input("Enter an Operator: "))
                operator_list= ["+", "-", "*", "/", "%", "//"]
                if operator in operator_list :
                        try:
                            num2= float(input("Enter second number= "))
                        except ValueError:
                            print("Invalid Input!, Restart Calculator")
                        else:
                             if operator=="+":
                                  print("Result=", num1+num2)
                             elif operator=="-":
                                  print("Result=", num1-num2)
                             elif operator=="*":
                                  print("Result=", num1*num2)
                             elif operator=="/":
                                  if num2==0:
                                        print("Division by Zero!, Restart Calculator")
                                  else:
                                        print("Result=", num1/num2)
                             elif operator=="%":
                                  print("Result=", num1%num2)
                             elif operator=="//":
                                  if num2==0:
                                        print("Division by Zero!, Restart Calculator")
                                  else:
                                        print("Result=", num1//num2)                                              
                else:
                     print("Invalid Input!, Restart Calculator")


elif calc_type==2:
    print("Calculator Operation: Simple exponent math, Enter Base, Enter Power, Get Result\n")
    check= True
    try:
          base=int(input("Enter the base (Integer Only)="))
    except ValueError:
          check=False
          print("Invalid Input!, Enter Integer Only! Restart Calculator")
    if check==True:
          try:
                exponent=int(input("Enter the exponent/power (Integer Only)="))
          except:
                check=False
                print("Invalid Input!, Enter Integer Only! Restart Calculator")
          if check==True:
                result=1
                for index in range(exponent):
                      result=result*base
                print("Result=",result)
else:
      print("Invalid Type Key! Restart Calculator")                       
        
    





#Math Quiz
quiz_questions= [
    ("Q1: What is 12 + 8 = ?", 20),
    ("Q2: What is 25 - 9 = ?", 16),
    ("Q3: What is 7 * 6 = ?", 42),
    ("Q4: What is 40 / 5 = ?", 8),
    ("Q5: What is 17 % 3 = ?", 2)
]
answer_list=[20, 16, 42, 8, 2]            # Here we will make a list of tuples, each tuple will contain the question and answer separated by commas,
score=0                                   # then we can access both in for loop again separated with commas
for questions , correct_answers in quiz_questions:
    print(questions)
    try:
        answer=float(input("Enter your Answer (Integers Only):"))
        if answer== correct_answers:
                    print("Correct Answer!")
                    score+=1
        else:
                    print("Incorrect Answer")
    except ValueError:
        score=0
        print("Invalid Input!, Score Reset to 0")
        
if score>=4:
        print("Congratulations! You Completed the Quiz, Your total Score is: ",score,"/5")
elif score==3:
        print("You passed the Quiz, but got 2 answers wrong Kid,Your total Score is: ",score,"/5")
elif score==2 or score==1:
        print("You passed the Quiz ALMOST!! 😒 Your total Score is: ",score,"/5")
else:
        print("Your score is: ",score,"/5 , You are either an extreme dumb in Mathematics, OR You do not understand what is an integer MR.!")










#Shopping_List:

shopping_list=["Dalda Ghee","Adrak","Pepsi","Mustard Oil" ]
quantity_items= []
print("Welcome to the Shopping List Program")
print("""Following is the list of actions you can perform in this program:
      1: Show List,- - - - - - - - - - - - - - - Keyword: Show
      2: Add an Item,- - - - - - - - - - - - - - Keyword: Add    (Will be ended at the end of List)
      3: Remove an Item,- - - - - - - - - - - -  Keyword: Remove
      4: Insert an item at specific Index,- -  - Keyword: insert (Item will be added in list before the index number you add)  
      5: Remove an item from specific Index,- -  Keyword: iRemove
      6: Sort the List in alphabetical order- -  Keyword: Sort 
      7: Show Number of items in List- - - - - - Keyword: Length
      8: Add Quantity of items in Shopping List- Keyword: Quantity
      9: Print the List on External file- - - -  Keyword: Write
      9: Exit the Program- - - - - - - - - - - - Keyword: Done\n""")
done=False
while not done:  
      list_keyword=["show","add","remove","insert","iremove","sort","length","quantity","write","done"]
      action_key=(input("Enter the Action Key you want to perform:"))
      action_key=action_key.lower()          # Here we just wrote action_key.lower() but fucntions like this lower upper e.t.c returns a new copy of the string, so assign it back to the variable like action_key=action_key.lower()
      
      if action_key==list_keyword[0]:
            i=0
            print("Index | Items                | Quantity")
            print("------------------------------------------")
            for i in range(len(shopping_list)):
                                 if i<len(quantity_items):
                                                  print(str(i).ljust(5),"|",shopping_list[i].ljust(20),"|",quantity_items[i])
                                                  i+=1
                                 else:
                                        print(str(i).ljust(5),"|",shopping_list[i].ljust(20),"|No Quantity Added")
                                        i+=1                                 
      elif action_key==list_keyword[1]:
            append_item=input("Enter the Item you want to add: ")
            shopping_list.append(append_item)
            print("Item added Sucessfully!\n")
      elif action_key==list_keyword[2]:
            remove_item=input("Enter the Item you want to remove: ")
            if remove_item in shopping_list:
                           shopping_list.remove(remove_item)
                           print("Item removed Sucessfully!\n")
            else:
                  print("Item not found in Shopping List")
      elif action_key==list_keyword[3]:
            try:
                  index_insert=int(input("Enter the Index before which item will be inserted: "))
            except ValueError:
                  print("Invaid Index, Try Again")
            else:
                  item_insert=input("Enter the item you want to insert: ")
                  shopping_list.insert(index_insert, item_insert)
                  print("Item inserted before index (",index_insert,") Sucessfully!\n")
      elif action_key==list_keyword[4]:
            try:
                  index_pop=int(input("Enter the index of item to be removed: "))
            except ValueError:
                  print("Invalid Index!, Try Again")
            else:
                  if index_pop>=0 and index_pop<=len(shopping_list)-1:           # Here we wrote this if line(if index_pop>=0 and index_pop<=len(shopping_list):) but the problem is, indexes start at 0, but len function will count from 1 onward, so we will write len(shopping_list)-1
                        print("The Item '",shopping_list[index_pop],"' at index (",index_pop,") removed Sucessfully!")
                        shopping_list.pop(index_pop)
                        print("\n")
                  else:
                        print("Index not found!, Try Again")
      elif action_key==list_keyword[5]:
            shopping_list.sort()
            print("List sorted Sucessfully!\n")
      elif action_key==list_keyword[6]:
            print("There are",len(shopping_list),"number of items in the Shopping List")
      elif action_key==list_keyword[7]:
            for items in shopping_list:
                  quant=input(f"Enter quantity of {items}: ")
                  quantity_items.append(quant)
      elif action_key==list_keyword[8]:
            open("D:\Python\Programs\Projects\_23-08\_file_shopping_list.txt")
            i=0
            print("Index | Items                | Quantity")
            print("------------------------------------------")
            for i in range(len(shopping_list)):
                                 if i<len(quantity_items):
                                                  print(str(i).ljust(5),"|",shopping_list[i].ljust(20),"|",quantity_items[i])
                                                  i+=1
                                 else:
                                        print(str(i).ljust(5),"|",shopping_list[i].ljust(20),"|No Quantity Added")
                                        i+=1
      elif action_key==list_keyword[9]:
            print("Program Ended, Thanks for using.")
            done=True
      elif action_key not in list_keyword:
            print("Invalid Key, Try Again!")

      
              











# Phonebook
phone_book= {
    "hassan" : "033649976741",
    "ayyan" : "03336145465",
    "ifrah" : "03314557678",
    "aslam" : "03446455478",
    "tanveer": "03336123158",
    "naila" : "03325563578",
}
print('Welcome to the PhoneBook Program, Following is the list of actions you can perform: ')
print("""
    Note: Use the indices of actions to access them (for e.g : Enter 1 to show phonebook)
    1: Show the Entire Phonebook 
    2: Find a Phonenumber by name
    3: Add a New Phonenumber or Update Phone Number of Existing Contact
    4: Remove an existing Phonenumber
    5: Dial a Phone number by name
    6: Exit Program""")
done= False
while not done:
              try:
                action_key= int(input("Enter the key to perform required action: "))
              except ValueError:
                print("Invalid Action key, Try Again!")
              else:
                    if action_key==1:
                          print("Name       |Phone Number")
                          for i in phone_book:
                                print(i.capitalize().ljust(10), "|",phone_book[i])
                    elif action_key==2:
                          name= input("Enter name: ")
                          name=name.lower()
                          if name in phone_book:
                                print(name.capitalize()+"'s phone number is: ",phone_book[name])
                          else:
                                print("Name not found in PhoneBook!")
                    elif action_key==3:
                          print("Enter 1 to add a New Contact  OR 2 to update number of existing contact")
                          try:
                              update_key= int(input("Enter key 1 OR 2: "))
                          except ValueError: 
                              print('Invalid Key! Try Again')
                          else:
                              if update_key==1:
                                    update_name= input("Enter name for new contact: ")
                                    update_name=update_name.lower()
                                    update_number= input("Enter phone number of new contact: ")
                                    phone_book.update({update_name : update_number})
                              elif update_key==2:
                                    update_name= input("Enter name of existing contact: ")
                                    update_name=update_name.lower()
                                    if update_name in phone_book:
                                          update_number=input("Enter new phone number for",update_name+"'s contact: ")
                                          phone_book.update({update_name : update_number})
                                    else:
                                          print("Name does not exist in Phonebook, If you want to add new contact use key 1 under Key 3 action")
                              else:
                                    print('Invalid Key, Try Again')
                    elif action_key==4:
                          remove_contact= input('Enter the name of contact to be removed: ')
                          remove_contact=remove_contact.lower()
                          if remove_contact in phone_book:
                                phone_book.pop(remove_contact)
                                print(remove_contact.capitalize()+"'s contact removed successfully!")
                          else:
                                print("Contact not found in PhoneBook!")
                    elif action_key==5:
                          dial_name= input("Enter name of contact to dial there number: ")
                          dial_name=dial_name.lower()
                          if dial_name in phone_book:
                                print("Dialing",dial_name.capitalize()+"'s phone number....")
                                print("+92"+phone_book[dial_name])
                                print("Number Dialed Successfully!")
                          else:
                                print("Contact not Found!")
                    elif action_key==6:
                          print("Phonebook Exited Successfully!")
                          print("Thanks for Using!")
                          done= True
                    else:
                          print("Invalid Action Key! Try Again")
                    
             






















# Student Marks Grading System
print("Welcome to the School's Grading Portal!")
print("You can enter your Obtained Numbers to know your Grade")
print("Note: Enter '-1' to exit the program ")
done=False
while not done:

    try:
        print("\n")
        marks=int(input("Enter your total Obtained Marks (Matric) / '-1' to exit: "))
        print("\n")
    except ValueError:
        print("Invalid Input!")
    else:
        if marks>=0 and marks<=1200:
            percentage= (marks/1200)*100
            percentage= round(percentage, 2)
            if percentage>=95:
                print("Congratulations! You have secured an Exceptional",percentage,"% !")
                print("Your Grade is an Exceptional A++ ! ")
            elif percentage>=90:
                print("Congratulations! You have secured an Outstanding",percentage,"% !")
                print("Your Grade is an Outstanding A+")
            elif percentage>=85:
                print("Congratulations! You have secured an Excellent",percentage,"% !")
                print("Your Grade is an Excellent A")
            elif percentage>=80:
                print("Congratulations! You have secured",percentage,"% !")
                print("Your Grade is a Very Good B++")
            elif percentage>=75:
                print("Congratulations! You have secured",percentage,"% !")
                print("Your Grade is a Good B+")
            elif percentage>=70:
                print("Congratulations! You have secured",percentage,"% !")
                print("Your Grade is a Fairly Good B")
            elif percentage>=60:
                print("You have secured",percentage,"% !")
                print("Your Grade is an Above Average C")
            elif percentage>=50:
                if percentage==50:
                        print("You passed!",percentage,"% ! Half Century Ahh Percentage, But Sadly this is'nt Cricket!")
                        print("Your Grade is an Average D")
                else:
                        print("You have secured",percentage,"% !")
                        print("Your Grade is an Average D")
            elif percentage>=40:
                print("You Passed.....BARELY! Percentage is ",percentage,"% ! Close to a Half Century, But sadly you got stuck in the 40s")
                print("You got an amazing Below Average Grade which is......................... C   Tadaaa!!")
            elif percentage<40 and percentage>15:
                print("Well WEll WELL! Do you still want to know the Percentage",percentage,"%")
                print("U got a Grade,..................... Read the first letter")
                print("It's U, You were meant for U")
                print("YOU MESSED UP BRO, YOU FAILED SUCCESSFULLY!")
            elif percentage<=15:
                print("You just fucked up Extremely BAD")
                print("No one get's grade here buddy!")
                print("Here is your fruit: ",percentage,"%")
            
            

            
        elif marks==-1:
            print("Program Exited! Thanks for Using") 
            done=True 
        else:
            print("Invalid Marks! For Matric the total numbers are 1200")


#Login System
credentials={
    "mail"     : 'hassan@gmail.com',
    "username" : 'hassan_0412',
    "password" : 'scavenger_8877',
}
print("\n\n")
print("Welcome to Instagram")
print("Enter Credentials to Login to your Account!")
print("You have only 3 Tries")
i=3
while i>=1 and i<=3:
        user_name= input(" >> Username or Mail Address |")
        pass_word= input(" >> Password                 |")
        if user_name==credentials["username"] or user_name==credentials["mail"] and pass_word==credentials["password"]:
                print("Logging in...........")
                print("Logged in Successfully!")
                i=4
        else:
                print("Wrong Credentials! Try Again")
                i-=1
                print(i,"Tries Left")
                if i==0:
                    print(i,"Tries Left!")
                    print("You can't login right now! Please Try Again Later!")
                    i=4





















#Multiplication Table
#Using for Loop

print("\n\n")
print("Multiplication Tables Program")

print("\n")

try:
    table_number=int(input("Enter the Table Number: "))
    table_length= int(input("Enter the Length of Table: "))
except ValueError:
    print("Invalid Input! Enter Integer Numbers Only!")
else:
    if table_number>0 and table_length>0:
        for i in range(1,table_length+1):
            print(table_number,"   X   ",str(i).ljust(2),"   =   ",table_number*i)
    else:
        print("Invalid Input! Enter Positive Integers Only")

#Using While Loop
print("\n\n")
print("Multiplication Tables Program")
print("\n")
try:
    table_number=int(input("Enter the Table Number: "))
    table_length= int(input("Enter the Length of Table: "))
except ValueError:
    print("Invalid Input! Enter Integer Numbers Only!")
else:
    if table_number>0 and table_length>0:
        index= 1
        while index:
            print(table_number,"   X   ",str(index).ljust(2),"   =   ",table_number*index)
            if index<table_length:
                index+=1
            else:
                break
    else:
        print("Invalid Input! Enter Positive Integers Only")


# Guess the Number Using for loops
import random
print("Welcome to the Guess the Number Game!")
print("""Difficulty Level Description:
        Easy: The Secret Number exists within numbers 1 to 20 and You will have 10 Tries
        Medium: The Secret Number exists within numbers 1 to 50 and You will have 15 Tries
        Hard: The Secret Number exists within numbers 1 to 100 and You will have 20 Tries
        Impossible: The Secret Number can exist from anywhere between 0 to Infinity
        Note: Enter Exit to end the game\n""")

done=False
while not done:
    level_difficulty=input("Enter difficulty level from the available ones (Enter Exit to eng game): ")
    level_difficulty=level_difficulty.lower()
    level_list=["easy","medium","hard","impossible"]
    if level_difficulty in level_list:
        if level_difficulty=="easy":
            random_number= random.randint(1,20)
            print("A Secret number is picked within the range of 1 to 20, Try to Guess it!\n")
            tries=10
            for i in range(0,10):
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        elif level_difficulty=="medium":
            random_number= random.randint(1,50)
            print("A Secret number is picked within the range of 1 to 50, Try to Guess it!\n")
            tries=15
            for i in range(0,15):
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        
        elif level_difficulty=="hard":
            random_number= random.randint(1,100)
            print("A Secret number is picked within the range of 1 to 50, Try to Guess it!\n")
            tries=20
            for i in range(0,20):
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        elif level_difficulty=="impossible":
            print("GO TOUCH SOME GRASS, VELA INSAAN!")


    elif level_difficulty=="exit":
        print("Game Ended!")
        done=True
    else:
        print("Invalid Input! Choose a Difficulty Level from the given list ONLY!")




#Guess game using While Loop:
print("Welcome to the Guess the Number Game!")
print("""Difficulty Level Description:
        Easy: The Secret Number exists within numbers 1 to 20 and You will have 10 Tries
        Medium: The Secret Number exists within numbers 1 to 50 and You will have 15 Tries
        Hard: The Secret Number exists within numbers 1 to 100 and You will have 20 Tries
        Impossible: The Secret Number can exist from anywhere between 0 to Infinity
        Note: Enter Exit to end the game\n""")
done=False
while not done:
    level_difficulty=input("Enter difficulty level from the available ones (Enter Exit to eng game): ")
    level_difficulty=level_difficulty.lower()
    level_list=["easy","medium","hard","impossible"]
    if level_difficulty in level_list:
        if level_difficulty=="easy":
            random_number= random.randint(1,20)
            print("A Secret number is picked within the range of 1 to 20, Try to Guess it!\n")
            tries=10
            while tries>0:
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        elif level_difficulty=="medium":
            random_number= random.randint(1,50)
            print("A Secret number is picked within the range of 1 to 50, Try to Guess it!\n")
            tries=15
            while tries>0:
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        
        elif level_difficulty=="hard":
            random_number= random.randint(1,100)
            print("A Secret number is picked within the range of 1 to 100, Try to Guess it!\n")
            tries=20
            while tries>0:
                user_guess=int(input("Enter your Guess: "))
                if user_guess==random_number:
                    print("Congratulations! You Guessed the Number Correctly, It was",random_number,"\n")
                    break
                else:
                    tries-=1
                    print("Incorrect Guess! You have",tries,"tries left!\n")
                if tries==0:
                    print("You ran out of Tries! The number was",random_number,"\n")
                    print("Try Again\n\n")
        elif level_difficulty=="impossible":
            print("GO TOUCH SOME GRASS, VELA INSAAN!")


    elif level_difficulty=="exit":
        print("Game Ended!")
        done=True
    else:
        print("Invalid Input! Choose a Difficulty Level from the given list ONLY!")
        






















#Calculator with Functions
print("Basic Calculator")
print("\n")
print("""Calculator Operation Description:
        '+' for Addition
        '-' for Subtraction
        '*' for Multiplication
        '/' for Division
        '%' for Modulus, Positive Numbers Only
        '//'for Integer Division, Positive Numbers Only
        '!' for Factorial
    'prime' for checking whether a number is Prime or Not
Note: Both Integer and Floating point input supported\n""")

def addition_function(num1, num2):
    add= num1+num2
    return add

def subtraction_function(num1, num2):
    subtract= num1-num2
    return subtract

def multiply_function(num1, num2):
    multiply= num1*num2
    return multiply

def division_function(num1, num2):
    divide= num1/num2
    return divide

def modulus_function(num1, num2):
    modulus= num1%num2
    return modulus

def intdivision_function(num1, num2):
    intdivide= num1//num2
    return intdivide

def factorial_function(num1):
    fact=1
    i=1
    while i<=num1:
        fact=fact*i
        i+=1
    return fact

def prime_check(num1):
    if num1>1:
        i=2
        while i<num1:
            prime=num1%i
            if prime==0:
                print("The Number",num1,"is not a Prime Number!")
                return
            i+=1
        print("The Number",num1,"is a Prime Number!")
    else:
        print("Prime Numbers are greater then 1 only")
done=False
while not done:

    num1= input("Enter first number (or type Exit to End Program)= ")
    if num1.lower()=="exit":
        print("Calculator Closed!")
        done=True
    else:
        try:
            num1=float(num1)
        except ValueError:
            print("Invalid Input!, Try Again!")
        else:
            operator= input("Enter an Operator (or type Exit to End Program): ")
            operator=operator.lower()
            if operator=="exit":
                print("Calculator Closed!")
                done=True
            else:
                operator_list= ["+", "-", "*", "/", "%", "//"]
                if operator in operator_list :
                    num2= input("Enter second number (or type Exit to End Program)= ")
                    if num2.lower()=="exit":
                        print("Calculator Closed!")
                        done=True
                    else:
                        try:
                            num2=float(num2)
                        except ValueError:
                            print("Invalid Input!, Try Again!")
                        else:
                            if operator=="+":
                                output=addition_function(num1,num2)
                                print("The answer is:",output)
                            elif operator=="-":
                                output=subtraction_function(num1,num2)
                                print("The answer is:",output)
                            elif operator=="*":
                                output=multiply_function(num1,num2)
                                print("The answer is:",output)
                            elif operator=="/":
                                if num2==0:
                                    print("Division by Zero!")
                                else:
                                    output=division_function(num1,num2)
                                    print("The answer is:",output)
                            elif operator=="%":
                                if num2==0:
                                    print("Division by Zero!")
                                else:
                                    output=modulus_function(num1,num2)
                                    print("The answer is:",output)
                            elif operator=="//":
                                if num2==0:
                                    print("Division by Zero!")
                                else:
                                    output=intdivision_function(num1,num2)
                                    print("The answer is:",output)
                elif operator=="!" or operator=="prime":
                            if operator=="!":
                                num1=int(num1)
                                output=factorial_function(num1)
                                print("The Factorial of",num1,"is:",output)
                            else:
                                num1=int(num1)
                                prime_check(num1)



        
                else:
                    print("Invalid Input!, Try Again!")


        



























#The Todo List Program
  

try:
      with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
            file=file_task.readlines()
            if file==[]:
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "a") as file_task:
                        file= file_task.write("""NO. | TASK                                              | COMPLETION |\n""")            # TASK NO. WIDTH= 4,   TASK WIDTH =25, COMPLETION WIDTH 12
                        task_no=1
            else:
                  task_no=len(file)
      print("\n\n")
      print("Welcome to the To-Do List Program!")
      print("Following is the list of actions that can be performed in the program:")
      print("""
                           
                     
                    |TO-DO LIST|
    NO.| TASK NAME                      | TASK KEY (INPUT)
    -------------------------------------
    1: | View the To-Do List            | View
    2: | Add a New Task                 | Add
    3: | Mark an existing Task Complete | Mark
    4: | Remove a Task                  | Remove
    5: | Clear To-Do List               | Clear
    6: | Search a Task by Keyword       | Search
    7: | Edit a Task by Index           | Edit
    8: | Exit To-Do List Program        | Exit   \n""")

except FileNotFoundError:
      print("No To Do List File Found at Directory!\n")
      print("""Creating a New To Do List File at the Following Directory:
               D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt
               File Name: _tasks.txt\n""")
      print("New To Do List File Created Successfully! You can now Continue with the To Do List Program\n\n")
      with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "w") as file_task:
            with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "a") as file_task:
                        file= file_task.write("""NO. | TASK                                              | COMPLETION |\n""")            # TASK NO. WIDTH= 4,   TASK WIDTH =25, COMPLETION WIDTH 12
                        task_no=1
      print("\n\n")
      print("Welcome to the To-Do List Program!")
      print("Following is the list of actions that can be performed in the program:")
      print("""
                           
                     
                    |TO-DO LIST|
    NO.| TASK NAME                      | TASK KEY (INPUT)
    -------------------------------------
    1: | View the To-Do List            | View
    2: | Add a New Task                 | Add
    3: | Mark an existing Task Complete | Mark
    4: | Remove a Task                  | Remove
    5: | Clear To-Do List               | Clear
    6: | Search a Task by Keyword       | Search
    7: | Edit a Task by Index           | Edit
    8: | Exit To-Do List Program        | Exit   \n""")

done=False
while not done:

    action_key=input("Enter the Action Key of any Task to perform: ")
    action_key=action_key.lower()
    action_key_list=["view", "add", "mark", "remove", "clear", "search","edit", "exit"]
    if action_key in action_key_list:
            if action_key=="view":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        file= file_task.read()
                        if task_no==1:
                              print('No Task Found in List!')
                        else:
                              print(file)
            
            elif action_key=="add":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "a") as file_task:
                        print("\n")
                        print("Program will repeatedly ask you to add new items!")
                        print("To Stop adding enter keyword: 'done'")
                        print("\n")
                        done1=False
                        while not done1:
                            add_task= input("Enter the Task you want to add OR (Done to exit): ")
                            add_task=add_task.lower()
                            if add_task=="done":
                                  print("Task Addition Stopped!\n")
                                  done1=True
                            elif add_task=="":
                                  print("No Task Entered! Please Type in Something to add")
                            else:
                                  add_task=add_task.capitalize()
                                  file= file_task.write(str(task_no).ljust(4)+"| "+add_task.ljust(50)+"|".ljust(12)+" |"+"\n")
                                  task_no+=1
                                  print("Task Added!")
            
            elif action_key=="mark":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        lines=file_task.readlines()
                        print("\n")
                        try:
                            mark_task=int(input("Enter the Task No. you want to mark as Complete: "))
                        except ValueError:
                              print("Invalid Task No. !")
                        else:
                              file=file_task.readlines()
                              if mark_task>=task_no or mark_task<=0:
                                    print("No Task exists at Index:",mark_task)
                              else:
                                    line_mark= lines[mark_task].rstrip("\n").split("|")    # Take the selected line and remove the "\n" at the end (rstrip)  # Then split it into separate parts (columns) wherever "|" appears, split makes a  pyhton list of our line by placing commas in place of |  # Example: "2 | Buy Milk       |           |" → ["2 ", " Buy Milk       ", "           ", ""]
                                    line_mark[2]=" Completed! "                            # We access the 3rd part (index 2 → Completion column) and replace it with "Complete"  # Now the list looks like: ["2 ", " Buy Milk       ", "   Complete   ", ""]
                                    lines[mark_task]= "|".join(line_mark)+"\n"             # Finally, join all the parts back together using "|" as the separator # This rebuilds the full line with updated completion status  # Add "\n" again at the end so it stays a proper line in the text file
                                    
                                    with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "w") as file_task:
                                          file_task.writelines(lines)
                                    print("Task at Index:",mark_task,"Marked Completed!")
            
            elif action_key=="remove":
                   with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        lines=file_task.readlines()
                        print("\n")
                        try:
                            remove_task=int(input("Enter the Task No. you want to Remove from the List: "))
                        except ValueError:
                              print("Invalid Task No. !")
                        else:
                              if remove_task>=task_no or remove_task<=0:
                                    print("No Task exists at Index:",remove_task)
                              else:
                                    lines.pop(remove_task)
                                    for i in range(1, len(lines)):     #lines uses readlines and has a list of all the lines of todo list, we loop through all lines, start from 1 because first line is header upto len(lines)
                                          line_remove= lines[i].split("|")   #Split makes a temporay list of each line, by putting commas in place of |
                                          line_remove[0]=str(i).ljust(4)     #We access the first item of temporarily made list of line by split, which is the counter, and overwrite it with i which will put the correct task_no
                                          lines[i]="|".join(line_remove)     #We join the temporary split list of each line with | again THIS WORKS PRETTY SIMILAR TO THE MARK COMPLETE ACTION ABOVE
                                    
                                    with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "w") as file_task:
                                          file_task.writelines(lines)
                                    print("Task at Index",remove_task,"Removed Successfully!")
            elif action_key=="clear":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        lines=file_task.readlines()
                        while len(lines)>1:
                              lines.pop()
                  
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "w") as file_task:
                        file_task.writelines(lines)
                  print("To-Do List Cleared!")
                  task_no=1
            
            elif action_key=="search":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        lines=file_task.readlines()
                  print("\n")
                  found= False
                  keyword= input("Enter a Keyword to Search/Filter related Task/s: ")
                  if keyword=="":
                        print("Please Enter a Keyword! No Input Found!")
                  else:
                        for i in range(1,len(lines)):
                              if keyword.lower() in lines[i].lower():
                                    print(lines[i].rstrip("\n"))
                                    found=True
                        if not found:
                              print("No Task found with the keyword:", keyword)
                       
            
            elif action_key=="edit":
                  with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "r") as file_task:
                        lines=file_task.readlines()
                        print("\n")
                        try:
                            edit_task=int(input("Enter the Task No. you want to edit: "))
                            print("\n")
                        except ValueError:
                              print("Invalid Task No. !")
                        else:
                               if edit_task>=task_no or edit_task<=0:
                                    print("No Task exists at Index:",edit_task)
                               else:
                                     line_edit=lines[edit_task].rstrip("\n").split("|")
                                     print("Task at Index",edit_task,"is",">>>>>>  ",line_edit[1])
                                     edited_task=input("Enter the Edited or Changed Task: ")
                                     if edited_task=="":
                                           print("Please Enter a Task! No Input Found!")
                                     else:
                                          line_edit[1]=" "+edited_task.ljust(50)
                                          lines[edit_task]="|".join(line_edit)+"\n"

                                          with open("D:\Python\Programs\Projects\_31-08 (29-08)\_tasks.txt", "w") as file_task:
                                                file_task.writelines(lines)
                                          print('Task Edited Successfully!')
            elif action_key=="exit":
                  print("\n")
                  print("All Progress Saved!")
                  print("To-Do List Program Exited!")
                  done= True
            
    else:
      print("Invalid Action Key!")


                                     
























#Password_Generator
import string
print("\n\n\n\n\n\n\n\n\n\n")
print("Welcome to the Password Generator Program!")
print("""You can generate different types of passwords, Following is the HOW TO?
            1: Simple Password: Contains only Alphabets (Upper and Lower Case)     (KEY: Simple)
            2: Medium Password: Contains Simple Password with Numbers              (KEY: Medium)
            3: Complex Password: Contains Medium password with Special Characters  (KEY: Complex)
            Type the Respective key to generate a password of that type
            You can also enter the length of password to be generated (MAX LENGTH: 16, MIN LENGTH: 4)
            Type Exit to exit the program!  """)

pass_simple= string.ascii_lowercase + string.ascii_uppercase
pass_medium= pass_simple + string.digits
pass_complex= pass_medium + string.punctuation 

done=False
while not done:
        print("\n")
        type_input= input("Enter a Key to generate password OR (Type Exit): ")
        type_input= type_input.lower()
        print("\n")
        type_input_list= ["simple", "medium", "complex"]
        if type_input in type_input_list:
            try:
                pass_length= int(input("Enter the Length of Password (MAX: 16, MIN: 4): "))
                print("\n")
            except ValueError:
                print("\n")
                print("Enter a Valid Integer Digit for Length!")
            else:
                if pass_length<=16 and pass_length>=4:
                        password=""
                        if type_input=="simple":
                                for i in range(pass_length):
                                    password+= random.choice(pass_simple)
                                password_list= list(password)
                                random.shuffle(password_list)
                                password="".join(password_list)
                                print("\nPassword Generated!")
                                print("The Passwrod is:  ",password)
                        
                        elif type_input=="medium":
                                for i in range(pass_length):
                                    password+= random.choice(pass_medium)
                                password_list= list(password)
                                random.shuffle(password_list)
                                password="".join(password_list)
                                print("\nPassword Generated!")
                                print("The Passwrod is:  ",password)

                        elif type_input=="complex":
                                for i in range(pass_length):
                                    password+= random.choice(pass_complex)
                                password_list= list(password)
                                random.shuffle(password_list)
                                password="".join(password_list)
                                print("\nPassword Generated!")
                                print("The Passwrod is:  ",password)
                            
                        else:
                              print("Invalid Key!")
                elif pass_length=="":
                      print("No Input Found!")
                else:
                      print("Length out of Limit!")
        elif type_input=="exit":
              print("Program Exited Successfully!")
              done=True               
        elif type_input=="":
                print("No Input Found! Type a Valid KEY!")
        else:
                print("Invalid Key!")

        














