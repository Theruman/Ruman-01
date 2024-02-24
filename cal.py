print('Select an operator:')
print('A for addition:')
print('B for subtraction:')
print('C for multiplcation:')
print('D for dividation:')
print('E for exit:')

while True:
    lists = ["a","b","c","d","e"]

    input_choice = input("Follow Above of List:").lower()

    if input_choice == list[4]:
        print("Good bye.......")
        print("Thanks for using this Calculator.")
        break
    Number1 = float(input("Enter 1st number:"))
    Number2 = float(input("Enter 2nd number:"))
    
        
        
    add = Number1+Number2
    sub = Number1-Number2
    mul = Number1*Number2
    div = Number1/Number2
        
        
    if input_choice==lists[0]:
        print(Number1,"+",Number2,"=",add)
    elif input_choice==lists[1]:
        print(Number1,"-",Number2,"=",sub)
    elif input_choice==lists[2]:
        print(Number1,"*",Number2,"=",mul)
    elif input_choice==lists[3]:
        print(Number1,"/",Number2,"=",div)
        
    else:
        print("invalid input") 
