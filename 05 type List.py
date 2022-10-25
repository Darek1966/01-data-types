
list = ["Ola", "Ania", 23, 99, "Rafał"]
print( type(list) ) # <class 'list'>
print(list)

print(list[0]) # Ola
print( len(list) ) # 5
print( list[4] ) # Rafał
print( list[len(list)-1] ) # Rafał
# print( list[5] ) # IndexError: list index out of range

print( list[-1] ) # Rafał
print( list[-2] ) # 99
# print( list[-6] ) # IndexError: list index out of range

print( list[1:4] ) # ['Ania', 23, 99] - od 1 - 3
print( list[2:] ) # [23, 99, 'Rafał'] - do końca listy

list[0] = "Kasia" # zmiana pierwszego indeksu
print(list) # ['Kasia', 'Ania', 23, 99, 'Rafał']

del list[2] # kasowanie - 23
print(list) # ['Kasia', 'Ania', 99, 'Rafał']

print( 99 in list ) # czy jest w liście - True
print( "Rafał" in list ) # True
print( "Ola" in list ) # False

if "Ania" in list: # jeżeli Ania jest w liście
    print("Ania jest w liście list")
    print("Kolejny kod") # spacja, wcięcie blok kodu

print("Dalszy kod") # bez wcięcia - nowy kod


for v in list: # pętla - wszystko z listy
    print(v) # pętla - wyświetli po kolei wszystkie elementy listy
              # nie musi być v, może być każda inna nazwa

data = [  # lista wielopozimowa, podwójne nawiasy
    ["Daniel", "Rafał"], # 0
    ["Kasia", "Ania"], # 1
    ["Ola", "Adam"] # 2
 ]

print(len(data)) # 3

print(data[1][0]) # Kasia
print(data[2][1]) # Adam

data1 = [1, 2, 3]
data2 = [4, 5, 6]

numbers = data1 + data2 # łączenie list
print(numbers) # [1, 2, 3, 4, 5, 6]

numbersX2 = numbers * 2 # mnożenie
print(numbersX2) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
