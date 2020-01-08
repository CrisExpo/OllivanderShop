from regular_item import RegularItem

class Backstage(RegularItem):
    
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        
    def update_quality(self):
        if self.sell_in > 10:
            self.update_quality += 1
            return self.update_quality
        
        if self.sell_in <= 10 and self.sell_in > 5:
            self.update_quality += 2
            return self.update_quality
        
        if self.sell_in <= 5 and self.sell_in > 0:
            self.update_quality += 3
            return self.update_quality
        
        if self.sell_in <= 0:
            self.update_quality = 0
            return self.update_quality
    
    def update_item(self):
        RegularItem.sell_in(self)
        Backstage.update_quality(self)
        RegularItem.check_quality(self)