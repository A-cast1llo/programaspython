list_mes =["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
           "Noviembre", "Diciembre"]
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    mes = int(input("Ingresar el numero del mes: "))
    if mes >=1 and mes <= 12: break  # para detener el bucle
print("El mes es", list_mes[mes-1], "y tiene", dias_mes[mes-1], "dias.")