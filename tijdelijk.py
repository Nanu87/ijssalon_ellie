
#vraag  2
from helper import decoreer

def print_aanbieding():
    mijn_prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5,
    }
    dict = {"key1" : 3, "key2" : 4, "key3" : 5}
    print("Current Dict is: ", dict)

    #vraag 3
    aanbieding = mijn_prijzen ["vanille"] * 0.8

    #vraag 4
    reclame_tekst = f"Vandag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
    print(reclame_tekst)

    #vraag 5
    reclame_tekst2 = reclame_tekst[:63]
    print(reclame_tekst2)

    #vraag 6
    reclame_tekst3 = reclame_tekst2.upper()
    print(reclame_tekst3)

    #vraag 7
    reclame_tekst4 = reclame_tekst3.split()
    print(reclame_tekst4)

    #vraag 8
    el = ["ZERO", "ONE"]
    for item in el:
        print(item)


    #vraag 9
    mystr = ""
    print(mystr.lower())

    elstr = "ZERO"
    print(elstr.lower())

    elstr = "ONE"
    print(elstr.lower())

    #vraag 10
    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())

            decoreer("Aanbieding")
            print_aanbieding()

prijzen = {
"aardbei" : 3,
"vanille" : 4,
"chocolade" : 5
}
aanbieding = prijzen["vanille"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: Vanille-ijs, 1 Liter – slechts € {aanbieding}"
print(reclame_tekst)

reclame_tekst2 = reclame_tekst[:63]
print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2.upper()
print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split()
print(reclame_tekst4)

for el in reclame_tekst4:
  if len(el) > 4:
    print(el.upper())
else:
    print(el.lower())


















