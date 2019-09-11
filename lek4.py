# Wandom dice wegenator

import random #Random är nu möjligt

print("wercome to dice monstahs") #Welcome message


#sides = int(input("Hur många sidor"))
try:
    sides = int(input("Hur många sidor"))
except:
    print("Du måste skriva in en siffra") #Om man skriver fel slumpar den automatisct mellan 1,6
    sides = int(input("Hur många sidor"))

#randomNumber = random.randint(1, sides)
#input(x = 1 while True: )
run ="y" 

while run.lower() =="y": #loop
    randomNumber = random.randint(1, sides) #Random generator
    print(randomNumber) 
    run = input("Roll another doice Y/N")


#while True:
