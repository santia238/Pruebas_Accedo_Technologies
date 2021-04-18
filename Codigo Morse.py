'''
edad = -7

if 0 < edad < 100:
    print("La edad es correcta")
else:
    print("Edad icorrecta")


salario_presidente = int(input("Introduce el salario del presidente: "))
print("Salario del presidente: " + str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print("Salario del director: " + str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario del jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del adiministrativo: "))
print("Salario del administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")

#USANDO AND, OR

print("Programa de becas")
distancia = int(input("Ingrese la distancia a la escuela en km: "))
print(distancia)
num_hermanos = int(input("Ingrese la cantidad de hermanos que tiene: "))
print(num_hermanos)
salario = int(input("Ingrese el salario que recibe su familia: "))
print(salario)

if distancia >= 40 and num_hermanos >= 2 or salario <= 20000:
    print("Usted tiene derecho a beca")
else:
    print("No tiene derecho a beca")


print("Asignaturas optativas año 2017")
print("Asignaturas optativas = Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")
asig= opcion.lower()

if asig in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura escogida " + asig)

else:
    print("La asignatura escogida no esta contemplada")
'''



print("1. Codificar de txt a morse")
print("2. Decodoficar de morse a txt")

opcion = int(input("Ingresa tu opcion: "))

if opcion == 1:
    valor = input("Ingresa tu mensaje de texto: ")
    txt = valor.upper()

    dic1 = {" ":" ", "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
            "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-",
            "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--.."}

    for i in range(0, len(txt)):
        print(dic1.get(txt[i]), end=" ")

elif opcion == 2:
    valor = input("Ingresa tu codigo morse: ")

    dic2 = {" ":" ", ".-":"A", "-...":"B", "-.-.":"C", "-..":"D", ".":"E", "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J",
            "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P", "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U",
            "...-":"V",".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z"}

    codigo = valor.split()

    for i in range(0, len(codigo)):
        print(dic2.get(codigo[i]), end="")


else:
    print("¡¡¡Opcion incorrecta!!!")    

   