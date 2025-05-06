# let's play some game 
import random
class GameCenter:
    def __init__(self):
        self.score = 0
        self.player_score = 0
        self.correct = 0

    def menu(self):
        print("[1]. Guess number")
        print("[2]. Rock paper scissors")
        print("[3]. Trivia pursuit quiz game")
        print("[4]. Pokemon card Binder Manager")
        print("[5]. Overall scoring system")
        print("[0]. Exit the program")

    def guess_number(self):
        b = random.randint(1, 10)
        attempt = 0
        while True:
            c = int(input("Enter the guess number between (1-10): "))
            attempt += 1
            score = 11 - attempt
            if c == b:
                print(f"Congratulations! You got it right in {attempt} attempts")
                print(f"Your score: {score}")
                self.score = score
                break
            elif c > b:
                print("Too high, try again")
            elif c < b:
                print("Too low, try again")
            else:
                print("Invalid input")

    def rock_paper_scissors(self):
        choice = ("rock", "paper", "scissors")
        playing = True
        self.player_score = 0
        computer_score = 0

        while playing:
            player = None
            computer = random.choice(choice)
            while player not in choice:
                player = input("Enter your choice: ").lower()

            print(f"Player: {player}")
            print(f"Computer: {computer}")

            if player == computer:
                print("It's a tie!")
            elif (player == "rock" and computer == "scissors") or \
                 (player == "paper" and computer == "rock") or \
                 (player == "scissors" and computer == "paper"):
                print("You won!")
                self.player_score += 1
            else:
                print("You lost!")
                computer_score += 1

            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                playing = False
                print(f"Your score: {self.player_score}, Computer score: {computer_score}")

    def quiz_game(self):
        name = input("Enter your name: ")
        print(f"Welcome to the quiz, {name}")
        print("We have 5 questions. Choose from A, B, C, D.")

        Questions = [
            {"Question_text": "1. What is the past tense of the verb go?",
             "options": ["A) going", "B) went", "C) gone", "D) go"], "correct_answer": "B"},
            {"Question_text": "2. What gas do plants take in from the air for photosynthesis?",
             "options": ["A) oxygen", "B) carbondioxide", "C) nitrogen", "D) hydrogen"], "correct_answer": "B"},
            {"Question_text": "3. 3-1+(3*5)*2",
             "options": ["A) 34", "B) -28", "C) 32", "D) 19"], "correct_answer": "C"},
            {"Question_text": "4. What can we get from the sun?",
             "options": ["A) light", "B) fire", "C) yellow colour", "D) tree"], "correct_answer": "A"},
            {"Question_text": "5. What is the product of 2*2*(-4)?",
             "options": ["A) 16", "B) 8", "C) -8", "D) -16"], "correct_answer": "D"},
        ]

        correct = 0
        incorrect = 0
        correct_ans = []
        wrong_ans = []

        for question in Questions:
            print(question["Question_text"])
            for option in question["options"]:
                print(option)
            yourAns = input("Answer: ").strip().upper()
            question["yourAns"] = yourAns
            print()

        for question in Questions:
            if question["yourAns"] == question["correct_answer"]:
                correct += 1
                correct_ans.append(question)
            else:
                incorrect += 1
                wrong_ans.append(question)

        self.score_percentage = (correct / 5) * 100
        print("Total correct:", correct)
        print("Total incorrect:", incorrect)
        print("Percentage:", self.score_percentage, "%")

        for q in correct_ans:
            print("Correct Question:", q["Question_text"])
        for q in wrong_ans:
            print("Incorrect Question:", q["Question_text"])
            print("Your Answer:", q["yourAns"])
            print("Correct Answer:", q["correct_answer"])

    def overall_score(self):
        overall_score = self.score + self.player_score + self.correct
        print(f"Overall Score: {overall_score}")

    def pokemon_card_binder_manager(self):
        class Pokemon:  
           def __init__(self, pokedex, page, row, column):
               self.pokedex = pokedex
               self.page = page
               self.row = row 
               self.column = column

           def get_position(self):
              return f"Page: {self.page}, Row: {self.row}, Column: {self.column}"
   
        class CardBindingManager:
           def __init__(self):
              self.cards = {}
              self.maximum_pokedex = 1025
              self.cards_per_page = 64
              self.rows = 8
              self.columns = 8
           
           def is_valid(self, pokedex):
              return isinstance(pokedex, int) and 1 <= pokedex <= self.maximum_pokedex
    
           def add_card(self, pokedex):
               if not self.is_valid(pokedex):
                   print("Invalid Pokédex number: Please enter a number between 1 and 1025.")
                   return
               if pokedex in self.cards:
                   print("Card already exists in the binder.")
                   return

               index = pokedex - 1 
               page = index // self.cards_per_page + 1
               index_on_page = index % self.cards_per_page
               row = index_on_page // self.columns + 1
               column = index_on_page % self.columns + 1
        
               card = Pokemon(pokedex, page, row, column)
               self.cards[pokedex] = card
               print(f"Pokémon #{pokedex} added at Page {page}, Row {row}, Column {column}.")

               if len(self.cards) == self.maximum_pokedex:
                  print("You have caught them all!!!")
               else:
                    total_score=len(self.cards)/ 1025 *int(100)
                    print(f"you caught: {total_score}% ")


           def view_position(self, pokedex):
                pokedex = int(pokedex)
                card = self.cards.get(pokedex)
                if card:
                   print(f"Pokémon #{pokedex} is at {card.get_position()}")
                else:
                   print("Pokémon not found in binder.")

           def show_all_cards(self):
                if not self.cards:
                   print("No Pokémon cards in the binder yet.")
                   return
                for number in sorted(self.cards):
                   card = self.cards[number]
                   print(f"#{number}: {card.get_position()}")

           def reset_binder(self):
                confirm = input("Are you sure you want to reset the binder? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.cards.clear()
                    print("Binder has been reset.")
                else:
                    print("Reset cancelled.")
            
        class Binder:
            def __init__(self):
                self.binder = CardBindingManager()
        
            def run(self):
                while True:
                    print("\nWelcome to Pokémon Card Binder Manager")
                    print("1. Add Pokémon Card")
                    print("2. View Card Position")
                    print("3. Show All Cards")
                    print("4. Reset Binder")
                    print("5. Exit")

                    choice = input("Choose an option: ").strip()

                    if choice == "1":
                        number = input("Enter Pokédex number: ").strip()
                        if number.isdigit():
                            self.binder.add_card(int(number))
                            print("Your card has been added to the binder.")
                            print("Try other functions to learn more about your card.")
                        else:
                            print("Invalid input. Please enter a valid number.")
                    
                    elif choice == "2":
                        number = input("Enter Pokédex number: ").strip()
                        if number.isdigit():
                            self.binder.view_position(int(number))
                        else:
                            print("Invalid input. Please enter a valid number.")
                    
                    elif choice == "3":
                        self.binder.show_all_cards()
                
                    elif choice == "4":
                        self.binder.reset_binder()
                
                    elif choice == "5":
                        print("Exiting. Goodbye!")
                        break
                    else:
                        print("Invalid option. Please try again.")


        if __name__ == "__main__":
            binding = Binder()
            binding.run()

    def run(self):
        self.menu()
        while True:
            option = int(input("Choose an option: "))
            if option == 1:
                self.guess_number()
            elif option == 2:
                print("lets play rock paper scissor game")
                self.rock_paper_scissors()
            elif option == 3:
                self.quiz_game()
            elif option == 4:
                self.pokemon_card_binder_manager()
            elif option == 5:
                self.overall_score()
            elif option == 0:
                print("Exiting the program.")
                print("Good bye")
                break
            else:
                print("Invalid choice.")
            self.menu()

# Run the game center
if __name__ == "__main__":
    game = GameCenter()
    game.run()
