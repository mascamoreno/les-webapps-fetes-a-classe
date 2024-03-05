listaAñoNacimiento=[1964, 1927, 1981, 1995, 2000, 2001, 2002, 2003, 2004]
listaEdad=[]
calculo = 0

for i in listaAñoNacimiento:
	calculo=2023 - i
	listaEdad.append(calculo)
print(listaEdad)