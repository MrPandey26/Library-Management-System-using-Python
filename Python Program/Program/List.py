def List():
    global bookName
    global authorName
    global quantity
    global price
    bookName=[]
    authorName=[]
    quantity=[]
    price=[]
    
    with open("books.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookName.append(a)
                elif(ind==1):
                    authorName.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    price.append(a.strip("$"))
                ind+=1
