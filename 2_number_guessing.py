# Mit Python kann man mathe machen !
print(2 + 3)
print(10 / 5)

# Mit variablen

a = 2
b = 4

# Addition
summe = a + b

print(summe)

# Soustraction

differenz = b - a

print(differenz)

# Vergleichen

c = 4
if b > a:
    print(a, "is größer als", b)
if c >= b:
    print(c, "ist nicht größer als", b)
if b == c:
    print(b, "und", c, "sind gleich groß")

d = input("Gibt eine Zahl ein")
# Die Eingabe sind immer string, man muss dann zum Integer wechseln, um
# den vergleich machen zu können

d = int(d)
# Um wieder zu string zu wechelsen
d = str(d)
d = int(d)

if d > 0:
    print(d, "ist ein positive Zahl")
if d == 0:
    print(d, "ist null")
else:
    print(d, "ist ein negative Zahl")
