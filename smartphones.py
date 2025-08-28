# Base Class: Device

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Subclass: Smartphone

class Smartphone(Device):
    def __init__(self, brand, model, os, battery):
        # Call the parent constructor
        super().__init__(brand, model)
        self.os = os
        self.battery = battery  # in percentage

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"🔋 Battery charged to {self.battery}%"

    def use(self, hours):
        drain = hours * 10  # 10% battery drain per hour
        self.battery = max(0, self.battery - drain)
        return f"📱 Used for {hours}h, battery at {self.battery}%"

    # Polymorphism: override parent method
    def info(self):
        return f"{self.brand} {self.model} running {self.os}, Battery: {self.battery}%"



# Subclass: SuperPhone

class SuperPhone(Smartphone):
    def __init__(self, brand, model, os, battery, ai_assistant):
        super().__init__(brand, model, os, battery)
        self.ai_assistant = ai_assistant

    def summon_ai(self):
        return f"🤖 {self.ai_assistant} is here to help you!"


# Program Execution / Testing

if __name__ == "__main__":
    # Create a normal smartphone
    phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 80)
    print(phone1.info())
    print(phone1.use(3))
    print(phone1.charge(25))

    print("-" * 40)

    # Create a super smartphone
    superphone = SuperPhone("Apple", "iPhone 16 Ultra", "iOS", 90, "Siri++")
    print(superphone.info())
    print(superphone.summon_ai())
