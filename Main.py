import math

def generar_menu(contador,text):
    print(f'{contador[0]}.- {text}')
    contador[0]+=1

def tabla_multiplicar(tabla):
    for j in range (7):
        list=[]
        for i in range (10):
            list.append(f'{j+1}X{i+1} = {(j+1) * (i+1)}')
        print(list)

def fibonacci(limite):
    lista = []
    a, b = 0,1
    while a < limite:
        lista.append(a)
        a, b = b, a + b
    print(lista)

def formula_general(a,b,c):
    x1,x2 = 'indefinido','indefinido'
    raiz = pow((b**2-(4*a*c)),0.5)
    try:
        x1 = round((((-b)+raiz)/(2*a)),2)
    except TypeError:
        print('El valor de X1 es indeterminado')
    try:
        x2 =round((((-b)-raiz)/(2*a)),2)
    except TypeError:
        print('El valor de X2 es indeterminado')
    
    print (f' X1 = {x1}  X2 = {x2}')

if __name__ == "__main__":
    correr = True
    while(correr):
        contador = [1]
        print("----------------------------------------")
        generar_menu(contador,'Serie de Fibonacci')
        generar_menu(contador,'Tabla de multiplicar del 7')
        generar_menu(contador,'Formula general')
        generar_menu(contador,'salir')
        try:
            opcion = int(input('\nINGRESA UNA OPCION :'))
            if(opcion == 1):
                fibonacci(limite=int(input('\nIngresa un valor limite para la serie: ')));
            elif(opcion == 2):
                print('\nTablas de Multiplicar')
                tabla_multiplicar(7)
            elif(opcion == 3):
                print('Formula General')
                A = int(input('ingresa un valor para A: '))
                B = int(input('ingresa un valor para B: '))
                C = int(input('ingresa un valor para C: '))
                formula_general(A,B,C)
            elif(opcion == 4):
                correr = False
        except ValueError:
            print('\nEl valor introducido es erroneo')
        
