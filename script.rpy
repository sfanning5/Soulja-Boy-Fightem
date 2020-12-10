define m = Character("Mom")
define t = Character("")
define ld = Character("Long Distance Soulja Boy")
define pb = Character("Pretty Boy Soulja Boy")
define ct = Character("Crank That Soulja Boy")
define ss = Character("Swag Soulja Boy")
define q = Character("???")
define s = Character("SWAG")
define wins = 0

screen say_at_top(msg):
    window id "window":
        vbox:
            spacing 10
            ypos -450
            xalign .5
            text msg

label start:

    scene bg_black at truecenter:
        zoom 2

    show screen say_at_top("How would you like to control your character during battle?")

    menu:
        "WASD":
            $ current_control_scheme = "WASD"

        "IJKL":
            $ current_control_scheme = "IJKL"

        "Arrow keys":
            $ current_control_scheme = "Arrow keys"

    hide screen say_at_top

    show screen say_at_top("Would you like to allow yourself to retry battles?")
    menu:
        "Yes.":
            $ ironman_mode = False

        "I don't lose.":
            $ ironman_mode = True

    hide screen say_at_top

    scene bg_bedroom at truecenter:
        zoom 1.7
    with dissolve

    #MUSIC: Music coming from laptop starts here

    m "Goodnight sweetie, make sure you don't stay up too late listening to music."

    t "{i}I better get to bed soon.{/i}"

    #ANIMATION: Eyes closed
    #MUSIC: Fades out here

    scene bg_white at truecenter:
        zoom 1
    with dissolve

    play sound mu_ring

    t "{i}Where am I?{/i}"

    t "{i}I guess the phone is for me.{/i}"

    #MUSIC: Instumental music plays

    show ch_distance at left
    with dissolve

    ld "Looks like we have our next challenger!"

    t "{i}What is happening?!{/i}"

    ld "You look confused. What's your name?"

    stop sound

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    define p = Character("[player_name]")

    p "My name is [player_name]."

    ld "Well then [player_name], welcome to Soulja Boy World."

    p "Soulja Boy World? You mean like THE Soulja Boy?!"

    ld "Not just one; there are many of us here in Soulja Boy World."

    ld "Even you could be a Soulja Boy."

    ld "Maybe even the next Swag Soulja Boy..."

    p "Swag Soulja Boy?"

    ld "He is the ultimate Soulja Boy, but there is only one way \nto reach him..."

    #ART: Zoom in

    ld "To fight in a Swag Battle!"

    #Art: Zoom out

    menu: #The three choices will go hard, medium, then easy for game difficulty

        "That sounds stupid.":

            $ set_difficulty(2)

            jump o1_1 #These numbers represent game 1 choice 1, the o stands for option

        "Bring it on!":

            $ set_difficulty(1)

            jump o1_2 #This one represents game 1 choice 2 for example

        "What is a Swag Battle?":

            $ set_difficulty(0)

            jump o1_3

label o1_1:

    p "That sounds stupid."

    #ART: Eyes glow
    ld "Oh, is it now?"

    jump game_1

label o1_2:

    p "Bring it on!"

    ld "I like your style kid."

    jump game_1

label o1_3:

    p "What is a Swag Battle?"

    ld "It's the way we figure out who is the most Swag in this world."

    ld "Now let's begin!"

    jump game_1

label game_1:
    #GAME: This is where the first game should take place, the following dialogue happens after the game

    call start_minigame from _call_start_minigame

    if _return:

        jump win_1 #The game should jump to win if the player wins and lose if the player looses, the one after represents that this is the first game

    else:

        jump lose_1

label win_1:

    $ wins += 1

    ld "Not bad kid, you're better than I thought."

    ld "With the sort of Swag you have, you may just make it to the top."

    ld "Now I'll send you to your next challanger."

    p "Wait, what do you mean my next chall-"

    #ANIMATION: Teleport animation

    jump pretty_boy_start

label lose_1: #This technically wont show up until the game is implimented

    ld "That's not a good look kid."

    ld "Still, that was only your first Swag Battle."

    ld "I'm sure you'll better do well in the next one."

    p "What do you mean the next o-"

    #ANIMATION: Teleport animation

    jump pretty_boy_start

label pretty_boy_start:

    scene bg_alley:
        zoom 1.7

    show ch_pretty at center:
        zoom .2
    with dissolve

    pb "It's ya boy, Pretty Boy Soulja Boy!"

    pb "What are you doing in my domain? Trying to cramp my style?"

    #ART: Zoom in

    pb "Trying to photobomb me!?"

    p "No, I just got here. I have no idea what's going on."

    #Art: Back up

    pb "That's cool, that's cool..."

    pb "Well this is my domain, so if you wanna be here you gotta fight me in a Swag Battle."

    #ART: pb goes to the side of the screen for a quick picture, then goes back to the center
    #SOUND: Camera flash sound effect

    pb "You do know what a Swag Battle is, don't you?"

    p "Yea, I just fought Long Distance Soulja Boy."

    pb "That chump?"

    pb "It's no wonder he sent you here, for a greater challange."

    pb "So, are you ready to take me on in a Swag Battle?"

    menu: #The three choices will go hard, medium, then easy for game difficulty

        "Sure, if you can handle not having your picture taken for long enough.":

            $ set_difficulty(4)

            jump o2_1
        "May the most Swag win!":

            $ set_difficulty(3)

            jump o2_2

        "Ok, but only if I get to take your picture after.":

            $ set_difficulty(2)

            jump o2_3

