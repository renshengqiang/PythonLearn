a = 3
if a == 2:
	print("a=2")
elif a == 3:
	print("a=3")
else:
	print("a=", a)

while a<10:
	print("a=", a)
	a=a+1
else:
	print("while loop is over")

i = 10
for i in range(10, 15):
	if i == 14:
		break
else:
	print("for loop is over")
