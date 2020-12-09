init python:

    config.keymap["accessibility"].remove('K_a') # Removes "A" from the default keybind
    config.keymap["director"].remove("d") # Removes "D" from the default keybind
    config.keymap["screenshot"].remove("s") # Removes "S" from the default keybind

    import math
    import pygame
    import copy

    defeat = False
    victory = False

    player_pos = Vector2(-1, -1) # Set to -1 and -1 so that the renderer knows to reposition the player at the start
    player_speed = 2.5
    projectile_speed = 1.6

    # Variables that scale with difficulty:
    minigame_duration = 17
    projectiles_per_second = 3.6
    projectile_types = 3

    dx = 0
    dy = 0

    wasd_controls = {
        pygame.K_w : [0, -1, False],
        pygame.K_s : [0, 1, False],
        pygame.K_a : [-1, 0, False],
        pygame.K_d : [1, 0, False]
    }

    ijkl_controls = {
        pygame.K_i : [0, -1, False],
        pygame.K_k : [0, 1, False],
        pygame.K_j : [-1, 0, False],
        pygame.K_l : [1, 0, False]
    }

    arrow_controls = {
        pygame.K_UP : [0, -1, False],
        pygame.K_DOWN : [0, 1, False],
        pygame.K_LEFT : [-1, 0, False],
        pygame.K_RIGHT : [1, 0, False]
    }

    control_schemes = {
        "WASD" : wasd_controls,
        "IJKL" : ijkl_controls,
        "Arrow keys" : arrow_controls
    }

    current_control_scheme = "WASD" # WASD controls by default
    player_controls = copy.deepcopy(control_schemes[current_control_scheme]);

    projectiles_spawned = 0
    projectiles = []

    # Difficulty possibility chart:
    # game 1:  0 1 2
    # game 2:      2 3 4
    # game 3:          4 5 6
    # game 4:              6 7 8

    # Sets the minigame difficulty, represented by a number 0-8. 8 is the hardest.
    def set_difficulty(difficulty):
        global minigame_duration
        global projectiles_per_second
        global projectile_types

        minigame_duration = 8 + 1.2 * difficulty # Ranges from 8 - 17.6 seconds
        projectiles_per_second = 3 + .1 * difficulty # Ranges from 3 to 3.8 projectiles per second

        if difficulty >= 6:
            projectile_types = 3

        elif difficulty >= 3:
            projectile_types = 2

        else:
            projectile_types = 1

    set_difficulty(7) # Sets default difficulty, this is only used for testing

    # Resets the minigame data so that the game can be played again
    # this could be made much better if i bothered to learn reflection in python.
    def reset_data():
        global victory
        global defeat
        global projectiles_spawned
        global projectiles
        global dx
        global dy
        global player_pos
        global player_controls

        defeat = False
        victory = False
        projectiles_spawned = 0
        projectiles = []
        dx = 0
        dy = 0
        player_pos = Vector2(-1, -1)

        player_controls = copy.deepcopy(control_schemes[current_control_scheme]); # sets controls, and stops original copy from being edited while in game

    def countdown(st, at, length):
        global victory

        remaining = length - st

        # Player wins the game
        if remaining <= 0:
            remaining = 0
            victory = True
            renpy.timeout(0)

        return Text("{alpha=0.5} " + ("%.1f" % remaining), color="#FFD700", size=200, bold=True), .1

    # Creates a projectile of the given type. In this case, type is represented by a number
    def create_projectile_of_type(type):
        # REALLY wish python had a switch statement right now
        if type == 0:
            return Projectile()
        elif type == 1:
            return HorizontalProjectile()
        elif type == 2:
            return DiagonalProjectile()

    # Spawns a projectile at a random location, intakes the width and height of the render
    def spawn_projectile(width, height):
        import random
        global projectiles_spawned

        new_proj = create_projectile_of_type(int(random.random() * projectile_types)) # Creates a projectile of a random type
        new_proj.generate_spawn_position(width, height)

        projectiles.append(new_proj)
        projectiles_spawned += 1

    class Minigame(renpy.Displayable):

        def __init__(self, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Minigame, self).__init__(**kwargs)

            self.player_image = renpy.displayable("Props/pr_player.png")

            self.last_time_rendered = 0 # The at value st the last time the minigame was rendered, used in calculating delta_time

        def render(self, width, height, st, at):
            global player_pos
            global defeat

            delta_time_modifier = (st - self.last_time_rendered) * 143 # the game was tested initially at 143 fps, so this modifier makes everything move as if it was at 143fps
            self.last_time_rendered = st

            if player_pos.x == -1 and player_pos.y == -1:
                player_pos = Vector2(width/2, height/2)

            render = renpy.Render(width, height)

            # Spawns projectiles if appropriate

            if(st * projectiles_per_second > projectiles_spawned):
                spawn_projectile(width, height)

            # Renders the given projectile
            def render_projectile(projectile):

                t = Transform(child=projectile.img, alpha=projectile.get_alpha_value(), xanchor=0.5, yanchor=0.5, xzoom=projectile.zoom_amount, yzoom=projectile.zoom_amount, rotate=projectile.rotation)
                proj_render = renpy.render(t, width, width, st, at)
                sizex, sizey = proj_render.get_size()

                render.blit(proj_render, (projectile.position.x - sizex/2, projectile.position.y - sizey/2))

            # Moving + Rendering all projectiles
            for projectile in projectiles:
                projectile.move(delta_time_modifier)
                render_projectile(projectile)

                # Checks for collisions
                COLLISION_DISTANCE = 65
                if projectile.position.distance(player_pos) < COLLISION_DISTANCE:
                    projectile.position_change = Vector2(0, 0)
                    defeat = True
                    renpy.timeout(0)

            # Moving + rendering player
            player_pos.x += dx * player_speed * delta_time_modifier
            player_pos.y += dy * player_speed * delta_time_modifier

            # Applying movement boundaries
            VERTICAL_PADDING = 50

            if player_pos.x < width / 4:
                player_pos.x = width / 4
            elif player_pos.x > width * 3 / 4:
                player_pos.x = width * 3 / 4
            if player_pos.y < VERTICAL_PADDING:
                player_pos.y = VERTICAL_PADDING
            elif player_pos.y > height - VERTICAL_PADDING:
                player_pos.y = height - VERTICAL_PADDING

            PLAYER_ZOOM = 0.8
            pl = renpy.render(Transform(child=self.player_image, xanchor=0.5, yanchor=0.5, xzoom=PLAYER_ZOOM, yzoom=PLAYER_ZOOM), width, width, st, at)

            playersize_x, playersize_y = pl.get_size()
            render.blit(pl, (player_pos.x - playersize_x/2, player_pos.y - playersize_y/2))


            renpy.redraw(self, .1)
            return render


        # Handles events.
        def event(self, ev, x, y, st):
            global dx
            global dy
            if ev.type == pygame.KEYDOWN and ev.key in player_controls and not player_controls[ev.key][2]:
                diffs = player_controls[ev.key]
                dx += diffs[0]
                dy += diffs[1]
                player_controls[ev.key][2] = True
            elif ev.type == pygame.KEYUP and ev.key in player_controls and player_controls[ev.key][2]:
                diffs = player_controls[ev.key]
                dx -= diffs[0]
                dy -= diffs[1]
                player_controls[ev.key][2] = False

            if defeat:
                return False

            elif victory:
                return True


        def visit(self):
            return [ ]

screen minigame(duration):

    $ reset_data()

    add "Backgrounds/bg_minigame_placeholder.png" at truecenter:
        xzoom 1.645
        yzoom 1.605

    add DynamicDisplayable(countdown, duration) at truecenter

    add Minigame():
        xalign 0.5
        yalign 0.5


label start_minigame:

    "{b}{i}ENGAGING SWAG BATTLE IN 3{/b}{/i}"

    "{b}{i}2{/b}{/i}"

    "{b}{i}1{/b}{/i}"

    "{b}{i}GO!!!{/b}{/i} (use [current_control_scheme] to move)"

    call screen minigame(minigame_duration)

    if _return:

        "{b}{i}GLORIOUS VICTORY!{/b}{/i}"

        return True

    else:

        "{b}{i}SHOCKING DEFEAT!{/b}{/i}"

        menu: #The three choices will go hard, medium, then easy for game difficulty

            "Try again":

                call start_minigame from _call_start_minigame_4

            "Accept rightful defeat":

                return False

    return _return
