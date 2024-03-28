class Funciones:
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista_numeros

    def funcion_primo(self):
        lista_primos = []
        for i in self.lista:
            if (self.__funcion_primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def __funcion_primo(self, numero):
        es_primo = True
        for i in range(2,numero):
            if numero % i == 0:
                es_primo = False
                break
        return es_primo
    
    def conversion_grados(self, origen, destino):
        parametros_esperados = ['celsius','kelvin','farenheit']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino))
        return lista_conversion
    
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
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial
    
    def __factorial(self, numero):
        if type(numero) != int:
            return 'El número debe ser un entero'

        if numero < 0:
            return 'El número debe ser positivo'
        
        if numero > 1:
            numero = numero * self.__factorial(numero - 1)
        
        return numero