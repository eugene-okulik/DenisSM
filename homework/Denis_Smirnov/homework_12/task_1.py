class Flower:
    def __init__(self, name, color, price, stem_length, freshness_days, lifespan_days):
        self.name = name
        self.color = color
        self.price = price
        self.stem_length = stem_length
        self.freshness_days = freshness_days
        self.lifespan_days = lifespan_days

class Rose(Flower):
    def __init__(self, color='red', price=100, stem_length=50, freshness_days=3, lifespan_days=7):
        super().__init__('Роза', color, price, stem_length, freshness_days, lifespan_days)

class Tulip(Flower):
    def __init__(self, color='yellow', price=60, stem_length=40, freshness_days=4, lifespan_days=6):
        super().__init__('Тюльпан', color, price, stem_length, freshness_days, lifespan_days)


class Daisy(Flower):
    def __init__(self, color='white', price=40, stem_length=30, freshness_days=2, lifespan_days=5):
        super().__init__('Маргаритка', color, price, stem_length, freshness_days, lifespan_days)

class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        total_days = sum(flower.lifespan_days for flower in self.flowers)
        return total_days / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.freshness_days)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def find_by(self, condition):
        return [flower for flower in self.flowers if condition(flower)]


#Проверка работы классов
rose = Rose(price=100, freshness_days=3)
tulip = Tulip(price=60, freshness_days=4)
daisy = Daisy(price=40, freshness_days=2)


bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(daisy)

print("Стоимость букета:", bouquet.get_total_price())
print("Среднее время жизни в днях:", bouquet.average_lifespan())

bouquet.sort_by_price()

print("\nЦветы по возрастанию цены:")
for flower in bouquet.flowers:
    print(f"{flower.name}, цена - {flower.price}")

cheap_flowers = bouquet.find_by(lambda flower: flower.price < 70)

print("\nЦветы дешевле 70:")
for flower in cheap_flowers:
    print(f"{flower.name}, цена - {flower.price}")