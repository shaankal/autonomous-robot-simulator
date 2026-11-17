from robot_sim.grid_world import GridWorld


def test_robot_moves_right():
    grid_world = GridWorld(size=5)
    grid_world.move_robot("right")
    assert grid_world.robot_position == (0, 1)

def test_robot_stays_inside_grid():
    grid_world = GridWorld(size=5)
    grid_world.move_robot("up")  # Move up from (0, 0) should be invalid
    assert grid_world.robot_position == (0, 0)

def test_robot_cannot_enter_obstacle():
    grid_world = GridWorld(size=5)
    grid_world.obstacles.add((0, 1))  # Place an obstacle to the right of the robot
    grid_world.move_robot("right")  # Attempt to move into the obstacle
    assert grid_world.robot_position == (0, 0)  # Robot should not move into the obstacle

def test_reset():
    grid_world = GridWorld(size=5)
    grid_world.move_robot("right")
    grid_world.reset()
    assert grid_world.robot_position == (0, 0)
