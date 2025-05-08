# Pokemon card binder management in Python
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
            score=len(self.cards)/ 1025 *int(100)
            print(f"you caught: {score}% ")

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

