#create veriable.
cr_pass=0
defer=0
fail=0

while True:
    #insert from user
    print("--------------------------------------------------------")
    cr_pass=int(input("Please enter your credits at pass:"))
    defer=int(input("Please enter your credit at defer:"))
    fail=int(input("Please enter your credit at fail:"))

    #programme.
    if cr_pass==120:
        print("Progress\n")
    elif cr_pass==100:
        print("Progress (module trailer)\n")
    elif fail>=80:
        print("Exclude\n")
    else:
        print("Do not progress – module retriever\n")
