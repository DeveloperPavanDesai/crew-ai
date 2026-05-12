from crews.game_studio_crew import game_studio_crew

def run():
    result = game_studio_crew.kickoff()

    print("\n")
    print("=" * 50)
    print("FINAL GAME DESIGN DOCUMENT")
    print("=" * 50)
    print(result)

if __name__ == "__main__":
    run()