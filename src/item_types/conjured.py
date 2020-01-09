from item_types.regular_item import RegularItem


class Conjured(RegularItem):
    
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
     
    def update_quality(self):
        self.quality -=2
        
    def update_item(self):
        RegularItem.sell_in(self)
        Conjured.update_quality(self)
        RegularItem.check_quality(self)   
    