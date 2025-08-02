import random

class TikTakToe:
    """
        Tiktaktoe game class
    """
    def __init__(self):
            self.board = [' '] * 10
            self.player_choice = None
            self.computer_choice = None
            self.current_turn = None
            
    def show_board(self):
        print('\n')
        print(f'{self.board[1]} | {self.board[2]} | {self.board[3]}')
        print('---------')
        print(f'{self.board[4]} | {self.board[5]} | {self.board[6]}')
        print('---------')
        print(f'{self.board[7]} | {self.board[8]} | {self.board[9]}')
        print('\n')
        
    def assign_players(self):
        """
            assign players and their markers
        """
        self.player_choice = self.get_player_choice()
        self.computer_choice = 'O' if self.player_choice == 'X' else 'X'
        if random.randint(0, 1) == 0:
            print("Player starts first")
            self.current_turn = 'player'
        else:
            print('Computer starts first')
            self.current_turn = 'computer'

    def get_player_choice(self):
        choice = input("Choose your marker ('X' or 'O'): ").upper()
        while choice not in ['X', 'O']:
            choice = input("Invalid choice. Please choose 'X' or 'O': ").upper()
        self.player_choice = choice
        return self.player_choice

    def has_player_won(self):
        win_combination = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                        (1, 4, 7), (2, 5, 8), (3, 6, 9),
                        (1, 5, 9), (3, 5, 7)]
        for combination in win_combination :
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == self.player_choice:
                print('Congrats you won')
                return 'player'
            elif self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == self.computer_choice:
                print('Computer won')
                return 'computer'
        return None 
    
    def swap_player_turn(self):
        if self.current_turn == 'player':
            self.current_turn = 'computer'
        else:
            self.current_turn = 'player'
        print(f"Current turn: {self.current_turn}")
        
    # def fix_spot(self, cell, marker=None):
    #     if marker is None:
    #         marker = self.player_choice
    #     if self.board[cell] == ' ':
    #         self.board[cell] = marker
    #         return True
    #     else:
    #         print("Spot already taken. Choose another spot.")
    #         return False
    def fix_spot(self, cell, marker):
        if self.board[cell] == ' ':
            self.board[cell] = marker
            return True
        return False
    def player_move(self):
        while True:
            try:
                position = int(input("Choose your position (1-9): "))
                if position not in range(1,10):
                    print("Position must be between 1 and 9.")
                    continue
                if self.fix_spot(position):
                    break
            except ValueError:
                print("Please enter a valid number.")
                
    def computer_move(self):
        available = [i for i in range(1, 10) if self.board[i] == ' ']
        position = random.choice(available)
        print(f"Computer chooses position {position}")
        self.fix_spot(position, self.computer_choice)

    def swap_player_turn(self):
        self.current_turn = 'computer' if self.current_turn == 'player' else 'player'

    def is_board_full(self):
        return ' ' not in self.board[1:]        

    def play_game(self):
        self.assign_players()
        self.show_board()

        while True:
            if self.current_turn == 'player':
                self.player_move()
            else:
                self.computer_move()

            self.show_board()

            winner = self.has_player_won()
            if winner:
                break

            if self.is_board_full():
                print("It's a tie!")
                break

            self.swap_player_turn()

if __name__ == "__main__":
    game = TikTakToe()
    game.play_game()
    print("Game Over")

