import datetime

import calendar

print('')
print('================= Example 1==================')
print('')

balance = 5000.0
interest_annual = 13.0 * 0.01
monthly_payment = 500.0


today = datetime.date.today()

print(today)


days_in_current_month = calendar.monthrange(today.year,  today.month)[1]

print(days_in_current_month)

start_date = today + datetime.timedelta(days=days_in_current_month + 1)

print(start_date)

end_date = start_date


while balance > 0:

    monthly_increment = 1.00 + interest_annual/12.0

    balance *= monthly_increment

    balance -= monthly_payment


    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date,  balance)

    days_in_current_month = calendar.monthrange(end_date.year,  end_date.month)[1]

    end_date = end_date + datetime.timedelta(days=days_in_current_month)


diff = end_date-start_date
# print(diff)
print(str('Loan finished in ')+str(diff.days//30) + ' Months')

print('')
print('======================= Example 2 =========================')
print('')

current_weight = 150

goal_weight = 70

avg_kilos_per_week = 1.5

start_date2 = datetime.date.today()

end_date2 = start_date

while current_weight > goal_weight:

    end_date2 += datetime.timedelta(days=7)

    current_weight -= avg_kilos_per_week

    print(end_date2, current_weight)

print('Reached goal in {} weeks'.format((end_date2-start_date2).days//7))

print('')
print('================= Example 3==================')
print('')

goal_subs = 1000000

current_subs = 50000

subs_to_go = goal_subs - current_subs

avg_subs_perday = 2537

import math

days_to_go = math.ceil(subs_to_go/avg_subs_perday) # this function rounds the value to its nearest value

start_date3 = datetime.date.today()

end_date3 = start_date3 + datetime.timedelta(days=days_to_go)

print(days_to_go)
print(start_date3, '-', end_date3)