label o2_1:

    p "Sure, if you can handle not having your picture taken \nfor long enough."

    #ART: Eyes glow
    pb "Oh, it is on!"

    jump game_2

label o2_2:

    p "May the most Swag win!"

    pb "Don't worry, I will."

    jump game_2

label o2_3:

    p "Ok, but only if I get to take your picture after."

    pb "Totally! I can sign it for you, too!"

    jump game_2

label game_2:
    #GAME: This is game 2

    call start_minigame from _call_start_minigame_1

    if _return:

        jump win_2

    else:

        jump lose_2

label win_2:

    $ wins += 1

    pb "Looks like you do have the most Swag..."

    pb "But before you go, one last picture!"

    #ART: White camera flash
    play sound mu_camera
    #MUSIC: Music fades out

    jump crank_that_start

label lose_2:

    pb "The fans are gonna love this!"

    pb "Another win for Pretty Boy Soulja Boy!"

    pb "Get over here; I need a picture with my opponent!"

    #ART: White camera flash
    play sound mu_camera
    #MUSIC: Music fades out

    jump crank_that_start

label crank_that_start:

    scene bg_club at truecenter:
        zoom 1.7

    show ch_crank at truecenter:
        zoom .7
        yalign 0
    with dissolve

    #MUSIC: Music with lyrics
    #ART: I don't know if Ren'Py would work with this stuff, but moving colored lights could be cool for this scene like its really at a club

    ct "Welcome to Superman: my club and my domain."

    #ART: Zoom in

    ct "Now tell me, can you Crank That Soulja Boy?"

    menu: #The three choices will go hard, medium, then easy for game difficulty

        "Isn't that your name?":

            $ set_difficulty(6)

            jump o3_1
        "Yes.":

            $ set_difficulty(5)

            jump o3_2

        "No.":

            $ set_difficulty(4)

            jump o3_3

label o3_1:

    p "Isn't that your name?"

    #ART: Eyes glow
    ct "Yes it is, now watch me YUUUAA!"
    play sound mu_you

    jump game_3

label o3_2:

    p "Yes."

    ct "Good, now watch me YUUUAA!"
    play sound mu_you

    jump game_3

label o3_3:

    p "No."

    ct "You don’t?"

    ct "Well I can teach you, now watch me YUUUAA!"
    play sound mu_you

    jump game_3

label game_3:
    #GAME: This is game 3

    call start_minigame from _call_start_minigame_2

    if _return:

        jump win_3

    else:

        jump lose_3

label win_3:

    $ wins += 1

    ct "Looks like you can crank it with the best of them."

    ct "I'm impressed."

    ct "I'm sending you up to Swag Soulja Boy, the last of us Soulja Boys..."

    #ART: Zoom in

    ct "...and the most Swag."

    #Animation: Teleport

    jump Swag_start

label lose_3:

    ct "Your moves aren't slick. I don't know if you have what it takes...."

    ct "...but I gotta send you up to the Swag Soulja Boy, the last of us Soulja Boys..."

    #ART: Zoom in

    ct "...with the most Swag."

    #Animation: Teleport

    jump Swag_start

label Swag_start:

    scene bg_space at truecenter:
        zoom 1.6

    show ch_swag at center:
        zoom .513
    with dissolve

    t "{i} Wow he is so big he doesn't even fit on screen. {/i}"

    ss "So..."

    ss "You've finally arrived."

    ss "I’ve been watching you, down there, in Soulja Boy world."

    ss "These chains I have collected from Soulja Boys all over."

    ss "I gain Swag from Soulja boys I defeat in Swag Battles."

    ss "But the thing is…"

    #ART: Zoom in

    ss "So do you."

    #ART: Back up

    ss "The only question now is if you have what it takes."

    ss "Can you defeat me in a Swag Battle and become the ultimate Soulja Boy?"

    menu: #The three choices will go hard, medium, then easy for game difficulty

        "I have more Swag than you ever will.":

            $ set_difficulty(8)

            jump o4_1
        "I’m ready for the final Swag Battle.":

            $ set_difficulty(7)

            jump o4_2

        "I like your chains.":

            $ set_difficulty(6)

            jump o4_3

label o4_1:

    p "I have more Swag then you ever will."

    #ART: Eyes glow
    ss "I see how it is…"

    ss "You are brave, but I will not hold back."

    jump game_4

