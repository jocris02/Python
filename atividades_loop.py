cont =0
for num in range(100):
    if num != 0 and num % 3 == 0:
        print(num)
        cont += 1
        if cont == 5:
            break
