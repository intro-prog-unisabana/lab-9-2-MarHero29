from aircraft import Aircraft

model = input("Enter aircraft model:\n")

plane = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")

    if command == "X":
        break

    action, feet = command.split()
    feet = int(feet)

    if action == "A":
        plane.climb(feet)

    elif action == "D":
        plane.descend(feet)

print(f"Final altitude: {plane.altitude} feet")