import unittest 

def checkIsogram(a):
    a = a.lower()
    tempSet = set()
    for i in a:
        if i in tempSet:
            return False
        else:
            tempSet.add(i)
    return True

class TestIsogram(unittest.TestCase): 
    def setUp(self): 
        pass

    def test_lowercase(self):
        self.assertTrue(checkIsogram('asdert'))
        self.assertFalse(checkIsogram('fafse'))

    def test_uppercase(self):         
        self.assertTrue(checkIsogram('AdstweH'))
        self.assertFalse(checkIsogram('Fafhrt'))

if __name__ == '__main__': 
    unittest.main()