import unittest
from logic import SaperLogic

class TestSaperLogic(unittest.TestCase):
    def test_bomb_count(self):
        logic = SaperLogic(5, 5, 5)
        bomb_count = sum(row.count(-1) for row in logic.board)
        self.assertEqual(bomb_count, 5)

    def test_reveal_empty(self):
        logic = SaperLogic(5, 5, 0)  # Brak bomb
        logic.reveal(0, 0)
        self.assertTrue(all(logic.revealed[row][col] for row in range(5) for col in range(5)))

    def test_reveal_bomb(self):
        logic = SaperLogic(3, 3, 1)
        for row in range(3):
            for col in range(3):
                if logic.board[row][col] == -1:
                    result = logic.reveal(row, col)
                    self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

