import random
from colorama import init, Fore, Style

# Initialize colorama for colored text
init(autoreset=True)

# List of good fortunes
good_fortunes = [
    "Yes, definitely!",
    "It is certain.",
    "You can count on it.",
    "Without a doubt!",
    "Everything points to yes."
]

# List of bad fortunes
bad_fortunes = [
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Better not tell you now."
]

def magic_8_ball():
    try:
        # Get the user's question
        question = input("Ask the Magic 8 Ball a question: ")

        # Check if the question ends with a question mark
        if not question.endswith('?'):
            raise ValueError("Your question must end with a '?'")
        
        # Generate a random number
        random_number = random.randint(1, 100)

        # Decide if it's a good or bad fortune based on odd/even
        if random_number % 2 == 0:
            # Even number, good fortune
            fortune = random.choice(good_fortunes)
            print(Fore.GREEN + fortune)
        else:
            # Odd number, bad fortune
            fortune = random.choice(bad_fortunes)
            print(Fore.RED + fortune)

    except ValueError as e:
        # Handle the exception and ask the user to provide a proper question
        print(Fore.YELLOW + str(e))

# Run the magic 8 ball function
magic_8_ball()