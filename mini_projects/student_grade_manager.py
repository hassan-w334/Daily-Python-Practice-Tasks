#Student Grade Manager
def load_make_file():
    print("\n\n\n\n\n\n\n\n")
    try:
        with open("_grade_manager.csv", "r") as file_grade:
            lines= file_grade.readlines()
            if not lines:                                             
                 with open("_grade_manager.csv", "w") as file_grade:
                      file_grade.write("Name,Marks\n")
            
            elif lines[0]!="Name,Marks\n":
                 with open("_grade_manager.csv", "w") as file_grade:
                      file_grade.write("Name,Marks\n")
                      file_grade.writelines(lines)
                      
                 
            else:
                pass
    except FileNotFoundError:
        print("\n NO FILE FOUND!")
        print("\n CREATING NEW FILE!")
        
        with open("_grade_manager.csv", "w") as file_grade:
            file_grade.write("Name,Marks\n")
        print("\n NEW FILE CREATED !\n\n\n")
load_make_file()


def read_file():
    with open("_grade_manager.csv", "r") as file_grade:
        return file_grade.readlines()
    

        

def add_file():
        done1=False
        while not done1:
            name= input("Enter the name of Student or (Type Done to Stop adding!): ")
            name=name.strip().lower()
            if name.replace(" ", "").isalpha() and name != "":
                  if name=="done":
                    print("\nData Addition Stopped!")
                    done1=True
                  else:
                        try:
                            marks= int(input("Enter the marks of Student: "))
                        except ValueError:
                            print("Invalid Input! Name and Marks not Added!")
                        else:
                            with open("_grade_manager.csv", "a") as file_grade:
                                file_grade.write(f"{name.title()},{marks}\n")
            elif name=="":
                    print("No Input Found!")
            else:
                 print("Only Alpha Characters Allowed for Names!!!")                        


def calculate_stats():
    lines= read_file()
    if len(lines)<=1:
         print("No Student Data Found!")   
    else:   
        marks_list=[]    
        highest_marks=-1
        highest_name= ""
        lowest_marks= 101
        lowest_name= ""
        for line in lines[1:]:                  
            line_parts= line.strip("\n").split(",")
            names= line_parts[0]
            marks=int(line_parts[1])

            if marks>highest_marks:
                 highest_marks=marks
                 highest_name= names
            
            if marks<lowest_marks:
                 lowest_marks=marks
                 lowest_name=names
            marks_list.append(marks)
        average= sum(marks_list)/len(marks_list)
        print("\nThe calculated student statistics of class are as follows:")
        print("\n>>> The Highest Achiever of Class is",highest_name+", He/She Secured",highest_marks,"as a whole!")
        print(">>> The Lowest Achiever of Class is",lowest_name+", He/She got only",lowest_marks,"as a whole!")
        print(">>> Average of Total Marks of Class:",str(average)+"%")

