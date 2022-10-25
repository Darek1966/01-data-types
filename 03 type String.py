
str = "Hello World!"
print(str);
print( len(str) ) # len - ilość znaków
print( type(str) ) # type - typ

print( str[ len(str) - 1 ] ) # liczone od zera dlatego -1

print( str[0:5] ) # Hello - jeden więcej czyli 5

print( str * 4 ) # powtórzenie 4 razy

strX3 = str * 3 # przypisany do zmiennej
print(strX3)

str2 = str + " and Hello again!" # łączenie łańcuchów
print(str2)

print(str2[6:]) # World! and Hello again! od 6 indeksu do końca

print(str2[::3]) # HlWl deogn - co trzecia litera

# tworzenie wielu linii, potrójny cudzysłów, lub apostrofy x 3
multiLine = """Pierwsza linia 
Druga linia
Trzecia linia
"""
print(multiLine)

multiLine2 = "Pierwsza linia\nDruga Linia\nTrzecia \t linia \" \\ "
print(multiLine2)