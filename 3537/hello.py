"""hello"""
import json
def main():
    """hello"""
    players = {}

    while True:
        line = input().strip()
        if line == "Start":
            break
        data = json.loads(line)
        players.update(data)

    dead_players = []

    while True:
        line = input().strip()
        if line == "End":
            break
        dead_players.append(line)

    alive_players = []
    for name in players:
        if name not in dead_players:
            alive_players.append(name)

    impostor_remains = 0
    for name in alive_players:
        if players[name] == "Impostor":
            impostor_remains += 1

    print(f"{impostor_remains} Impostor Remains")

    print("***Alive***")
    for name in sorted(alive_players):
        print(f"{name} : {players[name]}")

    print("***Dead***")
    for name in sorted(dead_players):
        print(f"{name} : {players[name]}")
main()
