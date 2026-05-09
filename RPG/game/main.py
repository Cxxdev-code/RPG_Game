
from models.hero import Hero
from models.enemy import Enemy
from models.DataManager import DataManager
from models.items import Item
from manager.game import Game
import random
import os
import time


if __name__ == "__main__":
    manager = Game()
    manager.start_battle()


