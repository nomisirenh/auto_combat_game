from src.misc.color import colors

class Team():
    def __init__(self, id, name: str, fighters):
        self.id = id
        self.name = name
        self.fighters = fighters
        self.color = None

        self.win = None
        self.fighting_tactic = None
        self.heal_tactic = None

    def get_fighters(self):
        """
        Return a list of all fighters in the team
        """
        return self.fighters

    def team_str(self):
        """
        Print all fighters that is in the team
        """
        print(f'- Team {self.color}{self.name}{colors.reset} contain:')
        
        for fighter in self.fighters:
            print("  --> ", end="")
            print(f"{fighter}")
    
    def set_team_tactic(self, tactic, heal_tactic):
        if tactic == None:
            self.fighting_tactic = "Random"
        else:
            self.fighting_tactic = tactic

        if heal_tactic == None:
            self.heal_tactic = "Random"
        else: 
            self.heal_tactic = heal_tactic
            
        for fighter in self.fighters:
            fighter.set_tactic(tactic)

            if fighter._class == "Priest":
                fighter.set_heal_tactic(heal_tactic)

    def fighters_alive(self):
        i = 0
        for f in self.fighters:
            if f.is_dead == False:
                i +=1
        return i
