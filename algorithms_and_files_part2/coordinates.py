"""
./steps.txt
"""

try:
    file_name = input()
    x_dir = 0
    y_dir = 0
    with open(file_name, "r", encoding = "utf-8") as f:
        for row in f:
            row = row.strip()
            if row:
                row = row.split(" ")
                direction = row[0]
                step = float(row[1])
                if direction == "right":
                    x_dir += step
                elif direction == "left":
                    x_dir -= step
                elif direction == "up":
                    y_dir += step
                elif direction == "down":
                    y_dir -= step
                else:
                    print("INVALID INPUT")
            else:
                continue

    print("X {:.3f}".format(x_dir))
    print("Y {:.3f}".format(y_dir))
except:
    print("INVALID INPUT")