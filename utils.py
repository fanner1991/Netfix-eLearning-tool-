from datetime import datetime
import time
import hashlib
import random
import json





# Function to handle social_engineering attacks
def handle_social_engin_attack():
    score = 0
    target = input ("\nYou arrived at the R block. Someone has approached to you asking your university email to add you in the University gamers club.\na: Proceed('provide Email address')\nb: Reject('no interested')\n")
    print("select one of the options\n")
    if target == "a":
        print("\nOps! Your University email account password has been changed ")
        looser = input("You were a victim of a social engineering attack, type 'yes' to see important information about social engineering attacks or 'no' to play another game  ")
        if looser == "yes":
            print("\nPlease click in the link below and read it carefully\n")
            print("https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10140957")
            time.sleep(5)
            read_inf =input("\nDiscuss the significance of social engineering attacks and explain the importance of being aware of them: \n")
            score =+1
            save_answers_to_file("Handle_Social_Engineering Attack", score)
            save_answers_to_file("Handle Social Enginering Attacks", read_inf )
            print("\ngoing back to main menu...")
            time.sleep(5)
        else:
            print("\nIt is important that you as cyber security student read and be aware of the types of attacks")
            save_score_to_file("Handle Social Engineering Attack", "NO COMPLETED") 
    elif target == "b":
        print("Good chooice!\nyou should never give out your email address or any other personal information to someone you don't know or trust, you could be victim of engineering attacks")
        score =+ 1
        save_answers_to_file("handle_social_engineering attack", score)
        time.sleep(5)
        print("\nEvent though you did the right choice, we recommend to click in the link below and read it carefully before start another game\n")
        print("https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10140957")
        print("\ngoing back to main menu...")
        time.sleep(5)
    else:
        print("invalid choice")
        handle_social_engin_attack()


# Simulate analyzing network traffic for malware
def malware():
    print("\nYou are in the library, but yon cannot entry now as a malware detection scan is in progress ")
    print("Scanning...")
    time.sleep(5)
    malware_detected = simulate_malware_detection()

    if malware_detected:
        print("\nAlert: Malware detected in the network traffic!")
        action = input("\nYou must take immediate action to prevent the malware from spreading. What do you suggest:\n")
        save_answers_to_file("Malware", action)
    else:
        print("No malware detected in the network traffic. The network is secure.")

        

# Function to simulate detecting malware in network traffic
def simulate_malware_detection():
    # Simulate random detection of malware
    return random.choice([True, False])


def ask_question(question, options, correct_answer, time_limit):
    print(question)
    if options:  # If there are options, print them
        for option in options:
            print(option)

    start_time = time.time()
    user_input = input("Enter your answer: ").strip().lower()
    end_time = time.time()

    elapsed_time = end_time - start_time
    if elapsed_time > time_limit:
        print("Time's up!")
        return False, elapsed_time
    
    # Convert correct_answer to string if it's boolean
    correct_answer_str = str(correct_answer).lower() if isinstance(correct_answer, bool) else correct_answer.lower()
    
    #compare answers correctly based on the game type
    is_correct = (user_input == correct_answer_str)
    return is_correct, elapsed_time


def play_game(game_type, questions, time_limit):
    score = 0
    total_time_taken = 0
    start_time = time.time()

    for q in questions:
        is_correct, elapsed_time = ask_question(q["question"], q.get("options"), q["answer"], time_limit)
        total_time_taken += elapsed_time
        if is_correct:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    total_quiz_time = time.time() - start_time
    print(f"Total time taken: {total_quiz_time:.2f} seconds")
    print(f"Your final score is {score} out of {len(questions)}.")
    badge = calculate_badge(score, len(questions), total_quiz_time, time_limit)
    print(f"Congratulations! You've earned the {badge} badge.")
    save_score_to_file(game_type, score, len(questions), badge)


def calculate_badge(score, total, total_time_taken, time_limit):
    if score == total:
        return "Superstar"
    elif score > total * 0.75:
        return "Adventurer"
    else:
        return "Explorer"

def save_score_to_file(game_type, score, total_questions, badge):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    encrypted_score = hashlib.sha256(str(score).encode()).hexdigest()

    with open("scores.txt", "a") as file:
        file.write(f"Game Type: {game_type}, Score: {score}, Out of {total_questions}, Badge: {badge}, Date and Time: {date_time}\n")   


def save_answers_to_file(game_type, answer):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("scores.txt", "a") as file:
        file.write(f"Game Type: {game_type}, Answer: {answer}, Date and Time: {date_time}\n")   



