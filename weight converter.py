weight = int(input("weight: "))
unit = (input("(L)bs or (K)gs: "))
if unit.upper() == "K":
    convert = weight / 0.45
    print("weight in Lbs: " + str(convert))
else:
    convert = weight * 0.45
    print("weight in Kgs: " +  str(convert))
