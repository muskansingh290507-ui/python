import tkinter as tk

# Initialize window
root = tk.Tk()
root.title("Simple Game")

# Create a canvas
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
canvas.pack()

# Colors for triangles
colors = ["black", "blue", "green", "orange", "purple"]

# Triangle size and spacing
point = 80
gap = 100

# Starting position
x_start = 100
y_start = 100

# Loop to create triangles in a row
for i, color in enumerate(colors):
    x_offset = x_start + i * (point + gap)

    # Triangle coordinates
    x1 = x_offset
    y1 = y_start

    x2 = x_offset + point
    y2 = y_start + point

    x3 = x_offset - point
    y3 = y_start + point

    # Draw triangle
    canvas.create_polygon(
        x1, y1, x2, y2, x3, y3,
        fill=color,
        outline="black"
    )

# Run game
root.mainloop()
