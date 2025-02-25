# Version 4.1 - Instructions
  **(written by our favourite teacher)**
  
We often require our program to do similar things in different parts of our code.
For example, we will need to animate our character, but will also be animating the enemies in a similar way.
Instead of writing functions that essentially do the same thing within each class, we can create a separate file that stores all these functions, and import them when they are needed.

1. Create an image_handler.py that will deal with all the image_handling like importing folders
2. The Character class represents a game character with movement functionality. The code utilizes 'config' and 'image_handle' for configuration settings and image handling, respectively.

https://replit.com/@JasonLiu6166/lvl-3-Character-Sprite-Example-Code#image_handler.py

### [Create]

Version 4.1.1 [Create] - image_handler.py

Version 4.1.2 [Update] -  config.py

Version 4.1.3 [Create] - /pics/ folder (find 5-8 images)

# Version 4.2 - Character Sprite
We will now implement our character with some basic controls.

1. Create an character.py and write the Character class.
2. character.py should import and utilize import_folder from image_handler
3. character.py should have an input() method that checks user input
4. character.py should have a move() method that moves the character according to user input

5. Add to config and have a third layer for level 1 called LEVEL_1_SPRITES. We will be using this to dictate where the character (and enemies) spawn
6. Add a spawn_sprites method in level_1.py that will iterate through LEVEL_1_SPRITES and spawn the character
Hint: This is very similar to how we spawned the tiles and obstacles

### [Create]
Version 4.2.1 - [Create] character.py

Version 4.2.2 - [Update] level_1.py

