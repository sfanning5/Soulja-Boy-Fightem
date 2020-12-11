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

        def add_to(self, vector2, modifier):
            return Vector2(self.x + (vector2.x * modifier), self.y + (vector2.y * modifier))

    class Projectile():
        alternating = False
        current_spawn_x = 0
        VERTICAL_PADDING = 10
        HORIZONTAL_PADDING = 150

        graphics = [
        "Props/pr_phone.png",
        "Props/pr_shades.png",
        "Props/pr_hat.png",
        "Props/pr_chain.png"
        ]

        def __init__(self):
            self.position = Vector2(200, -200)
            self.rotation = 0 # This projectile's rotation in degrees
            self.rotation_speed = self.determine_rotation_speed() # The change in rotation every frame
            self.start_position = self.position
            self.position_change = Vector2(0, 1) # The change in position every frame
            self.position_change.x *= projectile_speed
            self.position_change.y *= projectile_speed
            self.img = renpy.displayable(Projectile.graphics[current_level]) # Sets this projectile's graphics
            self.zoom_amount = .9
            self.fade_distance = 0 # The distance from the start at which the fade in animation will end

        def determine_rotation_speed(self):
            import random
            speed = 1.5 + random.random()
            speed *= random.choice([1, -1])
            return speed

        def move(self, delta_time):
            self.position = self.position.add_to(self.position_change, delta_time)
            self.rotation += self.rotation_speed

        # calculates what the alpha value of the projectile should be (this creates the fade in animation)
        def get_alpha_value(self):

            if self.fade_distance == 0: # Avoids divide by 0 errors
                return 1

            a = self.position.distance(self.start_position) / self.fade_distance
            if a > 1:
                a = 1
            return a

        # Returns the x position that the projectile should spawn at (making sure to distribute projectiles evenly)
        def get_spawn_x(self, max_x, variation):
            import random

            Projectile.current_spawn_x += random.random() * variation
            Projectile.current_spawn_x %= max_x # Keeps in correct range
            return Projectile.current_spawn_x

        def get_alternating(self):
            outp = Projectile.alternating
            Projectile.alternating = not Projectile.alternating
            return outp

        # Determines and sets the spawn position of this projectile
        def generate_spawn_position(self, width, height):
            import random

            X_VARIATION = width / 4

            new_pos = Vector2(0, 0)

            if self.get_alternating():
                new_pos.y = -Projectile.VERTICAL_PADDING
            else:
                new_pos.y = height + Projectile.VERTICAL_PADDING
                self.position_change.y *= -1

            new_pos.x = width/4 + self.get_spawn_x(width/2, X_VARIATION)

            self.position = new_pos
            self.start_position = self.position

    class HorizontalProjectile(Projectile):
        current_spawn_y = 0
        alternating = False

        def __init__(self):
            Projectile.__init__(self)
            self.position_change = Vector2(1, 0) # The change in position every frame
            self.position_change.x *= projectile_speed
            self.position_change.y *= projectile_speed
            self.fade_distance = 100

        # Overrides this function to ensure that this projectile type doesn't share an alternating value with standard projectiles
        def get_alternating(self):
            outp = HorizontalProjectile.alternating
            HorizontalProjectile.alternating = not HorizontalProjectile.alternating
            return outp

        # Overrides this function to return the correct y position instead
        def get_spawn_x(self, max_y, variation):
            import random

            HorizontalProjectile.current_spawn_y += random.random() * variation
            HorizontalProjectile.current_spawn_y %= max_y # Keeps in correct range
            return HorizontalProjectile.current_spawn_y

        # Determines and sets the spawn position of this projectile
        def generate_spawn_position(self, width, height):
            Projectile.generate_spawn_position(self, width, height)
            self.position = Vector2(width/4 - Projectile.HORIZONTAL_PADDING if self.position.y < 0 else 3 * width/4 + Projectile.HORIZONTAL_PADDING, self.position.x - width/4)
            if self.position.x > width/2:
                self.position_change.x *= -1

            self.start_position = self.position

    class DiagonalProjectile(Projectile):

        def __init__(self):
            Projectile.__init__(self)
            self.position_change = Vector2(1, 1) # The change in position every frame
            self.position_change.x *= projectile_speed
            self.position_change.y *= projectile_speed

        def generate_spawn_position(self, width, height):
            Projectile.generate_spawn_position(self, width, height)

            if self.position.x > width/2:
                self.position_change.x *= -1
