with open('somefile.txt', 'w+') as f:
    # Note that f has now been truncated to 0 bytes, so you'll only
    # be able to read data that you wrote earlier...
    f.write('somedata\n')
    f.seek(0) # Important: return to the top of the file before reading, other you'll just read an empty string
    data = f.read()


