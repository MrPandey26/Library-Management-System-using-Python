import List
import DateAndTime
def returnBooks():
    name=input("Enter the first name of borrower: ")
    a="Borrowed by-"+name+".txt" 
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect. Pls check once")
        returnBooks()

    b="Returned by-"+name+".txt" #generating the Return file
    with open(b,"w+")as f:
        f.write("Library Management System \n")
        f.write("Returned By: "+ name+"\n")
        f.write("Date: " + DateAndTime.getDate()+"    Time:"+ DateAndTime.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t      Authorname \t\tprice\n")


    total=0.0
    for i in range(3):
        if List.bookName[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+List.bookName[i]+"\t\t "+List.authorName[i]+"\t\t  "+"$"+List.price[i]+"\n")
                List.quantity[i]=int(List.quantity[i])+1 #adding the stock
            total+=float(List.price[i])
            
    print("\t\t\t\t\t\t\t\t"+"$"+str(total)) #total
    print("Is the book return date has already been expired?")
    print("Press Y for Yes and N for Nope") #if yes then it will charge some money else it will terminate
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day #calucalating the total charge
        with open(b,"a")as f:
            f.write("\t\t\t\t\t\t\t\tFine: $"+ str(fine)+"\n") #fine
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("books.txt","w+") as f:
            for i in range(3):
                f.write(List.bookName[i]+","+List.authorName[i]+","+str(List.quantity[i])+","+"$"+List.price[i]+"\n")
