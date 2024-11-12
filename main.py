import hashlib
import random
import time
from datetime import datetime
from tf_questions import tf_questions
from quiz_questions import quiz_questions  
from router_questions import router_questions
from securing_network_questions import se_net_questions
from monitoring_managing_devices_questions import mon_devices_questions
from ACLs_firewall_questions import firewall_questions
from intrusion_prevention_questions import int_prevention_questions
from layer2_endpoint_security_questions import lay2_endpoint_questions
from cryptography_questions import crypt_questions
from VPNs_questions import vpn_questions
from ASA_questions import asa_questions
from utils import handle_social_engin_attack
from utils import save_answers_to_file
from utils import play_game
from utils import malware


def play_quiz_game():
    play_game("Quiz", quiz_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", quiz_questions, 60)

def play_true_false_game():
    play_game("True/False", tf_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("True/False", tf_questions, 60)

def play_router_configuration_game():
    play_game("Router Configuration", router_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
         play_game("Router Configuration", router_questions, 60)

def play_securing_networks():
    play_game("Modules 1 – 4: Securing Networks", se_net_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", se_net_questions, 60)

def play_monitoring_managing_devices():
    play_game("Modules 5 - 7: Monitoring and Managing Devices", mon_devices_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", mon_devices_questions, 60)

def play_ACLs_firewalls():
    play_game("Modules 8 - 10: ACLs and Firewalls", firewall_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", firewall_questions, 60)

def play_intrusion_prevention():
    play_game("Modules 11 - 12: Intrusion Prevention", int_prevention_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", int_prevention_questions, 60)


def play_layer2_endpoint_security():
    play_game("Modules 13 - 14: Layer 2 and Endpoint Security", lay2_endpoint_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", lay2_endpoint_questions, 60)


def play_cryptography():
    play_game("Modules 15 - 17: Cryptography", crypt_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", crypt_questions, 60)

def play_VPNs():
    play_game("Modules 18  19: VPNs", vpn_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", vpn_questions, 60)

def play_ASA():
    play_game("Modules 20 – 22: ASA", asa_questions, 60)
    action = input("Would you like to play again or go to the main menu? (play/main): ").lower().strip()
    if action == "main":
        main()
    else:
        play_game("Quiz", asa_questions, 60)



def play_story_game():
    print("\nWelcome to the Netfix Story Game!")
    answer = input("Type play to start now or quit to main menu? (play/quit): ").lower().strip()
    
    if answer == "play":
        print("\nYou are a new Computer Science for Cyber Security student, arriving at Brookes University Wheatley campus.")
        print("")
        direction = input("We highly recommend exploring the right 'easy category' direction to warm up, once you have completed it and practice with the quiz and true/false question game, explore left 'intermediate category'. right/left/down: ").lower().strip()

        if direction == "right":
            print("")
            block_choice = input("\nMost of the blocks are located in this direction. Which block would you like to visit first? (D/PG/R/C): ").upper().strip()

            if block_choice == "PG":
                print("Entering block PG...")
                time.sleep(3)
                encryption = input ("You arrived at the PG block. While exploring, can you tell me or how would you define Encryption and which was the first encryption method used? ")
                save_answers_to_file("PG block", encryption )
                read_choice = input("\nWe have recorded your answer in a file, would you like to watch a video related to cryptography, it may help to improve your knowledge and future answers. (yes/no) " )
                if read_choice ==  "yes":
                    print("\nclick this link: https://www.youtube.com/watch?v=9pp9YpginNg")
                    watched = input("Please type 'done' once you have finished watching the video: ").lower().strip()
                    if watched == "done":
                        pass
               
                else:
                    print("\nit is an interesting video, you can watch it another time")
                    time.sleep (3)
        
                print("\nHash functions like SHA-256 are designed to take an input and produce a fixed-size string of bytes that appears random and is not meant to be inverted or decrypted. We will employ it in this activity for demostration purposes")
                encryption_attempt = input("type the same answer you provided to be encrypted: ").lower().strip()
                encrypt_choice = input("Now type encryption: ")
                if encrypt_choice == "encryption":
                    encryption_attempt = hashlib.sha256
                    print("your message has been encrypted, open the file and you'll see both answer 'unencrypted' and 'encrypted'.")
                    Add_info =input("\nCan you provided some information that you consider valuable from the Encryption video: ")
                    save_answers_to_file("PG block", Add_info)
                    time.sleep(3)
                    print("We finish exploring this block, lets go back to explore the remaining blocks\nExiting...")
                    time.sleep(3)
                    main()
                else:
                    print("We finish exploring this block, lets go back to explore the remaining blocks\nExiting...")
                    time.sleep(3)
                    main()
            

            elif block_choice == "R":
                print("Entering block R...")
                time.sleep(3)
                handle_social_engin_attack() 
                main()
            elif block_choice == "D":
                print("Entering block D...")
                time.sleep(3)
                print("\nYou arrived at the D block. Here, you need to do some basic configurations on Router1.")
                print("")
                play_router_configuration_game()
                main()

            elif block_choice == "C":
                print("Entering block C...")
                time.sleep(3)
                print("\nYou arrived at the C block, before we start it is important to highlight that this block is empty, it is designed to implement optional games. Therefore, we strongly recommend you to explore first to be familiar with the game and Python programming language.")
                Desgn_attemp = input("Do you want to return to main menu (yes/no)\n ")
                if Desgn_attemp == "yes":
                    main()
                else:
                    print("if you selected 'no', it means that you ready to start with your implementation.\nFirstly, you need to follow the steps.\n1. create backup files for main.py and utils.py as you will have to modify them.")
                    new_game =input("secondly, Provide comprehensive details about your new proposal and design such as name, logic, purpose: \n")
                    save_answers_to_file("Block C new Proposal: ", new_game)
                    print("saving...")
                    time.sleep(3)
                    print("it is time to start with your implementation, good luck!")
                    print("exiting...")
                    time.sleep(5)
                    exit()
            
            else:
                print("invalid choice")
            
        
        elif direction == "left":
            print("\nIf you are here, congratulations, you have achieved the time and score desired in the previous activities")
            print("Loading...")
            time.sleep(5)
            action = input("\nBefore we start, see the modules listed, pick one and select the option: \n"
            "a. Modules 1 - 4: Securing Networks\n"
            "b. Modules 5 - 7: Monitoring and Managing Devices\n"
            "c. Modules 8 - 10: ACLs and Firewalls\n"
            "d. Modules 11 - 12: Intrusion Prevention\n"
            "e. Modules 13 - 14: Layer 2 and Endpoint Security\n"
            "f. Modules 15 - 17: Cryptography\n"
            "g. Modules 18 - 19: VPNs\n"
            "h. Modules 20 - 22: ASA\n")
         
           
            if action == "a":
                print("Starting Module...\n")
                time.sleep(5)
                play_securing_networks()
            
         
            elif action == "b":
                print("Starting Module...")
                time.sleep(5)
                play_monitoring_managing_devices()
            
    
            elif action == "c":
                print("Starting Module...")
                time.sleep(5)
                play_ACLs_firewalls()
            
            elif action == "d":
                print("Starting Module...")
                time.sleep(5)
                play_intrusion_prevention()
            
            elif action == "e":
                print("Starting Module...")
                time.sleep(5)
                play_layer2_endpoint_security()

            elif action == "f":
                print("Starting Module...")
                time.sleep(5)
                play_cryptography()
            
            elif action == "g":
                print("Starting Module...")
                time.sleep(5)
                play_VPNs()

            elif action == "h":
                print("Starting Module...")
                time.sleep(5)
                play_ASA()

            else:
                print("invalid input")
                main()

        elif direction == "down":
            malware()
            print("Exiting...")
            time.sleep(5)
            main()


        else:
            print("Invalid input. Please enter a valid direction.")
            play_story_game()

    else:
        print("\nSelect another game option")
        main()

def main():
    print("\nWelcome to Netfix! Please choose one of the following options:")
    print("1: Quiz Game")
    print("2: True and False Game")
    print("3: Story Game")
    print("4: Exit")

    choice = input("\nEnter the number corresponding to your choice: ")
    if choice == "1":
        print("\nStarting Quiz Game...")
        print("")
        time.sleep (3)
        play_quiz_game() # Call function to start quiz game
    elif choice == "2":
        print("\nStarting True and False Game...")
        print("")
        time.sleep (3)
        play_true_false_game ()# Call function to start true and false game
    elif choice == "3":
        print("\nStarting Story Game...")
        print("")
        time.sleep (3)
        play_story_game() #call the function to start story game
    elif choice == "4":
        print("\nThank you for using Netfix, see you soon\n") 
        exit()
    else:
        print("Invalid choice. Please select a valid option.")
        main()
main ()
