price = 50451.28

print("Euro to Bitcoin converter")

while True:
    val_eur = float(input("Euro: ").replace(",", "."))
    val_bit = val_eur / price

    print("{0} Euro = {1} Bitcoin".format(val_eur, val_bit))

    cont = input("Continue? (Y/N)")
    if cont.upper() == "N":
        break
