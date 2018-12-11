'''
Util functions to calculate movement and position
'''
MAX_SPEED_X = 5
MAX_SPEED_Y = 12

DRAG = 0.2
GRAVITY = 0.4

def modifySpeedByPhysics(isOnTerrain, speed):
    speedX = _horizontalPhysics(isOnTerrain, speed[0])
    speedY = _verticalPhysics(isOnTerrain, speed[1])
    return (speedX, speedY)
    
            
def _horizontalPhysics(isOnTerrain, speedX):
    if isOnTerrain:
        if speedX > 0:
            speedX = max(speedX - DRAG, 0)
        elif speedX < 0:
            speedX = min(speedX + DRAG, 0)
            
    return speedX
            
def _verticalPhysics(isOnTerrain, speedY):
    if isOnTerrain and speedY <= 0:     # stop falling
        speedY = 0
    else:                                   # falling
        speedY -= GRAVITY
        if speedY < -MAX_SPEED_Y:
            speedY = -MAX_SPEED_Y
            
    return speedY
