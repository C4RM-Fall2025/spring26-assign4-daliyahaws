def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    periodic_yield = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0
    for t in range(1, periods + 1):
        bondPrice += coupon / (1 + periodic_yield) ** t

    bondPrice += face / (1 + periodic_yield) ** periods
    return bondPrice


y = 0.03
face = 2000000
couponRate = 0.04
m = 10

print(getBondPrice(y, face, couponRate, m, ppy=1))
print(getBondPrice(y, face, couponRate, m, ppy=2))
print(getBondPrice(y, face, couponRate, m))
