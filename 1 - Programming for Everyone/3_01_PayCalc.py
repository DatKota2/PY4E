rate = input("Enter the hourly rate of pay: ")
hours = input("Enter the number of hours worked for this pay period: ")
float_hours = float(hours)
float_rate = float(rate)

if float_hours > 40:
    overtimeRate = float_rate * 1.5
    overtimeHours = float_hours - 40
    overtimePay = overtimeHours * overtimeRate
    normalHours = float_hours - overtimeHours
else:
    overtimePay = 0
    normalHours = float_hours

totalPay = overtimePay + (float_rate * normalHours)

print(totalPay)
