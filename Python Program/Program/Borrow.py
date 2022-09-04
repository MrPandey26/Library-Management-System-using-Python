import DateAndTime
import List

def borrowBooks():
    borrowCode=False
    while(True):
        firstName=input("Enter the First Name: ")
        if firstName.isalpha():
            break
        print("please enter a valid first name") #if the first name is not valid it will print out
    while(True):
        lastName=input("Enter the Last Name: ")
        if lastName.isalpha():
            break
        print("please enter a valid last name") #if the last name is not valid it will print out.
            
    t="Borrowed by-"+firstName+".txt" #Generating a borrowd file
    with open(t,"w+") as f:
        f.write("Library Management System  \n")
        f.write("Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write("Date: " + DateAndTime.getDate()+"    Time:"+ DateAndTime.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \t\t price \n" )
    
    while borrowCode==False:
        print("Please select a option below:") 
        for i in range(len(List.bookName)):
            print("Enter", i, "to borrow book", List.bookName[i]) #Displaying books to boorrow
    
        try:   
            a=int(input())
            try:
                if(int(List.quantity[a])>0): #if the qunatity is greater than 0 then message will print out
                    print("Book is available in our library")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ List.bookName[a]+"\t\t  "+List.authorName[a]+"\t\t  "+"$"+List.price[a]+"\n") #Storing the data in a txt file

                    List.quantity[a]=int(List.quantity[a])-1 #reducing the qunatity
                    with open("books.txt","w+") as f:
                        for i in range(3):
                            f.write(List.bookName[i]+","+List.authorName[i]+","+str(List.quantity[i])+","+"$"+List.price[i]+"\n")


                    
                    loop=True
                    count=1
                    while loop==True:
                        option=str(input("Do you want to borrow more books?Press y for yes and n for nope.")) 
                        if(option.upper()=="Y"): #if user enters Y books will be display
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(List.bookName)):
                                print("Enter", i, "to borrow book", List.bookName[i]) #Displaying the books
                            a=int(input())
                            if(int(List.quantity[a])>0): #if the qunatity is greater than 0 then message will print out
                                print("Book is available in our library")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ List.bookName[a]+"\t\t  "+List.authorName[a]+"\t\t  "+"$"+List.price[a]+"\n")  #Storing the data in a txt file

                                List.quantity[a]=int(List.quantity[a])-1 #reducing the qunatity
                                with open("books.txt","w+") as f:
                                    for i in range(3):
                                        f.write(List.bookName[i]+","+List.authorName[i]+","+str(List.quantity[i])+","+"$"+List.price[i]+"\n")
                                        borrowCode=False
                            else:
                                loop=False
                                break
                        elif (option.upper()=="N"): #if the user enters N then it will terminate
                            print ("Thank you for borrowing books from our library ")
                            print("")
                            loop=False
                            borrowCode=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available in our library. Pls check other books")
                    borrowBooks()
                    borrowCode=False
            except IndexError:
                print("")
                print("Please choose book according to the given instruction. Thank You")
        except ValueError:
            print("")
            print("Please choose as given suggested.")
