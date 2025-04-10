import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Towers represented as stacks (list of discs)
towers = [[], [], []]

# Parameters
num_discs = 5
disc_height = 0.5
pause_time = 0.5

# Initialize tower A
towers[0] = list(reversed(range(1, num_discs + 1)))

def draw_towers():
    plt.clf()
    ax = plt.gca()
    ax.set_xlim(0, 9)
    ax.set_ylim(0, num_discs + 2)
    ax.axis('off')

    for i, tower in enumerate(towers):
        x_base = 2 + i * 3
        # Draw base and post
        ax.add_patch(patches.Rectangle((x_base - 0.05, 0), 0.1, num_discs + 1, color='black'))

        for j, disc in enumerate(tower):
            width = disc
            ax.add_patch(patches.Rectangle((x_base - width/2, j * disc_height + 0.5), width, disc_height, color='skyblue'))

    plt.pause(pause_time)

def move(n, from_tower, to_tower, aux_tower):
    if n == 1:
        disc = towers[from_tower].pop()
        towers[to_tower].append(disc)
        draw_towers()
    else:
        move(n-1, from_tower, aux_tower, to_tower)
        move(1, from_tower, to_tower, aux_tower)
        move(n-1, aux_tower, to_tower, from_tower)

# Setup plot
plt.ion()
fig = plt.figure(figsize=(10, 6))

draw_towers()
move(num_discs, 0, 2, 1)
plt.ioff()
plt.show()
