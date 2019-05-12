import listan
import unittest

class TestList(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.listan = listan.Listan()

    @classmethod
    def tearDown(cls):
        del cls.listan

    def test_length(self):
        self.assertEqual(self.listan.langd(), 0)
        for i in range(0, 100):
            self.listan.laggTill(i)
        self.assertEqual(self.listan.langd(), 100)

        for i in range(0, 100):
            self.listan.laggInForst(i)
        self.assertEqual(self.listan.langd(), 200)

    def test_firstNLast(self):
        for i in range(0, 100):
            self.listan.laggTill(i)
        self.assertEqual(self.listan.sist(), 99)
        self.assertEqual(self.listan.forst(), 0)
        for i in range(100, 200):
            self.listan.laggInForst(i)
        self.assertEqual(self.listan.langd(), 200)
        self.assertEqual(self.listan.sist(), 99)
        self.assertEqual(self.listan.forst(), 199)

    def test_fetch(self):
        for i in range(0, 100):
            self.listan.laggTill(i)
        for i in range(20, 40):
            self.listan.rem(i)
        self.assertEqual(self.listan.langd(), 80)
        self.listan.all()
        self.assertEqual(self.listan.fetch(19), 19)
        self.assertEqual(self.listan.fetch(27), 35)
        self.assertEqual(self.listan.fetch(79), 99)

    def test_sattInt(self):
        for i in range(0, 100):
            self.listan.laggTill(i)
        for i in range(20, 40):
            self.listan.rem(i)
        for i in range(20, 40):
            self.listan.sattIn(i, i)
        self.listan.all()
        self.assertEqual(self.listan.langd(), 100)
        self.assertEqual(self.listan.fetch(30), 30)        

        self.listan.sattIn(-1, 0)
        self.listan.sattIn(101, 101)
        self.listan.all()
        self.assertEqual(self.listan.langd(), 102)
        self.assertEqual(self.listan.fetch(0), -1)        
        self.assertEqual(self.listan.fetch(101), 101)        

if __name__ == '__main__':
        unittest.main()
