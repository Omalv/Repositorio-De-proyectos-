# Entradas
Salario_basico = 1000000
mes = 30
aportes = 0.08
auxilio_transporte = 117172
dias_trabajados = float(input("Ingrese los dias Trabajados\n"))
nombre = input(str("Ingrese su Nombre\n"))
apellido = input(str("Ingrese su Apellido\n"))
numero_de_identificacion = input("Ingrese su numero de identificacion\n")
# Procesos
a = Salario_basico // mes * dias_trabajados
b = auxilio_transporte // mes * dias_trabajados
c = a * aportes
proceso = a + b - c
"""proceso uno mas proceso dos  menos proceso 3 resultado final"""
print("EL VALOR A PAGAR A ESTE TRABAJADOR ES : ",proceso)
