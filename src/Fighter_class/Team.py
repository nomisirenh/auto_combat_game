
class Team():
    def __init__(self, id, name: str, fighters):
        self.id = id
        self.name = name
        self.fighters = fighters

    def get_fighters(self):
        """
        Return a list of all fighters in the team
        """
        return self.fighters

    def team_str(self):
        """
        Print all fighters that is in the team
        """
        print(f'Equipe {self.name} contient:')
        
        for fighter in self.fighters:
            print("--> ", end="")
            print(fighter)

    def fighters_alive(self):
        i = 0
        for f in self.fighters:
            if f.is_dead == False:
                i +=1
        return i
