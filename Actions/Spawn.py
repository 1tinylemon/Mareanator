import random

naturalBiomes = {
    "river": {
        "description": "A flowing body of water.",
        "fish": "Aquatic creatures that live in the river.",
        "ducks": "Water birds commonly found in rivers.",
        "water plants": "Plants that grow in or around water."
    },
    "forest": {
        "description": "A dense area with many trees.",
        "trees": "Tall woody plants that cover the forest.",
        "animals": "Various wildlife that inhabit the forest.",
        "mushrooms": "Fungi that grow on the forest floor."
    },
    "mountain": {
        "description": "A tall and rocky landform.",
        "rocks": "Large stones and rocky formations in the mountains.",
        "eagles": "Birds of prey that soar high in the mountains.",
        "mountain goats": "Hardy mammals adapted to mountainous terrain."
    },
    "cave": {
        "description": "A hollow underground space.",
        "bats": "Flying mammals that inhabit caves.",
        "stalactites": "Hanging mineral formations found in caves.",
        "minerals": "Various valuable minerals found within caves."
    },
    "village": {
        "description": "A small settlement with houses.",
        "houses": "Residential buildings where villagers live.",
        "villagers": "Inhabitants of the village.",
        "farms": "Agricultural areas where crops are grown."
    },
    "dungeon": {
        "description": "An underground maze or structure.",
        "monsters": "Hostile creatures that dwell in the dungeon.",
        "treasure chests": "Containers with valuable items hidden in the dungeon.",
        "traps": "Mechanisms designed to hinder or harm intruders."
    },
    "city": {
        "description": "A large urban area.",
        "buildings": "Structures that make up the cityscape.",
        "streets": "Roads and pathways that connect different areas of the city.",
        "shops": "Establishments where goods and services are provided."
    }
}

farmZones = {
    "pve": {
        "description": "A player versus environment farming zone.",
        "crops": "Plants cultivated for food or other purposes.",
    },
    "lowxp": {
        "description": "A farming zone with low experience gain.",
        "simple crops": "Easy-to-grow plants with low experience gain.",
        "pets": "Friendly animals kept as companions on the farm.",
        "garden decorations": "Ornaments and decorative items for the farm."
    }
}

def naturalSpawn(min_spawn=1, max_spawn=10):
    random_biome = random.choice(list(naturalBiomes.keys()))
    biome_description = naturalBiomes[random_biome]["description"]
    
    available_elements = list(naturalBiomes[random_biome].keys())[1:]
    num_elements = random.randint(min_spawn, min(max_spawn, len(available_elements)))
    spawned_elements = random.sample(available_elements, num_elements)
    
    print(f"Spawning in {random_biome}: {biome_description}")
    print(f"Spawned elements: {', '.join(spawned_elements)}")