import unittest
import RK1


class testRK1(unittest.TestCase):
    def setUp(self):
        self.test1 = [('elif', 4, 'C'), ('if', 2, 'C#'), ('else', 4, 'C#'),
                      ('switch', 6, 'C++'), ('case', 4, 'C++')]
        self.test2 = [('C#', 3.0), ('C', 4.0), ('Python', 4.0), ('C++', 5.0)]
        self.test3 = [('else', 'C'), ('elif', 'C'), ('else', 'C#'),
                      ('else', 'C++'), ('elif', 'C++'), ('else', 'Python')]

    def test1_rk(self):
        self.assertEqual(RK1.task1(RK1.one_to_many), self.test1)

    def test2_rk(self):
        self.assertEqual(RK1.task2(RK1.one_to_many), self.test2)

    def test3_rk(self):
        self.assertEqual(RK1.task3(RK1.many_to_many), self.test3)


if __name__ == '__main__':
    unittest.main()
