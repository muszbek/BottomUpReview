
import unittest
from game.background import Code, Empty
from util.textToPng import LEFT_PADDING
from util.isTerrainLogic import _isThisTerrainOnLine


class Test(unittest.TestCase):


    def setUp(self):
        self.playerWidth = 25
        self.charWidth = 10
        self.line = [Empty(), Empty(), Empty(), Code()]

    def tearDown(self):
        pass
    
    
    def _callFun(self, xCoord):
        return _isThisTerrainOnLine(self.line, xCoord, self.charWidth, self.playerWidth)


    def testShouldReturnOnTerrainWhenOnMiddle(self):
        xCoord = LEFT_PADDING + 13
        isTerrain = self._callFun(xCoord)
        self.assertTrue(isTerrain, "function should have returned that player is standing on terrain")
    
    def testShouldReturnOnTerrainWhenLeftOnEdge(self):
        xCoord = LEFT_PADDING + 10
        isTerrain = self._callFun(xCoord)
        self.assertTrue(isTerrain, "function should have returned that player is standing on terrain")
    
    def testShouldReturnOnTerrainWhenRightOnEdge(self):
        xCoord = LEFT_PADDING + 15
        isTerrain = self._callFun(xCoord)
        self.assertTrue(isTerrain, "function should have returned that player is standing on terrain")
    
    def testShouldReturnOnTerrainWhenBothSidesOnEdge(self):
        self.playerWidth = 30
        xCoord = LEFT_PADDING + 10
        isTerrain = self._callFun(xCoord)
        self.assertTrue(isTerrain, "function should have returned that player is standing on terrain")
    
    
    def testShouldReturnOnAirWhenOnMiddle(self):
        xCoord = LEFT_PADDING + 3
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")
    
    def testShouldReturnOnAirWhenLeftOnEdge(self):
        xCoord = LEFT_PADDING + 0
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")
    
    def testShouldReturnOnAirWhenRightOnEdge(self):
        xCoord = LEFT_PADDING + 5
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")
    
    def testShouldReturnOnAirWhenBothSidesOnEdge(self):
        self.playerWidth = 30
        xCoord = LEFT_PADDING + 0
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")
        
        
    def testShouldReturnOnAirWhenOnLeftPadding(self):
        xCoord = 0
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")
    
    def testShouldReturnOnAirWhenAfterEnd(self):
        xCoord = LEFT_PADDING + 50
        isTerrain = self._callFun(xCoord)
        self.assertTrue(not isTerrain, "function should have returned that player is standing on air")


if __name__ == "__main__":
    unittest.main()