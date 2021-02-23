from sample import arcade, disney, zoo,randium
import random

if __name__ == "__main__":
    m = random.choice([arcade, disney, randium, zoo])
    m.madlib()