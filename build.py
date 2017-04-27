import fontforge
import os

TABLE_NAME = "'liga' Standard Ligatures in Latin lookup 0"
SUBTABLE_NAME = TABLE_NAME + ' subtable'
START_CODEPOINT = 57344

GLYPH_DICTIONARY = { '_': 'underscore' }

# Return filenames in the 'glyphs' folder, without extension
def getIconNames():
  return map(lambda f: os.path.splitext(f)[0], os.listdir('glyphs'))

# Inserts elements in a font
def insertIcons(font, names):
  for name, i in zip(names, xrange(len(names))):
    code = START_CODEPOINT + i
    print(name)

    glyph = font.createMappedChar(code)
    glyph.importOutlines('glyphs/' + name + '.svg')
    glyph.addPosSub(SUBTABLE_NAME, tuple(map(lambda x: GLYPH_DICTIONARY.get(x, x), name)))

# Given a FontForge font, generate output fonts
def generateFonts(font, name):
  font.generate(name + '.woff') # Web Open Format output
  font.generate(name + '.otf') # Web Open Format output
  
# Main method to generate the fonts
def main():
  font = fontforge.open('base-font.sfd')
  names = getIconNames()

  insertIcons(font, names)

  generateFonts(font, 'icon-font')

main()
