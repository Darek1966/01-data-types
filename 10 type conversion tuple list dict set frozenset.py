
listData = [1,2,3,4,5,6]  # lista

tupleData = tuple(listData) # konwersja na krotkę - tuple
print(tupleData) # (1, 2, 3, 4, 5, 6)

otherList = list( ("Ola", 23, 234) ) # konwersja krotka na listę
print(otherList) # ['Ola', 23, 234] - lista, nawiasy kwadratowe

setData = set(otherList) # konwersja na zbiór
print( type(setData) ) # <class 'set'>
print(setData) # {234, 'Ola', 23} - zbiór, klamry

frozenSetData = frozenset(tupleData) # konwersja na zbiór niemutowalny
print(type(frozenSetData)) # <clas 'frozenset'>
print(frozenSetData) # ({1, 2, 3, 4, 5, 6}) - podwójny nawias

tupleData = ( ("Ola", 1234) , ("Adam", 23654) ) # krotka (klucz, wartość)

dictData = dict(tupleData) # konwersja na słownik
print(dictData) # wyświetli: {'Ola': 1234, 'Adam': 23654}
print(dictData["Ola"]) # wyświetli: 1234
