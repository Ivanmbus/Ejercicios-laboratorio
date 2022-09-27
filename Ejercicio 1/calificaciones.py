
#apartado a y b:
#a- numero de aciertos 
#e- numero de errores
#t- numero de respuestas correctas totales 
def calculo(a,e,t):
    nota = (a*10)/t-(e*10)/(50-t)
    print("Tu nota es" + str(nota))

def calculodenota():
    aciertos = int(input("Introduce tu número de aciertos ")) 
    errores = int(input("Introduce tu número de  errores "))
    totalrespuestas = int(input("Introduce el número de respuestas correctas totales "))
    calculo(aciertos,errores,totalrespuestas)

calculodenota()
