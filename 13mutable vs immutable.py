
# immutable: int, float, bool, str, tuple, frozenset

a = 1
addr1 = id(a) # adres

a += 1 # dodajemy 1
addr2 = id(a) # adres

print(addr1) # 2069821260016
print(addr2) # 2069821260048
print(addr1 == addr2) # False


# mutable types: list, set, dict
listData = [0,1,2]
addr1 = id(listData) # adres

listData += [3,4,5] # dodajemy 3, 4, 5
addr2 = id(listData) # adres

print(addr1) # 2069822646912
print(addr2) # 2069822646912
print(addr1 == addr2) # True
