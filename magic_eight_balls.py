# The Magic 8 Ball Program!

# Create two lists – one of “good” results and one of “bad” results.
# Allow your user to input a question.
# After they ask this question, generate a random number.
# If the number is odd, your user gets a bad fortune.
# If the number is even, they get a good fortune.
# Use Colorama to display bad fortunes in red text, and good fortunes in green text

###########################################################################################################################################################################################
# The code functioned upon running, with evidence of error handling. Efficient choices were made regarding data structures, control flow, and input.
###########################################################################################################################################################################################
# There is evidence of planning. The final product matches the plan – or there are clear comments / justifications as to why the plan had to be changed.
###########################################################################################################################################################################################
# The task was distributed fairly, with all team members providing equal effort. There is evidence of pair-programming, collaborative working, and support. The code has been made cohesive and consistent throughout.
###########################################################################################################################################################################################
# The code is complete. Areas which required research or support from the instructor have been labelled. Evidence of testing is present – or was demonstrated to the instructor in session.
###########################################################################################################################################################################################
# I can communicate effectively in a variety of situations to both a technical and non-technical audience
###########################################################################################################################################################################################
# Code comments are clear and contextual, in suitable places within the code. Any planning documents are good with sufficient detail. Variables and functions are well-named following the correct naming conventions.
###########################################################################################################################################################################################
# All aspects of the brief have been achieved accurately to produce a fully functioning program.
###########################################################################################################################################################################################

import random, colorama 

from colorama import Fore, Style, Back

# Created two lists – one of “good” results and one of “bad” results. 
# Fereshta Sarwarzada
list_of_good_results = [
        "It is decidedly so",
        "Without a doubt", 
        "Yes definitely", 
        "You may rely on it"]

list_of_bad_results = [
        "My reply is no", 
        "My sources say no", 
        "Outlook not so good", 
        "Very doubtful"]

# Function to ask and test the users question
# def ask_the_question():
#     question_asked = input("\nWhat is your greatest desire? ")
#     try:
#         assert question_asked.endswith("?")
#         return question_asked
#     except:
#         print("\nPlease use a question mark, or type 'Quit' to leave")

# Asking the user to enter their question.
users_question = input("\nWhat is your greatest desire? ")

while (users_question != "Quit"):
    try:
        assert users_question.endswith("?")

    # Generating a random number.
        random_number = random.randint(1,9)
        # print(random_number) # testing

        # If the number is even, they get a good fortune.
        # Using Colorama to display bad fortunes in red text, and good fortunes in green text
        #Laura Russell
        if (random_number % 2) == 0: 
            # Using a random method to pick a random fortune from the good list and print it out.
            print (f"{Fore.GREEN}{random.choice(list_of_good_results)} \n")
            print(Style.RESET_ALL)
            users_question = input("\nWhat is your greatest desire? ")

        # If the number is odd, your user gets a bad fortune.
        else: 
            # Using a random method to pick a random fortune from the bad list and print it out.
            print (f"{Fore.RED}{random.choice(list_of_bad_results)} \n")
            print(Style.RESET_ALL)
            users_question = input("\nWhat is your greatest desire? ")


    except:
        print("\nPlease use a question mark, or type 'Quit' to leave")
        users_question = input("\nWhat is your greatest desire? ")


