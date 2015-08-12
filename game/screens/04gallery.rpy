init python:
    gallery_folder = None
    gallery_all_unlocked = False
    gallery = Gallery(
        TutorialFolder(
            "tutorial",
            "assets/ui/gallerybtn-tips-%s.png"
        ),
        CharacterFolder(
            "akki",
            SpriteImageSet(
                "akki_sprite",
                akki,
                {
                    "base": "default",
                    "emotion_base": "default",
                    "eyes": "default",
                    "eyebrows": "default",
                    "mouth": "default",
                    "emotion": "default"
                },
                { "base": "human" },
                { "base": "naked" },
                state_filter=first
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_akki01"),
                thumb="assets/ui/gallery-akki-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_akki02"),
                thumb="assets/ui/gallery-akki-2-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-akki-3-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-akki-4-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-akki-5-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-akki-6-%s.png"),
            thumb="assets/ui/gallerybtn-akki-%s.png"
        ),
        CharacterFolder(
            "mirari",
            SpriteImageSet(
                "mirari_sprite",
                mirari,
                {
                    "base": "default",
                    "emotion_base": "default",
                    "eyes": "default",
                    "eyebrows": "default",
                    "mouth": "default",
                    "emotion": "default"
                },
                { "base": "human" },
                { "base": "baby doll" },
                { "base": "panties" },
                { "base": "naked" },
                state_filter=first
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_mira02"),
                thumb="assets/ui/gallery-mirari-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_mira01"),
                thumb="assets/ui/gallery-mirari-2-%s.png"),
            ImageBundle(
                RenpyImage("mira_back"),
                RenpyImage("mira_back nibble"),
                thumb="assets/ui/gallery-mirari-3-%s.png"),
            ImageBundle(
                RenpyImage("mira_foot"),
                RenpyImage("mira_foot nibble"),
                thumb="assets/ui/gallery-mirari-4-%s.png"),
            ImageBundle(
                RenpyImage("mira_breast"),
                thumb="assets/ui/gallery-mirari-5-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-mirari-6-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-mirari-7-%s.png"),
            thumb="assets/ui/gallerybtn-mirari-%s.png"
        ),
        CharacterFolder(
            "kael",
            SpriteImageSet(
                "kael_sprite",
                kael,
                {
                    "base": "default",
                    "emotion_base": "default",
                    "eyes": "default",
                    "eyebrows": "default",
                    "mouth": "default",
                    "emotion": "default",
                    "glasses": "default"
                },
                { "base": "apron" },
                { "base": "human" },
                { "base": "naked" },
                state_filter=first
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_kael01"),
                thumb="assets/ui/gallery-kael-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_kael02"),
                thumb="assets/ui/gallery-kael-2-%s.png"),
            ImageBundle(
                RenpyImage("kael_start"),
                RenpyImage("kael_start hand"),
                RenpyImage("kael_start kiss"),
                RenpyImage("kael_start pillow"),
                thumb="assets/ui/gallery-kael-3-%s.png"),
            ImageBundle(
                RenpyImage("kael_leaning"),
                RenpyImage("kael_leaning b"),
                thumb="assets/ui/gallery-kael-4-%s.png"),
            ImageBundle(
                RenpyImage("kael_kissing A1"),
                RenpyImage("kael_kissing A2"),
                RenpyImage("kael_kissing B"),
                thumb="assets/ui/gallery-kael-5-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-kael-6-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-kael-7-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-kael-8-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-kael-9-%s.png"),            
            thumb="assets/ui/gallerybtn-kael-%s.png"
        ),
        CharacterFolder(
            "orias",
            SpriteImageSet(
                "orias_sprite",
                orias,
                {
                    "base": "default",
                    "emotion_base": "default",
                    "eyes": "default",
                    "eyebrows": "default",
                    "mouth": "default",
                    "emotion": "default",
                    "glasses": "default"
                },
                { "base": "jacketless" },
                { "base": "tea" },
                { "base": "human" },
                { "base": "naked" },
                state_filter=first
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_orias01"),
                thumb="assets/ui/gallery-orias-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_orias02"),
                thumb="assets/ui/gallery-orias-2-%s.png"),
            ImageBundle(
                RenpyImage("orias_play cold"),
                RenpyImage("orias_play nipple"),
                RenpyImage("orias_play nipple_ice"),
                RenpyImage("orias_play nipple_suck"),
                thumb="assets/ui/gallery-orias-3-%s.png"),
            ImageBundle(
                RenpyImage("orias_play hot"),
                RenpyImage("orias_play wax_pour"),
                RenpyImage("orias_play wax_scratch"),
                thumb="assets/ui/gallery-orias-4-%s.png"),
            ImageBundle(
                RenpyImage("orias_play lick"),
                RenpyImage("orias_play kiss"),
                RenpyImage("orias_play kiss_blind"),
                thumb="assets/ui/gallery-orias-5-%s.png"),
            ImageBundle(
                RenpyImage("orias_play tickle"),
                RenpyImage("orias_play nipple_tickle"),
                RenpyImage("orias_play tickle_armpit"),
                RenpyImage("orias_play tickle_body"),
                RenpyImage("orias_play tickle_foot"),
                RenpyImage("orias_play tickle_thighs"),
                thumb="assets/ui/gallery-orias-6-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-orias-7-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-orias-8-%s.png"),
            ImageBundle(thumb="assets/ui/gallery-orias-9-%s.png"),            
            thumb="assets/ui/gallerybtn-orias-%s.png"
        ),
        ImageFolder(
            "other",
            ImageBundle(
                RenpyImage("item sock"),
                RenpyImage("item parfait"),
                RenpyImage("item bacon"),
                RenpyImage("item pizza"),
                RenpyImage("item tea"),
                RenpyImage("item toast"),
                RenpyImage("item pancakes"),
                thumb="assets/ui/gallery-other-1-%s.png"),
            ImageBundle(
                RenpyImage("nosex01"),
                RenpyImage("nosex02"),
                thumb="assets/ui/gallery-other-2-%s.png"),
            ImageBundle(
                RenpyImage("group", PannableDisplayable),
                thumb="assets/ui/gallery-other-3-%s.png"),
            thumb="assets/ui/gallerybtn-other-%s.png"
        ),
        ReplayFolder(
            "replay",
            ReplayBundle(
                "akki_sex",
                lambda: { "akki_name": "Akki",
                          "claire_name": persistent.akki_claire_name,
                          "akki_scenes": persistent.akki_scenes,
                          "sex_stop_statement": persistent.akki_sex_stop },
                thumb="assets/ui/gallery-replay-akki-%s.png"
                ),
            ReplayBundle(
                "mirari_sex",
                lambda: { "mirari_name": "Mirari",
                          "claire_name": persistent.mirari_claire_name,
                          "mirari_scenes": persistent.mirari_scenes,
                          "sex_stop_statement": persistent.mirari_sex_stop },
                thumb="assets/ui/gallery-replay-mirari-%s.png"
                ),
            ReplayBundle(
                "kael_sex",
                lambda: { "kael_name": "Kael",
                          "claire_name": persistent.kael_claire_name,
                          "kael_scenes": persistent.kael_scenes,
                          "sex_stop_statement": persistent.kael_sex_stop },
                thumb="assets/ui/gallery-replay-kael-%s.png"
                ),
            ReplayBundle(
                "orias_sex",
                lambda: { "orias_name": "Orias",
                          "claire_name": persistent.orias_claire_name,
                          "orias_scenes": persistent.orias_scenes,
                          "sex_stop_statement": persistent.orias_sex_stop },
                thumb="assets/ui/gallery-replay-orias-%s.png"
                ),
            thumb="assets/ui/gallerybtn-scenereplay-%s.png"
        )
    )

    gallery.add_unlockable_sprite(akki, "akki_sprite", state_filter=first)
    gallery.add_unlockable_sprite(mirari, "mirari_sprite", state_filter=first)
    gallery.add_unlockable_sprite(kael, "kael_sprite", state_filter=first)
    gallery.add_unlockable_sprite(orias, "orias_sprite", state_filter=first)
    
    gallery.add_unlockable_sprite(akki_foreplay, "akki_foreplay")
    gallery.add_unlockable_sprite(akki_missionary_sprite, "akki_missionary")
    gallery.add_unlockable_sprite(akki_cuddle_sprite, "akki_cuddle")



