a=float(input("enter your weight in kilograms"))
b=float(input("enter your hieght in meters"))
c=(a/(b**2))
if   19<=c<=24.9 :
    print("your are normal weight",c)
elif   25<=c<=29.9 :
    print("your are over weight",c)
elif   30<=c<=34.9 :        
    print("your are in obesity class 1",c)
elif   35<=c<=39.9 :        
    print("your are in obesity class 2",c)
elif   c>=40 :        
    print("your are in obesity class 3",c)
else :
    print("invalid")
  
