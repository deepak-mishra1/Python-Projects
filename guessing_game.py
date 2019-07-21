import random

num = random.randint(1,100)

mylist = [0]


print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")



while True:
    z = int(input("Enter a number "))
    print(z)

    if z < 1 or z > 100:
        print("Out Of Bound! Please try again: ")
        continue

    if num==z:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(mylist)} GUESSES!!')
        break
        
    mylist.append(z)
    
    
    
    if mylist[-2]:  
        if abs(num-z) < abs(num-mylist[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-z) <= 10:
            print('WARM!')
        else:
            print('COLD!')
            
    