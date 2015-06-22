init python:
    gallery_folder = "Akki"
    gallery = Gallery(
        GalleryFolder(
            "Akki",
            [CG("chibi_akki01", "assets/chibis/akki_hug.png")],
            [CG("chibi_akki02", "assets/chibis/akki_sit.png")],
            [SpriteCG("akki_foreplay", akki_foreplay,
                      {
                        "akki_bottom": "on",
                        "claire_arm": "down",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm": "down",
                        "heads": "kiss",
                        "claire_face": "default",
                        "akki_face": "default"
                        },
                      {
                        "akki_face": "D:",
                        "claire_face": "smile",
                        "heads": "apart"
                        },
                      {
                        "heads": "kiss",
                        "claire_face": "default",
                        "akki_face": "default",
                        "akki_arm": "breast"
                        },
                      {
                        "claire_face": "smile",
                        "akki_face": "nervous",
                        "heads": "apart"
                        },
                      {
                        "akki_face": "D:"
                        },
                      {
                        "claire_face": "pleasure"
                        }
                      )]
        ),
        GalleryFolder(
            "Orias",
            [CG("chibi_orias01", "assets/chibis/orias_tea.png")]
        ),
        GalleryFolder(
            "Kael",
            [CG("chibi_kael01", "assets/chibis/kael_laundry.png")]
        ),
        GalleryFolder(
            "Mirari",
            [CG("chibi_mira01", "assets/chibis/mirari_hair.png")]
        ),
        GalleryFolder(
            "Others",
            [CG("chibi_nosex01", "assets/chibis/NoOneEnd_01.png"),
             CG("chibi_nosex02", "assets/chibis/NoOneEnd_02.png")]
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
                    if bundle.unlocked > 0:
                        action Show("gallery_view", dissolve, bundle)

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
