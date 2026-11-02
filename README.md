# SquareUp

A Hotseat Strategy Game by Max Siuchta, Kairav Patel, Aman Ullah, and Elbron Khido

## To Install: 
Clone the Repository
```
git clone https://github.com/msiu7/MW-Strategy-Game
```

## To Run: 
### On Windows:
```
py game.py
```

### On Linux:
```
python game.py
``` 
or
```
python3 game.py
```
Note: pygame also has to be installed.
```
pip install pygame
```

## The Game:
At the beginning of the game, you choose how many players there are in the game, and how many turns you want the game to go on for. 
Whoever has the most points at the end of the game wins. 

## Scoring:
Points are given for controlling land, and having population. To be specific, land tiles are worth a base score of 5 points,
with 15 points for each level the tile has (more on that later), ocean tiles are worth 3 points, and each population is worth 1 point.

## Mechanics:
### Resources:
In the game there are 5 resources: Gold, which is used to buy tiles; Brick, which is used to upgrade tile levels; Food, which is used to grow population; Stone which is used to manage and move population; and Wood, which is used for tile upkeep.

### Tiles:
Each different type of tile produces different resources, and in varying amounts. The cost of a tile is dependent on its resource production. There are 4 types of land tiles.

Forest: Food (Range: [1, 5]) and Wood (Range: [1, 5])

Coast: Food (Range: [1, 5]) and Brick (Range: [1, 5])

Mountain: Stone (Range: [1, 5]) and Gold (Range: [1, 5])

Plains: Food (Range: [1, 10])

Ocean tiles work a little differently (see Treasure Hunting).

### Levels:
By default, when a tile is bought, it starts with level 1, which gives production of exactly the amount of resources stated when buying the tile per civilian. For each subsequent level, the production is multiplied by 2. The max level is 3, and the cost to upgrade a tile gets progressively more expensive as levels increase. It costs 1 wood per level to keep a tile at its level. If you don't have enough wood, you will start to lose levels. A tile can fall to level 0. At this point, it no longer produces anything.

### Population Growth and Decay:
Each population consumes 4 food per turn. If you don't have enough food to maintain your population, they will start to starve. Land tiles must always have at least 1 population, if starvation causes all population on a tile to be lost, then the tile is lost as well. Excess food and high food production creates natural population growth.

### Population Management:
When population are created, they are assigned initially as unemployed, which means they don't do anything. You can choose to either make them a civilian or a soldier. Civilians create production on a tile, each civilian gives production according to its tile, and the tile's level. Thus, having more civilians on a tile multiplies that tile's total production. Soldiers don't provide any production, but they can engage in battle. The first change from unemployed to either civilian or soldier is free. After that, civilians can be made soldiers, and vice versa, but it costs stone.

### Population Movement
Population can also be moved to different tiles. They can only be moved between adjacent tile, and each movement also costs stone.

### Battle:
Battles are essentially done by moving soldiers onto another player's tile. The result of the battle is based on dice rolls. If the attacking player defeats all soldiers on a tile, that player obtains that tile, its population, and its level. Unlike regular movement, battles don't cost any stone.

### Treasure Hunting:
Unlike a simple production stat like land tiles, ocean tiles have a treasure chance stat. If there is at least 1 civilian on an ocean tile, there is a chance of finding a random resource (amount in range [1, 20]). After treasure is found, there is a cooldown before treasure can be found on that tile again.

## Buttons/Controls:
### Bottom UI Bar:
From Right To Left:

End Turn - self explanatory, just click it to end your turn

Resource View - tells you your production per turn and how many of each resource you have

Civilian View - gives how many civilians are on each tile

Soldier View - gives how many soldiers are on each tile

Move Toggle - Only visible when in Civilian or Soldier View. When Green: use 2 clicks to move population, the first click tells where you want to move from, the second click gives where you want to move to. When Red, no movement will happen. Click the Move Toggle button itself in order to switch between green and red.

Tile Level View - gives tile level per tile

Treasure View - gives how many resources were found at sea last turn

Scoreboard - click to show the scoreboard

In general, for per tile views, players can only see values for tiles they own, and tiles adjacent to ones they own.

### On Screen Popups:
Buy Tile - if you click on an unowned tile, a bar split green and red at the bottom will be at the bottom of the popup. Click green to buy, red to cancel. You can only buy tiles adjacent to tiles you already own. If you don't own any tiles, your first tile must be a land tile.

For Owned Tiles - after clicking on an owned tile you have more options: the red button as usual to exit, the Manage Population button, which allows you to switch between soldiers and civilians, and the Upgrade Tile button. After pressing upgrade tile, click the white button in the middle to actually upgrade the tile.

# Enjoy! :)
