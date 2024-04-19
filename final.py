from time import *
import random as r
 
def mistake(par,user):
    error=0
    for i in range(len(par)):
        try:
           if par[i]!=user[i]:
                error+=1
        except:
            error+=1 
    return error              

def speed(strt,end,user):
    time_d=end-strt
    time_r=round(time_d,2)
    speed=len(user)/time_r
    return round(speed,2)



test=["I met a person who is a bussiness man, he is very rich and disciplined.","I am Riya . I am an intern at code clouse.","Your are good at study but not good in sports", "we are emplye here for past 20 years, our manager should respect us."]

test1=r.choice(test)
print(" *********Typing Speed********* ")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter : ")

time_2=time()
print("Speed:",speed(time_1,time_2,testinput),"w/sec")
print("Error:",mistake(test1,testinput))

