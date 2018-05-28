###Drawbot script
###Install Cantarell_Sketch1-Regular_20180527, Cantarell_Sketch2-Regular_20180527, Cantarell_Sketch3-Regular_20180527

format = "A4Landscape"
border = 25
gutter = border * .5

###Font to test
specimenFont = "Cantarell_Sketch1-Regular_20180527"
specimenFallbackFont = "Times New Roman Bold"

# characterOverviewPath = '~/Desktop/Cantarell_Specimen-20180528.txt'
# with open(characterOverviewPath, encoding="utf-8") as f:
#     characterOverview = f.read() 
characterOverview = '''αβγεηικλμνοπρτυ
aeklnoptuvy'''

# specimenPath = '~/Desktop/Cantarell_CharacterOverview-20180528.txt'
# with open(specimenPath, encoding="utf-8") as f:
#     specimenText = f.read()
specimenPath = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ
ΑΒΓΕΖΗΙΚΜΝΟΠΡΤΥΦΧ 
abcdefghijklmnopqrstuvwxyz
αβγεηικλμνοπρτυ

Ομορα οια, μια ρε αρμα! Μοριο ιοι ει ειμη ο «Αμε ρε ιερει, ερμαριο ορε», οροι. Ερμαρια ραμμα μαια. Ρεει ερημο ιερεια, ερμαρια, ομοιο ορμαει; Ερημοι αερια ροη, ορο αρε ερημια. Ναραμα αιμα, Χιο, Καρρο με ορρο Αμαρα Eρημη. €678.120, Καρμιο αεριε. 30 Χερια μερει Ταμε ο αερι ορρε, Joë Bousquet & Benoît de Sainte-Maure! Χορια μερει, αμοιρα η αμοιροι. Καρμα μιαρα ραμι, Υραμε ομοιο ερμοι μα ραμι ιο μοιραιο μη αρμα. Η Ηρα Ζει Κα; Μοιραια Ιαριμη μορια αμε «Ομηρεια, αμοιρο Ρημα», ορα ριμαρα…
Νερει αμοιρη ερεε η μερει 29,35 μαρμαρα Μαμα! «Αεριοι ‘οροι ομοια’ Ριμαρα μια ερμαια ομορα». Ταρμαρα ερημη ροι οι ρεει ομηρεια ομοιοι ιο μαια Μι, μαρμαρο ιερο μηροι ηρεμο. εηΑ Εια! Ειμη Ηρμα οια ορε Ηραιο αρμη ρεε ιερο ομηρεια. Ερμαριο, μιαρα, ορμη, αερια, μια η ρη. «This is not how adhension works dude!» Χιμαιρα, Κορη μιμερο, αμμοι. Ορο η οι ερμοι ομοιοι, ρε ροιαμη ορια αρμο μια μαρμαρα. Ρε! Μη! Εαρηρμα μιμε ορμο εαρ. Με ομοιο ηρεμε. Τα ειμαι η μοιραια, αμοιρη. Το ιερο αρα με αμοιρη ημερα, «αμε αρμε η μερει οι μαρμαρα. Ορμαει ερμα αερα η ρεμα;»
Η ορα ηρεμοι μια αμα η αεριε ορια. Αιμα μαρρο αραιη αρε, αμοιρα μαρμαρο! 80 μορεια αμε, 6033,77 ρε. Ζοη μορο εμει μοιραια ερμαια ερημη αμε. οΟι Κα εΜΑ Ζε. Ρημα η ορμα; There is not? Shocking! Ορμαει ηρεμα ερμο ρε ορα η ρεμα, μορια. Το αιμα ειμα, ομηρεια μηρε ερμαρια! Καρμαρα, 19 μερα, 20 ορρα η 34 ηρεμα ρημα.

Specimen text borrowed from Emilios Theofanous’ GSoC17-project:
https://github.com/eellak/gsoc17-Eczar/blob/master/GSoC17_Process/02_TestDocs/PrintTests/TestPrintDoc170620.py'''
hyphenation(True)



###Font size of the character overview
specimenFontSize = 130

###Font size of the text columns
columns = [14, 12, 10]


infoFont = "Cantarell-Regular"
infoFontSize = 10

font(infoFont, infoFontSize)
infoWidth, infoHeight = textSize("H")


import datetime
now = datetime.datetime.now()
infoString = now.strftime("Florian Fecher @grautesk | GSoC 2018 | PDF: %Y%m%d %H:%M")


pageWidth, pageHeight = sizes(format)
boxWidth = pageWidth - border * 2
boxHeight = pageHeight - border * 2 - infoHeight * 4



def createNewPage():
    newPage(format)    
    fallbackFont(specimenFallbackFont)
    font(infoFont, infoFontSize)
    textBox(infoString, (border, border, boxWidth, infoHeight), align="left")
    textBox(specimenFont, (border, pageHeight-border-infoHeight, boxWidth, infoHeight), align="left")



newDrawing()

###Character overview
while characterOverview:
    createNewPage()
    font(specimenFont, specimenFontSize)
    characterOverview = textBox(characterOverview, (border, border-infoHeight-border, boxWidth, boxHeight + border * 2 + infoHeight))


###Text columns
columnWidth = (boxWidth - gutter * (len(columns) - 1)) / len(columns)
columnHeight = boxHeight - infoHeight * 2

createNewPage()
for columnIndex in range(len(columns)):
    
    columnX = border + columnWidth * columnIndex + gutter * columnIndex
    columnY = border + infoHeight * 2 
    
    font(infoFont, infoFontSize)
    textBox("%s pt." % 
        (columns[columnIndex]), 
        (columnX, columnY+columnHeight+infoHeight, columnWidth, infoHeight))
    
    with savedState():
        font(specimenFont)
        #lineHeight(columns[columnIndex])
        fontSize(columns[columnIndex])
        textBox(specimenPath, (columnX, columnY, columnWidth, columnHeight))


###Page number
allPages = pages()
for pageIndex, page in enumerate(allPages):
    with page:
        font(infoFont, infoFontSize)
        textBox("P. %s/%s" % (pageIndex + 1, len(allPages)), 
            (border, border, boxWidth, infoHeight), align="right")


saveDate = now.strftime("%Y%m%d-%H%M")
saveImage("~/Desktop/%s_CantarellTest.pdf" % saveDate)
