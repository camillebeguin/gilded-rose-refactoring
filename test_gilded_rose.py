# -*- coding: utf-8 -*-
import unittest

import pytest

from gilded_rose import GildedRose, Item


@pytest.mark.parametrize(
    ("item", "expected_quality"),
    [
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 19), 
        (Item(name="+5 Dexterity Vest", sell_in=10, quality=0), 0),
        (Item(name="Aged Brie", sell_in=2, quality=0), 1),
        (Item(name="Aged Brie", sell_in=2, quality=50), 50),
        (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 6),
        (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
        (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 21),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=48), 50),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
        (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 50),
        (Item(name="Conjured", sell_in=3, quality=6), 4),  # TODO: make it work with "Conjured Mana Cake"
    ]
)
def test_quality_updates(item, expected_quality):
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert (item.quality == expected_quality)

        
if __name__ == '__main__':
    pytest.main()
