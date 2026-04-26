def leap_year(n):
    if n%400==0:
        print("leap year")
    elif n%4 and n%100:
        print("not a leap year")
    elif n%4==0:
        print("leap year")
    else:
        print("leap year")

n= int(input("Enter the year "))
leap_year(n)

    
