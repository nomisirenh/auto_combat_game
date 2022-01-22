from src.game import Game
from src.history import History
from src.misc.color import colors

class Main():
    def __init__(self) -> None:
        pass

    def main_menu(self):
        print(f"{colors.fgBrightMagenta}═════════COMBAT GAME═════════{colors.reset}")
        print(f"{colors.fgBrightBlue}   [1] PLAY GAME       {colors.reset}")
        print(f"{colors.fgBrightBlue}   [2] GAMES HISTORY    {colors.reset}")
        print(f"{colors.fgBrightBlue}   [3] QUIT            {colors.reset}")
        print(f"{colors.fgBrightMagenta}═════════════════════════════{colors.reset}")

        try:
            c = int(input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}"))
            assert c < 4 and c > 0

            if c == 1:
                self.game_menu()
            if c == 2:
                h = History()
                print("")
                h.menu()

        except (AssertionError, ValueError):
            print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
            self.main_menu()

    def game_menu(self):
        game = Game()
        print("")
        game.teams_description()
        print("")

        for team in game.teams:
            print(f"Select FIGHTING tactic for team {team.color}{team.name}{colors.reset}: ")
            print("    [1] Focus Warriors    ")
            print("    [2] Focus Rogues")
            print("    [3] Focus Priests")
            print("    [4] Focus Wizards")
            print("    [5] Focus enemy less HP")
            print("    [6] Random")

            c = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")
            while c not in ["1","2","3","4", "5", "6"]:
                print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
                c = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")
            print("")

            print(f"Select HEALING tactic for team {team.color}{team.name}{colors.reset}: ")
            print("    [1] Heal Warriors    ")
            print("    [2] Heal Rogues")
            print("    [3] Heal Priests")
            print("    [4] Heal Wizards")
            print("    [5] Heal ally with less HP")
            print("    [6] Random")

            d = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")
            while d not in ["1","2","3","4", "5", "6"]:
                print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
                d = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")
            print("")

            if int(c) == 1:
                tactic = "warrior"
            elif int(c) == 2:
                tactic = "Rogue"
            elif int(c) == 3:
                tactic = "Priest"
            elif int(c) == 4:
                tactic = "Wizard"
            elif int(c) == 5:
                tactic = "less HP"
            elif int(c) == 6:
                tactic = None

            if int(d) == 1:
                heal_tactic = "warrior"
            elif int(d) == 2:
                heal_tactic = "Rogue"
            elif int(d) == 3:
                heal_tactic = "Priest"
            elif int(d) == 4:
                heal_tactic = "Wizard"
            elif int(d) == 5:
                heal_tactic = "less HP"
            elif int(d) == 6:
                heal_tactic = None
            
            team.set_team_tactic(tactic, heal_tactic)

        game.do_fight()


if __name__ == '__main__':
    m = Main()
    m.main_menu()