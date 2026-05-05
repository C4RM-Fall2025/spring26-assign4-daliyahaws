def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    periodic_yield = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0
    weighted_sum = 0

    for t in range(1, periods + 1):
        pv = coupon / (1 + periodic_yield) ** t
        bondPrice += pv
        weighted_sum += t * pv

    pv_face = face / (1 + periodic_yield) ** periods
    bondPrice += pv_face
    weighted_sum += periods * pv_face

    bondDuration = (weighted_sum / bondPrice) / ppy

    return bondDuration


y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

print(getBondDuration(y, face, couponRate, m, ppy))
