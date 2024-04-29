# Zadani: https://kodim.cz/czechitas/python-oop/lekce/tridy/tridy/kniha

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha {self.title} ma {self.pages} stranek a stoji {self.price} Kc."

    def get_time_to_read(self, cas_precteni_stranky=4):
        celkem_minuty = cas_precteni_stranky * self.pages
        return f"{int(celkem_minuty / 60)}:{celkem_minuty % 60}"


book1 = Book("Harry Potter", 247, 599)
print(book1.get_info())
print(book1.get_time_to_read())

book2 = Book("Lord of the Rings", 670, 1000)
print(book2.get_info())
print(book2.get_time_to_read())
