import unittest
from unittest import mock
import src.Fighter_class.Fighter
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

        f = game.fighters[1]

        if f in game.teams[0].fighters:
            f_allies = game.teams[0].fighters
            f_enemies = game.teams[1].fighters
        else:
            f_allies = game.teams[1].fighters
            f_enemies = game.teams[0].fighters

        self.assertEqual(f.ally_team, f_allies)
        self.assertEqual(f.enemy_team, f_enemies)

    @mock.patch('src.Fighter_class.Fighter.threading.Thread.start', return_value=True)
    @mock.patch('src.Fighter_class.Fighter.threading.Thread.join', return_value=True)
    def test_do_fight(self, mock_tread_start, mock_thread_join):
        
        game = Game()
        game.do_fight()

    def test_generate_new_fighter(self):
        pass