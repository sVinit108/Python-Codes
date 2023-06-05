# Normal Way
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

# walrus operator (:=)
# It lets you assign a value to a variable right inside the condition of an if statement or while loop.
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)