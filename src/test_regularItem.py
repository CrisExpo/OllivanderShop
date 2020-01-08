from regular_item import RegularItem

def quality_bigger_than_zero():
    milk = RegularItem("milk", 10, 5)
    milk.update_item()
    assert milk.updated_item() == ("milk", 9, 4)
    
def quality_less_than_zero(): 
    icecream = RegularItem("Icecream", 0, 5)
    icecream.update_item()
    assert icecream.updated_item() == ("Icecream", -1, 3)

        