import time

class House:
    def __init__(self):
        self.inventory = []
        self.score = 0
        self.npcs = {
            "ghost": {
                "description": "A translucent figure floats in front of you.",
                "dialogue": "Help me find my lost locket, and I'll reveal a secret.",
                "item_required": "locket",
                "reward": "You found the ghost's locket.\nYou get 20 points",
            },
            "witch": {
                "description": "A wicked witch stands before you.",
                "dialogue": "I need a black cat's hair for my potion. Find it for me, and I'll reward you.",
                "item_required": "black cat hair",
                "reward": "Excellent! You have what I need. Now, let's begin the challenge.\nSolve this math puzzle within 60 seconds:",
            },
            "knight": {
                "description": "A brave knight in shining armor awaits your arrival.",
                "dialogue": "I've lost my sword in this haunted house. Help me find it, and I'll protect you.",
                "item_required": "sword",
                "reward": "Ah, you have the knight's sword! I challenge you to a word puzzle.",
            },
            "sorcerer": {
                "description": "A mysterious sorcerer with a pointed hat stands here.",
                "dialogue": "I sense you seek knowledge. Solve my riddle, and I'll share a secret.",
                "riddle": "What has keys but can't open locks?",
                "answer": "piano",
                "reward": "You answered my riddle correctly. You get 20 points",
            },
            "queen": {
                "description": "A brave queen",
                "dialogue": "Fight me if you can.",
                "riddle": "Does the night kingdom really exist?",
                "answer": "yes",
                "reward": "You answered my riddle correctly. You get 20 points",
            }
        }

    def talk_to(self, character):
        if character in self.npcs:
            npc = self.npcs[character]
            item_required = npc.get("item_required")

            if item_required and item_required not in self.inventory:
                return f"{npc['dialogue']} You need {item_required} if you need my help."

            if "riddle" in npc:
                print(npc["reward"])
                answer = input(npc["riddle"] + " ")
                if answer.lower() == npc["answer"]:
                    self.score += 20
                    return f"You answered correctly! {npc['reward']} Updated score is {self.score}."
                else:
                    return "Wrong answer! You receive no reward."

            return f"{npc['reward']} Updated score is {self.score}."
        else:
            return f"{character} is not there!"

# Example usage:
house = House()
print(house.talk_to("ghost"))
print(house.talk_to("witch"))
print(house.talk_to("sorcerer"))
print(house.talk_to("queen"))
print(house.talk_to("non_existent_npc"))
