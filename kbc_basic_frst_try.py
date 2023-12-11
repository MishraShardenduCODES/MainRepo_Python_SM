questions = [
    ["What is the capital city of France?", "a) London", "b) Paris", "c) Berlin", "d) Rome"],
    ['Which planet is known as the "Red Planet"?', "a) Venus", "b) Jupiter", "c) Mars", "d) Mercury"],
    ["Who painted the Mona Lisa?", "a) Michelangelo", "b) Leonardo da Vinci", "c) Vincent van Gogh", "d) Pablo Picasso"],
    ["What is the largest mammal in the world?", "a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Hippopotamus"],
    ['Which country is known as the "Land of the Rising Sun"?', "a) China", "b) Japan", "c) South Korea", "d) Thailand"],
    ["What is the chemical symbol for gold?", "a) Au", "b) Ag", "c) Pt", "d) Cu"],
    ['Who wrote the play "Romeo and Juliet"?', "a) William Shakespeare", "b) Charles Dickens", "c) Jane Austen", "d) Mark Twain"],
    ["What is the tallest mountain in the world?", "a) Mount Kilimanjaro", "b) Mount Everest", "c) Mount McKinley", "d) Mount Fuji"],
    ["What is the largest ocean in the world?", "a) Atlantic Ocean", "b) Indian Ocean", "c) Pacific Ocean", "d) Arctic Ocean"],
    ["Which of these is a programming language?", "a) HTML", "b) JPEG", "c) PDF", "d) CSS"]
]

answers = [
    "b) Paris",
    "c) Mars",
    "b) Leonardo da Vinci",
    "b) Blue Whale",
    "b) Japan",
    "a) Au",
    "a) William Shakespeare",
    "b) Mount Everest",
    "c) Pacific Ocean",
    "a) HTML"
]

hints = [
    "The city is known for the Eiffel Tower.",
    "It's the fourth planet from the sun.",
    "The artist's name starts with 'Leonardo'.",
    "This mammal inhabits the ocean and is the largest animal.",
    "This country is famous for cherry blossoms.",
    "Its symbol is derived from the Latin word 'aurum'.",
    "The playwright is known for his works in English literature.",
    "It's the highest peak in the Himalayas.",
    "This ocean is the largest and deepest.",
    "It's a markup language used for creating web pages."
]

hnt = 4
total_winnings = 0
question_number = 1

while question_number <= len(questions):
    question = questions[question_number - 1]
    print(f"\nQuestion {question_number}: {question[0]}")
    print('\n'.join(question[1:]))
    print("You have ", hnt, " lifelines left !!")    
    if hnt != 0:
        hnt_ln = input("Press Y for lifeline N is you dont want to use lifeline: ")
        if hnt_ln.lower() == 'y':
            print(hints[question_number - 1])
            hnt -= 1

    user_answer = input("Choose the correct option: ")

    if user_answer.lower() == answers[question_number - 1].lower():
        total_winnings += 50 * question_number
        print(f"That's the correct answer! You have won {total_winnings} Rupees")
        
        if question_number % 2 == 0:
            print(f"You can choose to leave the game with {total_winnings} Rupees")
            decision = input("Write 'Yes' to continue and 'No' to stop: ")
            if decision.lower() != 'yes':
                break
        if question_number %5 == 0:
            print(f"You can exit with {total_winnings} Rupee ")
            ex = str(input("Y for exit N to continue"))
            if( ex.lower == 'y' ):
                print(f"You won {total_winnings}, Byeee !!")
    else:
        print("It's the wrong answer. You lost!")
        break
    
    question_number += 1
