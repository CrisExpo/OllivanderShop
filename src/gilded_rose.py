from item_types.agedBried import AgedBrie
from item_types.backstage import Backstage
from item_types.conjured import Conjured
from item_types.sulfuras import Sulfuras
from item_types.regular_item import RegularItem
from item_types.item import Item

class GildedRose(object):
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for day in range(1, 32):
            print("-------------- day ", day, "--------------")
            for item in self.items:
                print(item)
                item.update_item()

    def updated_items(self):
        return self.items


if __name__ == "__main__":
    lista_items = GildedRose([
        RegularItem("+ 5 Dexterity Vest", 10, 20),
        AgedBrie("Aged Brie", 2, 0),
        RegularItem("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)])

    lista_items.update_quality()
 