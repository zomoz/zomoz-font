import fontforge
import csv

TABLE_NAME = "'liga' Standard Ligatures in Latin lookup 0"
SUBTABLE_NAME = TABLE_NAME + ' subtable'

GLYPH_DICTIONARY = { '_': 'underscore' }

# Abstracts away how to parse the icon configurations
def getInfo(filename):
  with open(filename, 'rb') as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
    return list(reader)

# Inserts elements in a font
def insertIcons(font, elements):
  for elem in elements:
    code, name = elem

    glyph = font.createMappedChar(int(code))
    glyph.importOutlines('glyphs/' + name + '.svg')
    glyph.addPosSub(SUBTABLE_NAME, tuple(map(lambda x: GLYPH_DICTIONARY.get(x, x), name)))

# Given a FontForge font, generate output fonts
def generateFonts(font, name):
  font.generate(name + '.woff') # Web Open Format output
  
# Main method to generate the fonts
def main():
  font = fontforge.open('base-font.sfd')
  info = getInfo('ligatures.csv')

  insertIcons(font, info)

  generateFonts(font, 'icon-font')

main()