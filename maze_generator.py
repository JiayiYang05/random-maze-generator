import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import colors
import random
from PIL import Image
import io
import os

def numgrid(shape, n):
    """
    Recreate MATLAB's numgrid function
    Creates a numbered grid with zeros on boundaries
    """
    if shape == 'S':  # Square region
        grid = np.zeros((n, n), dtype=int)
        # Number interior points sequentially
        counter = 1
        for i in range(1, n-1):
            for j in range(1, n-1):
                grid[i, j] = counter
                counter += 1
        return grid
    return None

def delsq(grid):
    """
    Recreate MATLAB's delsq function
    Creates discrete Laplacian for the grid
    """
    n = grid.shape[0]
    size = np.max(grid)  # Total number of interior points
    if size == 0:
        return np.zeros((0, 0))
    
    # Create sparse Laplacian matrix
    D = np.zeros((size, size))
    
    for i in range(n):
        for j in range(n):
            current = grid[i, j]
            if current == 0:
                continue
                
            # Check neighbors: up, down, left, right
            neighbors = []
            if i > 0 and grid[i-1, j] > 0:  # up
                neighbors.append(grid[i-1, j])
            if i < n-1 and grid[i+1, j] > 0:  # down  
                neighbors.append(grid[i+1, j])
            if j > 0 and grid[i, j-1] > 0:  # left
                neighbors.append(grid[i, j-1])
            if j < n-1 and grid[i, j+1] > 0:  # right
                neighbors.append(grid[i, j+1])
            
            # Diagonal: number of neighbors
            D[current-1, current-1] = len(neighbors)
            
            # Off-diagonal: -1 for connections
            for neighbor in neighbors:
                D[current-1, neighbor-1] = -1
    
    return D

def wall(p, q, m):
    """
    Calculate which barrier to remove between cells p and q
    Converts 1D cell indices to 2D barrier coordinates
    """
    # Convert 1D cell indices to 2D coordinates in cell grid
    row_p = (p - 1) // m
    col_p = (p - 1) % m
    row_q = (q - 1) // m  
    col_q = (q - 1) % m
    
    # The wall between cells p and q is at:
    # For horizontal move: barrier at (max(row_p, row_q), col_p * 2 + 1)
    # For vertical move: barrier at (row_p * 2 + 1, max(col_p, col_q))
    
    if row_p == row_q:  # Horizontal move
        barrier_row = row_p * 2 + 1
        barrier_col = max(col_p, col_q) * 2 + 2
    else:  # Vertical move
        barrier_row = max(row_p, row_q) * 2 + 2
        barrier_col = col_p * 2 + 1
    
    # Convert to 1D index in barrier graph
    n_barriers = m * 2 + 1
    i = barrier_row * n_barriers + barrier_col
    
    # For simplicity, we'll use a different approach
    # Just return unique identifiers for the barrier
    return min(p, q), max(p, q)

