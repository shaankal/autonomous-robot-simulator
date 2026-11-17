class GridWorld:
    def __init__(self, size):
        self.size = size
        self.robot_position = (0, 0)  # Starting position of the robot
        self.goal_position = (size - 1, size - 1)  # Goal position in the grid
        self.obstacles = set()  # Set to store obstacle positions

    def move_robot(self, direction):
        row, col = self.robot_position

        if direction == "up":
            row -= 1
        elif direction == "down":
            row += 1
        elif direction == "left":
            col -= 1
        elif direction == "right":
            col += 1
        else:
            print("Invalid direction.")
            return

        new_position = (row, col)

        if self.is_valid_position(new_position):
            self.robot_position = new_position
        else:
            print("Invalid move: obstacle or out of bounds.")
            return

        if self.robot_position == self.goal_position:
            print("Robot has reached the goal!")

    def is_valid_position(self, position):
        row, col = position
        if 0 <= row < self.size and 0 <= col < self.size:
            return position not in self.obstacles
        return False


# warehouse = GridWorld(8)
#
# print(warehouse.size)
# print(warehouse.robot_position)
# print(warehouse.goal_position)
# print(warehouse.obstacles)
