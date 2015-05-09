# Navigation included in main menus
screen menu_navigation(current):
    $ if current != "main-menu": renpy.hide_screen("start_popup")

    add "assets/ui/logo.png" yalign 1.0 xalign 0.5

    hbox:
        yalign 1.0

        if current == "main-menu":
            imagebutton action ShowTransient("start_popup"):
                idle "assets/ui/mm-nav-start-idle.png"
                hover "assets/ui/mm-nav-start-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"


        elif store.main_menu:
            imagebutton action ShowMenu("main_menu"):
                idle "assets/ui/mm-nav-return-idle.png"
                hover "assets/ui/mm-nav-return-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"
        else:
            imagebutton action Return():
                idle "assets/ui/mm-nav-return-idle.png"
                hover "assets/ui/mm-nav-return-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"

        if current == "options":
            imagebutton action ShowMenu("options_menu"):
                idle "assets/ui/mm-nav-options-hover.png"
                hover "assets/ui/mm-nav-options-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"
        else:
            imagebutton action ShowMenu("options_menu"):
                idle "assets/ui/mm-nav-options-idle.png"
                hover "assets/ui/mm-nav-options-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"


        null width 505

        if current == "extras":
            imagebutton action ShowMenu("extras_menu"):
                idle "assets/ui/mm-nav-extra-hover.png"
                hover "assets/ui/mm-nav-extra-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"
        else:
            imagebutton action ShowMenu("extras_menu"):
                idle "assets/ui/mm-nav-extra-idle.png"
                hover "assets/ui/mm-nav-extra-hover.png"
                activate_sound "assets/sfx/menu_select.ogg"
                hover_sound "assets/sfx/menu_hover3.ogg"


        imagebutton action Quit(confirm=True):
            idle "assets/ui/mm-nav-quit-idle.png"
            hover "assets/ui/mm-nav-quit-hover.png"
            activate_sound "assets/sfx/menu_select.ogg"
            hover_sound "assets/sfx/menu_hover3.ogg"


# The main menu
screen main_menu():
    tag menu

    window:
        style "mm_root"

    # Main background
    ## we should add a variation for when each of the routes is completed
    if not persistent.akki_complete:
        add "assets/ui/mm-akki.png" ypos 90
    elif persistent.akki_complete==True:
        add "assets/ui/mm-akki_full.png" ypos 90
    if not persistent.orias_complete:
        add "assets/ui/mm-orias.png" ypos 90 xpos 300
    elif persistent.orias_complete==True:
        add "assets/ui/mm-orias_full.png" ypos 90 xpos 300
    if not persistent.kael_complete:
        add "assets/ui/mm-kael.png" ypos 90 xpos 650
    elif persistent.kael_complete==True:
        add "assets/ui/mm-kael_full.png" ypos 90 xpos 650
    if not persistent.mirari_complete:
        add "assets/ui/mm-mirari.png" ypos 90 xpos 958 
    elif persistent.mirari_complete==True:
        add "assets/ui/mm-mirari_full.png" ypos 90 xpos 958 
    add "assets/ui/mm-white-border.png"
    add "assets/ui/mm-group-logo.png" xpos 1072

    use menu_navigation("main-menu")


# Popup displayed before the game starts, lets the user choose between
# starting a new game or loading a previous one.
screen start_popup():
    frame:
        style_group "mm_popup"

        vbox:
            imagebutton:
                auto "assets/ui/btn-newgame-%s.png" 
                action Start() 
                activate_sound "assets/sfx/game_start3.ogg" 
                hover_sound "assets/sfx/menu_hover3.ogg"
            imagebutton:
                auto "assets/ui/btn-continue-%s.png" 
                action ShowMenu("load") 
                activate_sound "assets/sfx/menu_select.ogg" 
                hover_sound "assets/sfx/menu_hover3.ogg"


