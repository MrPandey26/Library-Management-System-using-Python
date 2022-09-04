import Return #importing Return file
import List #importing List file
import DateAndTime #importing Date and time 
import Borrow #importing Borrow file

def start():
    while(True):
        print("        Welcome to our library                ")
        print("---------------------------------------------")
        print("Enter 1. Display available books in library")
        print("Enter 2. Borrow a Book from our library")
        print("Enter 3. Return a Book to out library")
        print("Enter 4. Exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("books.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                List.List()
                Borrow.borrowBooks()
            elif(a==3):
                List.List()
                Return.returnBooks()
            elif(a==4):
                print("Thank you for visiting our Library. Pls visit us again")
                break
            else:
                print("Please enter a valid option from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
