import unittest

from mopidy.mixers.dummy import DummyMixer

class BaseMixerTest(unittest.TestCase):
    MIN = 0
    MAX = 100

    ACTUAL_MIN = MIN
    ACTUAL_MAX = MAX

    def setUp(self):
        self.mixer = DummyMixer()

    def test_volume_is_None_initially(self):
        self.assertEqual(self.mixer.volume, None)

    def test_volume_set_to_min(self):
        self.mixer.volume = self.MIN
        self.assertEqual(self.mixer.volume, self.ACTUAL_MIN)

    def test_volume_set_to_max(self):
        self.mixer.volume = self.MAX
        self.assertEqual(self.mixer.volume, self.ACTUAL_MAX)

    def test_volume_set_to_below_min_results_in_min(self):
        self.mixer.volume = -10
        self.assertEqual(self.mixer.volume, self.ACTUAL_MIN)

    def test_volume_set_to_above_max_results_in_max(self):
        self.mixer.volume = self.MAX + 10
        self.assertEqual(self.mixer.volume, self.ACTUAL_MAX)
