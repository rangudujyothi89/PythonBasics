#list - can have duplicates , changeable, ordered
# remove duplicates in a list
numbers = [2,2,4,6,3,4,6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
# set - cannot have duplicates, changeable, ordered, cannot be indexed.
#tuple - round braces , immutable, not changeable
coordinates = (1,2,3)

#unpacking
x, y, z = coordinates

#dictionaries - key value pairs in braces, indexed based on key

#phone = input("phone number : ")
#digits_map = {
#    "1":"One",
#    "2":"Two",
#    "3":"Three"
#}
#output= ""
#for ch in phone:
#    output+= digits_map.get(ch,"!") + " "
#print(output)

#print("*********")

#message = input(">")
#words = message.split(' ')
#emojis = {
#    ":)" : "😀",
#    ":(" : "☹️"
#}

#output = ""
#for word in words:
#    output+= emojis.get(word, word) + " "

#print(output)

#def greet_user(name):
# print(f'Hi {name}!')

#print("start")
#greet_user("Jyothi")
#print("stop")

#keyword arguments - postion of parameters doesnt matter
#postion arguments take precedence
#def greetuser(firstname,lastname):
 #print(f'Hi {firstname} {lastname}!')

#print("start")
#greetuser(lastname="Rangudu", firstname= "Jyothi")
#print("stop")

#pyton returns none of a function if return stmt is not needed

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😀",
        ":(" : "☹️"
     }

    output=""
    for word in words:
        output+= emojis.get(word, word) + " "

    return output

message = input(">")
print(emoji_converter(message))

# try except - try catch block
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid Value")
