
setData = { 2,3,1,4,5 } # set
setData.add(22)         # dodajemy 22

setData.discard(1)      # kasujemy cyfrę 1
print(type(setData))    # <class 'set'>
print(setData)          # 2, 3, 4, 5, 22

for v in setData:       # pętla
    print(v)            # wyświetla wszystko po kolei

frozenData = frozenset(setData)     # tworzymy frozenset, niezmienialny
print(type(frozenData))             # <class 'frozenset'>
#frozenData.add(56)                 # błąd! nie można dodawać

for value in frozenData:            # literacja
    print(value)                    # pokaże wszystkie elementy frozenset

