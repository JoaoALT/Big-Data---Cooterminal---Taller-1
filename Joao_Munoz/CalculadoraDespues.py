"""
Created on Wed Aug 2, 2025
@author: Hugo Franco y Joao Alexandre Muñoz
"""
import math as math

class Calculadora:
    """
    Implementa una calculadora
    """

    tipo='cientifica'
    
    def __init__(self,operando1=0, operando2=0, operacion=None):
        self.operando1=operando1
        self.operando2=operando2
        self.operacion=operacion
        self.current_potencia = 0
        #Removed logic from constructor, moved to a method appart.
        
    
    def __str__(self):
        try:
            return str(self.operando1)+self.operacion+str(self.operando2)
        except Exception as err:
            return "Calculadora en espera... No operación definida."

    def operacion(self, operacion): #New method for operations
        if operacion is not None:
            if operacion=='+':
                print(self.suma())
            elif operacion=='-':
                print(self.resta())
            elif operacion=='*':
                print(self.multiplicacion())
            elif operacion=='/':
                print(self.division())
            elif operacion=='^':
                print(self.potencia())
            elif operacion=='^2':
                print(self.sqrt())
    
    def suma(self, operando2=None):
        self.operacion="+"
        try:
            if self.operando1 is not None and operando2 is not None:
                self.operando2=operando2
                self.operando1 = self.operando1+self.operando2
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None
    
    def resta(self, operando2=None):
        self.operacion="-"
        try:
            if self.operando1 is not None and operando2 is not None:
                self.operando2=operando2
                self.operando1 = self.operando1-self.operando2
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None
    
    def multiplicacion(self, operando2=None):
        self.operacion="*"
        try:
            if self.operando1 is not None and operando2 is not None:
                self.operando2=operando2
                self.operando1 = self.operando1*self.operando2
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None
    
    def division(self, operando2=None):
        self.operacion="/"
        try:
            if self.operando1 is not None and operando2 is not None:
                self.operando2=operando2
                self.operando1 = self.operando1/self.operando2
            return self
        except Exception as err:
            print('Gestión de excepciones:', err)
            return "valor no definido"
            
    def potencia(self, exponente): #New method for potencias.
        self.operacion="^"
        try:
            self.current_potencia = self.operando1**exponente
            return self.current_potencia
        except Exception as err:
            return "Exponente no valido. Por favor ingrese un valor congruente."
            
    def sqrt(self): #New method for square root.
        try:
            self.operacion="^2"
            return math.sqrt(self.operando1)
         except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None

class CalculadoraCientifica(Calculadora):
    
    def __init__(self,operando1=0, operando2=0, operacion=None):
        super().__init__(operando1,operando2,operacion)
        self.current_seno = 0
    
    def __str__(self):
        try:
            return str(self.operando1)+self.operacion+str(self.operando2)
        except Exception as err:
            return "Calculadora Cientifica en espera... No operación definida."

    def seno(self): #New seno method for child calculator.
        self.operacion="~"
        try:
            if self.operando1 is not None:
                self.operando1 = math.sin(self.operando1)
                print(self.operando1)
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None
    def coseno(self): #New seno method for child calculator.
        self.operacion="c~"
        try:
            if self.operando1 is not None:
                self.operando1 = math.cos(self.operando1)
                print(self.operando1)
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None
    def tan(self): #New seno method for child calculator.
        self.operacion="tan"
        try:
            if self.operando1 is not None:
                self.operando1 = math.tan(self.operando1)
                print(self.operando1)
            return self
        except Exception as err:
            print('Los operandos tiene que ser numericos', err)
            return None