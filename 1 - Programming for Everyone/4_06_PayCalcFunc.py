def computepay(h, r):
    float_hours = float(h)
    float_rate = float(r)

    if float_hours > 40:
        overtimeRate = float_rate * 1.5
        overtimeHours = float_hours - 40
        overtimePay = overtimeHours * overtimeRate
        normalHours = float_hours - overtimeHours
    else:
        overtimePay = 0
        normalHours = float_hours
    totalPay = overtimePay + (float_rate * normalHours)

    return totalPay


hrs = input("Enter Hours:")
rph = input("Enter Rate.: ")
p = computepay(hrs, rph)
print(p)

