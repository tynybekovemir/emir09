import random 
 
class SlotMachine: 
    def __init__(self, name): 
        self.name = name 
        self.user_balance = 100 
        self.game_balance = 0 
 
    def info(self): 
        print("Player Name:", self.name) 
        print("User Balance:", self.user_balance) 
        print("Game Balance:", self.game_balance) 
 
    def balance_up(self, amount): 
        self.user_balance -= amount 
        self.game_balance += amount 
 
    def top_up_balance(self, amount): 
        if amount > 100: 
            print("You can top up up to $100 only.") 
        else: 
            self.balance_up(amount) 
 
    def game(self): 
        secret_number = random.randint(1, 10) 
        attempts = 5 
 
        while attempts > 0: 
            guess = int(input("Enter your guess (1-10): ")) 
            if guess == secret_number: 
                self.game_balance += 50 
                print("Congratulations! You won $50.") 
                return 
            else: 
                self.user_balance -= 10 
                attempts -= 1 
                print("Wrong guess! Try again.") 
 
        print("You lost the game.") 
 
    def conclusion_money(self, amount): 
        if amount < 50: 
            print("You can withdraw a minimum of $50.") 
        else: 
            self.game_balance -= amount 
            self.user_balance += amount 
            print("Successfully withdrawn $", amount) 
 
    def main(self): 
        while True: 
            print("\nSlot Machine Commands:") 
            print("1 - Show player info") 
            print("2 - Top up game balance") 
            print("3 - Play the game") 
            print("4 - Withdraw game balance") 
 
            command = int(input("Enter command number: ")) 
 
            if command == 1: 
                self.info() 
            elif command == 2: 
                amount = int(input("Enter the amount to top up: ")) 
                self.top_up_balance(amount) 
            elif command == 3: 
                self.game() 
            elif command == 4: 
                amount = int(input("Enter the amount to withdraw: ")) 
                self.conclusion_money(amount) 
            else: 
                print("Invalid command. Please try again.") 
 
 
# Создание объекта класса SlotMachine 
player = SlotMachine("John") 
player.main()
