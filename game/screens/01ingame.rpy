# Dialogue
screen say(who, what, side_image=None, two_window=False):
    window:
        id "window"
        style_group "say"

        use quick_menu()

        if side_image:
            fixed:
                style_group "say_side_image"
                add "assets/ui/eclipse.png" xalign 0.0 yalign 1.0
                window:
                    has fixed
                    use say_dialogue(who, what)
                frame:
                    add side_image
        else:
            fixed:
                use say_dialogue(who, what)
                

screen say_dialogue(who, what):
    window:
        style "say_dialogue_window"
        text what id "what"

    if who:
        frame:
            style "say_nameplate_frame"
            text who id "who"


# Choices
screen choice(items):
    window:
        style "menu_window"

    vbox:
        style_group ("sexy_menu_choice" if store.in_sex else "menu_choice")

        for caption, action, chosen in items:
            if action:
                textbutton caption action action
            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True


# Input
screen input(prompt):
    window:
        style "input_window"

    frame:
        style_group "input_popup"

        has vbox

        label _(prompt)
        input id "input" style "input_text"
        null width 400 height 1
