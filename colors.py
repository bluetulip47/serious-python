#!/usr/bin/python3

#from bases import Bases

#print('hello world')

#bases = Bsaes()

class Paint(object):
    redmask = 0x110000
    greenmask = 0x001100
    bluemask = 0x000011

    def __init__(self):
#        self.color = colhex
        pass

    @classmethod
    def applymask(cls, mask):
        if mask == 'red':
            specific = str(ibases.toBase16(cls.redmask))
        elif mask == 'green':
            specific = str(cls.greenmask)
        elif mask == 'blue':
            specific = str(hex(cls.bluemask))
        else:
            print('invalid mask')
            return
        return specific

bluepaint = Paint().applymask('blue')

#print("{0:#0{6}x}".format(bluepaint, 6))

print(bluepaint)
