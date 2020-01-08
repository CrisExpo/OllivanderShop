from regular_item import RegularItem


class AgedBrie(RegularItem):
    
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in >= 0:
            self.quality += 1
        else:
            self.update_quality+= 2
        return self.quality
    
    def update_item(self):
        AgedBrie.sell_in(self)
        RegularItem.update_quality(self)
        RegularItem.check_quality(self)
