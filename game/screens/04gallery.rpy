init python:
    gallery_folder = "Akki"
    gallery = Gallery(
        GalleryFolder(
            "Akki",
            ImageSet(RenpyImage("chibi_akki01")),
            ImageSet(RenpyImage("chibi_akki02")),
            ReplayBundle("akki_sex",
                         akki_foreplay.snapshot( akki_bottom="on",
                                                 claire_arm="down",
                                                 claire_bottom="on",
                                                 claire_top="on",
                                                 akki_arm="down",
                                                 heads="kiss",
                                                 claire_face="default",
                                                 akki_face="default" ),
                         lambda: { "akki_name": "Akki",
                                   "claire_name": persistent.akki_claire_name,
                                   "akki_scenes": persistent.akki_scenes,
                                   "sex_stop_statement": persistent.akki_sex_stop }
                )
        ),
        GalleryFolder(
            "Orias",
            ImageSet(RenpyImage("chibi_orias01")),
            ImageSet(RenpyImage("chibi_orias02")),
            ImageSet(RenpyImage("orias_play cold"),
                     RenpyImage("orias_play nipple"),
                     RenpyImage("orias_play nipple_ice"),
                     RenpyImage("orias_play nipple_suck"),
                     RenpyImage("orias_play lick")),
            ImageSet(RenpyImage("orias_play hot"),
                     RenpyImage("orias_play wax_pour"),
                     RenpyImage("orias_play wax_rub"),
                     RenpyImage("orias_play wax_scratch"),
                     RenpyImage("orias_play kiss"),
                     RenpyImage("orias_play kiss_blind")),
            ImageSet(RenpyImage("orias_play tickle"),
                     RenpyImage("orias_play nipple_tickle"),
                     RenpyImage("orias_play tickle_armpit"),
                     RenpyImage("orias_play tickle_body"),
                     RenpyImage("orias_play tickle_foot"),
                     RenpyImage("orias_play tickle_thighs")),
            ReplayBundle("orias_sex",
                         orias_bed_sprite.snapshot(**orias_bed_initial),
                         lambda: { "orias_name": "Orias",
                                   "claire_name": persistent.orias_claire_name,
                                   "orias_scenes": persistent.orias_scenes,
                                   "sex_stop_statement": persistent.orias_sex_stop })
        ),
        GalleryFolder(
            "Kael",
            ImageSet(RenpyImage("chibi_kael01")),
            ImageSet(RenpyImage("chibi_kael02")),
            ImageSet(RenpyImage("kael_start"),
                     RenpyImage("kael_start hand"),
                     RenpyImage("kael_start kiss"),
                     RenpyImage("kael_start pillow")),
            ImageSet(RenpyImage("kael_leaning"),
                     RenpyImage("kael_leaning b")),
            ImageSet(RenpyImage("kael_kissing A1"),
                     RenpyImage("kael_kissing A2"),
                     RenpyImage("kael_kissing B")),
            ReplayBundle("kael_sex",
                         kael_warmup_sprite.snapshot(**kael_warmup_initial),
                         lambda: { "kael_name": "Kael",
                                   "claire_name": persistent.kael_claire_name,
                                   "kael_scenes": persistent.kael_scenes,
                                   "sex_stop_statement": persistent.kael_sex_stop })
        ),
        GalleryFolder(
            "Mirari",
            ImageSet(RenpyImage("chibi_mira01")),
            ImageSet(RenpyImage("chibi_mira02")),
            ImageSet(CG("mira_foot", "assets/CGs/mirari_massage_leg.jpg"),
                     CG("mira_foot nibble", "assets/CGs/mirari_nibble_foot.png")),
            ImageSet(CG("mira_back", "assets/CGs/mirari_massage_back.jpg"),
                     CG("mira_back nibble", "assets/CGs/mirari_nibble_ear.png")),
            ImageSet(CG("mira_breast", naked("assets/CGs/mirari_breasts{0}.jpg"))),
            ReplayBundle("mirari_sex",
                         mirari_lying_sprite.snapshot(**mirari_lying_initial),
                         lambda: { "mirari_name": "Mirari",
                                   "claire_name": persistent.mirari_claire_name,
                                   "mirari_scenes": persistent.mirari_scenes,
                                   "sex_stop_statement": persistent.mirari_sex_stop })
        ),
        GalleryFolder(
            "Others",
            ImageSet(RenpyImage("nosex01"),
                     RenpyImage("nosex02")),
            ImageSet(RenpyImage("item sock")),
            ImageSet(RenpyImage("item parfait"),
                     RenpyImage("item bacon"),
                     RenpyImage("item pizza"),
                     RenpyImage("item tea"),
                     RenpyImage("item toast"),
                     RenpyImage("item pancakes")),
            ImageSet(RenpyImage("group"))
        )
    )

    gallery.add_unlockable_sprite(akki_foreplay, "akki_foreplay")
    gallery.add_unlockable_sprite(akki_missionary_sprite, "akki_missionary")
    gallery.add_unlockable_sprite(akki_cuddle_sprite, "akki_cuddle")



screen gallery():
    tag menu

    vbox:
        style_group "gallery"

        hbox:
            style_group "gallery_folders"

            for name in map(lambda x: x.name, gallery.folders):
                textbutton _(name) action SetVariable("gallery_folder", name)

        hbox:
            style_group "gallery_images"

            for bundle in gallery[gallery_folder]:
                button:
                    if bundle.is_unlocked():
                        action bundle.display()

                    vbox:
                        frame:
                            add bundle.thumbnail at slot_screenshot


screen gallery_view(bundle):
    modal True
    default current = 0
    default old_displayable = Null()

    python:
        def next_image(b, x):
            for index in xrange(x + 1, len(b.images)):
                if not b.images[index].is_locked():
                    return index

        def prev_image(b, x):
            for index in xrange(x - 1, -1, -1):
                if not b.images[index].is_locked():
                    return index

        def go(bundle, current, x):
            return [
                SetScreenVariable("current", x),
                SetScreenVariable("old_displayable", bundle.images[current].image)
            ]

    window:
        style_group "gallery_view"

        has fixed

        frame:
            add bundle.images[current].image

        text "{0} / {1}".format(current + 1, bundle.total) style "gallery_view_status"

        key "game_menu" action Hide("gallery_view", transition=dissolve)

        $ next = next_image(bundle, current)
        $ prev = prev_image(bundle, current)
        if next is not None:
            key "dismiss" action go(bundle, current, next)
        else:
            key "dismiss" action Hide("gallery_view", transition=dissolve)

        if prev is not None:
            key "rollback" action go(bundle, current, prev)


init:
    style gallery_view_frame:
        background None
        xalign 0.5
        yalign 0.5

    style gallery_view_status:
        xalign 0.95
        yalign 0.95
        color "#ffffff"
        size 24
        outlines [(2, "#ff63a1", 0, 0)]
