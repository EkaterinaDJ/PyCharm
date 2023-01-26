# class Customers:
#     def __init__(self, name, surname, city, balance):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#     def __str__(self):
#         return f'"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'
#
# Customer_1 = Customers('Иван',  'Петров', 'Москва', 50)
# print(Customer_1)

class Customers:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    # def __str__(self):
    #     return f'"{self.name} {self.surname}. {self.city}."'

    def get_guest(self):
        return f'{self.name} {self.surname}. {self.city}.'


Customer_1 = Customers('Иван',  'Петров', 'Москва')
Customer_2 = Customers('Петр', 'Иванов', 'Казань')
Customer_3 = Customers('Елена', 'Федорова', 'Псков')
Customer_4 = Customers('Василий','Сергеев', 'Гатчина')
Customer_5 = Customers('Анна', 'Сергеева', 'Гатчина')

guest_list = [Customer_1, Customer_2, Customer_3, Customer_4, Customer_5]
for guest in guest_list:
    print(guest.get_guest())


# print(Customer_1)
