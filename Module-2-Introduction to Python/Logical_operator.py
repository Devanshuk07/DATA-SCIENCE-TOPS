#this operator is used to create logic and check true and false there we use logical operator.
# examples= (and), (or), (not) ;
from urllib3.util.connection import allowed_gai_family

a=10
b="deva"
print(a<=5 or b=="deva") #or means any 1 condition must be true

a=10
b="deva"
print(a>=10 and b=="deva") #and means both condition must be true

a=10
b=20
print(not (a<b)) #it will check a<b then return true or false if false then not means=false
#false false= true
#false true= false

a=20
b=50
print(not(a>=50 and b<=20))
