
data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafał"  # błąd! nie mozna modyfikować

names = data + ("Rafał",) # łączenie, przecinek
print(names)
print(len(names)) # 4
print(type(names)) # typ - Tuple 

numbers = 1, 2 ,3
print(type(numbers)) # typ - Tuple 

emptyTuple = () # pusta krotka
print(emptyTuple)
print(type(emptyTuple)) # typ - Tuple 

print(names[1]) # Ola
print(names[-1]) # Rafał
print(names[1:3]) # Ola, Kasia

cars = ( ("dodge", "ford") , ("pontiac") ) # wielopoziomowa
print(cars[0][0]) #doge

if "ford" in cars[0]: # True
    print("Ford w krotce nr 1") # będzie wyświetlał

del cars # kasowanie
# print(cars) - błąd

# del names[0] - nie można kasować

tupleX3 = names * 3 # zwielokrotnienie
print(tupleX3) 
