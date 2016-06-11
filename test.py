import unittest
import filecmp
from encoder import encode, decode

class TestEncoder(unittest.TestCase):
    def test_multiple_files(self):
        stream = bytearray('')
        encode('a.txt', stream)
        encode('b.txt', stream) 
        encode('c.txt', stream) 
       
        decode(stream, 'a2.txt')
        decode(stream, 'b2.txt')
        decode(stream, 'c2.txt')

        self.assertEqual(filecmp.cmp('a.txt','a2.txt'), True)
        self.assertEqual(filecmp.cmp('b.txt','b2.txt'), True)
        self.assertEqual(filecmp.cmp('c.txt','c2.txt'), True)

    def test_large_file(self):
        stream = bytearray('')
        encode('warandpeace.txt', stream)
        decode(stream, 'warandpeace2.txt')

        
        self.assertEqual(filecmp.cmp('warandpeace.txt','warandpeace2.txt'), True)

        # stream should be empty
        self.assertEqual(stream,'')
if __name__ == '__main__':
    unittest.main()