screen gallery():
    tag menu

    hbox:
        style_group "gallery"

        vbox:
            style_group "gallery_folders"

            for folder in gallery.folders:
                imagebutton:
                    auto folder.thumb
                    action [folder.select(), SetVariable("gallery_folder", folder.name)]

    # Character folders can't be shown on top of the other screens
    # because we need the character's sprite to show behind the
    # main menu. Also, tracking shown screens everywhere is hell.
    # Ugly hack ensues!
    $ cur_folder = gallery[gallery_folder]
    if isinstance(cur_folder, CharacterFolder):
        use image_folder(cur_folder.bundles, character=cur_folder.sprite)
    elif isinstance(cur_folder, ReplayFolder):
        use replay_folder(cur_folder.bundles)
    elif isinstance(cur_folder, ImageFolder):
        use image_folder(cur_folder.bundles)
        

screen replay_folder(bundles):
    tag gallery_folder

    fixed:
        style_group "replay_folder"
        
        frame:
            style_group "replay_folder_images"

            hbox:
                for bundle in bundles:
                    if bundle.is_unlocked():
                        imagebutton:
                            auto bundle.thumb
                            action bundle.show()
                    else:
                        add "assets/ui/gallery-replay-locked.png"


transform gallery_sprite:
    zoom 0.5
    xalign 1.0
    yalign 1.3

