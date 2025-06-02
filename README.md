# Space-Shooter
Space Shooter is a popular arcade-style game genre where players control a spaceship to defend against waves of invading aliens or enemies. The core gameplay involves moving the spaceship horizontally at the bottom of the screen while shooting projectiles upward to destroy enemy ships before they reach the player’s base. The game typically features increasing difficulty as enemies move faster or in larger numbers, requiring quick reflexes and strategic shooting. Space Shooter games provide fast-paced action, simple controls, and addictive gameplay, making them a classic and accessible choice for beginners learning game development. This project implements these concepts using Python and Pygame to create a fun, interactive experience with sound effects, scoring, and game-over conditions.

## Features
- Move the spaceship left and right using arrow keys.
- Shoot bullets by pressing the spacebar to hit aliens.
- Fifteen aliens move side-to-side and descend gradually.
- Bullet-alien collisions reset aliens and increase score.
- Background music plays continuously during gameplay.
- Laser and explosion sound effects trigger on shooting and hits.
- Display current score in the top-left corner.
- Game ends with “GAME OVER” if aliens reach near the spaceship.

## Project Workflow
- Initialize Pygame and mixer for graphics and sound.
- Load images and sounds required for the game.
- Set initial positions and speeds for spaceship, aliens, and bullets.
- Run game loop to process input, update positions, detect collisions, and draw.
- Update score and reset aliens and bullets on successful hits.
- Check for game over when aliens cross a vertical limit.
- Continuously refresh the display until the player quits or game ends.

## Model Used
- Event-driven loop that updates game state each frame.
- Multiple aliens managed with parallel lists for positions and speeds.
- Collision detected using distance formula between bullet and aliens.
- Single bullet state controlled to allow one bullet on screen at a time.
- Game over state triggered when aliens descend too far.

## Installation
Install Python:
- Make sure Python 3.x is installed on your system.
Download from:[ https://www.python.org/downloads/](https://www.python.org/downloads/)

Install Pygame Library:
- Open command prompt or terminal and run:
```bash
  pip install pygame
```

Prepare Game Assets:
- back.wav (background music)
- laser.wav (laser sound effect)
- explosion.wav (explosion sound effect)
- icon.png (game window icon)
- background.png (background image)
- arcade.png (spaceship image)
- enemy.png (alien enemy image)
- bullet.png (bullet image)

Run the Game Script:
- Navigate to the directory containing the script and assets.
- Run the Python script:
```bash
  python space_shooter_game.py
```

Controls:
- Use Left Arrow and Right Arrow keys to move spaceship.
- Press Spacebar to shoot bullets.
- Close the window or press the close button to exit.


  
