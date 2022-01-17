import random

from Topic import Topic


class GuessWordTopic(Topic):

    animals = ["dog", "cat", "horse", "pig", "cow", "elephant", "bird", "fish", "chicken", "snake",
               "whale", "turtle", "mouse", "butterfly", "bee", "monkey"]

    foods = ["hot dog", "carrots", "ham", "pizza", "cookie", "eggs", "banana", "fish", "chicken", "pancakes",
             "sandwich", "apple", "cheese", "bacon", "bread", "ice cream"]

    drinks = ["hot chocolate", "carrot juice", "pineapple juice", "milk", "chocolate milk", "egg nog", "water",
              "milkshake", "orange juice", "apple juice",
              "punch", "grape juice", "coffee", "tea", "smoothie", "soda"]

    natures = ["mountain", "moon", "sun", "glacier", "clouds", "animals", "waterfall",
               "saturn", "comet", "mars",
               "rain forest", "desert", "magma", "ocean", "electron", "light"]

    places = ["South America", "Canada", "New York", "Toronto", "Italy", "Niagara Falls", "USA",
              "Outer Space", "ISS", "Vancouver", "Paris", "Tokyo", "Denmark", "Sweden", 
              "Barcelona", "London", "Florida", "Kansas", "Baltimore", "Boston", "South Africa"]

    all_groups = [animals, foods, drinks, natures, places]

    def guess_animal(self):

        animal = self.animals[random.randint(1, len(self.animals) - 1)]
        guess = input("Guess the animal: ")
        guess_count = 1
        while guess.lower() != animal and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != animal:
            print("\nYou ran out of guesses!" + "\nThe animal was: " + animal + "\n")
        else:
            print("\nCongrats, you guessed the animal!\n")

    def guess_food(self):

        food = self.foods[random.randint(1, len(self.foods) - 1)]
        guess = input("Guess the food: ")
        guess_count = 1
        while guess.lower() != food and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != food:
            print("\nYou ran out of guesses!" + "\nThe food was: " + food + "\n")
        else:
            print("\nCongrats, you guessed the food!\n")

    def guess_drink(self):

        drink = self.drinks[random.randint(1, len(self.drinks) - 1)]
        guess = input("Guess the drink: ")
        guess_count = 1
        while guess.lower() != drink and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != drink:
            print("\nYou ran out of guesses!" + "\nThe drink was: " + drink + "\n")
        else:
            print("\nCongrats, you guessed the drink!\n")

    def guess_nature(self):

        nature = self.natures[random.randint(1, len(self.natures) - 1)]
        guess = input("Guess the nature: ")
        guess_count = 1
        while guess.lower() != nature and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != nature:
            print("\nYou ran out of guesses!" + "\nThe nature was: " + nature + "\n")
        else:
            print("\nCongrats, you guessed the nature!\n")

    def guess_place(self):

        place = self.places[random.randint(1, len(self.places) - 1)]
        guess = input("Guess the place: ")
        guess_count = 1
        while guess.lower() != place.lower() and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != place.lower():
            print("\nYou ran out of guesses!" + "\nThe place was: " + place + "\n")
        else:
            print("\nCongrats, you guessed the place!\n")

    def guess_all_group(self):

        all_group_type = self.all_groups[random.randint(1, len(self.all_groups) - 1)]
        all_group = all_group_type[random.randint(1, len(all_group_type) - 1)]
        guess = input("Guess the animal, food, drink, nature, or place: ")
        guess_count = 1
        while guess.lower() != all_group.lower() and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != all_group.lower():
            print("\nYou ran out of guesses!" + "\nThe word was: " + all_group + "\n")
        else:
            print("\nCongrats, you guessed the word!\n")
