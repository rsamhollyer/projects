# RACE CARS

This simple simulator runs a 'Drag-Race' type game where the human player races against 3 other computer players.

The AI uses simple set of conditionals and loops to 'roll-die' as a pseudo random number generator to make each game different.

The game uses general classes to create the game with it's methods and the cars with their own methods. It runs a function called start_game to initialize the game and start the player playing.

In the game itself, the computer players go first, rolling their die and either moving or not. Once they have all gone, the player gets their chance to go. The player's movement is determined by one of two selections; they can drive with more risk or not, which starts a die roll for them.

I would like to make this ia bit more robust by incorporating a way to change the lenth of the race and add more vehicles to the race pool.