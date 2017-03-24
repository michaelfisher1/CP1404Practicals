def main():

    incomes = []
    number_of_months = int(input("How many monthly incomes do you wish to calculate?"))

    for month in range(1,number_of_months+1):
        monthly_income = float(input("Enter income for month {}".format(month)))
        incomes.append(monthly_income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    print("\nIncome Report\n-----------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:<8}Total:${:5}".format(month + 1, income, total))


main()