label o4_2:

    p "I’m ready for the final Swag Battle."

    ss "You sound confident."

    ss "But confidence will only get you so far when battling me."

    jump game_4

label o4_3:

    p "I like your chains."

    ss "I see you understand proper Swag."

    ss "This is good."

    ss "But now, we must do Swag Battle!"

    jump game_4

label game_4:
    #GAME: This is game 4

    call start_minigame from _call_start_minigame_3

    if _return:

        jump win_4

    else:

        jump lose_4

label win_4:

    $ wins += 1

    ss "How could this happen?"

    ss "I am Swag Soulja Boy, the most Swag of all Soulja Boys."

    ss "This can’t be happening!"

    #ART: Swag soulja boy slowly starts to fade away

    ss "My swaaaaaaaagggggggg!"

    scene bg_space at truecenter:
        zoom 1.6
    with dissolve

    p "Hello?"

    q "Hello."

    p "Where are you?"

    p "Who are you?"

    q "I am nowhere, and I am everywhere..."

    s "I am SWAG, the force of Swag that controls this world."

    s "And this world is now your world."

    s "You may destroy it."

    s "You may leave it and return home."

    s "Or, if you posses enough Swag, you may rule it as the next Swag Soulja Boy."

    s "The choice is yours."

    menu:

        "Destroy Soulja Boy World.":

            jump o5_1
        "Return home.":

            jump o5_2

        "Become the next Swag Soulja Boy.":

            jump o5_3

label o5_1:

    s "I see..."

    s "Well, it is your choice."

    s "I will be sorry to see this world go."

    #ART: White flash
    play sound mu_explode
    #ART: Fade to black

    scene bg_black:
        zoom 2

    #END

    jump end

label o5_2:

    ss "If this is your choice, then I will return you to your home."

    ss "Back to your world."

    #ANIMATION: Teleport

    scene bg_bedroom at truecenter:
        zoom 1.7
    with dissolve

    m "Goodnight sweetie, make sure you don't stay up too late listening to music."

    t "{i}Did that really just happen?{/i}"

    t "{i}Has no time passed?{/i}"

    t "{i}I should probably turn off the music...{/i}"

    scene bg_black:
        zoom 2
    with Dissolve (5)

    t "{i}and get to bed.{/i}"

    #END

    jump end

label o5_3:

    if wins == 4:

        s "You have conquered all Soulja boys who stood in your path."

        s "You truly are the most Swag of all Soulja Boys."

        s "If you are to become ruler of this world, you must have a title."

        s "What will be your new name?"

        $ new_name = renpy.input("You're new name will be Swag _____ Soulja Boy, fill in the gap.")

        $ new_name = new_name.strip()

        define np = Character("Swag [new_name] Soulja Boy")

        np "I will be Swag [new_name] Soulja Boy."

        s "This is good."

        s "You shall rule over this world as the most Swag of all Soulja Boys."

        s "Are you ready Swag [new_name] Soulja Boy?"

        np "Yes."

    else:

        s "You do not posses enough Swag."

        menu:

            "Destroy Soulja Boy World":

                jump o5_1
            "Return home":

                jump o5_2

    #END

    jump end

label lose_4:

    ss "I have triumphed once again!"

    ss "However, the Swag you possess is rare, and it should \nnot be wasted."

    ss "I shall present you with a choice:"

    ss "You may return to your world..."

    ss "...or"

    ss "You may remain in Soulja Boy world, and become a \nSoulja Boy yourself."

    ss "The choice is yours."

    menu:

        "Stay in Soulja Boy World.":

            jump o6_1

        "Return home.":

            jump o6_2

label o6_1:

    ss "A good choice, I would not have liked seeing your Swag \ngo to waste."

    ss "Before I send you back down to Soulja Boy world, you must \nhave a title."

    ss "What will be your new name?"

    $ new_name_2 = renpy.input("Your new name will be _____ Soulja Boy, fill in the gap.")

    $ new_name_2 = new_name_2.strip()

    define np2 = Character("[new_name_2] Soulja Boy")

    np2 "I will be [new_name_2] Soulja Boy"

    ss "Excellent choice, I will now send you back down to \nSoulja Boy World."

    ss "Are you ready?"

    np2 "Yes."

    #END

    jump end

label o6_2:

    ss "I see..."

    ss "While I will be sad to see your Swag go, I will stay true to my word."

    #ANIMATION: Teleport

    scene bg_bedroom at truecenter:
        zoom 1.7

    m "Goodnight sweetie, make sure you don't stay up too late listening to music."

    t "{i}Did that really just happen?{/i}"

    t "{i}Has no time passed?{/i}"

    t "{i}I should probably turn off the music...{/i}"

    scene bg_black:
        zoom 2
    with Dissolve (5)

    t "{i}and get to bed.{/i}"

    #END

    jump end

label end:

    return
