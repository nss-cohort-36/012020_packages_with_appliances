class DishWasher:

    def __init__(self):
        self.clean = True
        self.dishes = []

    def run_dishwasher(self, cups):
        self.clean = True

    def load_dishwasher(self, dish):
        self.clean = False
        self.dishes.append(dish)
