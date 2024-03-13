bilangan = 0
ganjil = False
while ganjil == False:
    bilangan = int(input("Masukan bilangan ganjil"))
    if bilangan % 2 == 1:
        ganjil  = True
print(bilangan, "Yang kamu masukan adalah bilangan ganjil")
