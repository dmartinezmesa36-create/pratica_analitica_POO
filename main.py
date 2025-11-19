from Figurasgeometricas import Figurasgeometricas
from Triangulo import Triangulo
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma
from Cubo import Cubo
from esfera import Esfera



def menu():

    while True:
        print("-----------------MENU-----------------")
        print("triangulo (1) ")
        print("circulo (2) ")
        print("cuadrado (3) ")
        print("rectangulo (4) ")
        print("cilindro (5) ")
        print("paralelograma (6)")
        print("cubo (7) ")
        print("esfera(8)")
        print("Cerrar (0)")
        print("--------------------------------------")
        opcion = input("digite el numero de la figura que desea hallar el area: ")
        if opcion == "1":
            base = int(input("digite la base: "))
            altura = int(input("digite la altura: "))
            tr = Triangulo(altura,base)
            print("el area del triangulo es: ",opcion, "es", tr.area())

        elif opcion =="2":
            radio = int(input("digite el radio: "))
            ci = Circulo(radio)
            print("El area del circulo es:",opcion, "es",ci.area())

        elif opcion == "3":
            lado = float(input("digite el lado del cuadrado: "))
            cu = Cuadrado(lado)
            print("El area del cuadrado es:",opcion, "es",cu.area())

        elif opcion == "4":
            base = float(input("digite la base: "))
            altura = float(input("digite la altura: "))
            re = Rectangulo(base,altura)
            print("El area del rectangulo es:",opcion, "es" ,re.area())


        elif opcion == "5":
            radio = float(input("digite el radio del cilindro: "))
            altura = float(input("digite la altura del cilindro: "))
            
            ci = Cilindro("cilindro")
            ci.radio = radio
            ci.altura = altura
            print("El area del cilindro es:",opcion, "es",ci.area())
        
        elif opcion =="6":
            base = float(input("digite la base del paralelograma: "))
            altura = float(input("digite la altura del paralelograma: "))   
            pr= Paralelograma("paralelograma")
            pr.base = base
            pr.altura = altura
            print("El area del paralelograma es:",opcion, "es",pr.area())
        elif opcion =="7":
            lado = float(input("digite el lado del cubo: "))
            cu = Cubo("cubo")
            cu.lado = lado
            print("El area del cubo es:",opcion, "es",cu.area())
        elif opcion =="8":
            radio=float(input("digite el radio de la esfera: "))
            es= Esfera("esfera")
            es.radio= radio
            print("El area de la esfera es:",opcion, "es",es.area())
        else: 
            opcion == "0"
            print("fin del programa")
            break
menu()
    


        



