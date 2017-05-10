import unittest
import sumEvents
import pdb
# python -m unittest discover -p '*_test.py'

# Deliveries: 56988592
# Opens: 9094192
# Spam Reports: 21124

class TestSumEvents(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSumEvents, self).__init__(*args, **kwargs)
        self.data = sumEvents.getProviders(18)

    def test_it_gets_providers(self):
        self.assertIsInstance(self.data, (list))
        self.assertTrue(self.data[0].id)
        self.assertTrue(self.data[0].delivered)
        self.assertTrue(self.data[0].opens)
        self.assertTrue(self.data[0].spam_reports)

    def test_it_sums_delivered_events(self):
        self.assertTrue(sumEvents.sumDelivered(self.data))
