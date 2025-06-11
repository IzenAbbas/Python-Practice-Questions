x, y = 0, 0

print("Enter the movement commands (e.g., UP 5). Type '!' to stop:")

while True:
    command = input().strip()
    if command == "!":
        break
    direction, steps = command.split()
    steps = int(steps)

    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps
    elif direction.upper() == "RIGHT":
        x += steps
distance = (x**2 + y**2)**0.5
print("Distance from origin:", round(distance))
