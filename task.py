#task
holder=["riya","fathi","zulfa","yash"]
amount=[100,200,300,400]
c=input("enter sender name:")
d=input("enter the reciver name:")
e=int(input("enter the amount:"))
for i in holder:
    if(i==c):
           print("sender Available")
           x=(holder.index(i))
           print("Account Balance:",amount[x])
           print("suceessfully transfer")
           print("current Bank balance:",amount[x]-e)
    if(i==d):
           y=holder.index(i)
           print("Account Balance:",amount[y])
           print("amount transfer success")
           print("Current Bank Balance:",amount[y]+e)
           break
    else:
        print("this person was not available")
