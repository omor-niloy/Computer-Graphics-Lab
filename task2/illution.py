import matplotlib.pyplot as plt
import numpy as np

def draw_geometric_illusion():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw multiple rotated squares
    num_squares = 30
    angles = np.linspace(0, np.pi, num_squares)

    for angle in angles:
        square = np.array([
            [-1, -1],
            [1, -1],
            [1, 1],
            [-1, 1],
            [-1, -1]
        ])

        # Rotation matrix
        rot = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle),  np.cos(angle)]
        ])

        rotated_square = square @ rot.T
        ax.plot(rotated_square[:, 0], rotated_square[:, 1], color='black', linewidth=0.5)

    plt.title("Geometric Shape Illusion", fontsize=14)
    plt.show()

draw_geometric_illusion()