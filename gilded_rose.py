# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.agers = {
            "Conjured": ConjuredAger,
            "Aged Brie": AgedBrieAger,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassAger,
            "Sulfuras, Hand of Ragnaros": SulfurasAger,
        }

    def update_quality(self):
        for item in self.items:
            ager = self.agers.get(item.name) or DefaultItemAger
            ager(item).update_quality()
            item.sell_in -= 1
        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# agers
class ItemAger:
    _max_quality: int 
    _variation: int 

    def __init__(self, item):
        self.item = item

    def update_quality(self):
        pass 

    def clamp_quality(self):
        self.item.quality = max(0, min(self.item.quality, self._max_quality))

class DefaultItemAger(ItemAger):
    _variation = -1 
    _max_quality = 50

    def update_quality(self):
        if self.item.sell_in <= 0:
            self._variation *= 2

        self.item.quality += self._variation
        self.clamp_quality()

class ConjuredAger(DefaultItemAger):
    _variation = -2 

class AgedBrieAger(ItemAger):
    _variation = 1
    _max_quality = 50

    def update_quality(self):
        self.item.quality += self._variation 
        self.clamp_quality()

class BackstagePassAger(ItemAger):
    _variation = 1 
    _max_quality = 50

    def update_quality(self):
        if self.item.sell_in <= 0:
            self.item.quality = 0
        else:
            self._variation += 1 if self.item.sell_in <= 10 else 0
            self._variation += 1 if self.item.sell_in <= 5 else 0
            self.item.quality += self._variation 

        self.clamp_quality()

class SulfurasAger(ItemAger):
    def update_quality(self):
        pass


