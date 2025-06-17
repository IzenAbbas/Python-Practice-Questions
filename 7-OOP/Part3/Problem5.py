class Bill:
    def __init__(self, i, p):
        self.total = 0
        self.items = i
        self.price = p
        for i in self.price:
            self.total += i

    def display(self):
        for i, j in zip(self.items, self.price):
            print('Item:', i, ', Price:', j)
        print('Total Price:', self.total)


class CashPayment(Bill):
    def __init__(self, i, p, d, v):
        super().__init__(i, p)
        self.deno = d
        self.value = v

    def show_cash_payment_details(self):
        print("\n--- Cash Payment Details ---")
        super().display()
        print("Denominations Used:")
        for i, j in zip(self.deno, self.value):
            print(f'{i} x {j} = {i * j}')
        print("Total Cash:", sum(i * j for i, j in zip(self.deno, self.value)))


class ChequePayment(Bill):
    def __init__(self, i, p, cheque_no, bank_name):
        super().__init__(i, p)
        self.cheque_no = cheque_no
        self.bank_name = bank_name

    def show_check_payment_details(self):
        print("\n--- Cheque Payment Details ---")
        super().display()
        print('Cheque Number:', self.cheque_no)
        print('Bank Name:', self.bank_name)


items = ["External Hard Disk", "RAM", "Printer", "Pen Drive"]
price = [5000, 2000, 6000, 800]

option = int(input("Would you like to pay by cheque or cash (1/2): "))

if option == 1:
    name = input("Enter the name of the bank: ")
    cno = input("Enter the cheque number: ")
    cheque = ChequePayment(items, price, cno, name)
    cheque.show_check_payment_details()
else:
    deno = [10, 20, 50, 100, 500, 2000]
    value = [1, 1, 1, 2, 4, 5]
    cash = CashPayment(items, price, deno, value)
    cash.show_cash_payment_details()
