f = open('DATA.csv', 'r')
encabezado = f.readline()
campos = encabezado.split(';')
print (campos)
print (campos[0])
print (campos[1])
print (campos[2])
print (campos[3])

sumA = 0
sumB = 0
sumC = 0

for dato in f:
    reg = dato.split(';')
    match reg[1]:
        case 'A':
            sumA += int(reg[2])
         
        case 'B':
            sumB += int(reg[2])
            
        case 'C':
            sumC += int(reg[2])

print ('A:', sumA, 'B:', sumB, 'C:', sumC)  

f.close()

f = open('DATA.csv', 'a')
valA = 21
valB = 32
valC = 43

linea = '9;C;' + str(valC) + ';' + '03/01/2024' + '\n'

f.write(linea)
   