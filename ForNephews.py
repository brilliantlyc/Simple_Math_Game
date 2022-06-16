from Topic import Topic
from MathTopic import MathTopic
from GuessWordTopic import GuessWordTopic

name = input("What is your name? ")
print("Hello " + name + "!\n")

# Can add or remove topics from the topic_names list and the code will work based on the list
topic_names = ["Math", "Language", "Guess the Word", "Science", "Exit"]

topics = []
# the topics list contains Topic type objects
for topic_name in topic_names:
    topics.append(Topic(topic_name))


print("What would you like to do today? \n")


# this function shows the user the options, prompts them for a selection and returns the selection
def get_selection(topics_list):
    topic_count = 0
    while topic_count < len(topics_list):
        print("(" + str(topic_count + 1) + ") " + topics_list[topic_count])
        topic_count += 1
    print()
    topic_counter = 1
    prompt_str = "Please enter 1"

    # create the prompt string using the length of the topics list
    while topic_counter <= len(topics_list):
        topic_counter += 1
        if topic_counter < len(topics_list):
            prompt_str = prompt_str + ", " + str(topic_counter)
        elif topic_counter == len(topics_list):
            prompt_str = prompt_str + ", or " + str(topic_counter) + ": "

    # prompt the user to select from the topics list
    topic = input(prompt_str)
    valid_input = ""
    j = 0

    # create a string that contains all the valid inputs, e.g. "1234"
    while j < len(topics_list):
        j += 1
        valid_input += str(j)

    # if the user entered an invalid input then prompt them until they enter a valid one
    while topic not in valid_input:
        topic = input(prompt_str)
    return topic


def get_continue_choice(subtopic):
    continue_subject_prompt = "a"
    while continue_subject_prompt not in "yn":
        continue_subject_prompt = input("Continue " + subtopic + "? (Y/N): ").lower()
        if continue_subject_prompt == "n":
            return False
        elif continue_subject_prompt == "y":
            return True


exit_game = False

while not exit_game:

    # prompt user to select the topic
    selection = get_selection(topic_names)
    topic_selection = topic_names[int(selection)-1]
    if topic_selection != "Exit":
        print("\nOkay, let's do " + topic_selection + "!\n")
    else:
        exit_game = True
        print("\nThanks for playing!")

    # depending on the topic name, create a class of the topic and a subclass of subtopics and a generate the questions

    if topic_selection == "Math":
        myMathTopic = MathTopic("Math")
        math_subtopics = ["Addition", "Subtraction", "Multiplication", "Division", "Main Menu"]
        continue_math_topic = True

        while continue_math_topic:
            math_selection = get_selection(math_subtopics)
            subject = math_subtopics[int(math_selection) - 1]
            if subject == "Main Menu":
                continue_subject = False
                continue_math_topic = False
            else:
                continue_subject = True

            while continue_subject:

                score = 0
                for i in range(5):
                    if subject == "Addition":
                        score += myMathTopic.make_addition_question()
                    elif subject == "Subtraction":
                        score += myMathTopic.make_subtraction_question()
                    elif subject == "Multiplication":
                        score += myMathTopic.make_multiplication_question()
                    elif subject == "Division":
                        score += myMathTopic.make_division_question()
                print("\nYou got " + str(score) + "/5 right!\n")

                continue_subject = get_continue_choice(subject)
                print()

    elif topic_selection == "Guess the Word":
        myGuessWordTopic = GuessWordTopic("Guess the Word")
        score = 0
        guess_word_subtopics = ["Animals", "Food", "Drinks", "Nature", "Places", "All Groups", "Main Menu"]
        continue_guess_topic = True

        while continue_guess_topic:
            guess_word_selection = get_selection(guess_word_subtopics)
            word_group = guess_word_subtopics[int(guess_word_selection) - 1]
            if word_group == "Main Menu":
                continue_word_group = False
                continue_guess_topic = False
            else:
                continue_word_group = True

            while continue_word_group:
                if word_group == "All Groups":
                    myGuessWordTopic.guess_all_group()
                else:
                    myGuessWordTopic.guess_topic(word_group)

                continue_word_group = get_continue_choice(word_group)
                print()
