from persistence_demo.game import Game

def save_game():
    game = Game(5, 1500)
    with open("game_state.json", "w") as file:
        file.write(game.to_json())

    print("Game state saved.")

if __name__ == "__main__":
    save_game()