# Options menu
screen options_menu():
    default opt_menu = "text"
    tag menu

    window:
        style "mm_root"

    add "assets/ui/options-title.png"
    use menu_navigation("options")
    
    hbox:
        style_group "tabbar"

        button action SetScreenVariable("opt_menu", "text"):
            add ConditionSwitch(
                  "get_screen_var('opt_menu') == 'text'", "assets/ui/text-text-selected.png",
                  "True", "assets/ui/text-text.png"
                ) align (1.0, 1.0)

        button action SetScreenVariable("opt_menu", "sound"):
            add ConditionSwitch(
                  "get_screen_var('opt_menu') == 'sound'", "assets/ui/text-sound-selected.png",
                  "True", "assets/ui/text-sound.png"
                ) align(1.0, 1.0)

    if opt_menu == 'text':
        grid 2 3:
            style_group "mm_opts"
    
            vbox:
                frame:
                    add "assets/ui/h-text-speed.png"
                bar value Preference("text speed")
        
            vbox:
                frame:
                    add "assets/ui/h-ff-speed.png"
                bar value Preference("auto-forward time")
        
            vbox:
                frame:
                    add "assets/ui/h-skip-behaviour.png"
                hbox:
                    textbutton _("Seen Text") action Preference("skip", "seen")
                    textbutton _("All Text") action Preference("skip", "all")
        
            vbox:
                frame:
                    add "assets/ui/h-after-choices.png"
                hbox:
                    textbutton _("Stop Skipping") action Preference("after choices", "stop")
                    textbutton _("Keep Skipping") action Preference("after choices", "skip")
        
            vbox:
                frame:
                    add "assets/ui/h-font.png"
                hbox:
                    textbutton "Quicksand" action StylePreference("text", "quicksand")
                    textbutton "Open Dyslexic" action StylePreference("text", "open-dyslexic")
        
            vbox:
                frame:
                    add "assets/ui/h-18-content.png"
                hbox:
                    textbutton _("On") action SetPersistent("censor_18", True)
                    textbutton _("Off") action SetPersistent("censor_18", False)

    else:
        grid 2 2:
            style_group "mm_opts"

            vbox:
                frame:
                    add "assets/ui/h-music-volume.png"
                bar value Preference("music volume")

            vbox:
                frame:
                    add "assets/ui/h-sound-volume.png"
                bar value Preference("sound volume")

            vbox:
                frame:
                    add "assets/ui/h-transitions.png"
                hbox:
                    textbutton _("All") action Preference("transitions", "all")
                    textbutton _("None") action Preference("transitions", "none")

            vbox:
                frame:
                    add "assets/ui/h-display.png"
                hbox:
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
        

# Extras menu
screen extras_menu():
    default opt_menu = "credits"
    default folder = "Akki"
    tag menu

    window:
        style "mm_root"

    add "assets/ui/extra-title.png"
    use menu_navigation("extras")

    hbox:
        style_group "tabbar"

        button action SetScreenVariable("opt_menu", "credits"):
            add ConditionSwitch(
                  "get_screen_var('opt_menu') == 'credits'", "assets/ui/text-credits-selected.png",
                  "True", "assets/ui/text-credits.png"
                ) align (1.0, 1.0)

        button action SetScreenVariable("opt_menu", "gallery"):
            add ConditionSwitch(
                  "get_screen_var('opt_menu') == 'gallery'", "assets/ui/text-gallery-selected.png",
                  "True", "assets/ui/text-gallery.png"
                ) align (1.0, 1.0)

    if opt_menu == 'credits':
        add "assets/ui/credits.png" xpos 97 ypos 138
    else:
        use gallery(folder)


screen gallery(folder):
    tag menu

    vbox:
        style_group "gallery"

        hbox:
            style_group "gallery_folders"

            for name in map(lambda x: x.name, gallery.folders):
                textbutton _(name) action SetScreenVariable("folder", name)

        hbox:
            style_group "gallery_images"

            for bundle in gallery[get_screen_var("folder")]:
                button:
                    has vbox

                    frame:
                        add bundle.thumbnail at slot_screenshot
        

    
        

# Load screen
screen load():
    tag menu

    window:
        style "mm_root"

    add "assets/ui/load-title.png"

    use menu_navigation("load")
    use slot_picker()


# Save screen
screen save():
    tag menu
    
    window:
        style "mm_root"

    add "assets/ui/save-title.png"

    use menu_navigation("load")
    use slot_picker()


# Slots and navigation for both Save and Load screens
screen slot_picker():
    hbox:
        style_group "slot_picker_pagination"

        for i in range(1, 10):
            textbutton str(i) action FilePage(i)

    $ items_per_page = 3 * 2
    grid 3 2:
        style_group "slot_picker"

        for i in range(1, items_per_page + 1):
            button:
                action FileAction(i)
                has vbox

                $ file_name = FileSlotName(i, items_per_page)
                $ file_time = FileTime(i, empty=_(""))
                
                frame:
                    text "[file_name]. [file_time!t]"

                frame:
                    style "slot_picker_screenshot"
                    add FileScreenshot(i, empty=Null(width=1, height=1)) at slot_screenshot

                key "save_delete" action FileDelete(i)

# -- Popups / Messages / Confirmations ---------------------------------
screen yesno_prompt(message, yes_action, no_action):
    modal True

    window:
        style "confirm_popup_window"

    frame:
        style_group "confirm_popup"

        has vbox

        label _(message)
        hbox:
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

        null width 400 height 1

    # Right-click and escape answer "no".
    key "game_menu" action no_action



# Quick menu
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        imagebutton auto "assets/ui/quick-qsave-%s.png"   action [QuickSave(), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-qload-%s.png"   action [QuickLoad(), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-skip-%s.png"    action [Skip(), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-auto-%s.png"    action [Preference("auto-forward", "toggle"), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-save-%s.png"    action [ShowMenu("save"), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-load-%s.png"    action [ShowMenu("load"), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-options-%s.png" action [ShowMenu("options_menu"), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
        imagebutton auto "assets/ui/quick-quit-%s.png"    action [MainMenu(confirm=True), Play("sound", "assets/sfx/menu_select.ogg")] hovered Play("sound", "assets/sfx/menu_hover3.ogg")
