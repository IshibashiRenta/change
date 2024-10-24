print("購入する金額：")
nedan = int(input())
tounyu = 0
while(nedan > tounyu):
    print("値段を超える金額を入れてください：")
    tounyu = int(input())

oturi = tounyu - nedan

def oturi_tukuru(tounyu):
    if tounyu >= 500:
        maisu["500em"] = int(tounyu / 500)
        tounyu = tounyu % 500
    if tounyu >= 100:
        maisu["100en"] = int(tounyu / 100)
        tounyu = tounyu % 100
    if tounyu >= 50:
        maisu["50en"] = int(tounyu / 50)
        tounyu = tounyu % 50
    if tounyu >= 10:
        maisu["10en"] = int(tounyu / 10)
        tounyu = tounyu % 10

mai500 = 0
mai100 = 0
mai50 = 0
mai10 = 0
maisu = {"500em":mai500,"100en":mai100,"50en":mai50,"10en":mai10}

oturi_tukuru(oturi)
print(maisu)