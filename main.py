print("hi")

import random

number = 17
numbers = [6,8,10,]
print (number)
print(numbers)
empty_list  = []
print (empty_list)

empty_list.append(20)
print(empty_list)
empty_list.extend([14, 20, 4])
print (empty_list)

#             0 1 2 3 4 5 6 7 8 9 INDEKSAI
my_numbers = [1,2,3,4,5,6,7,8,9,10]
print(my_numbers)
print(my_numbers[6])

print(my_numbers[0:4])
print(my_numbers[4:8])
print(my_numbers[7:])
print(my_numbers[:4])
print(my_numbers[-2])
print(my_numbers[-5:])
print(my_numbers[:-5])
print(my_numbers[2:-5])
print(my_numbers[-6:-2])
print(my_numbers[-8:4])
print(my_numbers[:])
print(my_numbers[::2])
print(my_numbers[1::2])
print(my_numbers[3:7:2])
print(my_numbers[::3])
print(my_numbers[2:-2:2])
print(my_numbers[::-2])
print(my_numbers[::-1])
print(my_numbers[::-3])


# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
for _ in range(10):
    print("labas")
    print ("labas"*10)

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

my_numbers = [1,2,3,4,5,6,7,8,9,10]
print(my_numbers[:9])
print(my_numbers[:-1])

# 3Sukurkite masyvą iš dešimties augalų pavadinimų.4Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

plant = [ "pupa", "zirnis", "meta", "krapas", "morka", "ridikas", "cebule", "agurkas", " tresne", "vysnia"]
print(plant)
for elementas in plant:
    print(elementas)

plant = [ "pupa", "zirnis", "meta", "krapas", "morka", "ridikas", "cebule", "agurkas", " tresne", "vysnia"]
trumpi = 0
ilgi = 0

for plant in plant:
    if len(plant ) < 5:
        trumpi += 1
    elif len(plant) > 7:
        ilgi += 1

print(f"Žodžių trumpesnių nei 5 simboliai: {trumpi}")
print(f"Žodžių ilgesnių nei 7 simboliai: {ilgi}")
# 10.Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)

plant = [ "pupa", "zirnis", "meta", "krapas", "morka", "ridikas", "cebule", "agurkas", " tresne", "vysnia"]

tarp_5_ir_10 = 0

for zodis in plant:
    if 5 < len(zodis) < 10:  # Žodžiai, kurių ilgis tarp 6 ir 9 simbolių
        tarp_5_ir_10 += 1

print(f"Žodžių ilgesnių nei 5 simboliai, bet trumpesnių nei 10 simboliai: {tarp_5_ir_10}")





# 5. Atausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju.
# (atvirkščias ciklas)

for elementas in reversed(plant):
    print(elementas)

# 6.Atspausdinkite kas antrą  skaiciu nuo  10 iki 50 (porinius);

for num in range(1, 51):
    print(num)

for num in range(2, 51, 2):
    print(num)
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
#
# for num in range(10, 51, 2):
#     print(num)
#
# for num in range(2, 51, 2):
#     if num % 10 != 0:
#         print(num)


#Sukurkite ciklą kuris nuo 0  20.Suskaičiuokite, kiek  kintamasis i turėjo porine reikšmę

count = 0  # Kintamasis, saugantis porinių skaičių kiekį

for i in range(21):  # Ciklas nuo 0 iki 20
    if i % 2 == 0:  # Tikriname, ar skaičius porinis
        count += 1

print("Porinių skaičių kiekis:", count)


rnd_nums = []
for  i in range (0,301):
    rnd_nums.append(random.randint(0,301))
print(rnd_nums)
counter = 0
for num in rnd_nums:
    print (num)
    if num > 150:
        counter += 1
        print ("did")
print (f"{counter}")

# row = ""
# for num in rnd_nums:
#     rnd_nums.append(f"[{num}]" )
#
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.


print(",".join(str(x) for x in range(1, 3001) if x % 77 == 0))

# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.

for y in range(1, 26):
    row = ""#*************************
    for x in range(1, 26):
        row +=  "*"
    print(row)

# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

