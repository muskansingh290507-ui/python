import tkinter as tk

# Initialize window
root = tk.Tk()
root.title("Simple Game")

# Create a canvas
canvas = tk.Canvas(root, width=1000, height=1000, bg="black")
canvas.pack()

# Example: Draw a game object
sum = 20
for i in range(2):
    canvas.create_rectangle(sum, sum, 50, 50, fill="blue")
    sum = sum+sum

colors = ["red", "blue", "green", "orange", "purple"]

# Define rectangle dimensions and starting position
rect_width = 80
rect_height = 80
gap = 20  # Space between rectangles
x_start = 50
y_start = 50

# Loop to create rectangles in a row
for i, color in enumerate(colors):
    # Calculate coordinates for each rectangle
    x1 = x_start + (rect_width + gap) * i
    y1 = y_start
    x2 = x1 + rect_width
    y2 = y1 + rect_height
    
    # Draw the rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")  

colors = ["red", "blue", "green", "orange", "purple"]

# Define rectangle dimensions and starting position
rect_width = 80
rect_height = 80
gap = 20  # Space between rectangles
x_start = 50
y_start = 50

# Loop to create rectangles in a row
for i, color in enumerate(colors):
    # Calculate coordinates for each rectangle
    x1 = x_start + (rect_width + gap) * i
    y1 = y_start
    x2 = x1 + rect_width
    y2 = y1 + rect_height
    
    # Draw the rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")      

# Run game
root.mainloop()