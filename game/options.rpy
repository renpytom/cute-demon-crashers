init -1 python:
    optional_edits = False

init -1 python hide:
    # -- Persistent data -----------------------------------------------
    # `censor_18` is used for defining whether we should censor the sexy
    # bits or not.
    if persistent.censor_18 is None:
        persistent.censor_18 = False

    if persistent.menu_choices is None:
        persistent.menu_choices = {}

    # -- Config stuff --------------------------------------------------
    config.developer = True

    config.screen_width = 1280
    config.screen_height = 800

    config.thumbnail_width = 223
    config.thumbnail_height = 138

    config.window_title = u"Cute Demon Crashers!"

    config.name = "Cute Demon Crashers!"
    config.version = "0.0"

    #---for the voices -----------------------m_epi------
    config.voice_filename_format = "assets/voices/{filename}.ogg"

    # ------------------------------------------------------------------
    # Themes
    theme.roundrect(
        ## The color of an idle widget face.
        widget = "#ECC7D0",

        ## The color of a focused widget face.
        widget_hover = "#E1D4C9",

        ## The color of the text in a widget.
        widget_text = "#805C40",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#805C40",

        ## The color of a disabled widget face.
        disabled = "#C8AFA1",

        ## The color of disabled widget text.
        disabled_text = "#E1D4C9",

        ## The color of informational labels.
        label = "#805C40",

        ## The color of a frame containing widgets.
        frame = "#FCF5F2",

        ## The background of the main menu.
        mm_root = "assets/ui/menu-bg.png",

        ## The background of the game menu.
        gm_root = "assets/ui/menu-bg.png",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,
        )


init -1:
    transform button_hearts_transform:
        anchor (.5,.5)
        xalign 1.0
        yalign 0.0
        yoffset -25
        xoffset 15

    transform slot_screenshot:
        xoffset 29
        yoffset 37
        size (223, 138)

    transform say_image:
        xoffset -45
        yalign 1.1
        zoom 0.82


    # -- Default styles ------------------------------------------------
    style default:
        font "assets/fonts/quicksand.otf"
        size 22

    style button:
        ypadding 5
        left_padding 25
        right_padding 40
        ymargin 10
        background Frame("assets/ui/button-bg.png", 20, 14, tile=True)
        hover_background Frame("assets/ui/button-hover-bg.png", 25, 18, tile=True)
        selected_background Frame("assets/ui/button-hover-bg.png", 25, 18, tile=True)
        selected_foreground At("assets/ui/button-hearts.png", button_hearts_transform)

    style button_text:
        color "#b86cdf"

    style slider:
        left_bar LiveTile("assets/ui/bar-filled.png")
        right_bar LiveTile("assets/ui/bar-empty.png")
        right_gutter 0
        ysize 44
        thumb None


    # -- Top tabs on screens -------------------------------------------
    style tabbar_hbox:
        xpos 375
        ypos -10
        spacing 25

    style tabbar_button:
        xysize (364, 86)
        xpadding 0
        background "assets/ui/tab-idle.png"
        hover_background "assets/ui/tab-hover.png"
        selected_background "assets/ui/tab-hover.png"
        foreground None

    style tabbar_text:
        yalign 1.0
        xalign 1.0
        yoffset 20
        xoffset 10

    # -- Options screen ------------------------------------------------
    style mm_opts_grid:
        ypos 115
        xoffset 60
        right_padding 60
        xfill True

    style mm_opts_frame:
        background "assets/ui/name-bg.png"
        top_margin 20
        top_padding 20
        left_padding 60

    style mm_opts_hbox:
        spacing 40
        xoffset 60

    style mm_opts_slider:
        xsize 420
        xoffset 60

    style mm_opts_button:
        xsize 200

    style mm_opts_button_text:
        size 18

    # -- Start popup ---------------------------------------------------
    style mm_popup_frame:
        background "assets/ui/start-popup-bg.png"
        xpos 423
        ypos 239
        top_padding 80
        left_padding 60


    # -- Save / Load ---------------------------------------------------
    style slot_picker_pagination_hbox:
        xpos 490
        ypos 15

    style slot_picker_pagination_button:
        background "assets/ui/heart-page-idle.png"
        hover_background "assets/ui/heart-page-hover.png"
        selected_background "assets/ui/heart-page-hover.png"
        foreground None

    style slot_picker_pagination_button_text:
        xoffset -15
        yoffset 15
        color "#ffffff"
        outlines [(2, "#00000000", 1, 1), (2, "#ff8ec1", 0, 0)]
        hover_outlines [(2, "#a45fdf", 1, 1), (2, "#ff63a1", 0, 0)]
        selected_outlines [(2, "#a45fdf", 1, 1), (2, "#ff63a1", 0, 0)]

    style slot_picker_grid:
        ypos 100
        xpos 100
        spacing 0

    style slot_picker_button:
        background None
        foreground None
        ymargin 0
        top_padding 0
        bottom_padding 10

    style slot_picker_frame:
        background "assets/ui/name-bg.png"
        left_padding 80
        top_padding 30

    style slot_picker_text:
        color "#fff"
        size 22

    style slot_picker_screenshot:
        yoffset -10
        xoffset 60
        xsize 302
        ysize 202
        background "assets/ui/slot-bg.png"
        hover_foreground "assets/ui/slot-fg.png"

    # -- Gallery -------------------------------------------------------
    style gallery_hbox:
        xpos 0
        ypos 150
        spacing 20

    style gallery_folders_vbox:
        spacing 2

    style gallery_images_hbox:
        box_wrap True
        xpadding 30

    style gallery_images_button is slot_picker_button

    style gallery_images_frame is slot_picker_screenshot


    # -- Confirm popups ------------------------------------------------
    style confirm_popup_window:
        xfill True
        yfill True
        background Solid((0, 0, 0, 127))

    style confirm_popup_frame:
        xpos 409
        ypos 47
        xpadding 90
        background "assets/ui/confirm-popup-bg.png"

    style confirm_popup_vbox:
        ypos 240
        xsize 400
        xalign 0.5
        spacing 30

    style confirm_popup_label_text:
        xalign 0.5
        text_align 0.5
        color "#fff"
        outlines [(2, "#ff63a1", 0, 0)]

    style confirm_popup_hbox:
        xalign 0.5
        spacing 50

    style confirm_popup_button:
        xpadding 50
        hover_foreground At("assets/ui/button-hearts.png", button_hearts_transform)

    # -- Choices -------------------------------------------------------
    style menu_window is confirm_popup_window

    style menu_choice_vbox:
        yalign 0.5
        xalign 0.5
        yoffset -40

    style menu_choice_button:
        xpadding 100
        top_padding 20
        ysize 115
        xsize 1027
        background "assets/ui/btn-choice-idle.png"
        hover_background "assets/ui/btn-choice-hover.png"
        activate_sound "assets/sfx/menu_select.ogg"
        hover_sound "assets/sfx/menu_hover3.ogg"

    style menu_choice_button_text:
        color "#ffffffcc"
        hover_color "#ffffff"
        outlines [(2, "#ff63a1", 0, 0)]
        size 24
        text_align 0.5


    style sexy_menu_choice_vbox is menu_choice_vbox

    style sexy_menu_choice_button_text is menu_choice_button_text

    style sexy_menu_choice_button is menu_choice_button:
        ysize 131
        xsize 686
        background "assets/ui/sexy-button-idle.png"
        hover_background "assets/ui/sexy-button-hover.png"
        top_padding 15


    # -- Dialogue boxes ------------------------------------------------
    style say_window:
        yalign 1.0
        xalign 0.0
        xfill True
        background None
        xpadding 0
        ypadding 0

    style say_vbox:
        spacing 0

    style say_nameplate_frame:
        background "assets/ui/nameplate-bg.png"
        yalign 1.0
        xoffset 20
        yoffset -227

    style say_label:
        color "#ffffff"
        size 24
        xoffset 75
        yoffset 33
        bold False
        outlines [(2, "#6c58c1", 1, 1), (2, "#926ae5", 0, 0)]

    style say_dialogue_window:
        xfill True
        ysize 227
        xpadding 100
        left_padding 50
        ypadding 50
        background Frame("assets/ui/text-box.png", 226, 112, right=80, tile=True)

    style say_dialogue:
        xoffset 50
        color "#ffffff"
        size 24
        outlines [(2, "#ff63a1", 0, 0)]

    style say_thought is say_dialogue:
        xoffset 0

    style say_side_image_frame:
        background None
        xpadding 0
        ypadding 0
        yalign 1.0
        yoffset 50

    style say_side_image_window:
        background None
        yalign 1.0
        left_margin 153
        xfill True
        ypadding 0
        xpadding 0

    # -- Quick menu ----------------------------------------------------
    style quick_hbox:
        xalign 1.0
        xoffset -20
        yalign 1.0
        yoffset -205

    style quick_button:
        xpadding 0
        left_margin 10

    style quick_button_text:
        size 20

    # -- Input ---------------------------------------------------------
    style input_window is confirm_popup_window
    style input_popup_frame is confirm_popup_frame
    style input_popup_vbox is confirm_popup_vbox
    style input_popup_label_text is confirm_popup_label_text:
        xalign 0.5
        text_align 0.5

    style input_text:
        xalign 0.5
        text_align 0.5
        size 32
        outlines [(2, "#ff63a1", 0, 0)]


    # -- House map -----------------------------------------------------
    style housemap_window:
        align (0, 0)
        xfill True
        yfill True

    style housemap_fixed:
        xysize (859, 539)
        align (0.5, 0.5)

    style housemap_description is say_dialogue:
        xoffset 0
        xpos 74
        ypos 426
        xsize 355



