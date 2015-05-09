init python:
    gallery_folder = "Akki"
    gallery = Gallery(
        GalleryFolder(
            "Akki",
            [CG("chibi_akki01", "assets/chibis/akki_hug.png")],
            [CG("chibi_akki02", "assets/chibis/akki_sit.png")]
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
        GalleryFolder("Others")
    )

    def bundle_to_stateful_displayable(bundle, state):
        return StateMachineDisplayable(
            "gallery_bundle",
            state,
            dict(zip(range(bundle.total), map(lambda x: x.image, bundle.images)))
        )


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
                        action Show("gallery_view", dissolve, bundle, bundle_to_stateful_displayable(bundle, 0))

                    vbox:
                        frame:
                            add bundle.thumbnail at slot_screenshot

                        
screen gallery_view(bundle, displayable):
    modal True

    python:
        def next_image(b, x):
            for index in xrange(x + 1, len(b.images)):
                if not b.images[index].is_locked():
                    return index
    
        def prev_image(b, x):
            for index in xrange(len(b.images) - 1, x, -1):
                if not b.images[index].is_locked():
                    return index

        def go(x):
            def action():
                displayable.set_state(with_dissolve, x)

            return action
            
    $ current = displayable.current_state
    window:
        style_group "gallery_view"

        has fixed

        frame:
            add displayable

        text "{0} / {1}".format(current + 1, bundle.total) style "gallery_view_status"

        key "dismiss" action Hide("gallery_view", transition=dissolve)

        $ next = next_image(bundle, current)
        $ prev = prev_image(bundle, current)
        if next is not None:
            key "focus_right" action go(next)
            
        if prev is not None:
            key "focus_left" action go(prev)
        
        
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
