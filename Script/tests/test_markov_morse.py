import unittest

from Script.morse import *


class test_markov_morse(unittest.TestCase):
    def test_generate_markov_morse(self):
        try:
            generate_markov_morse("sherlock", "txt", 1)
            assert True, "test_markov_morse Successful"
        except:
            assert False, "test_markov_morse Failed"


if __name__ == '__main__':
    unittest.main()
