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

    def guess_topic(self, topic_name):

        if topic_name == "Animals":
            topic_word = self.animals[random.randint(1, len(self.animals) - 1)]
        elif topic_name == "Food":
            topic_word = self.foods[random.randint(1, len(self.foods) - 1)]
        elif topic_name == "Drinks":
            topic_word = self.drinks[random.randint(1, len(self.drinks) - 1)]
        elif topic_name == "Nature":
            topic_word = self.natures[random.randint(1, len(self.natures) - 1)]
        elif topic_name == "Places":
            topic_word = self.places[random.randint(1, len(self.places) - 1)]
        
        guess = input("Guess the " + topic_name + ": ")
        guess_count = 1
        while guess.lower() != topic_word and guess_count < 5:
            guess = input("Guess again: ")
            guess_count += 1
        if guess.lower() != topic_word:
            print("\nYou ran out of guesses!" + "\nThe " + topic_name + " was: " + topic_word + "\n")
        else:
            print("\nCongrats, you guessed the " + topic_name + "!\n")

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
