import math
print("Jyothi Rangudu")
print('*' * 10)
#name = input('what is your name? ')
#color = input('what is your favourite color? ')
#print(name + ' likes ' + color)
#Type Conversion
int('1982')

#multiline str
course = '''
Hi Jyothi 
this is multiline example
'''
print(course)

cod = 'Python for beginners'
print(cod[1:-1])

#formatted string - prefix string with f
first='john'
last='smith'
msg= f'{first} [{last}] is a coder'
print(msg)

#length of str
print(len(cod))

print(cod.replace('beginners','absolute beginers'))
print(cod.find('P',0,3))

x=2.9
print(round(x))
print(math.floor(x))

isithot = False
isitcold = False

if isithot:
    print("it is hot day")
elif isitcold:
    print("its a cold day")
else:
    print("its a lovely day")



price = 1000000
credit = True
if credit:
    downpayment = 0.1*price
else:
    downpayment = 0.2*price

print(f"Downpayment : ${downpayment}")

#weight = int(input('Weight : '))
#unit = input('(L)bs or (K)g : ')
#if unit.upper() == "L" :
#    converted =weight * 0.45
#    print(f" You are {converted} kilos")
#else:
#    converted = weight / 0.45
#    print(f" You are {converted} lbs")

#car game
command=""
while command.lower() != "quit" :
    command= input("> ").lower()
    if command == "start":
        print('car started')
    elif command == "stop":
        print('car stopped')
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I dont understand")


for item in 'Python':
    print(item)

# range function -
for item in range(5,10, 2):
    print(item)

#nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

print('****************')

#numbers = [5,2,5,2,2]
#for x in numbers:
#    output = ''
#    for count in range(x):
#        output+= 'l'
#    print(output)