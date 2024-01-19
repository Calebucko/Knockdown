# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:14:38 2024

@author: Caleben Jahn
"""
"""
Knock knock
whos there?
oink oink
oink oink who?
I'm confused are you a pig or an owl?
"""


name= input("Hi there, whats your name?")
output=f"""
Hello {name}, nice to meet you
"""
print(output)

response1=input("You wanna hear a joke?")
response2=input("knock knock")
response3=input("oink oink")


if response1 == "yes":
    print("knock knock.")
    if response2 == "whos there?":
        print("oink oink")
        if response3 == "oink oink who?":
            print("I'm confused, are you a pig or an owl?")
        else:
            print("If you didn't want to do the joke you could have just told me")
    else:
        print("I just wanted to tell you a joke you jerk.")
else:
     print("Ok, fine. Buzzkill")
        
       
    
      
    
    
                



