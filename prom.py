notas=[5.0, 5.0, 4.5, 0.0, 0.0, 2.0]
porcentajes=[0.5, 0.3, 0.2, 0.6, 0.3, 0.3]

variable_numerador=0
variable_denominador=0

for i in range(6):
    variable_numerador+=notas[i]*porcentajes[i]
    variable_denominador+=porcentajes[i]

promedio=variable_numerador/variable_denominador
print("promedio:", promedio)