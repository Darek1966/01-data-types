
contacts = { # nawiasy klamrowe
    "Ola" : "ola@example.com", # przypisanie wartości do klucza
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com" # dodanie nowej wartości

print(contacts["Ola"])
print(contacts["Daniel"]) # 30
print(type(contacts)) # klass doct
print(len(contacts)) # 4

print( contacts.keys() ) # lista kluczy
print( contacts.values() ) # lista wartości

for key in contacts:
    print( key + " " + str(contacts[key]) )
# key - nowa zmienna
# str - trzeba skonwerterować ponieważ jest tam jedna liczba
# " " - spacja
print(" ") # spacja

for key, value in contacts.items():
    print( key, " ", value)
