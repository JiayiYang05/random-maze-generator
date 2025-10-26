# 🎛️ Random Maze Generator | DFS Application
<br><br>

## 🚀 Overview

> **"A maze is essentially a spanning tree of the grid!"**<br>
> This Python project generates mazes using a Randomized Depth-First Search (DFS) algorithm with backtracking. 

<br><br>
- ✅**Perfect Mazes:** Every cell is reachable, with exactly one path between any two points (no cycles).
- ✅**Customizable Size:** Easily generate mazes of different sizes.
- ✅**Visual Output:** The maze is displayed as a clean grid using Python's `matplotlib`.
  
---
<br><br>
## 📸 How it looks?

### 1. Maze Construction

<div align="center">
  <img src="assets/maze_construction.gif" width="600" />
  
  *Animated random maze construction.*
</div>


### 2. Maze Solution

<table width="100%" style="border-collapse: collapse;" align="center">
  <tr>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;">15 x 15</h3>
      <img src="assets/15x15maze.png" alt="ALU Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;">15 x 15 solution</h3>
      <img src="assets/15x15maze-with-solution.png" alt="ALU Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"></p>
    </td>
  </tr>
  
  <tr>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;">25 x 25</h3>
      <img src="assets/25x25maze.png" alt="ALU Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;">25 x 25 solution</h3>
      <img src="assets/25x25maze-with-solution.png" alt="ALU Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"></p>
    </td>
  </tr>
</table>

---
<br><br>
## 🏗️ How it works?

```mermaid
flowchart TD
    A[Step 1: <br>Perfect Maze = Spanning Tree] --> B[Step 2: <br>Choose alogorithm to generate spanning tree]
    
    B --> C[Prim's]
    B --> D[DFS<br>Long, winding paths offer exploratory feelings]
    B --> E[Wilson's]
    B --> F[Kruskal's] 
    D --> G[Step 3: <br>Code Design<br>Forward: Long paths + Backtrack: Dead-ends]
```
