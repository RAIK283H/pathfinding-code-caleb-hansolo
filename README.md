# Pathfinding Starter Code

<h1>Random Pathin Explanation</h1>
<br>
My random pathing algorithm essentially makes the current node the start of the graph, and then chooses a random edge, 
chooses the node it connects to as its next current node, and repeats until it has found target and then stops when
it reaches the end after finding its target.

<br>
<br>
<h1>New Statistic - Most visited node</h1>
This new statistic that I added shows the node that has been visited the most in the path. While this doesn't matter 
so much for other pathfinding algorithms like DFS and Djikstra, for random path, it shows which node the walk gets 
"caught up on" the most, showing the area/node where the most time was spent in the path.