import unittest
import task
# Adding a comment

class TestCase(unittest.TestCase):

    def test1(self):
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)

    def test2(self):
        expected = "Hola World"
        self.assertEqual(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
