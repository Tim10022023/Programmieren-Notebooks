import re
transactionOne = dict(type="Purchase", amount=100, date="14.01.2024")
transactionTwo = dict(type="Sale", amount=150, date="15.01.2024")
transactionThree = dict(type="Purchase", amount = 110, date="14.01.2024")

allTransactions=[transactionOne, transactionTwo, transactionThree]
z = 0
for x in allTransactions:
    if x["date"]=="14.01.2024":
        z+=1
print("Transactions yesterday: " + str(z))

def find_all(my_key, my_value):
    values = [transaction for transaction in allTransactions if transaction[my_key]==my_value]
    return values

    
def print_result(my_result):
    if my_result<0:
        print("You lost money: " + str(my_result))
    else:
        print("You earned money: " + str(my_result))

def sum_up(par):
    a = 0
    for x in allTransactions:
        if x["type"]==par:
            a+=x["amount"]
    return a


def pruefe_datum_format(datum):
    pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')

    if re.match(pattern, datum):
        return True
    else:
        return False

print(pruefe_datum_format(allTransactions[0]["date"]))
my_transactions = find_all("date", "14.01.2024")
print(my_transactions)
result = sum_up("Sale") - sum_up("Purchase")
print_result(result)