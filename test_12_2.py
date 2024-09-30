from module_12_2 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", 10)
        self.runner_andrei = Runner("Андрей", 9)
        self.runner_nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            result_str = {place: participant.__str__() for place, participant in value.items()}
            print(f"{key}: {result_str}")

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_andrei_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

if __name__ == '__main__':
    unittest.main()