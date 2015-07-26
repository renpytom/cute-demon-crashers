# disable click for credits
screen disable_Lmouse():
    key "mouseup_1" action NullAction()

# repurpose menu for Replay mode
screen replay_controls():
    key "game_menu" action [Hide("replay_controls"), renpy.end_replay]


# Stop button
screen sex_stop(target):
    imagebutton:
        auto "assets/ui/stop_sex_%s.png"
        action Jump(target)
        xalign .99
