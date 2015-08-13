transform gallery_sprite:
    zoom 0.5
    xalign 1.0

transform kael_sprite_pos:
    yalign 1.2

transform akki_sprite_pos:
    yalign 1.2
    
transform mirari_sprite_pos:
    yalign 1.1
    
transform orias_sprite_pos:
    yalign 1.5

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
                state_filter=first,
                transform_=akki_sprite_pos
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_akki01"),
                thumb="assets/ui/gallery-akki-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_akki02"),
                thumb="assets/ui/gallery-akki-2-%s.png"),
            ImageBundle(
                RenpyImage("akki_kiss A"),
                RenpyImage("akki_kiss B"),
                thumb="assets/ui/gallery-akki-3-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "akki_foreplay",
                    akki_foreplay,
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm": "down",
                        "claire_arm": "down",
                        "heads": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm": "down",
                        "claire_arm": "down",
                        "heads": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm ": "breast",
                        "claire_arm": "down",
                        "heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm ": "breast",
                        "claire_arm": "chest",
                        "heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "down",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "O"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "O"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "on",
                        "akki_arm ": "down",
                        "claire_arm": "down",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "down",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "on",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "O"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "akki_arm": "down",
                        "claire_top": "bra",
                        "claire_arm": "down",
                        "heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "off",
                        "akki_arm ": "breast",
                        "claire_arm": "down",
                        "heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "off",
                        "akki_arm ": "breast",
                        "claire_arm": "down",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "off",
                        "akki_arm ": "breast",
                        "claire_arm": "chest",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "on",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "down",
                        "claire_arm": "down",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "down",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "on",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "crotch",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "O"
                        },
                    {
                        "akki_bottom": "off",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "down",
                        "claire_arm": "down",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "happy"
                        },
                    {
                        "akki_bottom": "off",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "handjob",
                        " heads ": "kiss",
                        "akki_face": "none",
                        "claire_face": "none"
                        },
                    {
                        "akki_bottom": "off",
                        "claire_bottom": "off",
                        "claire_top": "off",
                        "akki_arm ": "finger",
                        "claire_arm": "down",
                        " heads ": "apart",
                        "akki_face": "happy",
                        "claire_face": "O"
                        }
                ),
                thumb="assets/ui/gallery-akki-4-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "akki_missionary",
                    akki_missionary_sprite,
                    { "claire": 1, "akki": 1 },
                    { "claire": 2, "akki": 2 },
                    { "claire": 2, "akki": 3 },
                    { "claire": 2, "akki": 4 },
                    { "claire": 4, "akki": 1 },
                    { "claire": 3, "akki": 5 },
                    { "claire": 1, "akki": 6 }
                    ),
                thumb="assets/ui/gallery-akki-5-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "akki_cuddle",
                    akki_cuddle_sprite,
                    { "akki": 3, "claire": 3, "base": "clothed" },
                    { "akki": 3, "claire": 1, "base": "naked" },
                    { "akki": 2, "claire": 2, "base": "naked" },
                    { "akki": 1, "claire": 2, "base": "naked" },
                    { "akki": 3, "claire": 3, "base": "naked" }
                    ),
                thumb="assets/ui/gallery-akki-6-%s.png"),
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
                state_filter=first,
                transform_=mirari_sprite_pos                
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_mira01"),
                thumb="assets/ui/gallery-mirari-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_mira02"),
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
            ImageBundle(
                SpriteImageSet(
                    "mirari_lying",
                    mirari_lying_sprite,
                    {
                        "panties":  "on",
                        "claire_arm":  "fold",
                        "mirari_arm": "fold",
                        "mirari_face": "tender",
                        "claire_face": "oh"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "fold",
                        "mirari_arm": "breast",
                        "mirari_face": "happy",
                        "claire_face": "smile"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "fold",
                        "mirari_arm": "touch",
                        "mirari_face": "happy",
                        "claire_face": "pleasure"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "fold",
                        "mirari_arm": "touch",
                        "mirari_face": "tender",
                        "claire_face": "O"
                        },
                    {
                        "panties":  "on",
                        "claire_arm":  "breast",
                        "mirari_arm ": "breast",
                        "mirari_face ": "happy",
                        "claire_face": "smile"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "breast",
                        "mirari_arm": "breast",
                        "mirari_face": "happy",
                        "claire_face": "smile"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "touch",
                        "mirari_arm": "touch",
                        "mirari_face": "pleasure",
                        "claire_face": "pleasure"
                        },
                    {
                        "panties":  "off",
                        "claire_arm":  "fold",
                        "mirari_arm": "lick",
                        "mirari_face": "tease",
                        "claire_face": "shock"
                        }
                    ),
                thumb="assets/ui/gallery-mirari-6-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "mirari_cuddle",
                    mirari_cuddle_sprite,
                    mirari_cuddle_initial,
                    { "mirari": 2, "claire": 1 },
                    { "mirari": 3, "claire": 2 }
                    ),
                thumb="assets/ui/gallery-mirari-7-%s.png"),
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
                state_filter=first,
                transform_=kael_sprite_pos                
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_kael01"),
                thumb="assets/ui/gallery-kael-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_kael02"),
                thumb="assets/ui/gallery-kael-2-%s.png"),
            ImageBundle(
                RenpyImage("kael_start"),
                thumb="assets/ui/gallery-kael-3-%s.png"),
            ImageBundle(
                RenpyImage("kael_start hand"),
                RenpyImage("kael_start kiss"),
                RenpyImage("kael_start pillow"),
                thumb="assets/ui/gallery-kael-4-%s.png"),
            ImageBundle(
                RenpyImage("kael_leaning"),
                RenpyImage("kael_leaning b"),
                thumb="assets/ui/gallery-kael-5-%s.png"),
            ImageBundle(
                RenpyImage("kael_kissing A1"),
                RenpyImage("kael_kissing A2"),
                RenpyImage("kael_kissing B"),
                thumb="assets/ui/gallery-kael-6-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "kael_warmup",
                    kael_warmup_sprite,
                    kael_warmup_initial,
                    { "kael": 2, "claire": 2 },
                    { "kael": 3, "claire": 3 }
                    ),
                thumb="assets/ui/gallery-kael-7-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "kael_missionary",
                    kael_missionary_sprite,
                    { "kael": 2, "claire": 2 },
                    { "kael": 2, "claire": 1 },
                    { "kael": 1, "claire": 1 },
                    { "kael": 3, "claire": 3 },
                    { "kael": 4, "claire": 3 },
                    { "kael": 1, "claire": 4 },
                    { "kael": 4, "claire": 6 }
                    ),
                thumb="assets/ui/gallery-kael-8-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "kael_cuddles",
                    kael_cuddles_sprite,
                    kael_cuddles_initial,
                    {
                        "kael_naked": False,
                        "claire_naked": True,
                        "claire_face": 2,
                        "kael_face": 2
                        },
                    {
                        "kael_naked": True,
                        "claire_naked": True,
                        "claire_face": 1,
                        "kael_face": 1
                        },
                    {
                        "kael_naked": True,
                        "claire_naked": True,
                        "claire_face": 2,
                        "kael_face": 2
                        }
                    ),
                thumb="assets/ui/gallery-kael-9-%s.png"),            
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
                state_filter=first,
                transform_=orias_sprite_pos
            ).get_items(),
            ImageBundle(
                RenpyImage("chibi_orias01"),
                thumb="assets/ui/gallery-orias-1-%s.png"),
            ImageBundle(
                RenpyImage("chibi_orias02"),
                thumb="assets/ui/gallery-orias-2-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "orias_bed",
                    orias_bed_sprite,
                    orias_bed_initial,
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":False,
                        "blindfold":False,
                        "claire_face":"happy",
                        "orias_face":"smile"
                        },
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":False,
                        "blindfold":False,
                        "claire_face":"content",
                        "orias_face":"smile"
                        },
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":False,
                        "blindfold":True,
                        "claire_face":"content",
                        "orias_face":"smile"
                        },
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":True,
                        "blindfold":False,
                        "claire_face":"shiver",
                        "orias_face":"laugh"
                        },
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":False,
                        "blindfold":True,
                        "claire_face":"laugh",
                        "orias_face":"laugh"
                        },
                    {
                        "naked":False,
                        "panties":"on",
                        "tiedup":True,
                        "blindfold":True,
                        "claire_face":"pleasure",
                        "orias_face":"smile"
                        },
                    {
                        "naked":False,
                        "panties":"off",
                        "tiedup":True,
                        "blindfold":True,
                        "claire_face":"O",
                        "orias_face":"smile"
                        }
                    ),                
                thumb="assets/ui/gallery-orias-3-%s.png"),
            ImageBundle(
                RenpyImage("orias_play cold"),
                RenpyImage("orias_play nipple"),
                RenpyImage("orias_play nipple_ice"),
                RenpyImage("orias_play nipple_suck"),
                thumb="assets/ui/gallery-orias-4-%s.png"),
            ImageBundle(
                RenpyImage("orias_play hot"),
                RenpyImage("orias_play wax_pour"),
                RenpyImage("orias_play wax_rub"),
                RenpyImage("orias_play wax_scratch"),
                thumb="assets/ui/gallery-orias-5-%s.png"),
            ImageBundle(
                RenpyImage("orias_play tickle"),
                RenpyImage("orias_play nipple_tickle"),
                RenpyImage("orias_play tickle_armpit"),
                RenpyImage("orias_play tickle_foot"),
                RenpyImage("orias_play tickle_thighs"),
                thumb="assets/ui/gallery-orias-6-%s.png"),
            ImageBundle(
                RenpyImage("orias_play kiss"),
                RenpyImage("orias_play kiss_blind"),
                thumb="assets/ui/gallery-orias-7-%s.png"),
            ImageBundle(
                RenpyImage("orias_finish oral"),
                RenpyImage("orias_finish finger"),
                thumb="assets/ui/gallery-orias-8-%s.png"),
            ImageBundle(
                SpriteImageSet(
                    "orias_cuddles",
                    orias_cuddles_sprite,
                    orias_cuddles_initial,
                    {
                        "orias_naked": False,
                        "claire_naked": True,
                        "claire_face": 3,
                        "orias_face": 1
                        },
                    {
                        "orias_naked": True,
                        "claire_naked": True,
                        "claire_face": 2,
                        "orias_face": 2
                        },
                    {
                        "orias_naked": True,
                        "claire_naked": True,
                        "claire_face": 4,
                        "orias_face": 3
                        },
                    {
                        "orias_naked": True,
                        "claire_naked": True,
                        "claire_face": 3,
                        "orias_face": 4
                        },
                    {
                        "orias_naked": True,
                        "claire_naked": True,
                        "claire_face": 3,
                        "orias_face": 1
                        }
                    ),                
                thumb="assets/ui/gallery-orias-9-%s.png"),            
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
                lambda: persistent.akki_replay,
                lambda: { "akki_name": "Akki",
                          "claire_name": persistent.akki_claire_name,
                          "akki_scenes": persistent.akki_scenes,
                          "sex_stop_statement": persistent.akki_sex_stop },
                thumb="assets/ui/gallery-replay-akki-%s.png"
                ),
            ReplayBundle(
                "mirari_sex",
                lambda: persistent.mirari_replay,
                lambda: { "mirari_name": "Mirari",
                          "claire_name": persistent.mirari_claire_name,
                          "mirari_scenes": persistent.mirari_scenes,
                          "sex_stop_statement": persistent.mirari_sex_stop },
                thumb="assets/ui/gallery-replay-mirari-%s.png"
                ),
            ReplayBundle(
                "kael_sex",
                lambda: persistent.kael_replay,
                lambda: { "kael_name": "Kael",
                          "claire_name": persistent.kael_claire_name,
                          "kael_scenes": persistent.kael_scenes,
                          "sex_stop_statement": persistent.kael_sex_stop },
                thumb="assets/ui/gallery-replay-kael-%s.png"
                ),
            ReplayBundle(
                "orias_sex",
                lambda: persistent.orias_replay,
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

    gallery.add_unlockable_sprite(mirari_lying_sprite, "mirari_lying")
    gallery.add_unlockable_sprite(mirari_cuddle_sprite, "mirari_cuddle")

    gallery.add_unlockable_sprite(kael_warmup_sprite, "kael_warmup")
    gallery.add_unlockable_sprite(kael_missionary_sprite, "kael_missionary")
    gallery.add_unlockable_sprite(kael_cuddles_sprite, "kael_cuddles")

    gallery.add_unlockable_sprite(orias_bed_sprite, "orias_bed")
    gallery.add_unlockable_sprite(orias_cuddles_sprite, "orias_cuddles")


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
