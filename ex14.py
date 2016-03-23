from sys import argv

script, user_name, cat_name = argv
prompt = '> '

print "Hi %s, I'm the %s script. and your cat is named %r?" % (user_name, script, cat_name)
print "I'd like to axe you a few questions. "
print "Do you like me %s? " % user_name
likes = raw_input(prompt)

print "Do you really like your cat %s? " % cat_name
cat = raw_input(prompt)

print "Where do you live %s? " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, not sure where that is.
And you have a %r computer. Nice.
And apparenetely you don't like your %r. Shame on you.
""" % (likes, lives, computer, cat_name)
