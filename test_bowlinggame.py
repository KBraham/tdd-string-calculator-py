
import unittest

class Frame:

    def __init__(self, index) -> None:
        self.score = []
        self.index = index

    def Roll(self, pins):
        self.score.append(pins)


    def IsSpare(self):
        return len(self.score) > 1 and sum(self.score[:2]) == 10

    def IsStrike(self):
        return len(self.score) == 1 and self.score[0] == 10

    def IsPlayed(self):
        return self.IsStrike() or (self.index < 10 and len(self.score) >= 2) or (self.index == 10 and len(self.score) == 3)

    def getScore(self):
        return sum(self.score)



class Game:
    def __init__(self) -> None:
        self.score = []
        self.frames = []
        self.frames.append(Frame(1))

    def Roll(self, pins):
        if self.frames[-1].IsPlayed():
            self.frames.append(Frame(len(self.frames)))

        self.frames[-1].Roll(pins)
        # self.score.append(pins)

    def Score(self):
        points = 0
        for i,x in enumerate(self.frames):
            if i < 9:
                if x.IsStrike():
                    points += sum(self.NextTwoRolls(i))

                elif x.IsSpare():
                    points += self.frames[i+1].score[0]

            points += x.getScore()
        return points

    def NextTwoRolls(self, index):
        rolls = []
        rolls.append(self.frames[index+1].score[0])

        if self.frames[index+1].IsStrike():
            rolls.append(self.frames[index+2].score[0])
        else:
            rolls.append(self.frames[index+1].score[1])

        return rolls


class TestGameMethods(unittest.TestCase):

    def setUp(self) -> None:
        self._game = Game()
        return super().setUp()

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


    def test_GivenTenRoundsWithTwoStrikesConsecutivelyExpectScore49(self):
        self._game.Roll(1)
        self._game.Roll(1)

        self._game.Roll(10)
        self._game.Roll(10)

        for i in range(14):
            self._game.Roll(1)

        self.assertEqual(49, self._game.Score())


    def test_GivenTenRoundsWithAllStrikesExpectScore300(self):

        for i in range(12):
            self._game.Roll(10)

        self.assertEqual(300, self._game.Score())

    def test_GivenTenRoundsWithAllSparesExpectScore150(self):

        for i in range(21):
            self._game.Roll(5)

        self.assertEqual(150, self._game.Score())