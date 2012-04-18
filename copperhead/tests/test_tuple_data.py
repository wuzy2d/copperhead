import unittest
from copperhead import *

class TupleData(unittest.TestCase):
    def testTypeTupleScalars(self):
        source = (1, 2.0)
        result_type, result_value = runtime.driver.induct(source)
        self.assertEqual(repr(result_type), "Tuple(Long, Double)")
    def testTypeTupleSequences(self):
        source = ([1, 2], [3.0, 4.0])
        result_type, result_value = runtime.driver.induct(source)
        self.assertEqual(repr(result_type), "Tuple(Seq(Long), Seq(Double))")
    def testTypeNestedTuple(self):
        source = (1, (2, 3.0, (4.0, 5)), 6.0)
        result_type, result_value = runtime.driver.induct(source)
        self.assertEqual(repr(result_type), "Tuple(Long, Tuple(Long, Double, Tuple(Double, Long)), Double)")

@cu
def test_tuple((m, n), b):
    """Test tuple assembly/disassembly.
    Tuples disassembled in arguments!
    Tuples disassembled in statements!
    Tuples assigned to other tuples!
    Tuples assigned to identifiers!
    Tuples returned!"""

    #tuple = tuple bind
    q, r = m, n
    #tuple pack
    s = q, r
    #tuple unpack
    t, u = s
    o, p = b
    #return tuple
    return t + o, u + p

@cu
def test_tuple_return():
    """Test returning a tuple by identifier"""
    a = 1, 2
    return a
        
class TupleExtract(unittest.TestCase):
    def testTuple(self):
        source_a = (1, 2)
        source_b = (5, 6)
        golden = (6, 8)
        self.assertEqual(test_tuple(source_a, source_b), golden)
    def testTupleReturn(self):
        self.assertEqual(test_tuple_return(), (1, 2))
        
if __name__ == "__main__":
    unittest.main()