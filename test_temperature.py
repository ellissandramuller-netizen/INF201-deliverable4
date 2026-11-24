
from temperature import Temperature

temp1 = Temperature(25, "C")
temp2 = Temperature(77, "F")
temp3 = Temperature(298.15, "K")

print(temp1.to_celsius())
print(temp2.to_celsius())
print(temp3.to_celsius())