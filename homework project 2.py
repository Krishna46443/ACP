#show_processing_animation()
def show_processing_animation():
    print("Spy Bot is working...")
    print("Analysis complete!")

#analyze_sentiment(text)
def analyze_sentiment(text):
    if "happy" in text or "good" in text:
        return "Positive"

    elif "sad" in text or "bad" in text:
        return "Negative"

    else:
        return "Neutral"

#execute_command(command)
def execute_command(command):
    if command == "summary":
        print("Here is your summary")

    elif command == "reset":
        print("Data has been reset")

    elif command == "history":
        print("Here is your history")

    elif command == "help":
        print("Commands are summary, reset, history and help")

    else:
        print("Invalid command")

#get_valid_name()
def get_valid_name():
    name = input("Enter your name: ")

    while not name.isalpha():
        print("Please use letters only.")
        name = input("Enter your name: ")

    return name 
print("hello")
