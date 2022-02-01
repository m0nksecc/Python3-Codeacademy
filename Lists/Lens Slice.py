# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#using count
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#using len
num_pizzas = len(toppings)

#print string
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#2d list, asked to create 2d list from scratch but found an easier way on StackOverFlow
pizza_and_prices = list(zip(prices, toppings))

#using sort
pizza_and_prices.sort()

#storing value of cheapest pizza
cheapest_pizza = pizza_and_prices[1]
print(cheapest_pizza)

#storing value of most expensive pizza
priciest_pizza = pizza_and_prices[6]

#using pop
pizza_and_prices.pop(6)

#using insert
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#using List Slicing
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

