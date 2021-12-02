import unittest
from src.Fighter_class.Class import Warrior
from src.game import Game
from src.Fighter_class.Fighter import FighterInterface

class Game_testing(unittest.TestCase):
    def test_get_fighters(self):
        game = Game()
        fighters = game.get_figthers_from_db()

        self.assertTrue(len(fighters) == 20)

        for fighter in fighters:
            self.assertIsInstance(fighter, FighterInterface)
            fighters.pop(fighters.index(fighter))
            self.assertNotIn(fighter, fighters)

    def test_assign_team(self):
        game = Game()
        
        teams = game.teams
        for team in teams:
            self.assertTrue(len(team.fighters) == 10)

        team1 = teams[0]
        team2 = teams[1]

        #verify that the fighters in team 1 are not in team 2
        for fighter in team1.fighters:
            self.assertNotIn(fighter, team2.fighters)