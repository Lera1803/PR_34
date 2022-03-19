summ = 0
summq = 0
i = 1
while i != 0:
        i = int(input())
        summ += i
        summq = summq + i**2
        if summ == 0:
            break
print (summq)
