import atleta_20241 as atl

a1 = atl.Atleta('Juan', 90, 1.75)

a1.comer()
a1.comer()



print(a1.nombre, a1.peso, a1.estatura)
print('imc:',a1.calcular_imc())