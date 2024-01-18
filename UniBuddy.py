#   This is a chatbot named "UniBuddy" designed to make the transition smoother for freshmen.

print("Hello there! My name is UniBuddy, and I will endeavour to facilitate your university experience :)")
print("If you do not mind, I would like to ask you a few questions to get to know you a little.")

#   Gathering user data
name = input("\nWhat is your name? ").capitalize()
country = input(f"\nWelcome to the university {name}. Where do you come from? ").capitalize()
print(f"\nYou are from {country}, that is a beautiful place.\n")

    
while True:                         # Handling age input with error checking
    try:
        age = int(input(f"How old are you, {name}? "))
        break
    except ValueError:
        print("Please enter a valid age.")

# Providing personalized messages based on age
if age < 18:
    print("\nWow! You must be a genius to start university so young! \nThere are different specific events all week for freshmen you might be interested in participating.")
elif 18 <= age < 35:
    print(f"\nExciting times ahead of you, {name}! Check out the freshman-specific events happening this week.")
elif 35 <= age <= 50:
    print("\nIt's never too late to educate oneself and expand your education. \nThere are various activities for students of all ages to enjoy here.")
else:
    print(f"\n{age} is a fun age to start university at!\n")


# Gathering favorite colour
favorite_colour = input("\nWhat's your favorite colour? ").lower()

# Providing personalised society or club suggestions based on favorite colour
if favorite_colour == "blue":
    print("\nYou might enjoy joining the Esports Society on campus. They welcome all competitive gamers whether they prefer watching or participating.")
elif favorite_colour == "red":
    print("\nMaybe you might enjoy joining the Red American Football Club.")
elif favorite_colour == "green":
    print("\nYou might enjoy joining the Young Greens Club.")
elif favorite_colour == "yellow":
    print("\nYou might enjoy joining the Anime and Manga Society.")
else:
    print("That's unique. Feel free to explore the various clubs and activities on the campus!")

print("\nThank you for answering my question. If you have questions, you can ask me and I will do my best to answer them.\n When you are done asking your questions, you can just type 'exit' to stop our interaction.")

# Storing all questions and answers in variables
all_questions = ["what can I do to connect and make friends with other students?", 
                "Who can help me with my curriculum form?", 
                "I do not know if university is for me. What should I do?",
                "Where can I find out more about student accommodation?", 
                "What clubs does the university offer?",
                "How can I get involved in extracurricular activities?",
                "What resources are available for academic support?",
                "Where can I find information about internships and job opportunities?",
                "How do I navigate the campus and find my classes?",
                "Are there any student discounts available in the area?"]

all_answers = ["Making friends at uni can take time, but you should maybe start by looking into societies, groups, or activities that interest you.\n\n", 
                "You can speak to your course advisor or an Orientation Leader.\n\n", 
                "Finding the 'something' that can motivate you. Break up your year into periods of study with short and long-term goals for your course and do not forget to factor in time to relax and enjoy yourself.\n\n",
                "The Students' Representative Council can help you with that.\n\n", 
                "The university offers a wide range of clubs.\n\n",
                "To get involved in extracurricular activities, explore the Student Union and various club fairs on campus. You can also check online platforms for upcoming events.\n\n",
                "For academic support, visit the Learning Resource Center or connect with tutors and study groups. Your professors and academic advisors are also valuable resources.\n\n",
                "To explore internships and job opportunities, visit the Career Services office. They can assist you with resume building, interview skills, and connecting with potential employers.\n\n",
                "Navigate the campus by attending orientation events, using campus maps, and reaching out to upperclassmen. Don't hesitate to ask for directions if needed!\n\n",
                "Check out local businesses and establishments for student discounts. Your university ID may also grant you discounts at certain places.\n\n"]

# Prompting user for a question 
user_input = input("\nWas there a question you wanted to ask me?\n").strip("?").strip().lower()
if user_input == "yes":
    print(f"\n Great! Feel free to ask any question you have, {name}. However, here are some questions frequently asked:\n")   

else:
    user_input == "exit"
    print(f"It was nice chatting with you! Good luck with your uni journey {name}!")

while True:
    # printing out all the questions for the user to choose from
    for i, question in enumerate(all_questions, start=1):
        print(f"{i}. {question}")

    # prompting user for a question 
    user_input = input("\nDo you have a specific question you want to ask me? (Enter the question number or type 'exit' to end)\n").strip("?").strip().lower()

    if user_input == "exit":
        print(f"It was nice chatting with you! Good luck with your uni journey, {name}!")
        break       #   exit the loop and the interaction if the user type 'exit' 

    else:
        try:
            question_number = int(user_input)
            if 1 <= question_number <= len(all_questions):            # if the user enters a valid question number, provide the answer
                selected_question = all_questions[question_number - 1]
                print(f"You've selected: {selected_question}")
                print(f"Answer: {all_answers[question_number - 1]}")
            else:
                # if the entered question number is not valid, prompt the user to enter a valid one
                print("Invalid question number. Please enter a number within the range or type 'exit' to end.")
        except ValueError:
            # if the entered input is not a valid number, prompt the user to enter a valid question number
            print("Invalid input. Please enter a valid question number or type 'exit' to end.")
