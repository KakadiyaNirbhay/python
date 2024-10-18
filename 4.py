# x=int(input("enter the age:->"))

# if   1<= x <=18:
#     print("chaild")
# elif 19 <= x <= 45:
#     print("yang man")
# elif 46 <= x <=75:
#     print("midal yang man") 
# elif 76 <= x <=99:
#     print("old man")
# else:
#     print("not avelebal man")             

# x=input("enter your moblie number: +91 ")
# if (len(x)==10 and x.isdigit ()):
#     print("correct number")
# else:
#     print("incorrect number")

# i=1
# while i<=20:
#     if i==8:
#         break
#     print(i)
#     i+=1
# while i<=20:
#     i+=1    
#     if i == 13:
#         continue
#     print(i)        

# def hello():
#     x = "my name is nirbhay"
#     print(x[:2]+x[7:2:-1]+x[7:])
# hello()    

# def nirbhay():
#     if 5!=5:
#         print("Right")
#     else:
#         print("Wrong")
# nirbhay()

# def rummy():
#     for i in range(1,6):
#         for j in range(1,7-i):
#             print(j,end="")
#         print()
    
# rummy()

# biltin

# print("hii")
# print(len("my name is nirbhay"))
# x= int (22)
# print(x)

# user defin function :

# def k (n=(1,2,3,4,5,6),k=[24,56,"nirbhay"]):
#     print(n,k)
# k()


# def jojo(k=[1,2,3,34,45,54,24,4,5,6,7],p=("word","error")):
#     if 45 in k:
#         print("Right")
#     else:
#         print("Worng") 
#     if "word" not in p:
#         print("true")
#     elif "done" not in p:
#         print("False")
#     else:
#         print("error") 
# jojo()                      

# parameters:

# def go(x,y):
#     print("answer is :",x*y)
#     print("answer is :",x+y)
# go(30,20)    
     
# def off(f,g):
#     print("addtion :",f+g)
#     print("list:",f,g)
#     print(f[1:5])
# n=(3,5,7,9,2)
# k=(1,2,3,4,5)
# off(n,k)     

# def short(good,food):
#     self =good+food
#     return self
# b=short(10,7)
# print("addition :",b)

# def hot(who,the):
#     fore=who%the
#     fore=who/the
#     fore=who//the
#     fore=who*the
#     fore=who+the
#     fore=who**the
#     return fore
# worry = hot(60,30)
# print("got it :",worry)

# preameter pass function  :

# def none(tata):
#     for x in tata:
#         print(x)
# kk = [1,2,3,5,7,98,"none nirva"]
# none(kk)

# def Nike(diss,track,to ,drak):
#     g=(diss+track-to *drak)
#     if g>10:
#         print("right")
#     elif g <30:
#         print("wrong")
#     else:
#         print("all is wrong")
# Nike(100,400,30,20)            


# winner = []
# for i in range(5):
#     x = input(f"Enter the name {i+1}:-  ")
#     y = int(input(f"Enter the speed{i+1}:- "))
#     winner. append((x,y))

# time=[(x,500/y)for x,y in winner]
# for i in range(len(time)):
#     for j in range(i+1,len(time)):
#         if time[i][1]>time[j][1]:
#             time[j],time[i]=time[i],time[j]
# print("\ntop 3 winners of the 500 meters race:")
# for i in range(3):
#     print(f"{i+1}st win :{time[i][0]}")

# winners=[time[0][0],time[1][0],time[2][0]]

# speeds = []
# for i in range(3):
#     w = (input(f"Enter the speed {winners[i]}:- "))
#     speeds. append((winners[i],w))

# time_300=[(x,300/y)for x,y in speeds]
# for i in range(len(time_300)):
#     for j in range(i+1,len(time_300)):
#         if time_300[i][1]>time_300[j][1]:
#             time_300[j],time_300[i]=time_300[i],time_300[j]
# print("\ntop 1 winners of the 300 meters race:")


        
        
# if winner:
#     print("Winners:", ', '.join(winner))
# else:
#     print("No winners this time.")


# def hii(x):
#     y="my name is nirbhay"
#     print(y[6:2:-1])
# hii("my name is nirbhay")        

# n=lambda a,b,c,d:(a+b,c*b,b-c,d/a)
# print(n(65,566,5,76))

# def name(will):
#     will=lambda a,s,d,f:() 

# import random
# player=["nity","aniket","maulik","jay","jevin"]
# print(player)


# score1=random.randrange(100,400)
# print("the score of ",player[0],"is",score1)

# score2=random.randrange(100,400)
# print("the score of ",player[1],"is",score2)

# score3=random.randrange(100,400)
# print("the score of ",player[2],"is",score3)

# score4=random.randrange(100,400)
# print("the score of ",player[3],"is",score4)

# score5=random.randrange(100,400)
# print("the score of ",player[4],"is",score5)

# play=max(score1,score2,score3,score4,score5)
# print("the max score is",play)
# # play=max(score1,score2,score3,score4,score5)
# # print("the max score is",play)
# # play=max(score1,score2,score3,score4,score5)
# # print("the max score is",play)

# if score1>score2 and score1>score3 and score1>score4 and score1>score5 :
#     score=score1
#     player[0]
# elif score2>score1 and score2>score3 and score2>score4 and score2>score5 :    
#     score=score2
#     player[1]
# elif score3>score1 and score3>score2 and score3>score4 and score3>score5 :    
#     score=score3
#     player[2]
# elif score4>score1 and score4>score2 and score4>score3 and score4>score5 :    
#     score=score4
#     player[3]
# else:    
#     score=score5
#     player[4]

