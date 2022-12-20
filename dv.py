# encoding=utf-8
ingreso = input('Ingresa tu RUT sin puntos ni Dígito verificador:')

rut = map(int, str(ingreso))

x = len(rut)
factor = 2
result = 0
//comentarios 
while x > 0:
    x = x -1
    valor = int(rut[x])
    result = result + (valor * factor)

    if factor == 7:
        factor = 2
    else:
       factor = factor + 1   

modulo = result % 11       
digito = 11 - modulo

if digito == 11: digito = "K"
if digito == 10: digito = 1



print("Su dígito verificador es, {}".format(digito))