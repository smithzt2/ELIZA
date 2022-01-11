#!/usr/bin/env python3

###########################################################
###########################################################
#
#
#                       eliza.py
#
#                   Zachary Smith
#                   Spring 2021
#
###########################################################
####################### Purpose ###########################
#
#   This program's purpose is to simulate a Rogerian
#   Pyschotherapist. It will mirror questions back to the
#   user in an attempt to "help" the user with their
#   problem.
#
###########################################################
######################### Use #############################
#
#   Does not take command line arguments.
#   execute in directory:  python3 eliza.py
#
###########################################################
##################### How it works ########################
#
#   main():
#       gets the client's name
#       moves control to conversation()
#
#   conversation():
#       loops until client enters EXIT
#
#       word spots and gives specific replies
#       if no word is spotted,
#           mirrors the phrase back to the user
#
###########################################################
###########################################################
#
#   Possible improvements
#       more word spots with specific responses
#       tailor generated responses to a previous topic
#           (I.E
#               Client-> My girlfriend broke up with me
#               Eliza -> How is your romantic life?
#               Client-> It is not going well...
#               Eliza -> What can you do to improve your lovelife?
#                           etc.
#           )
#       flag responses already used to prevent looping the same things
#
###########################################################
###########################################################
#
#   Example execution
#       ELIZA -> Hello, my name is Eliza. What is your name?
#       CLIENT-> Zach
#       ELIZA -> Hello, Zach. What can I help you with?
#       CLIENT-> I hate my job
#       ELIZA -> Do you like your career?
#       CLIENT-> No
#       ELIZA -> Can you please elaborate on that?
#       CLIENT-> I am stressed all the time
#       ELIZA -> Why are you stressed all the time
#
###########################################################
###########################################################

# re for regular expressions
# random for choosing a random response
import re
import random


def main():
    client = input("[TYPE \"EXIT\" AT ANYTIME TO QUIT]Hello, my name is Eliza. What is your name?")
    if client == "exit":
        print("Goodbye.")
        quit()
    print("Hello, " + client + ". What can I help you with?")

    conversation(client)


def conversation(client):
    # Randomly selected responses
    # hmm = ["I don't quite understand.", "Could you word that differently?", "Why?", "Please rephrase that, " + client + "."]
    bc = ["Are you sure that is why?", "Why do you think that is?", "Is there anything else it could be?"]

    while True:

        sentence = input()
        statement = sentence.lower()

        # Word spots
        #   each case has its own predetermined response

        # CONVERSATION TERMINATION
        if statement == "exit":
            print("I hope I helped. Have a nice day.")
            break
        # Specific class example
        elif re.search(r'^.*?\s?(crave)\s?.*?$', statement):
            print("Why do you think you crave that?")
        # think
        elif re.search(r'^.*?\s?(think)\s?.*?$', statement):
            print("Is there any reason you think that?")
        # feel
        elif re.search(r'^.*?\s?(feel)\s?.*?$', statement):
            print("Why do you feel that way?")
        # pets
        elif re.search(r'^.*?\s?(cat)\s?.*?$', statement) or re.search(r'^.*?\s?(dog)\s?.*?$', statement) or re.search(r'^.*?\s?(bird)\s?.*?$', statement) or re.search(r'^.*?\s?(pet)\s?.*?$', statement) or re.search(r'^.*?\s?(fish)\s?.*?$', statement):
            print("Tell me of your pets.")
        # Father
        elif re.search(r'^.*?\s?(dad)\s?.*?$', statement) or re.search(r'^.*?\s?(father)\s?.*?$', statement):
            print("What do you think about your father?")
        # Mother
        elif re.search(r'^.*?\s?(mom)\s?.*?$', statement) or re.search(r'^.*?\s?(mother)\s?.*?$', statement):
            print("What do you think about your mother?")
        # Seek other immediate help
        elif re.search(r'^.*?\s?(kill)\s?.*?$', statement):
            print("Please contact a medical professional immediately.")
        # Job
        elif re.search(r'^.*?\s?(job)\s?.*?$', statement) or re.search(r'^.*?\s?(job)\s?.*?$', statement):
            print("Do you like your career?")
        # Romantic relationship
        elif re.search(r'^.*?\s?(partner|boyfriend|girlfriend|relationship)\s?.*?$', statement):
            print("How is your romantic life?")
        # Want / Need
        elif re.search(r'^.*?\s?(want|need)\s?.*?$', statement):
            print("Do you think that is important?")
        # Stress
        elif re.search(r'^.*?\s?(stress|stressful|exhausted|tired)\s?.*?$', statement):
            print("Is it important to you to relax?")
        # Fear
        elif re.search(r'^.*?\s?(scare(d)?|fear|frighten(s)?)\s?.*?$', statement):
            print("Why does that frighten you?")
        # Loss / Death
        elif re.search(r'^.*?\s?(lost|death|died|die|dying)\s?.*?$', statement):
            print("Is loss hard on you?")

        # No spotted word found
        else:
            # Attempt to match a response pattern

            # "I am ..." pattern
            if re.search(r'(^i am\s)|(^i\'m\s)', statement):
                if re.search(r'\?', statement):
                    re.sub(r'\.', "?", statement)
                else:
                    statement = statement + "?"

                # Flip pronouns
                statement = re.sub(r'\smy\s', " your ", statement)
                statement = re.sub(r'\smine\s', " yours ", statement)
                print(re.sub(r'^i am\s', "Why are you ", statement))

            # Search for "Because ..."
            elif re.search(r'^because\s', statement):
                print(bc[random.randrange(0, 3, 1)])

            # One word response
            elif re.search(r'\s', statement) is None:
                print("Can you please elaborate on that?")

            # Nothing else fits a response
            else:
                # print(hmm[random.randrange(0, 4, 1)])
                print("Why?")


if __name__ == "__main__":
    main()

