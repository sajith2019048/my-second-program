#create veriable........

cr_pass=0##insert veriables
defer=0##insert veriables
fail=0##insert veriables
choice=0#staff choice.
count1=0#$$$counting "Progress" 
count2=0#$$$counting "Trailing"
count3=0#$$$counting "Excluded"
count4=0#$$$counting "Retriever"
total=0#@@@@all counting values total


#start the programme..........
print("--------------------------------------------------------")
print("Staff Version with Histogram\n")
while True:
    #insert from user
    cr_pass=int(input("Enter your total PASS credits:"))
    defer=int(input("Enter your total DEFER credits:"))
    fail=int(input("Enter your total FAIL credits:"))

    #programme..........
    if cr_pass==120:
        print("Progress\n")
        count1=count1+1
    elif cr_pass==100:
        print("Progress (module trailer)\n")
        count2=count2+1
    elif fail>=80:
        print("Exclude\n")
        count3=count3+1
    else:
        print("Do not progress – module retriever\n")
        count4=count4+1
    print("Would you like to enter another set of data?")
    choice=str(input("Enter 'y' for yes or 'q' to quit and view results:"))
    if choice=="Y" or choice=="y":
        print("\n")
        continue
    if choice=="Q" or choice=="q":
        print("--------------------------------------------------------")
        print("Horizontal Histogram")
        print("Progress",count1,":",("*"*count1))
        print("Trailer",count2,":",("*"*count2))
        print("Retriever",count4,":",("*"*count4))
        print("Excluded",count3,":",("*"*count3))
        print("\n")
        total=count1+count2+count3+count4
        print(total,"outcomes in total.")
        print("--------------------------------------------------------")
        
        break
