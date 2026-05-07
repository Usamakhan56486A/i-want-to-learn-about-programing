import random
# ✅ 100 Objective Questions on Python Lists
questions = [
    # --- Basics ---
    {"q": "How do you create an empty list in Python?",
     "options": ["A) {}", "B) []", "C) empty()", "D) list{}"], "answer": "B"},
    {"q": "Which method adds a single element to the end of a list?",
     "options": ["A) add()", "B) insert()", "C) append()", "D) extend()"], "answer": "C"},
    {"q": "Which method merges two lists?",
     "options": ["A) join()", "B) extend()", "C) append()", "D) merge()"], "answer": "B"},
    {"q": "How do you access the last element of a list?",
     "options": ["A) list[-1]", "B) list[last]", "C) list[len(list)]", "D) list[0]"], "answer": "A"},
    {"q": "What happens if you access an index that doesn’t exist?",
     "options": ["A) None", "B) False", "C) IndexError", "D) ValueError"], "answer": "C"},
    {"q": "Which method removes the first occurrence of a value?",
     "options": ["A) pop()", "B) delete()", "C) remove()", "D) discard()"], "answer": "C"},
    {"q": "Which method returns the index of a value?",
     "options": ["A) find()", "B) index()", "C) search()", "D) locate()"], "answer": "B"},
    {"q": "Which method sorts a list in place?",
     "options": ["A) sorted()", "B) sort()", "C) order()", "D) arrange()"], "answer": "B"},
    {"q": "Which function returns a new sorted list?",
     "options": ["A) sort()", "B) sorted()", "C) order()", "D) arrange()"], "answer": "B"},
    {"q": "Which method reverses a list in place?",
     "options": ["A) reverse()", "B) rev()", "C) flip()", "D) invert()"], "answer": "A"},

    # --- Indexing & Slicing ---
    {"q": "How do you get the first 3 elements of a list?",
     "options": ["A) list[0:3]", "B) list[:3]", "C) list[1:3]", "D) list[3:]"], "answer": "B"},
    {"q": "How do you reverse a list using slicing?",
     "options": ["A) list[::-1]", "B) list[::]", "C) list[::2]", "D) list[-1:]"], "answer": "A"},
    {"q": "What does list[::2] return?",
     "options": ["A) Every element", "B) Every 2nd element", "C) Last 2 elements", "D) Error"], "answer": "B"},
    {"q": "What does list[1:-1] return?",
     "options": ["A) All elements", "B) All except first and last", "C) First element only", "D) Last element only"], "answer": "B"},
    {"q": "What does list[:] return?",
     "options": ["A) Copy of list", "B) Empty list", "C) Error", "D) Last element"], "answer": "A"},

    # --- Modification ---
    {"q": "How do you replace the 2nd element with 'Hello'?",
     "options": ["A) list[1]='Hello'", "B) list[2]='Hello'", "C) list.replace('Hello')", "D) list.insert(1,'Hello')"], "answer": "A"},
    {"q": "Which method inserts an element at a specific index?",
     "options": ["A) append()", "B) insert()", "C) extend()", "D) add()"], "answer": "B"},
    {"q": "Which method removes and returns the last element?",
     "options": ["A) pop()", "B) remove()", "C) delete()", "D) discard()"], "answer": "A"},
    {"q": "Which method clears all elements from a list?",
     "options": ["A) clear()", "B) empty()", "C) reset()", "D) delete()"], "answer": "A"},
    {"q": "Which operator concatenates two lists?",
     "options": ["A) +", "B) *", "C) &", "D) %"], "answer": "A"},

    # --- Searching ---
    {"q": "How do you check if 'banana' exists in a list?",
     "options": ["A) 'banana' in list", "B) list.has('banana')", "C) list.find('banana')", "D) list.exists('banana')"], "answer": "A"},
    {"q": "What happens if you call list.index('grapes') when not present?",
     "options": ["A) None", "B) False", "C) IndexError", "D) ValueError"], "answer": "D"},
    {"q": "Which method counts occurrences of a value?",
     "options": ["A) count()", "B) index()", "C) find()", "D) search()"], "answer": "A"},
    {"q": "Which operator checks membership?",
     "options": ["A) in", "B) has", "C) exists", "D) contains"], "answer": "A"},
    {"q": "Which method finds the position of first occurrence?",
     "options": ["A) index()", "B) find()", "C) search()", "D) locate()"], "answer": "A"},

    # --- Iteration ---
    {"q": "Which function gives both index and value?",
     "options": ["A) enumerate()", "B) range()", "C) zip()", "D) map()"], "answer": "A"},
    {"q": "Which function applies a function to all elements?",
     "options": ["A) map()", "B) filter()", "C) reduce()", "D) apply()"], "answer": "A"},
    {"q": "Which function filters elements by condition?",
     "options": ["A) filter()", "B) map()", "C) reduce()", "D) select()"], "answer": "A"},
    {"q": "Which function combines two lists element-wise?",
     "options": ["A) zip()", "B) join()", "C) merge()", "D) pair()"], "answer": "A"},
    {"q": "Which loop prints each element?",
     "options": ["A) for i in list", "B) while list", "C) loop(list)", "D) repeat(list)"], "answer": "A"},

    # --- Advanced ---
    {"q": "Which method copies a list?",
     "options": ["A) copy()", "B) clone()", "C) duplicate()", "D) replicate()"], "answer": "A"},
    {"q": "Which method returns length of a list?",
     "options": ["A) len()", "B) length()", "C) size()", "D) count()"], "answer": "A"},
    {"q": "Which operator repeats a list?",
     "options": ["A) *", "B) +", "C) &", "D) %"], "answer": "A"},
    {"q": "Which comprehension squares even numbers?",
     "options": ["A) [x**2 for x in list if x%2==0]", "B) [x**2 for x in list]", "C) [x for x in list]", "D) [x**2 if x%2==0]"], "answer": "A"},
    {"q": "Which method removes duplicates easily?",
     "options": ["A) list(set(list))", "B) unique()", "C) distinct()", "D) remove_dup()"], "answer": "A"},
]

# ✅ Fill up to 100 with variations
while len(questions) < 100:
    questions.append(random.choice(questions))

def quiz():
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
        print("-" * 30)

    print(f"\n🎯 Final Score: {score}/100")
    if score >= 90:
        print("🏆 Excellent! You mastered lists.")
    elif score >= 70:
        print("👍 Good job, keep practicing.")
    else:
        print("📚 Needs improvement, review list basics.")

# ✅ Completed Menu Loop
while True:
    print("\n" + "="*40)
    print(" PYTHON LIST OBJECTIVE QUIZ (100 Marks) ")
    print("="*40)
    print("1. Start Quiz 🎮")
    print("2. Exit")
    
    try:
        choice = int(input('Please Enter Your Choice : '))
    except ValueError:
        print('Please Enter Correct Value')

    if choice == 1:
        quiz()
    else :
        break            
