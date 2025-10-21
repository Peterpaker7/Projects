
import csv

AMOUNT_PER_MEMBER = 200

with open('swimmingpool.csv', 'w', newline='') as f:
    w = csv.writer(f)
    col = ['Name', 'Members', 'Hrs', 'Amount', 'Payment Mode']
    w.writerow(col)
    ent_no = 1
    while True:
        print(f'S.no:{ent_no}')
        while True:
            try:
                mem = int(input('Enter How many members:'))
                if mem >= 0:
                    break
                else:
                    print('Cannot be negative again')
            except ValueError:
                print('Invalid Try Again :(')
        member_names = []
        for i in range(mem):
            while True:
                name = input(f'Enter the name{i+1}:')
                if name.isalpha() or ' ' in name:
                    break
                else:
                    print('Cant be number')
            member_names.append(name)
        while True:
            try:
                hrs = int(input('Enter how many hours(in numbers):'))
                if hrs >= 0:
                    break
                else:
                    print('Cant be the Letters ')
            except ValueError:
                print('Invalid Try Again :(')
        total_amount = AMOUNT_PER_MEMBER
        payment_details = {}
        while True:
            try:
                pay = int(input('Enter the payment mode (1) cash, (2) Gpay, (3) done: '))
                if pay == 1:
                    mode = 'cash'
                elif pay == 2:
                    mode = 'gpay'
                elif pay == 3:
                    break
                else:
                    print('Invalid payment mode.')
                while True:
                    try:
                        amount_paid = float(input(f'Enter amount paid by {mode}: '))
                        if amount_paid >= 0:
                            payment_details[mode] = amount_paid
                            break
                        else:
                            print('It cant be negative')
                    except ValueError:
                        print('Invalid Try Again :(')
            except ValueError:
                print('Invalid input.')
        TAP = sum(payment_details.get(mode, 0) for mode in ['cash', 'gpay'])
        payment_str = ', '.join([f"{mode}: {amount}" for mode, amount in payment_details.items()])
        for i, name in enumerate(member_names):
            member_count = mem if i == 0 else ''
            hours = hrs if i == 0 else ''
            amount = total_amount if i == 0 else ''
            payment = payment_str if i == 0 else ''
            data = [name, member_count, hours, amount, payment]
            w.writerow(data)
        ch = input('Enter Y to enter more details or N: ')
        if ch.lower() == 'n':
            break
        ent_no += 1
