def getIncomeTax(salary):
    if salary < 12500:
        return 0
    elif 12500 <= salary <= 50000:
        return (salary - 12500) * 0.2
    elif 50001 <= salary <= 150000:
        return 7500 + (salary - 50000) * 0.4
    elif salary > 150000:
        return 47500 + (salary - 150000) * 0.45

salary = 100000


tax_amount = getIncomeTax(salary)

print("Tax amount for salary £{} is £{}".format(salary, tax_amount))