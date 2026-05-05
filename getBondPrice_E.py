def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0

    for i, y in enumerate(yc):
        t = i + 1
        cf = coupon
        if i == len(yc) - 1:
            cf += face
        pv = cf / (1 + y) ** t
        bondPrice += pv

    return bondPrice


yc = [.010, .015, .020, .025, .030]
face = 2000000
couponRate = .04

print(getBondPrice_E(face, couponRate, yc))
