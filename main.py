import math
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type')
parser.add_argument('-pa', '--payment')
parser.add_argument('-pr', '--principal')
parser.add_argument('-pe', '--periods')
parser.add_argument('-i', '--interest')

args = parser.parse_args()
months_in_year = 12
type_ = args.type
negative = 0
argsno = 1
if args.payment is not None:
    p = float(args.payment)
    if p < 0:
        negative += 1
    argsno += 1
if args.principal is not None:
    P = float(args.principal)
    if P < 0:
        negative += 1
    argsno += 1
if args.periods is not None:
    n = int(args.periods)
    if n < 0:
        negative += 1
    argsno += 1
if args.interest is not None:
    i = float(args.interest) / (months_in_year * 100)
    if i < 0:
        negative += 1
    argsno += 1

if type_ == 'diff' and args.payment is None and argsno >= 4 and negative == 0:  # calculate monthly payments
    if P > 0 and n > 0 and args.interest != None:
        total = 0
        for month in range(1, n + 1):
            diff = math.ceil(P / n + i * (P - (P * (month - 1)) / n))
            print(f'Month {month}: payment is {diff}')
            total += diff
        print(f'\nOverpayment = {int(total - P)}')

    # loan_principal = float(input('Enter the loan principal:'))
    # monthly_payment = int(input('Enter the monthly payment:'))
    # loan_interest = float(input('Enter the loan interest:'))
    #
    # nominal_rate = loan_interest / (months_in_year * 100)
    #
    # months = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_rate * loan_principal), 1 + nominal_rate))
    # years = math.floor(months / months_in_year)
    # if months % months_in_year == 1:
    #     plural = 'month'
    # else:
    #     plural = 'months'
    # if years == 1:
    #     plural_years = 'year'
    # else:
    #     plural_years = 'years'
    # if months < months_in_year:
    #     print(f'It will take {months} {plural} to repay the loan')
    # elif months % months_in_year == 0:
    #     print(f'It will take {years} {plural_years} to repay the loan')
    # else:
    #     print(f'It will take {years} {plural_years} and {months % months_in_year} {plural} to repay the loan')
elif type_ == 'annuity' and argsno >= 4 and negative == 0:  # calculate annuity
    if args.periods is None:  # calculate monthly payments
        n = math.ceil(math.log(p / (p - i * P), 1 + i))
        years = math.floor(n / months_in_year)
        if n % months_in_year == 1:
            plural = 'month'
        else:
            plural = 'months'
        if years == 1:
            plural_years = 'year'
        else:
            plural_years = 'years'
        if n < months_in_year:
            print(f'It will take {n} {plural} to repay the loan')
        elif n % months_in_year == 0:
            print(f'It will take {years} {plural_years} to repay the loan')
        else:
            print(f'It will take {years} {plural_years} and {n % months_in_year} {plural} to repay the loan')
        print(f'Overpayment = {int(p * n - P)}')
    elif args.payment is None:  # calculate annuity
        p = math.ceil(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))

        print(f'Your monthly payment = {p}!')
        print(f'Overpayment = {int(p * n - P)}')

    elif args.principal is None:  # calculate loan principal
        P = math.floor(p / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))

        print(f'Your loan principal = {P}!')
        print(f'Overpayment = {int(p * n - P)}')

else:
    print('Incorrect parameters')
