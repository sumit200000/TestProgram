import random

responses = [
    "Yes, definitely.",
    "It is certain.",
    "Without a doubt.",
    "Yes, you may rely on it.",
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
    "Very doubtful."
]

def magic_8ball():
    print("Welcome to the Magic 8-Ball Game!")
    while True:
        question = input("Ask the Magic 8-Ball a question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Thinking...")
            answer = random.choice(responses)
            print(f"The Magic 8-Ball says: {answer}\n")

if __name__ == "__main__":
    magic_8ball()

response_count = {response: 0 for response in responses}

def magic_8ball_with_poll():
    print("Welcome to the Magic 8-Ball Game with Polling!")
    while True:
        question = input("Ask the Magic 8-Ball a question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Thanks for playing! Here are the most common responses:")
            for response, count in response_count.items():
                print(f"{response}: {count} times")
            break
        else:
            print("Thinking...")
            answer = random.choice(responses)
            response_count[answer] += 1
            print(f"The Magic 8-Ball says: {answer}\n")

if __name__ == "__main__":
    magic_8ball_with_poll()
