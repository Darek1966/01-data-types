
print(bool()) # False

# falsy values, czyli wartości które dają false przy konwersji na boolean
print( bool(False) ) # False False
print( bool(0) ) # 0 False
print( bool(0.0) ) # 0.0 False
print( bool( () ) ) # puste krotki False
print( bool( [] ) ) # puste listy False
print( bool( {} ) ) # puste zbiory False
print( bool( '' ) ) # pusty łańcuch False
print( bool( None ) ) # None - brak wartości False

print( bool(True) ) # True
print( bool(10) ) # True
print( bool(-10) ) # True
print( bool(-12.234) ) # True
print( bool( (1,2,3) ) ) # krotka True
print( bool( [0] ) ) # lista nie jest pusty True
print( bool( {0} ) ) # zbiór True
print( bool( "z" ) ) # łańcuch True
