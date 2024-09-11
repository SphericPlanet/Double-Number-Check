num = int(input("Enter a number: "))
if num > 50:
   print(num, "is greater than 50")
   if num % 2 == 0:
      print("also it's even")
   else:
        print("also it's odd")
else:
    print(num, "is not greater than 50")