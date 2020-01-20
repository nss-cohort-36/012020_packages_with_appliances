from appliances import CoffeeMaker, DishWasher, Refrigerator, Dryer, Washer, AirConditioner

kenmore = Washer()
kenmore.run_washer()

samsung = Refrigerator()
print("Current temperature in the refrigerator: ", samsung.temp)

goodman = AirConditioner()
goodman.run_ac(75)
