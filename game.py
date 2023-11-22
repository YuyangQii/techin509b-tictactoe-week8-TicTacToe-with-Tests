import os
import logging
from board import Board
from player import Player

class Game:
    def __init__(self, single_player_mode):
        self.board = Board()
        self.players = [Player('X')]
        if single_player_mode:
            self.players.append(Player('O', is_bot=True))
        else:
            self.players.append(Player('O'))
        self.current_player_index = 0

    def start(self):
        self.setup_logging()
        logging.info("Game started")
        while self.board.get_winner() is None and not self.board.is_full():
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            row, col = current_player.make_move(self.board.board)
            if self.board.make_move(row, col, current_player.symbol):
                self.switch_player()
            else:
                logging.warning(f"Invalid move by {current_player.symbol}")
        self.end_game()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def end_game(self):
        self.board.print_board()
        winner = self.board.get_winner()
        if winner:
            print(f"\n{winner} wins!")
        else:
            print("\nThe game is a draw.")
    
    def take_turn(self):
        print(f"\n{self.current_player}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        return self.board.make_move(row, col, self.current_player)
    
    @staticmethod
    def setup_logging():
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logging.basicConfig(
            filename=os.path.join(log_directory, 'game.log'),
            level=logging.INFO,
            format='%(asctime)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


if __name__ == '__main__':
    single_player_mode = input("Single player mode? (y/n): ").lower() == 'y'
    game = Game(single_player_mode)
    game.start()