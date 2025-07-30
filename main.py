import os

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(self):
      self.name = ""
      self.sympol = ""

    def chooose_name(self):
      while True:
        name = input("Enter your name(letters only): ")
        if name.isalpha():
          self.name = name
          break
        print("Invalid name. Please enter letters only.")

    def choose_symbol(self):
      while True:
        symbol = input(f"{self.name}, choose your symbol (a single letter): ")
        if symbol.isalpha() and len(symbol) == 1:
          self.sympol = symbol.upper()
          break
        print("Invalid symbol. Please enter a single letter.")

class Menu:
  def validate_choice(self):
    while True:
      choice = int(input("Enter your choice (1, 2): "))
      if choice != 1 and choice != 2:
        print("Invalid choice. Please enter 1 or 2.")
      else:
        self.choice = choice
        break
    return self.choice
    
  def display_menu(self):
    print("Welcome to Tic Tac Toe!")
    print("1. Start Game")
    print("2. Quit")

    return self.validate_choice()
    
  def display_endgame_menu(self):
    menu_text = """
    Game Over!
    1. Restart Game
    2. Quit
    """
    print(menu_text)
    return self.validate_choice()

class Board:
  def __init__(self):
    self.board = [str(i) for i in range(1, 10)]

  def display_board(self):
    for i in range(0, 9, 3):
      print("|".join(self.board[i:i+3]))
      if i < 6:
        print("-" * 5)

  def is_valid_move(self, choise):
    return self.board[choise-1].isdigit()

  def update_board(self, choise, symbol):
    if self.is_valid_move(choise):
      self.board[choise-1] = symbol
      return True
    return False

  def reset_board(self):
    self.board = [str(i) for i in range(1, 10)]

class Game:
  def __init__(self):
    self.players = [Player(), Player()]
    self.board = Board()
    self.menu = Menu()
    self.current_player_idx = 0

  def setup_player(self):
    for number, player in enumerate(self.players, start=1):
      print(f"Player {number} enter your details")
      player.chooose_name()
      player.choose_symbol()
      clear_screen()

  def switch_player(self):
    self.current_player_idx = 1 - self.current_player_idx
    
  def play_turn(self):
    player = self.players[self.current_player_idx]
    self.board.display_board()
    print(f"{player.name}'s turn ({player.sympol})")
    while True:
      try:
        cell_choise = int(input("Choose a cell (1-9): "))
        if 1 <= cell_choise <= 9 and self.board.update_board(cell_choise, player.sympol):
          clear_screen()
          break
        else:
          print("Invalid move. Try again.")
      except ValueError:
        print("Invalid input. Enter a number between 1 and 9.")
    self.switch_player()
  
  def check_winner(self):
    win_combinations = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
      [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
      [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
      if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
        return True
    return False

  def check_draw(self):
    return all(not cell.isdigit() for cell in self.board.board)

  def restart_game(self):
    self.board.reset_board()
    self.current_player_idx = 0
    self.play_game()

  def play_game(self):
    while True:
      self.play_turn()
      if self.check_winner() or self.check_draw():
        if self.check_winner() is True:
          self.board.display_board()
          print(f"Congratulations {self.players[1-self.current_player_idx].name} wins!")
        else:
          self.board.display_board()
          print("Ops! It's a draw!")
        choice = str(self.menu.display_endgame_menu())
        if choice == "1":
          clear_screen()
          self.restart_game()
        else:
          self.quit_game()
          break

  def quit_game(self):
    print("Thank you for playing! Goodbye!")
    exit()
  
  def start_game(self):
    choise = self.menu.display_menu()
    if choise == 1:
      self.setup_player()
      self.play_game()
    else:
      self.quit_game()


game = Game()
game.start_game()