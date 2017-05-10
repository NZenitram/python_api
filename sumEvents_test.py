import unittest
import sumEvents
import pdb
# python -m unittest discover -p '*_test.py'

class TestSumEvents(unittest.TestCase):

    def test_it_gets_providers(self):
        data = sumEvents.getProviders(18)
        self.assertIsInstance(data, (list))
