
import unittest
from util.isTerrainLogic import isOnTerrain
from util.textToPng import LEFT_PADDING
from game.tiles import Empty, Code


class Test(unittest.TestCase):


    def setUp(self):
        self.bgMap = [[Code(), Empty(), Empty(), Empty(), Code()],
                    [Code(), Code(), Code(), Code(), Code()],
                    [Empty(), Empty(), Empty(), Empty(), Empty()]]
        self.charSize = (10, 10)
        self.playerWidth = 30

    def tearDown(self):
        pass
    
    
    def _callFun(self, pos):
        return isOnTerrain(pos, self.charSize, self.bgMap, self.playerWidth)


    def testStandingOnTerrainShouldReturnTrue(self):
        pos = (10 + LEFT_PADDING, 20)
        onTerrain = self._callFun(pos)
        self.assertTrue(onTerrain, "Should have returned true, staning on terrain.")
        
    def testStandingOnAirOnLineShouldReturnFalse(self):
        pos = (10 + LEFT_PADDING, 30)
        onTerrain = self._callFun(pos)
        self.assertTrue(not onTerrain, "Should have returned false, staning on air on a line.")
        
    def testStandingOnAirBetweenLinesShouldReturnFalse(self):
        pos = (10 + LEFT_PADDING, 25)
        onTerrain = self._callFun(pos)
        self.assertTrue(not onTerrain, "Should have returned false, staning on air between lines.")
        
    def testStandingOnBottomShouldReturnTrue(self):
        pos = (10 + LEFT_PADDING, 0)
        onTerrain = self._callFun(pos)
        self.assertTrue(onTerrain, "Should have returned true, staning on bottom.")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()