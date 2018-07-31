###Drawbot script
###Install Cantarell Regular_20180731


###Basic page setup
format = "A4Landscape"
border = 25
gutter = border * .5


###Font to test, change accordingly (also in saveImage)
specimenFont = "Cantarell Regular_20180731"
specimenFallbackFont = "Times New Roman Bold"


###Font size of the character overview and text columns
characterOverviewFontSize = 130
diacriticsOverviewFontSize = 45
columns = [14, 12, 10]


###Font used for the info at the top and bottom of the page
infoFont = "Cantarell Regular_20180731"
infoFontSize = 9
font(infoFont, infoFontSize)
infoWidth, infoHeight = textSize("H")


###Page and text box setup
pageWidth, pageHeight = sizes(format)
boxWidth = pageWidth - border * 2
boxHeight = pageHeight - border * 2 - infoHeight * 4
def createNewPage():
    newPage(format)    
    fallbackFont(specimenFallbackFont)
    font(infoFont, infoFontSize)
    textBox(infoString, (border, border, boxWidth, infoHeight), align="left")
    textBox(specimenFont, (border, pageHeight-border-infoHeight, boxWidth, infoHeight), align="left")

###Import text from files stored on GitHub
###It opens the URL, gets the raw data, converts to text, closes the connection
from urllib.request import urlopen

characterOverviewPath = "https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/00_PROCESS/05_Test/TXT/Cantarell_CharacterOverview_20180731.txt"
response = urlopen(specimenPath, timeout=5)
specimenText = response.read()
specimenText = specimenText.decode("utf-8")
response.close()
    
    diacriticsOverviewPath = "https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/00_PROCESS/05_Test/TXT/Cantarell_CharacterOverviewDiacritics_20180731.txt"
response = urlopen(specimenPath, timeout=5)
specimenText = response.read()
specimenText = specimenText.decode("utf-8")
response.close()

specimenPath = "https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/00_PROCESS/05_Test/TXT/Cantarell_Specimen_20180604.txt"
response = urlopen(specimenPath, timeout=5)
specimenText = response.read()
specimenText = specimenText.decode("utf-8")
response.close()
    
polytonicSpecimenPath = "https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/00_PROCESS/05_Test/TXT/Cantarell_SpecimenPolytonic_20180731.txt"
response = urlopen(specimenPath, timeout=5)
specimenText = response.read()
specimenText = specimenText.decode("utf-8")
response.close()
    
upperCaseSpecimenPath = "https://raw.githubusercontent.com/eellak/gsoc2018-cantarell/master/00_PROCESS/05_Test/TXT/Cantarell_SpecimenUpperCase_20180731.txt"
response = urlopen(specimenPath, timeout=5)
specimenText = response.read()
specimenText = specimenText.decode("utf-8")
response.close()



import datetime
now = datetime.datetime.now()
infoString = now.strftime("Florian Fecher @grautesk | GSoC 2018 | PDF: %Y%m%d %H:%M")



newDrawing()

###Character overview
while characterOverview:
    createNewPage()
    font(specimenFont, characterOverviewFontSize)
    characterOverview = textBox(characterOverview, (border, border-infoHeight-border, boxWidth, boxHeight + border * 2 + infoHeight))

###Diacritics overview
while diacriticsOverview:
    createNewPage()
    font(specimenFont, diacriticsOverviewFontSize)
    tracking(18)
    diacriticsOverview = textBox(diacriticsOverview, (border, border-infoHeight-border, boxWidth, boxHeight + border * 2 + infoHeight))

###Text columns
columnWidth = (boxWidth - gutter * (len(columns) - 1)) / len(columns)
columnHeight = boxHeight - infoHeight * 2

createNewPage()
for columnIndex in range(len(columns)):
    
    columnX = border + columnWidth * columnIndex + gutter * columnIndex
    columnY = border + infoHeight * 2 
    
    language("Greek")
    hyphenation(True)
    
    font(infoFont, infoFontSize)
    textBox("%s pt." % 
        (columns[columnIndex]), 
        (columnX, columnY+columnHeight+infoHeight, columnWidth, infoHeight))
    
    with savedState():
        font(specimenFont)
        #lineHeight(columns[columnIndex])
        fontSize(columns[columnIndex])
        textBox(specimenText, (columnX, columnY, columnWidth, columnHeight))
        
###Upper case text columns
createNewPage()
for columnIndex in range(len(columns)):
    
    columnX = border + columnWidth * columnIndex + gutter * columnIndex
    columnY = border + infoHeight * 2 
    
    language("Greek")
    hyphenation(True)
    
    font(infoFont, infoFontSize)
    textBox("%s pt." % 
        (columns[columnIndex]), 
        (columnX, columnY+columnHeight+infoHeight, columnWidth, infoHeight))
    
    with savedState():
        font(specimenFont)
        fontSize(columns[columnIndex])
        textBox(upperCaseSpecimenText, (columnX, columnY, columnWidth, columnHeight))
        
###Polytonic text columns
createNewPage()
for columnIndex in range(len(columns)):
    
    columnX = border + columnWidth * columnIndex + gutter * columnIndex
    columnY = border + infoHeight * 2 
    
    language("Greek")
    hyphenation(True)
    
    font(infoFont, infoFontSize)
    textBox("%s pt." % 
        (columns[columnIndex]), 
        (columnX, columnY+columnHeight+infoHeight, columnWidth, infoHeight))
    
    with savedState():
        font(specimenFont)
        fontSize(columns[columnIndex])
        textBox(polytonicSpecimenText, (columnX, columnY, columnWidth, columnHeight))


###Page number
allPages = pages()
for pageIndex, page in enumerate(allPages):
    with page:
        font(infoFont, infoFontSize)
        tracking(0)
        textBox("P. %s/%s" % (pageIndex + 1, len(allPages)), 
            (border, border, boxWidth, infoHeight), align="right")


saveDate = now.strftime("%Y%m%d-%H%M")
saveImage("~/Desktop/Cantarell Regular_20180731_%s.pdf" % saveDate)