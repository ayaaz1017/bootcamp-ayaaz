from persistence_demo.game import Game

def load_game():
    try:
        with open("game_state.json", "r") as file:
            json_data = file.read()
        game = Game.from_json(json_data)
        print(f"Loaded Game - Level: {game.level}, Score: {game.score}")
    except FileNotFoundError:
        print("No saved game state found.")

if __name__ == "__main__":
    load_game()
