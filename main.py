from crews.game_studio_crew import game_studio_crew

def run():
    result = game_studio_crew.kickoff()

    print("\n")
    print("=" * 60)
    print("AI GAME STUDIO - FINAL OUTPUT")
    print("=" * 60)
    print(result)

if __name__ == "__main__":
    run()