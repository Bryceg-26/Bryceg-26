import random
import time
print("Welcome to the game, your task is to think of a question... any question.")
print("Your question must be yes or no, and you MUST I say MUST be ready for an answer you may not like... let the game begin")
question = input("Your question is? ")
responses = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "You're cooked my guy"
]
print("thinking...............")
print("elavator music.. doo doo doo doo do do do, do do doo do do! do do do, doo doo doo doo do do do, do do doo do do! do do do")
answer = random.choice(responses)
time.sleep(3)
print("Thanks for playing my game, the magic eight ball has decided")
print(f"Your answer is... {answer}")