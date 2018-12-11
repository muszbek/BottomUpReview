
import unittest
from util.isTerrainLogic import _getLine, _isOnLine, getLineHeightsBetweenTwoHeight
from util.isTerrainLogic import NotStandingOnLineException


class Test(unittest.TestCase):


    def setUp(self):
        self.map = [0, 1, 2, 3]
        self.charHeight = 10

    def tearDown(self):
        pass


    def testShouldReturnRightElement(self):
        yCoord = 20
        element = _getLine(self.map, yCoord, self.charHeight)
        self.assertEqual(element, 1, "Element returned as 'line' should have been 1, it was: " + str(element))
        
    def testShouldFailNotOnLine(self):
        yCoord = 25
        
        try:
            _getLine(self.map, yCoord, self.charHeight)
            self.fail()
        except NotStandingOnLineException:
            pass
        
        
    def testShouldReturnOnLine(self):
        yCoord = 20
        isOnLine = _isOnLine(yCoord, self.charHeight)
        self.assertTrue(isOnLine, "Should have returned true, y coordinate is on line.")
        
    def testShouldReturnNotOnLine(self):
        yCoord = 21
        isOnLine = _isOnLine(yCoord, self.charHeight)
        self.assertTrue(not isOnLine, "Should have returned false, y coordinate is not on line.")
        
    def testShouldReturnOnLineOnBottom(self):
        yCoord = 0
        isOnLine = _isOnLine(yCoord, self.charHeight)
        self.assertTrue(isOnLine, "Should have returned true, bottom should act as on a line.")
        
        
    def testShouldReturnToCheckTwoHeights(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 22, 2)
        self.assertEqual(toCheck, [20, 10], "Heights to return are wrong: " + str(toCheck))
        
    def testShouldReturnToCheckOneHeight(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 21, 19)
        self.assertEqual(toCheck, [20], "Height to return is wrong: " + str(toCheck))
        
    def testShouldReturnNothingToCheckDidNotMove(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 20, 20)
        self.assertEqual(toCheck, [], "Should not have returned any heights to check: " + str(toCheck))
        
    def testShouldReturnNothingToCheckOnUpperBound(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 20, 19)
        self.assertEqual(toCheck, [], "Should not have returned any heights to check: " + str(toCheck))
        
    def testShouldReturnNothingToCheckOnLowerBound(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 11, 10)
        self.assertEqual(toCheck, [], "Should not have returned any heights to check: " + str(toCheck))
        
    def testShouldReturnNothingToCheckGoingUpwards(self):
        toCheck = getLineHeightsBetweenTwoHeight(self.charHeight, 2, 22)
        self.assertEqual(toCheck, [], "Should not have returned any heights to check: " + str(toCheck))


if __name__ == "__main__":
    unittest.main()