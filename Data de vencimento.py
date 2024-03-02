from datetime import date
atual="{}".format(date.today())
atual=atual.replace("-", " ")
atual=atual.split()
print(atual)
v=input("Informe a data de vencimento: ")
v=v.replace("/", " ")
v=v.split()
v=v[::-1]
v[2]=int(v[2])
atual[2]=int(atual[2])	
print(v)
if atual[0]<v[0]:
	print("A data de vencimento não expirou.")
elif atual[0]==v[0]:
	if atual[1]<v[1]:
		print("A data de vencimento não expirou.")
	elif atual[1]==v[1]:
		if atual[2]<v[2]:
			print("A data de vencimento não expirou.")
		elif atual[2]==v[2]:
			print("A data de vencimento expira hoje")
		elif atual[2]>v[2]:
			print("A data de vencimento expirou.")
	elif atual[1]>v[1]:
		print("A data de vencimento expirou.")
elif atual[0]>v[0]:
	print("A data de vencimento expirou.")