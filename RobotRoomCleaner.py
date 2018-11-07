# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

"""
思路：DFS + backtracking
"""

class Solution(object):
    def cleanRoom(self, robot):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #注意：方向的顺序有讲究！

        #go back to the starting position
        def goBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(pos, robot, cur, visited):
            if pos in visited:
                return
            visited.add(pos)

            robot.clean()                        #要打扫当前cell, 容易忽略！！
            for i in range(4):
                if robot.move():
                    dfs((pos[0]+directions[cur][0], pos[1]+directions[cur][1]), robot, cur, visited)
                    goBack(robot)
                robot.turnRight()
                cur = (cur + 1) % len(directions)

        dfs((0,0), robot, 0, set())
