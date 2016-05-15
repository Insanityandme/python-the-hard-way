class Kangaroo(object):

    def __init__(self, contents=None):
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Returns a string representation of this Kangaroo and
        the contents of the pouch, with one item per line.
        """
        t = [object.__str__(self) + ' with pouch contents: ']
        for obj in self.pouch_contents:
            s = '   ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)


def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(attr, obj)

kanga = Kangaroo()
roo = Kangaroo()
print roo.pouch_contents
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(Kangaroo())

print kanga
print roo
