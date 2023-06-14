num=int(input(""))
resto3=0
resto5=0
soma=0
num-=1
while num > 0:
    resto3=num%3
    resto5=num%5
    if resto5 == 0 or resto3 == 0:
        soma+=num
    num-=1
print(soma)
    