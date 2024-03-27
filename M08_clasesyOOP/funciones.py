class Funciones:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def funcion_primo(self):
        for i in self.lista:
            if (self.__funcion_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def __funcion_primo(self, numero):
        es_primo = True
        for i in range(2,numero):
            if numero % i == 0:
                es_primo = False
                break
        return es_primo
    
    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def __conversion_grados(self, valor, origen, destino):

        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'farenheit':
            if destino == 'celsius':
                valor_destino = (valor - 32) * 5 / 9
            elif destino == 'farenheit':
                valor_destino = valor
            elif destino == 'kelvin':
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')

        return valor_destino
    
    def mas_repetido(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))
    
    def __factorial(self, numero):
        if type(numero) != int:
            return 'El número debe ser un entero'

        if numero < 0:
            return 'El número debe ser positivo'
        
        if numero > 1:
            numero = numero * self.__factorial(numero - 1)
        
        return numero