def list_all_students():
    lines=read_file()
    if len(lines)<=1:
        print("No Student Data Found!") 
    else:
        print("""You have three options for Sorting Srudent data in the generated List:
            1: Sort by Alphabetical Order of Student Names >>>>>>>>>>>  (Enter '1' as Input!)
            2: Sort by Marks of Students 'Highest to Lowest'>>>>>>>>>>  (Enter '2' as Input!)
            3: Sort in Original Entry Order (as students were added) >> (Enter '3' as Input! ) """)
        try:
            choice= int(input("Enter Sort Option Choice (1,2 or 3): "))
        except ValueError:
             print("Invalid Choice Try Again!")
        else:
            students=[]
            for line in lines[1:]:
                    line_parts= line.strip("\n").split(",")
                    if len(line_parts)!=2:
                        continue
                    students.append(line_parts)
            if choice==1:
                students= sorted(students, key=lambda x:x[0])
                i=1
                print("|","No.","|"," Names".ljust(22),"|","Marks".ljust(4),"|")
                print("----------------------------------------")
                for student in students:
                    names= student[0]
                    marks= student[1]
                    print("| ",str(i)," | ",names.ljust(20)," | ",marks.ljust(4),"|")      
                    if i<=len(names):
                        i+=1
                    else:
                        break
            
            elif choice==2:
                students= sorted(students, key=lambda x:int(x[1]), reverse=True)
                i=1
                print("|","No.","|"," Names".ljust(22),"|","Marks".ljust(4),"|")
                print("----------------------------------------")
                for student in students:
                    names= student[0]
                    marks= student[1]
                    print("| ",str(i)," | ",names.ljust(20)," | ",marks.ljust(4),"|")      
                    if i<=len(names):
                        i+=1
                    else:
                        break
            elif choice==3:
                i=1
                print("|","No.","|"," Names".ljust(22),"|","Marks".ljust(4),"|")
                print("----------------------------------------")
                for line in lines[1:]:
                    line_parts= line.strip("\n").split(",")
                    if len(line_parts)!=2:
                        continue
                    names= line_parts[0]
                    marks= line_parts[1]
                    print("| ",str(i)," | ",names.ljust(20)," | ",marks.ljust(4),"|")      # Can also write this as  #print(f"| {str(i).ljust(3)} | {names.ljust(20)} | {marks.ljust(5)} |")
                    if i<=len(names):
                        i+=1
                    else:
                        break
            else:
                 print("Invalid Choice Try Again!")
               
def search_student():
        lines=read_file()
        if len(lines)<=1:
            print("No Student Data Found!")
        else:
             name_search=input("Enter the name of student to Search for: ")
             name_search=name_search.strip().lower()
             if name_search.replace(" ", "").isalpha() and name_search != "":
                    i=0
                    file_index=1
                    found=False
                    for line in lines[1:]:
                        line_parts=line.strip("\n").split(",")
                        names= line_parts[0]
                        marks= line_parts[1]
                        i+=1
                        file_index+=1
                        if name_search==names.lower():
                            print("\nStudent Found!\n")
                            print("|","No.","|"," Names".ljust(22),"|","Marks".ljust(4),"|")
                            print("| ",str(i)," | ",names.ljust(20)," | ",marks.ljust(4),"|")
                            print("\nThe Index of Student named",names,"inside actual Excel file is",file_index)

                            found=True
                            break
                    if found==False:
                         print("No Data found for",name_search.title())
             else:
                  print("Only Alpha Characters Allowed! No Empty Input!")
                  
def remove_student():
        lines=read_file()
        if len(lines)<=1:
            print("No Student Data Found!")
        else:
            name_remove= input("Enter the name of student to delete from List: ")
            name_remove= name_remove.strip().lower()
            if name_remove.replace(" ", "").isalpha() and name_remove != "":
                i=0
                file_index=1
                found=False
                for line in lines[1:]:
                    line_parts=line.strip("\n").split(",")
                    names= line_parts[0]
                    marks= line_parts[1]
                    i+=1
                    file_index+=1
                    if name_remove==names.lower():
                         print("\nStudent named",names,"is found at index",str(i)+", Marks=",marks,"\n")
                         print(names+"'s data at Excel File index",file_index,"has been removed from the Grade Manager List Successfully!")
                         found=True
                         lines.pop(i)
                         with open("_grade_manager.csv", "w") as file_grade:
                              file_grade.writelines(lines)
                if not found:
                     print("No Data found for",name_remove.title())
            else:
                 print("Only Alpha Characters Allowed! No Empty Input!")