init -1 python hide:

    # Fonts that may be chosen by the user
    renpy.register_style_preference(
        "text", "quicksand", style.say_dialogue, "font", "assets/fonts/quicksand.otf")
    renpy.register_style_preference(
        "text", "open-dyslexic", style.say_dialogue, "font", "assets/fonts/open-dyslexic.otf")

    # cursor
    config.mouse = {
        "default": [("assets/ui/cursor.png", 0, 0)]
    }


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "assets/sfx/menu_select.ogg"
    style.imagemap.activate_sound = "assets/sfx/menu_select.ogg"

    style.button.hover_sound = "assets/sfx/menu_hover3.ogg"
    style.imagemap.hover_sound = "assets/sfx/menu_hover3.ogg"


    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "assets/sfx/sfx_test.ogg"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "assets/music/Orangebeat - Romantic Tension.mp3"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    # ------------------------------------------------------------------
    # Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    ## Used for providing auto-choices for menus
    def menu_choice_before_callback(choices, name):
        if _in_replay:
            return persistent.menu_choices.get(name, None)

    def menu_choice_after_callback(choice_, name):
        if not _in_replay:
            persistent.menu_choices[name] = choice_
    
    config.menu_choice_before_callback = menu_choice_before_callback
    config.menu_choice_after_callback = menu_choice_after_callback
    
    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "cute-demon-crashers-1425242232"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 0

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "Cute_Demon_Crashers-Akki_and_Mirari-1.0.7"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Cute Demon Crashers - Akki and Mirari"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # Declare two archives.
    build.archive("scripts", "all")
    build.archive("images", "all")

    # Put script files into the scripts archive.
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

