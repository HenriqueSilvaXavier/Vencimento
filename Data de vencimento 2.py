from datetime import datetime
atual=datetime.now()
atual=datetime(year=atual.year, month=atual.month, day=atual.day)
print(atual)
v=input("Informe a data de vencimento: ")
v=v.split("/")
for n in range(0, len(v)):
	v[n]=int(v[n])
v2=datetime(year=v[2], month=v[1], day=v[0])
print(v2)
if atual>v2:
	print("A data expirou")
elif atual==v2:
	print("A data expira hoje")
elif atual<v2:
	print("A data não expirou.")