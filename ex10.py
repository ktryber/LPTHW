tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a\\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape Sequences

# \\ = Backslash
# \'' = Single-quote
# \"" = Double-quote
# \a = ASCII bell (BEL)
# \b = ASCII backspace (BS)
# \f = ASCII formfeed (FF)
# \n = ASCII linefeed (LF)
# \N{name} = Character named name in the unicode database (unicode only)
# \r ASCII = Carriage Retrun (CR)
# \t ASCII = Horizontal Tab (TAB)
# \uxxxx = Character with 16-bit hex value xxxx (unicode  only)
# \ Uxxxxxxxx = Character with 32-bit hex value xxxxxxxx (unicode only)
# \v = ASCII vertical tab (VT)
# \ooo = Character with octal value ooo
# \xhh = Character with hex value hh

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
