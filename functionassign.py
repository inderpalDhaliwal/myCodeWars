# Write a function that produces two numbers, and compare the two numbers. When your first number is higher 
# than the second number, a message appears You Made It , when your second number is higher than the first number a message appears It’s Ok, Try Next Time . 
#def main():
#     import random
#     num1 = random.randint(0,100)
#     num2 = random.randint(0,100)
#     print(num1,num2)
#     if num1 > num2:
#         print('You made it')

#    

#     else:
#         print("its okay try next time")


# main()



#what if i wanted to loop this until its true? 

def main():
    import random
    
    while True:
        num1 = random.randint(0,100)
        num2 = random.randint(0,100)
        print(f"Generated numbers: num1 = {num1}, num2 = {num2}")


        if num1 > num2:
            print('You Made It')
            break
        elif num2 == num1:
            print('its a tie')
        else:
            print('Its okay try next time')

main()
