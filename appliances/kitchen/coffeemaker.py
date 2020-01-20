class CoffeeMaker:

    def __init__(self):
        self.max_cups = 4

    def make_coffee(self, cups):
        if cups <= self.cups:
            print(f'{cups} cups of coffee has been brewed!')
        else:
            print(f'Sorry, coffee will overflow!')
