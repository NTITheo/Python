#num1 = input("Mata in ett heltal: ")

operator = input("Välj reäknesätt(+, -, *, /): ")

try:
    num1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    num1 = 0    

try:
    num2 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    num2 = 0    

if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":    
    total = num1 * num2
elif operator == "/":
    try:
        total = num1 / num2
    except ZeroDivisionError:
        print("Fucking hidiot!")
else:
    print("FEL")

print("Summan är:", total)


#
# total = num1, operator, num2

#num2 = input("Mata in ett heltal: ")
#total = int(num1) + int(num2)

#print ("totaln är:" + str(total))
#print ("totaln är:", total)

#num1 = input("Mata in ett heltal: ")
#num2 = input("Mata in ett heltal: ")
#total = num1 + num2    # byter till int
#print ("totaln är:", total)