init python:
    gallery_charidx = 0
    
screen image_folder(bundles, character=None):
    tag gallery_folder

    python:
        def get_image(images, index):
            if index == 0 or images[index].is_unlocked():
                return images[index].get_displayable()
            else:
                return Null()

        def get_next(images, index):
            for i in xrange(index + 1, len(images)):
                if images[i].is_unlocked():
                    return i

        def get_prev(images, index):
            for i in xrange(index - 1, -1, -1):
                if i == 0 or images[i].is_unlocked():
                    return i
    
    fixed:
        style_group "gallery_folder"

        frame:
            style_group "gallery_folder_images"
            
            hbox:
                for bundle in bundles:
                    if bundle.is_unlocked():
                        fixed:
                            style_group "gallery_folder_bundle"

                            imagebutton:
                                auto bundle.thumb
                                action bundle.show()
                            window:
                                $ total = bundle.get_total()
                                $ unlocked = len(bundle.get_unlocked())
                                text "{0} / {1}".format(unlocked, total)
                    else:
                        add "assets/ui/gallery-locked.png"

                        

        if character is not None:
            add get_image(character, gallery_charidx) at gallery_sprite

            hbox:
                style_group "gallery_character_select_outfit"

                $ prev_image = get_prev(character, gallery_charidx)
                $ next_image = get_next(character, gallery_charidx)

                if prev_image is not None:
                    imagebutton:
                        auto "assets/ui/gallery-outfitselect-left-%s.png"
                        action SetVariable("gallery_charidx", prev_image)
                else:
                    null width 21

                text "{0} / {1}".format(gallery_charidx + 1, len(character))

                if next_image is not None:
                    imagebutton:
                        auto "assets/ui/gallery-outfitselect-right-%s.png"
                        action SetVariable("gallery_charidx", next_image)
                else:
                    null width 21

                
                    

screen gallery_view(images):
    modal True
    default current = 0
    default old_displayable = Null()

    python:
        def next_image(images, x):
            for index in xrange(x + 1, len(images)):
                if images[index] is not None:
                    return index

        def prev_image(images, x):
            for index in xrange(x - 1, -1, -1):
                if images[index] is not None:
                    return index

        def go(images, current, x):
            return [
                SetScreenVariable("current", x),
                SetScreenVariable("old_displayable", images[current].get_displayable())
            ]

    window:
        style_group "gallery_view"

        has fixed

        frame:
            style "gallery_view_displayable_frame"
            
            add images[current].get_displayable()

        text "{0} / {1}".format(current + 1, len(images)) style "gallery_view_status"

        key "game_menu" action Hide("gallery_view", transition=dissolve)

        $ next = next_image(images, current)
        $ prev = prev_image(images, current)
        if next is not None:
            key "dismiss" action go(images, current, next)
        else:
            key "dismiss" action Hide("gallery_view", transition=dissolve)

        if prev is not None:
            key "rollback" action go(images, current, prev)


init:
    style gallery_view_window:
        xpadding 0
        ypadding 0
        xfill True
        yfill True
    
    style gallery_view_displayable_frame:
        background None
        xalign 0.5
        yalign 0.5

    style gallery_view_displayable_frame:
        xpadding 0
        ypadding 0
        
    style gallery_view_status:
        xalign 0.95
        yalign 0.95
        color "#ffffff"
        size 24
        outlines [(2, "#ff63a1", 0, 0)]
