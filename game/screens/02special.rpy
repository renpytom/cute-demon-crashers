# disable click for credits
screen disable_Lmouse():
    key "mouseup_1" action NullAction()

# repurpose menu for Replay mode
screen replay_controls():
    key "game_menu" action [Hide("replay_controls"), renpy.end_replay]


# Stop button
init python:
    def maybe_stop_scene(ev, **kwargs):
        def should_stop():
            return context.current == renpy.store.sex_stop_statement \
               and renpy.store.sex_stop_label
        
        if ev == "begin":
            context = renpy.game.context()
            renpy.store.last_statement = context.current
            if _in_replay and should_stop():
                renpy.jump(renpy.store.sex_stop_label)
            
    config.character_callback = maybe_stop_scene

screen sex_stop(target):
    imagebutton:
        auto "assets/ui/stop_sex_%s.png"
        action Jump(target)
        xalign .99

screen sex_stop_red(target):
    imagebutton:
        auto "assets/ui/stop_sex_red-%s.png"
        action Jump(target)
        xalign .99

    
# Tutorial
screen tutorial:
    default cur_screen_num = 1
    python:
        cur_screen = "assets/ui/tut/tips_%s.jpg"%(cur_screen_num)
    add cur_screen
    imagebutton:
        auto "assets/ui/tut/tips_prev_%s.png"
        insensitive Null(width=1)
        action If(cur_screen_num == 1, None, SetScreenVariable("cur_screen_num", cur_screen_num-1))    
        hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        xpos 80
        ypos 680
    imagebutton:
        auto "assets/ui/tut/tips_next_%s.png"
        action If(cur_screen_num == 6, None, SetScreenVariable("cur_screen_num", cur_screen_num+1))    
        hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        insensitive Null(width=1)
        xpos 1040
        ypos 680
    imagebutton: 
        auto "assets/ui/tut/tips_exit_%s.png"
        action Return()
        hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        xpos 1140
        ypos 15


init:
    style phone_message_vbox:
        xalign 0.5
        yalign 0
        ypos 570
        xsize 240
        xoffset -10
        
    style phone_message_frame:
        background Solid("#d9398c")
        ypadding 10
        xpadding 10

    style phone_message_contents:
        spacing 10

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        
    style phone_message_who is phone_message:
        color "#ecf0f1"
        size 18

    style phone_message_what is phone_message:
        color "#ffffff"
        size 18
        
screen phone_message(who, what):
    vbox at incoming_message:
        style_group "phone_message"

        add "assets/ui/bubble-tip.png" at phone_message_bubble_tip
        frame:
            style_group "phone_message"

            vbox:
                style "phone_message_contents"
                
                text who style "phone_message_who"
                text what style "phone_message_what"
        
