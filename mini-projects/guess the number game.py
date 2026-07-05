import random
number=random.randint(0,10)
point=100
hak=int(input("How many attempts will it take to find the correct number?:"))
kırılacak_puan=point/hak
i=0
while i<hak:
    guess=int(input("Guess the number:"))

    if guess == number:
        print(f"Congratulations, you guessed correctly.\nYour score is:{point}")
        break
    else:
        point-=kırılacak_puan
        if point<0:
            point=0
        print(f"Incorrect guess,\nyour score is:{point}")
    i+=1