def generate_maze(n=15, branching='middle', create_gif=True):
    """
    Generate a random maze using DFS with backtracking
    """
    m = n - 1  # Cell grid size
    
    print(f"Generating {n}x{n} barrier grid -> {m}x{m} cell grid")
    print(f"Expected cells: 1 to {m*m}")

    # Create cell graph C - we'll build this manually
    C = nx.Graph()
    
    # Add all cells as nodes
    for i in range(1, m*m + 1):
        C.add_node(i)
    
    # Initialize algorithm state
    available = list(range(1, m*m + 1))  # Nodes we haven't visited
    branches = []
    tree = []  # Will store edges as (p, q) pairs
    p = 1  # Start at first cell
    
    # For GIF creation
    gif_frames = []
    
    iteration = 0
    while available:
        iteration += 1
        if iteration > 10000:  # Safety break
            print("Iteration limit reached")
            break
            
        # Mark current cell as visited
        if p in available:
            available.remove(p)
        
        # Get unvisited neighbors
        unvisited_neighbors = []
        
        # Check all four possible neighbors
        current_row = (p - 1) // m
        current_col = (p - 1) % m
        
        # Left neighbor
        if current_col > 0:
            left_neighbor = p - 1
            if left_neighbor in available:
                unvisited_neighbors.append(left_neighbor)
        
        # Right neighbor  
        if current_col < m - 1:
            right_neighbor = p + 1
            if right_neighbor in available:
                unvisited_neighbors.append(right_neighbor)
        
        # Up neighbor
        if current_row > 0:
            up_neighbor = p - m
            if up_neighbor in available:
                unvisited_neighbors.append(up_neighbor)
        
        # Down neighbor
        if current_row < m - 1:
            down_neighbor = p + m
            if down_neighbor in available:
                unvisited_neighbors.append(down_neighbor)

        if unvisited_neighbors:
            # Random choice from available neighbors
            q = random.choice(unvisited_neighbors)
            tree.append((p, q))
            
            # Add edge to cell graph
            C.add_edge(p, q)
            
            # If multiple choices, remember this branch point
            if len(unvisited_neighbors) > 1:
                branches.append(p)
            
            p = q
            
            # Capture frame for GIF (only capture every few steps to reduce file size)
            if create_gif and iteration % 2 == 0:  # Capture every 2nd step
                frame = capture_maze_frame(C, tree, p, m, iteration)
                gif_frames.append(frame)
                
        else:
            # Backtrack
            if not branches:
                break
                
            if branching == 'first':
                idx = 0
            elif branching == 'last':
                idx = len(branches) - 1
            else:  # 'middle'
                idx = len(branches) // 2
                
            p = branches[idx]
            del branches[idx]
    
    print(f"Maze generation complete. Graph has {C.number_of_nodes()} nodes and {C.number_of_edges()} edges")
    print(f"Nodes in graph: {sorted(list(C.nodes()))[:10]}...")  # Show first 10 nodes
    
    # Create GIF if requested
    if create_gif and gif_frames:
        # Add a few extra frames at the end to show completion
        for _ in range(3):
            final_frame = capture_maze_frame(C, tree, p, m, iteration, final=True)
            gif_frames.append(final_frame)
        
        gif_path = create_maze_gif(gif_frames)
        return C, tree, gif_path
    
    return C, tree, None

