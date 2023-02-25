course='python for everybody'
#using whitespace for spacing the words after string concatenation
a="python"
b=" for"
c=" everybody"
print(a+b+c)
#testing built-in string functions
print(course)
q=course.title()
w=course.upper()
e=course.lower()
#taking user input
a=input("enter the word to be replaced\n")
b=input("enter the replacement\n")
r=course.replace(str(a),str(b))
c=input("enter the word to be found\n")
t=course.find(str(c))
print("\n",q,"\n",w,"\n",e,"\n",str(r).title(),"\n",t)


#formatting strings using % operator and format specifiers
brand = "HP OMEN CORE i7 12th GEN"
exchangeRate = 1.24
price=1299
message0 = "The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR" %(brand,price,exchangeRate)
print (message0)

#formatting strings using format() function/operator
user_name="Danush"
user_height=1.82
user_weight=73
country="India"
wins=11
losses=0
script="Ladies and Gentlemen it's time for the main event of the evening,for the undisputed UFC welterweight championship of the World, fighting out of red corner, we have, the reigning, the defending undisputed Ufc welterweight champion {0:s}, with a professional record of {1:d} wins and {2:d} losses, fighting out of {3:s}, weighing in at {4:d} kilos and {5:4.2f} meters tall".format(user_name,wins,losses,country,user_weight,user_height)
print("\n\n",script)