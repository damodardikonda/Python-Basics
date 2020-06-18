import datetime
import calendar


print("how many month requires to creadit carx bill")

balance=5000
interest_rate=13 *0.1#0.1 gives you an decimal point
month_payment=500

today=datetime.date.today()
current_day_in_month=calendar.monthrange(today.year,today.month)[1]#it will provides output in tuple year or month
Remaining_days=current_day_in_month-today.day

print("Remaining_days")
print(Remaining_days)

print("starting date of next month")
start_date=today+datetime.timedelta(days=Remaining_days+1)
print("Start date is")
print(start_date)

end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
