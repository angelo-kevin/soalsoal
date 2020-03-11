import unittest 

def checkSegitiga(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return "Error"
    else:
        longest = max(a, b, c)
        shortest = min(a, b, c)
        medium = a + b + c - longest - shortest
        if (shortest + medium <= longest):
            return "Error"
        elif (a == b == c):
            return "Segitiga Sama Sisi"
        elif (a == b or a == c or b == c):
            return "Segitiga Sama Kaki"
        else:
            return "Segitiga Sembarang"

class TestIsogram(unittest.TestCase): 
    def setUp(self): 
        pass

    def test_Error0andNegative(self):
        self.assertEqual(checkSegitiga(0, 1, 2), "Error")
        self.assertEqual(checkSegitiga(-1, 4, 2), "Error")

    def test_SyaratSegitiga(self):
        self.assertEqual(checkSegitiga(1, 1, 4), "Error")
        self.assertEqual(checkSegitiga(3, 9, 1), "Error")
    
    def test_Segitiga(self):
        self.assertEqual(checkSegitiga(4, 4, 4), "Segitiga Sama Sisi")
        self.assertEqual(checkSegitiga(5, 4, 4), "Segitiga Sama Kaki")
        self.assertEqual(checkSegitiga(3, 4, 5), "Segitiga Sembarang")

if __name__ == '__main__': 
    unittest.main()