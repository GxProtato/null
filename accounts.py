import datetime
import pytz


class Account:
    """simple accounts class with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        self.attribute = "attribute"
        print("account created for " + self._name)

    def deposite(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("insufficient balance")

    def show_balance(self):
        print("balance is {}".format(self._balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

# george = Account("george", 0)
# george.deposite(1999)
# # george.show_balance()

if __name__ == '__main__':
    george = Account("george", 0)
    george.show_balance()
    george.deposite(100)
    george.withdraw(200)
    george.show_transaction()
    george.newattribute = "zero"


    steph = Account("steph", 800)
    steph.deposite(100)
    steph.withdraw(200)
    steph.show_transaction()

    print(george.__dict__)
    print(Account.__dict__)
    print(george.attribute)