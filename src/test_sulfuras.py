from sulfuras import Sulfuras
import unittest
import pytest

class AddTest(unittest.TestCase):
    def sulfuras_test():
        sulfuras = Sulfuras("sulfuras", 0, 80)
        sulfuras.update_item()
        assert sulfuras.updated_item() == ("Sulfuras", 0, 80)
