
floatNum = 23.24234234 # liczba rzeczywista
intNum = int(floatNum) # konwerja na 'int'
print( type(intNum) )  # <class 'int'>
print(intNum) # wyświetli 23

print( int(" 678    ") )  # 678
print( int(99) )    # 99

intNum = 56 
float1 = float(intNum) # konwersja na 'float'
print( type(float1) ) # <class 'float'>
print(float1)   # 56.0

str1 = "123.5476786" # łańcuch znaków
float2 = float(str1)  # konwersja na 'float'
print( type(float2) )  # <class 'float'>
print( float2 )  # 123.5476786
print( float(89.798) ) # 89.798

# konwersja na łańcuch znaków
print( "Wartość float1: " + str(float1) + " " + str(78) + " " + str([1,2,3,4]) )
# wyświetli: Wartość float1: 56.0 78 [1, 2, 3, 4]

print("Wartość float1", float1, " ", 78, [1,2,3]) # drugi sposób
# wyświetli: Wartość float1 56.0   78 [1, 2, 3]
