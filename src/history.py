from src.db.get_db import get_history, get_max_battle_id
from src.misc.color import colors

class History():
    def __init__(self) -> None:
        pass

    def menu(self):
        max = get_max_battle_id()
        print(f"{colors.fgBrightMagenta}════════════HISTORY═══════════{colors.reset}")
        print(f"       There is {max} battle         ")
        print(f"{colors.fgBrightMagenta}══════════════════════════════{colors.reset}")

        try:
            c = int(input(f"{colors.fgBrightYellow}Select a battle you want the battle you want to see [1-{max}]: {colors.reset}"))
            assert c <= max and c > 0

            datas = get_history(c)
        
            winner_team = list()
            loser_team = list()

            for d in datas:
                if d[4] == datas[0][8]:
                    winner_team.append(d)
                else:
                    loser_team.append(d)
            print("")
            print(f"{colors.fgMagenta}Winner team{colors.reset} was {winner_team[0][8]} using FIGHTING tactic: focus {winner_team[0][6]} and HEALING tactic: focus {winner_team[0][7]}")
            print(f"Number of survivors: {winner_team[0][10]}")
            for w in winner_team:
                print(f"  =>{w[1]}, {w[2]} {w[3]} {colors.fgRed}{'DEAD' if w[5] == 0 else f'{w[5]} hp'}{colors.reset}")
            print("")
            print(f"{colors.fgMagenta}Loser team{colors.reset} was {loser_team[0][9]} using FIGHTING tactic: focus {loser_team[0][6]} and HEALING tactic: focus {loser_team[0][7]}")
            for l in loser_team:
                print(f"  =>{l[1]}, {l[2]} {l[3]} {colors.fgRed}{'DEAD' if l[5] == 0 else f'{l[5]} hp'}{colors.reset}")

        except (AssertionError, ValueError):
            print(f"{colors.fgRed}WRONG CHOICE{colors.reset}")
            self.menu()