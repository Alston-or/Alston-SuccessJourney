time=int(input(" Enter the time:"))
sig= input("Enter a.m or p.m:")

if(time>=6 and time<=12):
 if sig=="a.m":
    print("Good Morning")
elif(time>12 and time<3):
 if sig=="noon":
      print("Good Afternoon")
elif(time>=3 and time<=12):
    if sig=="p.m":
        print("Good Evening")
else:
    print("INCORRECT TIME")

