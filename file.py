# author=> Prabhjot 


from os import path
from os import remove
def menu():
    print('1-enter one to create a new student file')
    print('2-enter 2 to add data in  student file')
    print('3-enter 3 the read the student file data')
    print('4-enter 4 to delete the student file')
    print('5-enter 5 to search student information')
    return input("select the any option from above : ")
    
    


def create_file():
    filename=input("enter the file name : ")
    filename+=('.txt')
    
    if path.exists(filename):
        print("the file is already exits so selcetnm the option 2 ")
    else:
      file=open(filename,"w")
      student=[]
      number= int(input("how many student you want to add in new file : "))

      for i in range(number):
       student.append(input("enter the student id ; ")+'\n')
       student.append(str(input("enter the student first name : "))+'\n')
       student.append(str(input("enter the student last name :"))+'\n')
       student.append(str(input("enter the student major : "))+'\n')
       student.append(input("enter the student phone : ")+'\n')
       student.append(input("enter the student gpa : ")+'\n')
       student.append(input("enter the student date of birth : ")+'\n')
      
      
       file.writelines(student)
       file.close()
       print(student)
def addinfile():
    filename=input("enter the file name : ")
    filename+=('.txt')
    if path.exists(filename):
        
     file=open(filename,"a")
     student=[]
    
    
     number=int(input("how many students you wants to add in file : "))
     for i in range(number):
      
    
      student.append(input("enter the student id ; ")+"\n")
      student.append(str(input("enter the student first name : "))+"\n")
      student.append(str(input("enter the student last name :"))+"\n")
      student.append(str(input("enter the student major : "))+"\n")
      student.append(input("enter the student phone : ")+"\n")
      student.append(input("enter the student gpa : ")+"\n")
      student.append(input("enter the student date of birth : ")+"\n")
      
        
        # print(student)
     file.writelines(student)
     print(f"information add successfully")
     file.close()
     print(student)
    else:
        print("the file dose note exist please select option 1 to create the file")
       
def deletethefile():
    print("to delete the file please enter the file name : ")
    filename=input("enter the file name to delete : ")
    filename+=('.txt')
    if path.exists(filename):
        remove(filename)
        print(f"the {filename} is delete permanatily")
    else:
        print("the file is not exist")
    

def read():
    filename=input("enter the file name to read things: ")
    filename+=('.txt')
    if path.exists(filename):
     file=open(filename,"r")
     ff=file.readlines()
     print(ff)
    else:
        print("file dose not avalible")
    file.close()

def find():
    filename=input("Enter the file name to serch student information :  ")
    filename+=(".txt")
    if path.exists(filename):
        
        file=open(filename, "r")
        string=input("enter the student id : ")
        index=0
        for i in file:
            index+=1
            if string in i:
                print(f"the {string} find at {index} line")
                for i in range(index,index+7):
            
                 data = file.readlines()
                 print(data)
            else: 
                print("the student id can not found")    

             
              
                
              
            

    else:
        print("file not found")
    file.close()


def main():
     menu()
     
     while True:
        choose= menu()
        if choose=='1':
             create_file()
        elif choose=='2':
            addinfile()
        elif choose=='3':
            read()
        elif choose=='4':
            deletethefile()
        elif choose=='5':
            find()
        
        else:
          print('please choose the the right option')
          break
        


main()