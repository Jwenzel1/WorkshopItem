from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Set

from category import Category
from crafting_material import CraftingMaterial


@dataclass
class Item:

    name: str
    value: int
    hours_to_craft: int
    categories: Set[Category]
    required_materials: Dict[CraftingMaterial, int]

    def to_json(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "value": self.value,
            "hours_to_craft": self.hours_to_craft,
            "categories": [category.value for category in self.categories],
            "required_materials": {
                crafting_material.value: quantity
                for crafting_material, quantity in self.required_materials.items()
            },
        }


class WorkshopItem(Enum):

    ISLEWORKS_BAKED_PUMPKIN = Item(
        name="Isleworks Baked Pumpkin",
        value=48,
        hours_to_craft=4,
        categories={Category.FOODSTUFFS},
        required_materials={
            CraftingMaterial.ISLAND_PUMPKIN: 1,
            CraftingMaterial.ISLAND_SAP: 3,
        },
    )
    ISLEWORKS_BARBUT = Item(
        name="Isleworks Barbut",
        value=50,
        hours_to_craft=6,
        categories={Category.ATTIRE, Category.METALWORKS},
        required_materials={
            CraftingMaterial.ISLAND_COPPER_ORE: 3,
            CraftingMaterial.ISLAND_SAND: 3,
        },
    )
    ISLEWORKS_BED = Item(
        name="Isleworks Bed",
        value=144,
        hours_to_craft=8,
        categories={Category.FURNISHINGS, Category.TEXTILES},
        required_materials={
            CraftingMaterial.SANCTUARY_FUR: 4,
            CraftingMaterial.ISLAND_COTTON_BALL: 2,
            CraftingMaterial.ISLAND_LOG: 2,
        },
    )
    ISLEWORKS_BOILED_EGG = Item(
        name="Isleworks Boiled Egg",
        value=52,
        hours_to_craft=4,
        categories={Category.FOODSTUFFS, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_EGG: 1,
            CraftingMaterial.ISLAND_LAVER: 3,
        },
    )
    ISLEWORKS_BRICK_COUNTER = Item(
        name="Isleworks Brick Counter",
        value=57,
        hours_to_craft=6,
        categories={Category.FURNISHINGS, Category.UNBURIED_TREASURES},
        required_materials={
            CraftingMaterial.ISLAND_CLAY: 2,
            CraftingMaterial.ISLAND_LIMESTONE: 2,
            CraftingMaterial.ISLAND_PALM_LOG: 2,
        },
    )
    ISLEWORKS_BRONZE_SHEEP = Item(
        name="Isleworks Bronze Sheep",
        value=76,
        hours_to_craft=8,
        categories={Category.FURNISHINGS, Category.METALWORKS},
        required_materials={
            CraftingMaterial.ISLAND_TINSAND: 3,
            CraftingMaterial.ISLAND_COPPER_ORE: 3,
            CraftingMaterial.ISLAND_LOG: 2,
        },
    )
    ISLEWORKS_BRUSH = Item(
        name="Isleworks Brush",
        value=52,
        hours_to_craft=4,
        categories={Category.SUNDRIES, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.SANCTUARY_FUR: 1,
            CraftingMaterial.ISLAND_PALM_LOG: 3,
        },
    )
    ISLEWORKS_BUTTER = Item(
        name="Isleworks Butter",
        value=52,
        hours_to_craft=4,
        categories={Category.INGREDIENTS, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_MILK: 1,
            CraftingMaterial.ISLAND_ROCK_SALT: 3,
        },
    )
    ISLEWORKS_CARAMELS = Item(
        name="Isleworks Caramels",
        value=97,
        hours_to_craft=6,
        categories={Category.CONFECTIONS},
        required_materials={
            CraftingMaterial.ISLAND_SUGARCANE: 4,
            CraftingMaterial.SANCTUARY_MILK: 2,
        },
    )
    ISLEWORKS_CAVALIERS_HAT = Item(
        name="Isleworks Cavaliers Hat",
        value=97,
        hours_to_craft=6,
        categories={Category.ATTIRE, Category.TEXTILES},
        required_materials={
            CraftingMaterial.SANCTUARY_FEATHER: 2,
            CraftingMaterial.ISLAND_COTTON_BALL: 2,
            CraftingMaterial.ISLAND_HEMP: 2,
        },
    )
    ISLEWORKS_CORAL_RING = Item(
        name="Isleworks Coral Ring",
        value=50,
        hours_to_craft=6,
        categories={Category.ACCESSORIES, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_CORAL: 3,
            CraftingMaterial.ISLAND_VINE: 3,
        },
    )
    ISLEWORKS_CORN_FLAKES = Item(
        name="Isleworks Corn Flakes",
        value=62,
        hours_to_craft=4,
        categories={Category.PRESERVED_FOOD},
        required_materials={
            CraftingMaterial.ISLAND_CORN: 2,
            CraftingMaterial.ISLAND_SUGARCANE: 2,
        },
    )
    ISLEWORKS_CROOK = Item(
        name="Isleworks Crook",
        value=144,
        hours_to_craft=8,
        categories={Category.ARMS, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.SANCTUARY_FANG: 4,
            CraftingMaterial.ISLAND_QUARTZ: 2,
            CraftingMaterial.ISLAND_LOG: 2,
        },
    )
    ISLEWORKS_CULINARY_KNIFE = Item(
        name="Isleworks Culinary Knife",
        value=52,
        hours_to_craft=4,
        categories={Category.SUNDRIES, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.ISLAND_CLAW: 1,
            CraftingMaterial.ISLAND_PALM_LOG: 3,
        },
    )
    ISLEWORKS_EARRINGS = Item(
        name="Isleworks Earrings",
        value=52,
        hours_to_craft=4,
        categories={Category.ACCESSORIES, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_FANG: 1,
            CraftingMaterial.ISLAND_VINE: 3,
        },
    )
    ISLEWORKS_ESSENTIAL_DRAUGHT = Item(
        name="Isleworks Essential Draught",
        value=64,
        hours_to_craft=6,
        categories={Category.CONCOCTIONS, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_JELLYFISH: 2,
            CraftingMaterial.ISLAND_PALM_LEAF: 2,
            CraftingMaterial.ISLAND_LAVER: 2,
        },
    )
    ISLEWORKS_FIRESAND = Item(
        name="Isleworks Firesand",
        value=33,
        hours_to_craft=4,
        categories={Category.CONCOCTIONS, Category.UNBURIED_TREASURES},
        required_materials={
            CraftingMaterial.ISLAND_SAND: 2,
            CraftingMaterial.ISLAND_LIMESTONE: 1,
            CraftingMaterial.ISLEWORT: 1,
        },
    )
    ISLEWORKS_GARDEN_SCYTHE = Item(
        name="Isleworks Garden Scythe",
        value=108,
        hours_to_craft=6,
        categories={Category.SUNDRIES, Category.METALWORKS},
        required_materials={
            CraftingMaterial.SANCTUARY_CLAW: 3,
            CraftingMaterial.ISLAND_IRON_ORE: 2,
            CraftingMaterial.ISLAND_PALM_LOG: 1,
        },
    )
    ISLEWORKS_GARNET_RAPIER = Item(
        name="Isleworks Garnet Rapier",
        value=163,
        hours_to_craft=8,
        categories={Category.ARMS, Category.UNBURIED_TREASURES},
        required_materials={
            CraftingMaterial.RAW_ISLAND_GARNET: 2,
            CraftingMaterial.ISLAND_COPPER_ORE: 3,
            CraftingMaterial.ISLAND_TINSAND: 3,
        },
    )
    ISLEWORKS_GRILLED_CLAM = Item(
        name="Isleworks Grilled Clam",
        value=33,
        hours_to_craft=4,
        categories={Category.FOODSTUFFS, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_CLAM: 2,
            CraftingMaterial.ISLAND_LAVER: 2,
        },
    )
    ISLEWORKS_GROWTH_FORMULA = Item(
        name="Isleworks Growth Formula",
        value=163,
        hours_to_craft=8,
        categories={Category.CONCOCTIONS},
        required_materials={
            CraftingMaterial.ISLAND_ALYSSUM: 2,
            CraftingMaterial.ISLEWORT: 3,
            CraftingMaterial.ISLAND_BRANCH: 3,
        },
    )
    ISLEWORKS_HORA = Item(
        name="Isleworks Hora",
        value=86,
        hours_to_craft=6,
        categories={Category.ARMS, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_CARAPACE: 2,
            CraftingMaterial.ISLAND_STONE: 4,
        },
    )
    ISLEWORKS_HORN = Item(
        name="Isleworks Horn",
        value=97,
        hours_to_craft=6,
        categories={Category.SUNDRIES, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_HORN: 2,
            CraftingMaterial.ISLAND_CLAY: 2,
            CraftingMaterial.ISLAND_HEMP: 2,
        },
    )
    ISLEWORKS_IRON_AXE = Item(
        name="Isleworks Iron Axe",
        value=86,
        hours_to_craft=8,
        categories={Category.ARMS, Category.METALWORKS},
        required_materials={
            CraftingMaterial.ISLAND_IRON_ORE: 3,
            CraftingMaterial.ISLAND_LOG: 3,
            CraftingMaterial.ISLAND_SAND: 2,
        },
    )
    ISLEWORKS_JAM = Item(
        name="Isleworks Jam",
        value=93,
        hours_to_craft=6,
        categories={Category.INGREDIENTS},
        required_materials={
            CraftingMaterial.ISLEBERRY: 3,
            CraftingMaterial.ISLAND_SUGARCANE: 2,
            CraftingMaterial.ISLAND_SAP: 1,
        },
    )
    ISLEWORKS_MACUAHUITL = Item(
        name="Isleworks Macuahuitl",
        value=50,
        hours_to_craft=6,
        categories={Category.ARMS, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.ISLAND_PALM_LOG: 3,
            CraftingMaterial.ISLAND_STONE: 3,
        },
    )
    ISLEWORKS_NECKLACE = Item(
        name="Isleworks Necklace",
        value=33,
        hours_to_craft=4,
        categories={Category.ACCESSORIES, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.ISLAND_BRANCH: 3,
            CraftingMaterial.ISLAND_VINE: 1,
        },
    )
    ISLEWORKS_ONION_SOUP = Item(
        name="Isleworks Onion Soup",
        value=93,
        hours_to_craft=6,
        categories={Category.FOODSTUFFS},
        required_materials={
            CraftingMaterial.ISLAND_ONION: 3,
            CraftingMaterial.ISLAND_ROCK_SALT: 2,
            CraftingMaterial.ISLEWORT: 1,
        },
    )
    ISLEWORKS_PARSNIP_SALAD = Item(
        name="Isleworks Parsnip Salad",
        value=57,
        hours_to_craft=4,
        categories={Category.FOODSTUFFS},
        required_materials={
            CraftingMaterial.ISLAND_PARSNIP: 2,
            CraftingMaterial.ISLEWORT: 1,
            CraftingMaterial.ISLAND_SAP: 1,
        },
    )
    ISLEWORKS_PICKLED_RADISH = Item(
        name="Isleworks Pickled_Radish",
        value=124,
        hours_to_craft=8,
        categories={Category.PRESERVED_FOOD},
        required_materials={
            CraftingMaterial.ISLAND_RADISH: 4,
            CraftingMaterial.ISLAND_APPLE: 2,
            CraftingMaterial.ISLAND_SUGARCANE: 2,
        },
    )
    ISLEFISH_PIE = Item(
        name="Islefish Pie",
        value=93,
        hours_to_craft=6,
        categories={Category.CONFECTIONS, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_WHEAT: 3,
            CraftingMaterial.ISLEFISH: 2,
            CraftingMaterial.ISLAND_SUGARCANE: 1,
        },
    )
    ISLEWORKS_PORCELAIN_VASE = Item(
        name="Isleworks Porcelain Vase",
        value=86,
        hours_to_craft=8,
        categories={Category.SUNDRIES, Category.UNBURIED_TREASURES},
        required_materials={
            CraftingMaterial.ISLAND_LEUCOGRANITE: 3,
            CraftingMaterial.ISLAND_QUARTZ: 3,
            CraftingMaterial.ISLAND_CLAY: 2,
        },
    )
    ISLEWORKS_POTION = Item(
        name="Isleworks Potion",
        value=33,
        hours_to_craft=4,
        categories={Category.CONCOCTIONS},
        required_materials={
            CraftingMaterial.ISLAND_PALM_LEAF: 2,
            CraftingMaterial.ISLEWORT: 2,
        },
    )
    ISLEWORKS_PUMPKIN_PUDDING = Item(
        name="Isleworks Pumpkin Pudding",
        value=93,
        hours_to_craft=6,
        categories={Category.CONFECTIONS},
        required_materials={
            CraftingMaterial.ISLAND_PUMPKIN: 3,
            CraftingMaterial.SANCTUARY_EGG: 1,
            CraftingMaterial.SANCTUARY_MILK: 1,
        },
    )
    ISLEWORKS_QUARTZ_RING = Item(
        name="Isleworks Quartz Ring",
        value=86,
        hours_to_craft=8,
        categories={Category.ACCESSORIES, Category.UNBURIED_TREASURES},
        required_materials={
            CraftingMaterial.ISLAND_QUARTZ: 3,
            CraftingMaterial.ISLAND_IRON_ORE: 3,
            CraftingMaterial.ISLAND_STONE: 2,
        },
    )
    ISLEWORKS_RIBBON = Item(
        name="Isleworks Ribbon",
        value=64,
        hours_to_craft=6,
        categories={Category.ACCESSORIES, Category.TEXTILES},
        required_materials={
            CraftingMaterial.ISLAND_COTTON_BALL: 2,
            CraftingMaterial.ISLAND_COPPER_ORE: 2,
            CraftingMaterial.ISLAND_VINE: 2,
        },
    )
    ISLEWORKS_ROPE = Item(
        name="Isleworks Rope",
        value=43,
        hours_to_craft=4,
        categories={Category.SUNDRIES, Category.TEXTILES},
        required_materials={
            CraftingMaterial.ISLAND_HEMP: 2,
            CraftingMaterial.ISLEWORT: 1,
            CraftingMaterial.ISLAND_VINE: 1,
        },
    )
    ISLEWORKS_SALT_COD = Item(
        name="Isleworks Salt Cod",
        value=64,
        hours_to_craft=6,
        categories={Category.PRESERVED_FOOD, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLEFISH: 4,
            CraftingMaterial.ISLAND_ROCK_SALT: 2,
        },
    )
    ISLEWORKS_SAUERKRAUT = Item(
        name="Isleworks Sauerkraut",
        value=48,
        hours_to_craft=4,
        categories={Category.PRESERVED_FOOD},
        required_materials={
            CraftingMaterial.ISLAND_CABBAGE: 1,
            CraftingMaterial.ISLAND_ROCK_SALT: 3,
        },
    )
    ISLEWORKS_SCALE_FINGERS = Item(
        name="Isleworks Scale Fingers",
        value=144,
        hours_to_craft=8,
        categories={Category.ATTIRE, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_CARAPACE: 4,
            CraftingMaterial.ISLAND_IRON_ORE: 2,
            CraftingMaterial.ISLAND_COTTON_BALL: 2,
        },
    )
    ISLEWORKS_SHARK_OIL = Item(
        name="Isleworks Shark Oil",
        value=163,
        hours_to_craft=8,
        categories={Category.SUNDRIES, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_HAMMERHEAD: 2,
            CraftingMaterial.ISLAND_LAVER: 3,
            CraftingMaterial.ISLAND_SAP: 3,
        },
    )
    ISLEWORKS_SHEEPFLUFF_RUG = Item(
        name="Isleworks Sheepfluff Rug",
        value=108,
        hours_to_craft=6,
        categories={Category.FURNISHINGS, Category.CREATURE_CREATIONS},
        required_materials={
            CraftingMaterial.SANCTUARY_FLEECE: 3,
            CraftingMaterial.ISLAND_COTTON_BALL: 2,
            CraftingMaterial.ISLAND_HEMP: 1,
        },
    )
    ISLEWORKS_SILVER_EAR_CUFFS = Item(
        name="Isleworks Silver Ear Cuffs",
        value=163,
        hours_to_craft=8,
        categories={Category.ACCESSORIES, Category.METALWORKS},
        required_materials={
            CraftingMaterial.ISLAND_SILVER_ORE: 2,
            CraftingMaterial.ISLAND_TINSAND: 3,
            CraftingMaterial.ISLAND_CORAL: 3,
        },
    )
    ISLEWORKS_SPRUCE_ROUND_SHIELD = Item(
        name="Isleworks Spruce Round Shield",
        value=163,
        hours_to_craft=8,
        categories={Category.ATTIRE, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.ISLAND_SPRUCE_LOG: 2,
            CraftingMaterial.ISLAND_COPPER_ORE: 3,
            CraftingMaterial.ISLAND_STONE: 3,
        },
    )
    ISLEWORKS_SQUID_INK = Item(
        name="Isleworks Squid Ink",
        value=43,
        hours_to_craft=4,
        categories={Category.INGREDIENTS, Category.MARINE_MERCHANDISE},
        required_materials={
            CraftingMaterial.ISLAND_SQUID: 2,
            CraftingMaterial.ISLAND_ROCK_SALT: 2,
        },
    )
    ISLEWORKS_SWEET_POPOTO = Item(
        name="Isleworks Sweet Popoto",
        value=86,
        hours_to_craft=6,
        categories={Category.CONFECTIONS},
        required_materials={
            CraftingMaterial.ISLAND_POPOTO: 2,
            CraftingMaterial.SANCTUARY_MILK: 1,
            CraftingMaterial.ISLAND_SAP: 3,
        },
    )
    ISLEWORKS_TOMATO_RELISH = Item(
        name="Isleworks Tomato Relish",
        value=62,
        hours_to_craft=4,
        categories={Category.INGREDIENTS},
        required_materials={
            CraftingMaterial.ISLAND_TOMATO: 2,
            CraftingMaterial.ISLAND_SUGARCANE: 1,
            CraftingMaterial.ISLEWORT: 1,
        },
    )
    ISLEWORKS_TUNIC = Item(
        name="Isleworks Tunic",
        value=86,
        hours_to_craft=6,
        categories={Category.ATTIRE, Category.TEXTILES},
        required_materials={
            CraftingMaterial.SANCTUARY_FLEECE: 2,
            CraftingMaterial.ISLAND_VINE: 4,
        },
    )
    ISLEWORKS_VEGETABLE_JUICE = Item(
        name="Isleworks Vegetable Juice",
        value=93,
        hours_to_craft=6,
        categories={Category.CONCOCTIONS},
        required_materials={
            CraftingMaterial.ISLAND_CABBAGE: 3,
            CraftingMaterial.ISLEWORT: 2,
            CraftingMaterial.ISLAND_LAVER: 1,
        },
    )
    ISLEWORKS_WOODEN_CHAIR = Item(
        name="Isleworks Wooden Chair",
        value=50,
        hours_to_craft=6,
        categories={Category.FURNISHINGS, Category.WOODWORKS},
        required_materials={
            CraftingMaterial.ISLAND_LOG: 4,
            CraftingMaterial.ISLAND_VINE: 2,
        },
    )

    def __str__(self) -> str:
        return self.value.name

    @classmethod
    def items_in_category(cls, category: Category) -> Set["WorkshopItem"]:
        return {item for item in cls if category in item.value.categories}

    @property
    def items_in_same_categories(self) -> Set["WorkshopItem"]:
        return {
            item
            for item in WorkshopItem
            if item != self
            and item.value.categories.intersection(self.value.categories)
        }