def edit_student():
        lines=read_file()
        if len(lines)<=1:
            print("No Student Data Found!")
        else:
            name_edit= input("Enter the name of student to Edit his/her data: ")
            name_edit= name_edit.strip().lower()
            if name_edit.replace(" ", "").isalpha() and name_edit != "":
                    i=0
                    file_index=1
                    found=False
                    for line in lines[1:]:
                        line_parts=line.strip("\n").split(",")
                        names= line_parts[0]
                        marks= line_parts[1]
                        i+=1
                        file_index+=1
                        if name_edit==names.lower():
                            print("Student Data Found! It is as Follows: ")
                            print("Name:",names,"  Marks=",str(marks)+", at Index",i," OR Excel Row",file_index,"\n")
                            found=True
                            break
                    if not found:
                         print("No Data found for Student named",name_edit.title())
                         
                    if found:        
                        print("Enter '1' to Edit Name of Student OR Enter '2' to Edit Marks of Student")
                        try:
                            choice=int(input("Enter 1 or 2: "))
                        except ValueError:
                            print("Invalid Choice, Try Again!")
                        else:
                            if choice==1:
                                edited_name= input("Enter new Name OR Edit the Existing one: ")
                                if edited_name.replace(" ", "").isalpha() and edited_name != "":
                                    lines[i]=f"{edited_name.title()},{marks}\n"
                                    print("Student Data Updated Successfully!")
                                else:
                                    print("Only Alpha Characters Allowed! No Empty Input!")
                            elif choice==2:
                                try:
                                    edited_marks= int(input("Enter new marks OR Edit the Existing one: "))
                                except ValueError:
                                     print("Invalid Input! Try Again!")
                                else:
                                     lines[i]=f"{names.title()},{edited_marks}\n"
                                     print("Student Data Updated Successfully!")
                            else:
                                 print("Invalid Choice! Try Again!")
                            with open("_grade_manager.csv", "w") as file_grade:
                                 file_grade.writelines(lines)
                            
            else:
                 print("Only Alpha Characters Allowed! No Empty Input!")

def clear_data():
    lines=read_file()
    if len(lines)<=1:
        print("List Already Empty!")
    else:
         lines.clear()
         print("List Cleared Successfully")
         with open("_grade_manager.csv", "w") as file_grade:
            file_grade.writelines(lines)
         if not lines or lines[0]!="Name,Marks\n":                        
                 with open("_grade_manager.csv", "w") as file_grade:
                      file_grade.write("Name,Marks\n")
        
         

#-------------------------------------------------------------------------------------------------------------------------------------#

print("Welcome to the Student Grade Manager!")
print("Following is the List of Actions that can be performed in this Program:")
print("""
    |  No.  | Actions                                | Action Key |
    |------------------------------------------------|------------|
    |   1   | Add a New Student                      | Add        |
    |   2   | Calculate Academic Stats of Student/s  | Stats      |
    |   3   | List all Students                      | List       |
    |   4   | Search a Student by Name               | Search     |
    |   5   | Remove a Student and Data              | Remove     |
    |   6   | Edit an Existing Student's Information | Edit       |
    |   7   | Clear all Data                         | Clear      |
    |   8   | Exit Program                           | Exit       |
      
        NOTE: ENTER THE ACTION KEYS TO PERFORM RESPECTIVE ACTION
        NOTE: THE PROGRAM WILL AUTOMATICALLY MAKE, LOAD, READ AND SAVE THE INFO IN FILE   
        NOTE: YOU CAN ACCESS THE CSV FILE IN THE SAME DIRECTORY AS THE PROGRAM\n        """) 

done=False
while not done:
     action_key=input("Enter an Action Key: ")
     action_key=action_key.lower()
     action_key_list=["add", "stats", "list", "search", "remove", "edit", "clear"]
     if action_key in action_key_list:
            if action_key=="add":
                 add_file()
            elif action_key=="stats":
                 calculate_stats()
            elif action_key=="list":
                 list_all_students()
            elif action_key=="search":
                 search_student()
            elif action_key=="remove":
                 remove_student()
            elif action_key=="edit":
                 edit_student()
            elif action_key=="clear":
                 clear_data()


            

     elif action_key=="exit":
            print("Program Exited!")
            print("Thanks for Using!")
            done=True
     
     elif action_key=="":
            print("No Input Found!")
     
     else:
          print("Invalid Action Key! Try Again!")
          


