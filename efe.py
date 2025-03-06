class Banking:
    exchange_rates = {
        "USD": {"EUR": 1, "UAH": 43},
        "EUR": {"USD": 1, "UAH": 41.5},
        "UAH": {"USD": 1, "EUR": 0.97}
    }

    def __init__(self, name="", balance=0.0, currency=""):
        self.name = name
        self.balance = balance
        self.currency = currency

    def print_info(self):
        print(f"Ім'я клієнта: {self.name}\nБаланс: {self.balance} {self.currency}")

    def currency_checker(self, currency):
        if currency not in Banking.exchange_rates:
            raise ValueError(f"Валюта {currency} не підтримується!")

    def convert_currency(self, amount, from_currency, to_currency):
        self.currency_checker(from_currency)
        self.currency_checker(to_currency)
        if from_currency == to_currency:
            return amount
        try:
            rate = Banking.exchange_rates[from_currency][to_currency]
            return amount * rate
        except KeyError:
            raise ValueError(f"Курс між {from_currency} і {to_currency} не знайдено.")

    def change_currency(self, new_currency):
        self.currency_checker(new_currency)
        if self.currency != new_currency:
            self.balance = self.convert_currency(self.balance, self.currency, new_currency)
            self.currency = new_currency

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більше нуля.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більше нуля.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount

b = Banking(name="Іван Іванов", balance=1000, currency="USD")
b.print_info()

b.deposit(500)
b.print_info()

b.change_currency("EUR")
b.print_info()

b.withdraw(200)
b.print_info()

try:
    b.change_currency("GBP")
except ValueError as e:
    print(e)
