from os import execlp
from src.game import Game
from src.misc.color import colors

class Main():
    def __init__(self) -> None:
        pass

    def main_menu(self):
        print(f"{colors.fgBrightMagenta}══════COMBAT GAME══════{colors.reset}")
        print(f"{colors.fgBrightBlue}   [1] PLAY GAME       {colors.reset}")
        print(f"{colors.fgBrightBlue}   [2] GAMES HISTORY    {colors.reset}")
        print(f"{colors.fgBrightBlue}   [3] QUIT            {colors.reset}")
        print(f"{colors.fgBrightMagenta}═══════════════════════{colors.reset}")

        try:
            c = int(input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}"))
            assert c < 4 and c > 0

            if c == 1:
                self.game_menu()

        except (AssertionError, ValueError):
            print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
            self.main_menu()

    def game_menu(self):
        game = Game()
        print("")
        game.teams_description()
        print("")

        for team in game.teams:
            print(f"Select fighting tactic for team {team.color}{team.name}{colors.reset}: ")
            print("    [1] Focus Warriors    ")
            print("    [2] Focus Rogues")
            print("    [3] Focus Priests")
            print("    [4] Focus Wizards")
            print("    [5] Random")

            c = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")
            while c not in ["1","2","3","4", "5"]:
                print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
                c = input(f"{colors.fgBrightYellow}ENTER CHOICE: {colors.reset}")

            if int(c) == 1:
                team.set_team_tactic("warrior")
            elif int(c) == 2:
                team.set_team_tactic("Rogue")
            elif int(c) == 3:
                team.set_team_tactic("Priest")
            elif int(c) == 4:
                team.set_team_tactic("Wizard")
            elif int(c) == 5:
                team.set_team_tactic(None)

        game.do_fight()


if __name__ == '__main__':
    m = Main()
    m.main_menu()