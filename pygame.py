import random 
class Unit:
    def __init__(self, name, hp, atk, def_, exp, rank, unit_type):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_ = def_
        self.exp = exp
        self.rank = rank
        self.unit_type = unit_type

    def attack(self, target):
        damage = self.atk - target.def_
        target.hp -= damage
        print("{} attacks {} for {} damage!".format(self.name, target.name, damage))

def game_loop(player_team, ai_team):
    while True:
        # Display game status
        print("Player Team:")
        for i, unit in enumerate(player_team):
            print("Unit {}: {} ({} HP, {} ATK, {} DEF)".format(i+1, unit.name, unit.hp, unit.atk, unit.def_))
        print("\nAI Team:")
        for i, unit in enumerate(ai_team):
            print("Unit {}: {} ({} HP, {} ATK, {} DEF)".format(i+1, unit.name, unit.hp, unit.atk, unit.def_))

        # Player turn
        print("\nPlayer's turn:")
        player_choice = int(input("Choose a unit to attack with (1-3): "))
        attacker = player_team[player_choice-1]
        target_choice = int(input("Choose a target to attack (1-3): "))
        target = ai_team[target_choice-1]
        attacker.attack(target)

        # Remove defeated units
        ai_team = [unit for unit in ai_team if unit.hp > 0]

        # Check if AI team is defeated
        if not ai_team:
            print("Player wins!")
            break

        # AI turn
        print("\nAI's turn:")
        attacker = random.choice(ai_team)
        target = random.choice(player_team)
        attacker.attack(target)

        # Remove defeated units
        player_team = [unit for unit in player_team if unit.hp > 0]

        # Check if player team is defeated
        if not player_team:
            print("AI wins!")
            break

# Initialize player and AI teams
player_team = [Unit("Najib Razak", 100, 10, 5, 0, 1, "Warrior"),
               Unit("Kiasu Uncle", 100, 15, 8, 0, 2, "Tanker"),
               Unit("linbeh jiang linbeh shi linbeh de shi", 100, 12, 6, 0, 3, "Warrior")]
ai_team = [Unit("Paikia", 100, 8, 10, 0, 1, "Tanker"), 
           Unit("AhBeng", 100, 12, 5, 0, 2, "Warrior"), 
           Unit("AhLian", 100, 10, 7, 0, 3, "Tanker")]

# Start game loop
game_loop(player_team, ai_team)
