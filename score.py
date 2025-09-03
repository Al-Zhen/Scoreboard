from prettytable import PrettyTable

# Store players as a dictionary {ign: (score, class)}
players = {}

def get_rank_label(rank):
    if rank == 1:
        return "1st place"
    elif rank == 2:
        return "2nd place"
    elif rank == 3:
        return "3rd place"
    else:
        return f"{rank}th place"

while True:
    print("\n--- Tournament Scoreboard ---")
    ign = input("Enter IGN (or 'q' to quit): ").strip()
    if ign.lower() == 'q':
        break

    player_class = input("Enter Class: ").strip()
    try:
        score = int(input("Enter Score: ").strip())
    except ValueError:
        print("Invalid score. Please enter a number.")
        continue

    # Update or add new player
    if ign in players:
        print(f"Updating {ign}'s score...")
    players[ign] = (score, player_class)

    # Sort players by score (descending)
    sorted_players = sorted(players.items(), key=lambda x: x[1][0], reverse=True)

    # Display table
    table = PrettyTable()
    table.field_names = ["Rank", "Score", "IGN", "Class"]

    for idx, (ign, (score, pclass)) in enumerate(sorted_players, start=1):
        table.add_row([get_rank_label(idx), score, ign, pclass])

    print(table)
