from temperature import Temperature

temp1 = Temperature(0, "C")
temp2 = Temperature(32, "F")
temp3 = Temperature(100, "C")

print(temp1 < temp3)
print(temp1 <= temp2)
print(temp3 > temp1)
print(temp1 >= temp2)
print(temp3 < temp1)
