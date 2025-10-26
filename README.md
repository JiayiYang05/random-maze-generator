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

### 1. The Complete System
<div align="center">

  <img src="images/complete.png" alt="Completed Computer Image Demo" width="500"/>

*The fully assembled 8-bit breadboard computer*

</div>


### 2. Component Close-ups

<table width="100%" style="border-collapse: collapse;">
  <tr>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> ALU Unit</h3>
      <img src="images/alu.png" alt="ALU Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>ALU able to add and subtract.</em></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> Clock</h3>
      <img src="images/clock.png" alt="Clock Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>Adjustable-speed clock module with a manual mode.</em></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> Registers</h3>
      <img src="images/register.png" alt="Registers Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>Three 8-bit registers: A, B, and IR.</em></p>
    </td>
  </tr>
  <tr>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> RAM</h3>
      <img src="images/ram.png" alt="RAM Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>16 bytes of RAM with 4-bit addresses.</em></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> Program Counter</h3>
      <img src="images/program-counter.png" alt="Program Counter Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>PC keeps track of currently executing instructions.</em></p>
    </td>
    <td width="33.33%" align="center" style="padding: 20px; border: 1px solid #e1e4e8; vertical-align: top; width: 300px; height: 350px;">
      <h3 style="font-size: 1.4em; margin: 0 0 20px 0;"> Control Unit</h3>
      <img src="images/control.png" alt="Control Unit Image Demo" width="250" style="border-radius: 8px;"/><br>
      <p style="margin: 15px 0 0 0;"><em>Instruction decoding and execution logic.</em></p>
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