def capture_maze_frame(C, tree, current_cell, m, iteration, final=False):
    """Capture current maze state as an image frame"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Plot cell graph and current path
    if final:
        ax1.set_title(f'Maze Complete! (Step {iteration})')
    else:
        ax1.set_title(f'Maze Construction Progress (Step {iteration})')
    
    pos_C = {i: ((i-1) % m, (i-1) // m) for i in C.nodes()}
    
    # Draw all cells
    nx.draw_networkx_nodes(C, pos_C, ax=ax1, node_size=50, node_color='lightgray')
    
    # Draw current tree edges
    if tree:
        tree_graph = nx.Graph()
        tree_graph.add_edges_from(tree)
        nx.draw_networkx_edges(tree_graph, pos_C, ax=ax1, edge_color='red', width=2)
    
    # Highlight current cell
    if current_cell in pos_C:
        node_color = 'blue' if final else 'green'
        nx.draw_networkx_nodes(C, pos_C, nodelist=[current_cell], ax=ax1, 
                              node_size=100, node_color=node_color)
    
    # Plot the maze representation
    ax2.set_title('Maze Walls')
    plot_maze_walls(ax2, C, m)
    
    ax1.set_aspect('equal')
    ax2.set_aspect('equal')
    ax1.set_xlim(-1, m)
    ax1.set_ylim(-1, m)
    ax2.set_xlim(-1, m)
    ax2.set_ylim(-1, m)
    
    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=80)  # Reduced DPI for smaller file
    buf.seek(0)
    plt.close(fig)  # Close the figure to free memory
    return Image.open(buf)

def create_maze_gif(frames, filename="maze_construction.gif"):
    """Create and save an animated GIF from the frames"""
    if not frames:
        print("No frames to create GIF")
        return None
    
    # Save in current directory (works in Colab)
    gif_path = filename
    
    # Save as GIF
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=400,  # milliseconds per frame
        loop=0,  # 0 = infinite loop
        optimize=True,
        quality=85  # Reduce quality for smaller file
    )
    
    print(f"Animated GIF saved to: {gif_path}")
    print(f"Total frames: {len(frames)}")
    print(f"File size: {os.path.getsize(gif_path) / 1024:.1f} KB")
    
    # Display the GIF in Colab
    from IPython.display import Image as IPImage
    display(IPImage(filename=gif_path))
    
    # Provide download link
    from google.colab import files
    files.download(gif_path)
    
    return gif_path

def plot_maze_walls(ax, C, m):
    """Plot the maze as walls between cells"""
    # Draw all possible walls
    for i in range(m):
        for j in range(m):
            cell = i * m + j + 1
            x, y = j, i
            
            # Check right wall
            if j < m - 1:
                right_cell = cell + 1
                if not C.has_edge(cell, right_cell):
                    ax.plot([x + 1, x + 1], [y, y + 1], 'k-', linewidth=2)
            
            # Check bottom wall
            if i < m - 1:
                bottom_cell = cell + m
                if not C.has_edge(cell, bottom_cell):
                    ax.plot([x, x + 1], [y + 1, y + 1], 'k-', linewidth=2)
    
    # Draw outer walls
    ax.plot([0, m], [0, 0], 'k-', linewidth=3)  # Bottom
    ax.plot([0, m], [m, m], 'k-', linewidth=3)  # Top  
    ax.plot([0, 0], [0, m], 'k-', linewidth=3)  # Left
    ax.plot([m, m], [0, m], 'k-', linewidth=3)  # Right

def plot_final_maze(C, m, path=None):
    """Plot the final maze"""
    plt.figure(figsize=(10, 10))
    
    # Plot the maze walls
    plot_maze_walls(plt.gca(), C, m)
    
    # Highlight solution path if provided
    if path:
        # Draw path through centers of cells
        for i in range(len(path) - 1):
            cell1 = path[i]
            cell2 = path[i + 1]
            
            row1 = (cell1 - 1) // m
            col1 = (cell1 - 1) % m
            row2 = (cell2 - 1) // m
            col2 = (cell2 - 1) % m
            
            x1, y1 = col1 + 0.5, row1 + 0.5
            x2, y2 = col2 + 0.5, row2 + 0.5
            
            plt.plot([x1, x2], [y1, y2], 'r-', linewidth=3)
    
    plt.title(f'Random Maze ({m}x{m})')
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def solve_maze(C, start=1, end=None):
    """Find shortest path through maze"""
    if end is None:
        # Use the bottom-right corner cell
        m = int(np.sqrt(len(C.nodes())))
        end = m * m
    
    print(f"Looking for path from {start} to {end}")
    print(f"Graph nodes: {len(C.nodes())}, edges: {len(C.edges())}")
    
    # Verify nodes exist
    if start not in C:
        print(f"Start node {start} not in graph")
        return None
    if end not in C:
        print(f"End node {end} not in graph")
        # Find the actual last node
        end = max(C.nodes())
        print(f"Using last node: {end}")
    
    try:
        path = nx.shortest_path(C, start, end)
        print(f"Found path with {len(path)} steps")
        return path
    except nx.NetworkXNoPath:
        print("No path exists between start and end")
        return None

# Example usage
if __name__ == "__main__":
    # Generate maze with GIF creation
    n = 11  # Smaller for faster GIF creation
    C, tree, gif_path = generate_maze(n=n, branching='middle', create_gif=False)
    
    m = n - 1
    print(f"Maze size: {m}x{m} cells")
    
    # Plot final maze
    plot_final_maze(C, m)
    
    # Solve maze
    path = solve_maze(C, 1, m*m)
    if path:
        print(f"Solution path: {path}")
        plot_final_maze(C, m, path)
    else:
        print("No solution path found")
        # Plot without path
        plot_final_maze(C, m)
