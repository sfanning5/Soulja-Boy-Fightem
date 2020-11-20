init python:

    # This file contains all non-player classes for the minigame

    class Vector2:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        # Computes the distance between this point and another given point
        def distance(self, vector2):
            return (((self.x - vector2.x) ** 2) + ((self.y - vector2.y) ** 2)) ** .5

        # Adds this vector to the given vector and returns the result
        def add_to(self, vector2):
            return Vector2(self.x + vector2.x, self.y + vector2.y)

    class Projectile():

        def __init__(self):
            self.position = Vector2(200, -200)
            self.position_change = Vector2(0, 1) # The change in position every frame
            self.position_change.x *= projectile_speed
            self.position_change.y *= projectile_speed
            self.img = renpy.displayable("Props/pr_placeholderProjectile.png")
            self.zoomed = False
            self.zoom_amount = 1

        def move(self):
            self.position = self.position.add_to(self.position_change)
