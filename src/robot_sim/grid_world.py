class GridWorld:
    def __init__(self, size):
        self.size = size
        self.robot_position = (0, 0)  # Starting position of the robot
        self.goal_position = (size - 1, size - 1)  # Goal position in the grid
        self.obstacles = set() #Set to store obstacle positions

    def move_robot(self, new_position):
        if self.is_valid_position(new_position):
            self.robot_position = new_position
        else:
            print("Invalid move. Position is either out of bounds or occupied by an obstacle.")

    def is_valid_position(self, position):
        x, y = position
        if 0 <= x < self.size and 0 <= y < self.size:
            return position not in self.obstacles
        return False



# warehouse = GridWorld(8)
#
# print(warehouse.size)
# print(warehouse.robot_position)
# print(warehouse.goal_position)
# print(warehouse.obstacles)