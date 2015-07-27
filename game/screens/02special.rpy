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
