# Dictionary of Python concepts
python_dict = {
    "list": "An ordered, mutable collection of items.",
    "tuple": "An ordered, immutable collection of items.",
    "dict": "A collection of key-value pairs.",
    "set": "An unordered collection of unique items.",
    "function": "A block of reusable code defined with def.",
    "class": "A blueprint for creating objects.",
    "keys()": "Returns all dictionary keys as a view object.",
    "values()": "Returns all dictionary values as a view object.",
    "items()": "Returns all dictionary key-value pairs as tuples.",
    "update()": "Adds or updates key-value pairs in a dictionary.",
    "pop()": "Removes a key-value pair by key.",
    "get()": "Safely retrieves a value by key, returns None if not found."
}

# Quiz questions
quiz_questions = [
    ("Which symbol is used to define key-value pairs in a dictionary?", ":"),
    ("What method safely retrieves a value without error if the key doesn't exist?", "get()"),
    ("Which method removes a key-value pair from a dictionary?", "pop()"),
    ("What does my_dict.keys() return?", "dict_keys view object"),
    ("Can lists be dictionary keys?", "No, because they are mutable"),
    ("What does my_dict.items() return?", "dict_items view object (tuples)")
]

def show_menu():
    print("\n=== PYTHON DICTIONARY QUIZ MENU ===")
    print("1. View Dictionary Information")
    print("2. Take Quiz")
    print("3. Add New Term")
    print("4. Exit")

def view_dictionary():
    print("\n--- Dictionary Information ---")
    for key, value in python_dict.items():
        print(f"{key}: {value}")

def take_quiz():
    print("\n--- Quiz Time ---")
    score = 0
    for question, answer in quiz_questions:
        user_answer = input(f"{question}\nYour answer: ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {answer}\n")
    print(f"Your final score: {score}/{len(quiz_questions)}")

def add_term():
    key = input("Enter new Python term: ")
    value = input("Enter its definition: ")
    python_dict[key] = value
    print(f"✅ Term '{key}' added successfully!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        view_dictionary()
    elif choice == "2":
        take_quiz()
    elif choice == "3":
        add_term()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

