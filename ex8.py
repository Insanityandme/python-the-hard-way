# stores 4 %r specifiers into the variable formatter. Just a good way to DRY it up.
formatter = "%r %r %r %r"
formatters = "%s %s %s %s"
formatter_less = "%r %r %r"
formatter_more = "%r %r %r %r %r %r"

# Taking 4 integers for printing. 
print formatter % (1, 2, 3, 4)

# Same thing but strings
print formatter % ("one", "two", "three", "four")

# Just prints boolean values as they are, no real use here
print formatter % (True, False, False, True)

# prints the contents of itself 4 times
print formatter % (formatter, formatter, formatter, formatter) 

# prints 4 strings, would recommend %s here instead. 
# Python is clever, It'll use double quotes for strings
# that contain single quotes when generating the representation
# to minimize escapes:
print formatter_more % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "This is redonk",
        "Super redonk",
        "How much redonk?"
        )
