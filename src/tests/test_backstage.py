from backstage import Backstage
import unittest
import pytest
class AddTest(unittest.TestCase):
    def sell_in_plus_1():
        backsetage = Backstage("VIP", 12, 10)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 11, 11)

    def sell_in_plus_2():
        backsetage = Backstage("VIP", 6, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 5, 17)
        
    def sell_in_plus_3():
        backsetage = Backstage("VIP", 5, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 4, 18)
        
    def sell_in_equal_0():
        backsetage = Backstage("VIP", 1, 15)
        backsetage.update_quality()
        assert backsetage.updated_item() == ("VIP", 0, 0)