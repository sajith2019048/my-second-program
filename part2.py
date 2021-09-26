#create veriable.
cr_pass=0
defer=0
fail=0
valid=[0,20,40,60,80,100,120]#finding range.
values=[]

#start the programme.
print("--------------------------------------------------------")
while True:
    try:
        #insert from user
        cr_pass=int(input("Please enter your credits at pass:"))
        values.append(cr_pass)#append values list
        if cr_pass in valid :##is in range.
            defer=int(input("Please enter your credit at defer:"))
            values.append(defer)#append values list
            if defer in valid :##is in range.
                fail=int(input("Please enter your credit at fail:"))
                values.append(fail)#append values list
                if fail in valid :##is in range.
                    if sum(values)<=120:#calculation values list and find <=120.
                        #programme. 
                        if cr_pass==120:
                            print("Progress\n")
                        elif cr_pass==100:
                            print("Progress (module trailer)\n")
                        elif fail>=80:
                            print("Exclude\n")
                        else:
                            print("Do not progress – moduleretriever\n")
                        pass
                    else:
                        print("Total incorrect.\n")
                else:
                    print("Out of range.\n")
            else:
                print("Out of range.\n")
        else:
            print("Out of range.\n")
        values.clear()##clear the values list and start with empty list.
    except ValueError:
        print("Integer required\n")
        pass
      