print("Scenarijus 1: Stabdome iškritus herbui")
while True:
    toss = random.randint(0, 1)
    result = "H" if toss == 0 else "S"
    print(result)
    if toss == 0:
        break
print("\nScenarijus 2: Stabdome iškritus 3 herbams")
h_count = 0
while h_count < 3:
    toss = random.randint(0, 1)
    result = "H" if toss == 0 else "S"
    print(result)
    if toss == 0:
        h_count += 1
print("\nScenarijus 3: Stabdome iškritus 3 herbams iš eilės")
h_streak = 0
while h_streak < 3:
    toss = random.randint(0, 1)
    result = "H" if toss == 0 else "S"
    print(result)
    if toss == 0:
        h_streak += 1
    else:
        h_streak = 0

# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20,
# Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir
# “Partiją laimėjo: ​laimėtojo vardas​”. Taškų kiekį generuokite funkcija ​random.randint(x,x)
# ​. Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol,
# kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

# kazys_taskai = 0
# petras_taskai = 0
# while  kazys_taskai< 222 and petras_taskai < 222:
#      petras_saskes = random.randint(10,20)
#      kazys_saskes = random.randint(5,25)
#      kazys_taskai += kazys_saskes
#      petras_taskai += petras_saskes
#      print(f"Petras{petras_saskes}, Kazys {kazys_saskes}")
# if petras_taskai>=222:
#     print(f"Petras laimi su {petras_taskai} taskais")
# elif kazys_taskai >= 222:
#     print ("Kazys laimi")


# # Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija.
# # Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# # “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm.
# # Suskaičiuokite kiek reikia smūgių.
# # “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė
# # (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį.
# # Suskaičiuokite kiek reikia smūgių.
#
# vinies_ilgis = 85
#
# for  i in range(0,5):
#     sukalta = 0
#     smugiai = 0
#     while sukalta <=vinies_ilgis:
#         smugis = random.randint(5,20 )
#         sukalta += smugis
#         smugiai += 1
#         print (f'{i+1}-tas vinis, {smugiai}, {sukalta}')


#
# random_numbers = random.sample(range(1, 201), 50)
# random_string = " ".join(map(str, random_numbers))
# print(random_string)

#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# # Generuojame 50 unikalių atsitiktinių skaičių nuo 1 iki 200
# random_numbers = random.sample(range(1, 201), 50)
# random_string = " ".join(map(str, random_numbers))
#
# # Filtruojame tik pirminius skaičius
# prime_numbers = sorted([num for num in random_numbers if is_prime(num)])
# prime_string = " ".join(map(str, prime_numbers))
#
# print("Pirmas stringas:", random_string)
# print("Antras stringas:", prime_string)

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.

# for y in range(0, 25):
#     row = ""#*************************
#     for x in range(0, 25):
#         if y == x or  x + y == 24 :
#             row += "|| "
#         else:
#             row +=  "* "
#     print(row)


# for y in range(0, 25):
#     row = ""
#     for x in range(0, 25):
#         row +=  "* "
#     print(row)
#
# n = 20  # Rombo pusės aukštis
#
#  # Viršutinė rombo dalis
# for i in range(1, n + 1, 2):
#     print(" " * ((n - i) // 2) + "* " * i)
# # Apatinė rombo dalis
# for i in range(n - 2, 0, -2):
#     print(" " * ((n - i) // 2) + "* " * i)
#
#
# import turtle
#
#
# # # Sukuriame turtle objektą
# # t = turtle.Turtle()
# #
# # # Piešiame rombą
# # for angle in [50, 130, 50, 130]:  # Kampai
# #     t.forward(100)  # Kraštinės ilgis
# #     t.left(angle)
# # turtle.done()
# #
# #


for y in range(11,20):
    row = ""
    for x in range(0,20):
        if (20 - y < x and x < (20/2)) or (x < y and x >= (20/2)):
            row += "*"
        else:
            row +=" "
    print(row)
for y in range(0,10):
    row = ""
    for x in range(0,20):
        if (20 - y > x and x > (20/2)) or (x > y and x <= (20/2)):
            row += "*"
        else:
            row +=" "
    print(row)

# git config --global user.email "gantel@gmail.com"
# git config  --global user.name "rolandastub"
 print( "labas")