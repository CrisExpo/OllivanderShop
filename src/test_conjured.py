from conjured import Conjured
import unittest
import pytest

class AddTest(unittest.TestCase):
    def quality_minus_2():
        backsetage = Backstage("VIP", 6, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 5, 17)
        

        backsetage = Backstage("VIP", 5, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 4, 18)


        backsetage = Backstage("VIP", 1, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 0, 0)