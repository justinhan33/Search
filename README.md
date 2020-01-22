# Search
In this project, we will implement general search algorithms and apply them to different Pacman scenarios in order to help our Pacman agent find paths through his maze world, both to reach a particular location and to collect food (the dots) efficiently.

## Instructions:
1. Download the associated files
2. After downloading and changing to the directory, run the following command `python3 pacman.py` to play the Pacman maze arcade game normally
3. Otherwise, refer to the `commands.txt` file for a list of commands that allows the user to see the different search algorithms (DFS, BFS, UCS, A*) in action under various scenarios (different mazes)

## Notes:
* `GoWestAgent` is the simplest search agent which always goes West (a trivial reflex agent).
* __Admissibility vs. Consistency:__ Heuristics are just functions that take search states and return numbers that estimate the cost to a nearest goal. More effective heuristics will return values closer to the actual goal costs. To be __admissible__, the heuristic values must be lower bounds on the actual shortest path cost to the nearest goal (and non-negative). To be __consistent__, it must additionally hold that if an action has cost c, then taking that action can only cause a drop in heuristic of at most c.
* Admissibility __does not__ guarantee consistency. However, consistency guarantees admissibility.
* Running the commands for A* search may longer than the others (so do not panic if nothing happens for the first few seconds!).
