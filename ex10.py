tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# The only reason why you might need """ instead of ''' (or vice-versa)
# is if the string itself contains a triple quote!

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '''this string contains """ so use triple single-quotes.'''
print """this string contains ''' so use triple double-quotes."""

# Escape sequences testing
print "hello \\ little slash guy"

# Single quotes
print "how are you \' single quote?"

# Double-quote
print "all is well with \" double quote atleast"

# ASCI BEL
print "beep beep says the \a\\a mobile"

# ASCI Backspace
print "backspace a\bre deleti\bng words in here! watch out for \\b!!!"

# ASCII form feed (FF)
print "\\f totally breaks a page, \f right?"

# ASCII lLinefeed (LF)
print "Lemme give you a completely new line,\nthanks!"

# \N{name} Characted named in the Unicode database (Unicode only)

# Carriage Return (CR)
print "holy shit, we have a carriage return on our hands!"
print "holy shit, we have a carriage \rreturn on our hands!"

# Horizontal tab (TAB)
print "We all know about dem \ttabs"

# Character with a 16-bit hex value xxxx (Unicode only)
unicode_example = '\u0057'.decode('unicode_escape')
print "\uxxxx, hmm let's try it out!", unicode_example
print u'\\u0e4f\\u032f\\u0361\\u0e4f'.decode('unicode_escape'), "You can print out all sorts of symbols yo"

# Character with a 32-bit hex value xxxxxxxx (Unicode only)
print "\Uxxxxxxxx, hmm lol wat!"
print '/U00224499'.decode('unicode_escape')

# ASCII vertical tab (VT)
print "shit dis da ver\vtical tab shit right here"

# Character with hex value hh
print "this example writes a string ABC using hex"
print "\x41\x42\x43"

# Character with octal value ooo
print "this time using octal"
print "\101\102\103"

# HAXX CODE
print "HAXX CODE LOOK IN COMMENTS"
""" while True:
    for i in ["/","-","|","\\","|"]:
        print "%s/r" % i,
"""

# Combining format strings and escape sequences
print "%r" % '\101'
