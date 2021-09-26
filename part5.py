#create veriable......
Pass=[120,100,100,80,60,40,20,20,20,0]
Fail=[0,0,20,20,20,40,60,80,100,120]
seen = set()
uniq = []
count1=0
count2=0
count3=0
count4=0

#Fail list has same numbers then it print seven("Do not progress – module retriever")
#therefore I use this code to stop it......
for x in Fail:
    if x not in seen:
        uniq.append(x)
        seen.add(x)

for i in Pass:
    if i == 120:
        print("Progress")
        count1+=1
    elif i ==100:
        print("Progress (module trailer)")
        count2+=1
for m in uniq:
    if m >= 80:
        print("Exclude")
        count3+=1
    else:
        print("Do not progress – module retriever")
        count4+=1
print("\n")
#Display the counts
print("Progress  1:",("*"*count1))
print("Trailer   2:",("*"*count2))
print("Retriever 3:",("*"*count4))
print("Excluded  4:",("*"*count3))
print("\n")

#Calculate total of count.
total=count1+count2+count3+count4
print(total,"outcomes in total.")
