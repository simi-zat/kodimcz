# Zadani: https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dedicnost/cenny-balik

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}"

    # def get_info(self):
    #     return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}"

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359





