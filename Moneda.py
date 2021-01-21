import random
r_1=random.randint(1,6)
r_2=random.randint(1,6)
r_3=random.randint(1,6)
r_4=random.randint(1,6)

class Person:
    pass
# n=name v=victories l=loses b=best_punctuation 
# w=worst_punctuation
    def __init__(self,n,v,l,b,w):
        self.n=n
        self.v=v
        self.l=l
        self.b=b
        self.w=w



v=0
l=0
b=0
w=0

a=Person(player_1,v,0,0,0)
b=Person(player_2,v,0,0,0)
c=Person(player_3,0,0,0,0)
d=Person(player_4,0,0,0,0)


player_1=input("Write the name of the 1st player: ")
player_2=input("Write the name of the 2nd player: ")
player_3=input("Write the name of the 3rd player: ")
player_4=input("Write the name of the 4rt player: ")

p_1="{} trhow {}".format(player_1,r_1)
p_2="{} trhow {}".format(player_2,r_2)
p_3="{} trhow {}".format(player_3,r_3)
p_4="{} trhow {}".format(player_4,r_4)


