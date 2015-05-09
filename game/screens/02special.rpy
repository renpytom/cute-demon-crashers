# disable click for credits
screen disable_Lmouse():
    key "mouseup_1" action NullAction()


# Stop button
screen sex_stop(target):
    imagebutton:
        auto "assets/ui/stop_sex_%s.png"
        action Jump(target)
        xalign .99
