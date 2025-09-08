# Expense Tracker

def load_make_file():
    print("\n\n\n\n\n\n\n\n\n")
    try:
        with open("_expense_tracker.csv", "r") as file_tracker:
            lines= file_tracker.readlines()
            if not lines:
                with open("_expense_tracker.csv","w") as file_tracker:
                    file_tracker.write("Category,Amount\n")
            elif lines[0]!="Category,Amount\n":
                with open("_expense_tracker.csv","w") as file_tracker:
                    file_tracker.write("Category,Amount\n")           
            else:
                pass
    except FileNotFoundError:
        print("File not Found!\n\n")
        print("Creating New file at same directory as the program.py!\n\n")
        
        with open("_expense_tracker.csv","w") as file_tracker:
                    file_tracker.write("Category,Amount\n")
        print("New File Created! Named: _expense_tracker.csv")

load_make_file()

def read_file():
        with open("_expense_tracker.csv", "r") as file_tracker:
            return file_tracker.readlines()

def add_expense():
    done1= False
    while not done1:
            category_expense= input("Enter Expense Category OR (Enter Done to exit): ")
            category_expense= category_expense.strip().lower()
            if category_expense.replace(" ","").isalpha() and category_expense!="":                 
                    if category_expense=="done":
                         print("Expense Addition Stopped!")
                         done1= True
                    else:
                            try:
                                amount_expense= int(input("Enter the Amount of Expense: "))
                            except ValueError:
                                print("Invalid Input! Expense not Added!")
                            else: 
                                with open("_expense_tracker.csv","a") as file_tracker:
                                    file_tracker.write(f"{category_expense.title()},{amount_expense}\n")
            elif category_expense=="":
                 print("No Input Found!")
            else:
                 print("Only Alpha Characters Allowed for Names!!!")

def list_all_expense():
        lines= read_file()
        if len(lines)<=1:
             print("No Data Found!")
        else:
                print("|"+" No. "+"|"+" Categories".ljust(20)+"  |"+"  Amount (Pkr)".ljust(4)+"  |")
                print("|-----|----------------------|----------------|")
                i=1
                amounts_list=[]
                for line in lines[1:]:
                    line_parts= line.strip("\n").split(",")
                    if len(line_parts)!=2:
                        continue
                    categories= line_parts[0]
                    amounts= line_parts[1]
                    if categories.lower() in ["total amount","list"]:
                         continue
                    print( f"|  {str(i)}  | {categories.ljust(20)} |  {amounts.ljust(12)}  | ")
                    amounts_list.append(int(amounts))
                    if i<=len(lines):
                        i+=1
                    else:
                        break
                
                total_amount= sum(amounts_list)
                print("|-----|----------------------|----------------|")
                print( f"|  -  | Total Amount         |  {str(total_amount).ljust(12)}  | ")
                try:
                    choice= int(input("""Do you want to Write the Total Amount in Expense Tracker External File?
>>> Enter '1 for Yes' and '0 for NO': """))
                except ValueError:
                     print("Invalid Choice!")
                else:
                        if choice==1:
                            last_line= lines[-1].strip("\n").split(",")
                            if last_line[0].strip().lower()=='total amount':
                                 print("Total Amount already found in File!")
                            else:  
                                with open("_expense_tracker.csv","a") as file_tracker:
                                    file_tracker.write(f"Total Amount,{total_amount}\n")
                                print("Done!")
                        elif choice==0:
                            print("Answer: No, Continuing Program\n")
                        else:
                            print("Invalid Choice")

                          
def list_bycat():
        lines=read_file()
        if len(lines)<=1:
             print("No Data Found!")
        else:
            dict_data={}
            for line in lines[1:]:
                line_parts= line.strip("\n").split(",")
                if len(line_parts)!=2:
                    continue
                categories= line_parts[0]
                amounts= line_parts[1]
                if categories.lower() in ["total amount","list"]:
                    continue
                amounts=int(amounts)
                if categories in dict_data:               
                    dict_data[categories]+= amounts
                else:
                    dict_data[categories]=amounts
            print("| Category         | Amount by Category Pkr |")
            print("|------------------|------------------------|")
            for category,amount in sorted(dict_data.items(), key=lambda x:x[1],reverse=True)  :              
                print(f"| {category.ljust(16)} | {str(amount).ljust(22)} |")
            print("|------------------|------------------------|")
            total_amount= sum(dict_data.values())
            print(f"| Total Amount     | {str(total_amount).ljust(22)} |")
        


def file_clear():
        lines=read_file()
        if len(lines)<=1:
            print("List Already Empty!")
        else:
            lines.clear()
            with open("_expense_tracker.csv","w") as file_tracker:
                file_tracker.write("Category,Amount\n")
            print("Expense Tracker List Cleared!")

                
                




                        
print("\n\nWelcome to the Expense Tracker Program!")
print("""
      Following is the List of Actions you can perform in the Program:
    |  No.  | Actions                                    | Action Key |
    |----------------------------------------------------|------------|
    |   1   | Add New Expense Data (Amount and Category) | Add        |
    |   2   | List all Expense Data (With Calculations)  | List       |
    |   3   | List Expense Data Categorically            | ByCat      |
    |   4   | Clear all Data                             | Clear      |
    |   5   | Exit Program                               | Exit       |
      
        NOTE: ENTER THE ACTION KEYS TO PERFORM RESPECTIVE ACTION
        NOTE: THE PROGRAM WILL AUTOMATICALLY MAKE, LOAD, READ AND SAVE THE INFO IN FILE   
        NOTE: YOU CAN ACCESS THE CSV FILE IN THE SAME DIRECTORY AS THE PROGRAM\n
      """)
done= False
while not done:
    print("\n")
    action_key= input("Enter an Action Key: ")
    action_key= action_key.strip().lower()
    action_key_list= ["add", "list", "bycat","clear"]
    if action_key in action_key_list:
         if action_key=="add":
                add_expense()
         elif action_key=="list":
                list_all_expense()
         elif action_key=="bycat":
                list_bycat()
         elif action_key=="clear":
                file_clear()
         
    elif action_key=="":
         print("No Input Found!")
    elif action_key=="exit":
         print("Program Exited Successfully! All changes have been saved!")
         print("Thanks for using!")
         done=True
    else:
         print("Invalid Key!")



