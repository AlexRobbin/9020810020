num = dict(first = 1 , second = 2, third = 3)

print(num)

power = {key : value for key, value in num.items()}

print(power)


print("-----------------------")


doubleNum = {x : x**2 for x in [1, 2, 3, 4, 5, 6]}

print(doubleNum)


print("-----------------------")


secondnum = {t : ("zoj" if t % 2 == 0 else "fard") for t in [1, 2, 3, 4, 5, 6 , 7] }

print(secondnum)