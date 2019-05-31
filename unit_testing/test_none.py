import unittest


class TestNone(unittest.TestCase):

    def test_if_None_then_false(self):
        name = None
        self.assertFalse(name, "Should be false")

    def test_if_some_val_then_true(self):
        name = "John"
        self.assertTrue(name, "Should be true")
