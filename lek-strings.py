firstName = "Theo"
middleName = "Per"
lastName = "Larefalk"

gamerTag = "snubby"

print(gamerTag.capitalize())

print(firstName, middleName, lastName)

print(firstName.swapcase())

#print(f"{firstName[0:3].lower()}{lastName[0:3].lower()}19")
#userName = "firstName[0:3].lower()lastName[0:3].lower()19"

userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"

print(userName)






#tecken = """()parenteser 
#[] hakparanteser , 
#{} måsvingar" 
#: kolon 
#; semikolon 
#, komma 
#\" dubbelfnutt, 
#\' enkelfnutt"""

#print(tecken[13:200])