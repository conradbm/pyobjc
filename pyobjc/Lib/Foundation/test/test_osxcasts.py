import unittest

from objc import *
from Foundation import *

try:
    # These tests are only usefull on MacOS X when using MacPython
    from Carbon.CF import *


    class TestTollFreeBridging( unittest.TestCase ):
        def testExplicitToCF(self):
            o = NSArray.arrayWithArray_(("a", 1, 1.9))
            self.assert_(isinstance(o, NSArray))

            c = ObjectToCF(o)
            self.assert_(isinstance(c, CFArrayRef))

        def testExplictFromCF(self):
            c = CFArrayCreateMutable(0)
            self.assert_(isinstance(c, CFMutableArrayRef))

            o = CFToObject(c)
            self.assert_(isinstance(o, NSMutableArray))

        def testImplicitFromCF(self):
            c = CFArrayCreateMutable(0)
            self.assert_(isinstance(c, CFMutableArrayRef))

            nsa = NSMutableArray.array()
            nsa.addObject_(c)

            o = nsa[0]
            self.assert_(isinstance(o, NSMutableArray))

except ImportError:
    pass

if __name__ == '__main__':
    unittest.main( )
