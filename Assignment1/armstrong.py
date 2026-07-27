num = int (input("enter the number: "))
n = num
order = len(str(n))
sum = 0
while num>0:

    sum += (num%10) ** order
    num//=10

if n == sum :
    print("armstrong number raixa")
else:
    print("armstrong number rahinaxa")