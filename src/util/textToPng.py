from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from game import tiles

LEFT_PADDING = 3
RIGHT_PADDING = 3
LINE_SPACING = 3

def textToPng(text, fullpath, fontColor="#000000", bgColor="#FFFFFF", fontsize=12):

    font = ImageFont.truetype("../res/consola.ttf", fontsize)

    lines = ('\n' + text).split('\n')
    bgMap = []
    
    charSize = font.getsize("A")
    
    charWidth = charSize[0]
    charHeight = charSize[1] + LINE_SPACING
    imgHeight = charHeight * (len(lines) + 0)
    
    textLength = max(list(map(len, lines)))
    textWidth = charWidth * textLength
    imgWidth = LEFT_PADDING + textWidth + RIGHT_PADDING

    img = Image.new("RGBA", (imgWidth, imgHeight), bgColor)
    draw = ImageDraw.Draw(img)

    y = -LINE_SPACING   # line spacing needs to start from bottom of line, not top
    for line in lines:
        bgMap.append(_mapLine(line))
        draw.text( (LEFT_PADDING, y), line, fontColor, font=font)
        y += charHeight

    img.save(fullpath)
    return bgMap, (charWidth, charHeight)
    
    
def _mapLine(lineText):
    mapLine = []
    
    if lineText:
        for char in lineText:
            if char == " ":
                mapLine.append(tiles.Empty())
            else:
                mapLine.append(tiles.Code())
                
    else:
        mapLine.append(tiles.Empty())
            
    return mapLine


def _printMap(bgMap):
    for mapLine in bgMap:
        _printLine(mapLine)
        
def _printLine(mapLine):
    lineCode = ""
    for char in mapLine:
        if isinstance(char, tiles.Empty):
            lineCode += "E"
        elif isinstance(char, tiles.Code):
            lineCode += "C"
            
        lineCode += " "
        
    print(lineCode)


if __name__ == "__main__":
    text = \
    "    y = 0\n" + \
    "    for line in lines:\n" + \
    "        draw.text( (LEFT_PADDING, y), line, color, font=font)\n" + \
    "        y += line_height"
    
    result = textToPng(text, '../test/test.png')
    _printMap(result[0])
    
    

            #
           # #
          #   #
         #     #
        ##     ##
          #   #
          #   #
          #   #
          #   #
          #   #
          #####
          
    ### GET TO THE TOP ###
        