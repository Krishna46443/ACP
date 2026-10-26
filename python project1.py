print("welcome to Enhanced Chatbot")
name = input ("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")
while True:
    mood = input(
        f"\nHi {name}! How are you today? "
        "(good, bad, or neutral): "
        ).lower()
    if mood == "good":
        print("thats good to hear! I'm glad to hear your having a good day.")
    elif mood == "neutral":
        print("i'm sorry you're having a difficult day, i hope things get better")
    elif mood == "neutral":
        print("That's okay! sometimes it's just an ordinary day")
    else:
        print("I didn't recognise that mood, but thanks for telling me!")

    hobby = input(
        f"\n{name}, wat is your favourit hobby or activity? "
    )

    print(f"that actually sounds interesting")

    choise = input(
        "\n Would like to continue chatting? (yes/no):"
    ).lower()
    if choice == "no":
        print(f"\nGoodbye")
        break
    elif choice =="yes":
        print("\nGreat lets keep chatting")

            
    