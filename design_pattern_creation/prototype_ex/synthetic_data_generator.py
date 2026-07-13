from abc import ABC, abstractmethod
import copy
import random
from typing import List
import json

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class EnemyPrototype(Prototype):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Enemy(name={self.name}, health={self.health}, attack_power={self.attack_power})"

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "attack_power": self.attack_power
        }

class SyntheticDataGenerator:
    def __init__(self, prototype: EnemyPrototype):
        self.prototype = prototype

    def generate_batch(self, size: int, variation_ranges: dict = None) -> List[EnemyPrototype]:
        """Generate a batch of enemies with controlled random variations."""
        if variation_ranges is None:
            variation_ranges = {
                "health": (-20, 20),
                "attack_power": (-5, 5)
            }
        
        variants = []
        for i in range(size):
            # Clone the prototype
            variant = self.prototype.clone()
            
            # Apply random variations within specified ranges
            variant.health += random.randint(*variation_ranges["health"])
            variant.attack_power += random.randint(*variation_ranges["attack_power"])
            
            # Ensure values don't go below 1
            variant.health = max(1, variant.health)
            variant.attack_power = max(1, variant.attack_power)
            
            # Add suffix to name for unique identification
            variant.name = f"{variant.name}_{i+1}"
            
            variants.append(variant)
        
        return variants

    def save_to_json(self, variants: List[EnemyPrototype], filename: str):
        """Save the generated data to a JSON file."""
        data = [variant.to_dict() for variant in variants]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

def main():
    # Create base prototypes for different enemy types
    goblin_prototype = EnemyPrototype("Goblin", 100, 15)
    troll_prototype = EnemyPrototype("Troll", 200, 25)
    
    # Create generators for each enemy type
    goblin_generator = SyntheticDataGenerator(goblin_prototype)
    troll_generator = SyntheticDataGenerator(troll_prototype)
    
    # Generate different batches with different variation ranges
    
    # Regular variations
    goblins = goblin_generator.generate_batch(10)
    print("Generated Goblins:")
    for goblin in goblins:
        print(goblin)
    
    # High variations for stronger enemies
    high_variations = {
        "health": (-50, 50),
        "attack_power": (-10, 10)
    }
    
    trolls = troll_generator.generate_batch(5, high_variations)
    print("\nGenerated Trolls (high variation):")
    for troll in trolls:
        print(troll)
    
    # Save all generated data
    all_enemies = goblins + trolls
    goblin_generator.save_to_json(all_enemies, "synthetic_enemies.json")
    print("\nAll enemy data saved to synthetic_enemies.json")

if __name__ == "__main__":
    main()