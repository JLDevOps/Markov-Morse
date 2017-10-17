import unittest

from Script.markov_chain import *


class test_markov_morse(unittest.TestCase):
    ## This test is not able to be processed by travis-cl due to "no audio device connected"
    # def test_generate_markov_morse(self):
    #     generate_markov_morse("sherlock", "txt", 1)
    #     assert True, "test_markov_morse Successful"

    def test_generate_markov_chain(selfs):
        try:
            generate_markov_text("sherlock", "txt", 1)
            assert True, "test_generate_markov_chain Successful"
        except:
            assert False, "test_generate_markov_chain Failed"

    def test_generate_short_markov_chain(selfs):
        try:
            generate_short_markov_text("sherlock", "txt", 1, 140)
            assert True, "test_generate_short_markov_chain Successful"
        except:
            assert False, "test_generate_short_markov_chain Failed"


if __name__ == '__main__':
    unittest.main()
