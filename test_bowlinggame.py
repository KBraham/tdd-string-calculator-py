
import unittest

class Frame:

    def __init__(self) -> None:
        self.score = []

    def Roll(self, pins):
        self.score.append(pins)


    def IsSpare():
        return len(self.score) > 1 and sum(self.score[:2]) == 10

    def IsStrike():
        return self.score[0] == 10

    def getScore():
        return sum(self.score)



class Game:
    def __init__(self) -> None:
        self.score = []

    def Roll(self, pins):
        # if pins == 10:
        #     self.score.append(0)
        self.score.append(pins)

    def Score(self):
        points = 0
        print(self.score)
        for i,x in enumerate(self.score):
            if self.isBonus(i):
                x *= 2
            points += x
        return points

    def isBonus(self, i):
        if i >= 1 and self.score[i-1] == 10:
            return True
        elif i >= 2 and self.score[i-2] == 10:
            return True
        elif i >= 2 and self.isEndOfFrame(i-1) and i < 20:
            if sum(self.score[i-2:i]) == 10:
                return True
        return False

    def isEndOfFrame(self, round):
        number_of_tries = 0
        for i,x in enumerate(self.score):
            if i > round:
                break
            number_of_tries += 1
            if x == 10:
                number_of_tries += 1

        return number_of_tries % 2 == 0


class TestGameMethods(unittest.TestCase):


    def setUp(self) -> None:
        self._game = Game()
        return super().setUp()


    def test_GivenTwoRoundsWithOneStikeExpectEndOfFrame(self):
        self._game.Roll(1)
        self._game.Roll(1)
        self._game.Roll(10)
        self.assertTrue(self._game.isEndOfFrame(2))

    def test_GivenTwoRoundsWithOneStikeAndOneTryExpectEndOfFrame(self):
        self._game.Roll(1)
        self._game.Roll(1)
        self._game.Roll(10)
        self._game.Roll(1)
        self.assertFalse(self._game.isEndOfFrame(3))

    def test_GivenAbandonedGameExpectScore0(self):
        self.assertEqual(0, self._game.Score())

    def test_GivenTenRoundsWith1ScoreExpectScore20(self):
        for i in range(20):
            self._game.Roll(1)

        self.assertEqual(20, self._game.Score())

    def test_GivenTenRoundsWithOneSpareExpectScore29(self):
        for i in range(6):
            self._game.Roll(1)

        self._game.Roll(4)
        self._game.Roll(6)

        for i in range(12):
            self._game.Roll(1)

        self.assertEqual(29, self._game.Score())

    def test_GivenTenRoundsWithNoSpareButConsecutive10PointsExpectScore28(self):
        for i in range(5):
            self._game.Roll(1)

        self._game.Roll(4)
        self._game.Roll(6)

        for i in range(13):
            self._game.Roll(1)

        self.assertEqual(28, self._game.Score())

    def test_GivenTenRoundsWithOneSpareFollowedWith9PointsExpectScore36(self):
        for i in range(2):
            self._game.Roll(1)

        self._game.Roll(4)
        self._game.Roll(6)
        self._game.Roll(1)
        self._game.Roll(8)

        for i in range(14):
            self._game.Roll(1)

        self.assertEqual(36, self._game.Score())


    def test_GivenTenRoundsWithOneSpareAtEndOfGameExpectScore35(self):
        for i in range(18):
            self._game.Roll(1)

        self._game.Roll(4)
        self._game.Roll(6)
        self._game.Roll(7)

        self.assertEqual(35, self._game.Score())

    def test_GivenTenRoundsWithOneStrikeExpectScore30(self):
        self._game.Roll(10)

        for i in range(18):
            self._game.Roll(1)

        self.assertEqual(30, self._game.Score())


    # def test_GivenTenRoundsWithTwoStrikesConsecutivelyExpectScore49(self):
    #     self._game.Roll(1)
    #     self._game.Roll(1)

    #     self._game.Roll(10)
    #     self._game.Roll(10)

    #     for i in range(14):
    #         self._game.Roll(1)

    #     self.assertEqual(49, self._game.Score())