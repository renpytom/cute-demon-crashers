# Resources used by the whole game
init -1:
    # -- Transitions to use with set_state() ---------------------------
    python:
        with_dissolve = Dissolve(0.5, alpha=True)


        # -- Music ---------------------------------------------------------
        music_claire = "assets/music/Orangebeat - Claire Suite.mp3"
        music_akki = "assets/music/Orangebeat - Akki.mp3"
        music_mirari = "assets/music/Orangebeat - Mirari.mp3"
        music_kael = "assets/music/Orangebeat - Kael.mp3"
        music_orias = "assets/music/Orangebeat - Orias.mp3"
        music_daily = "assets/music/Orangebeat - Daily Life Suite.mp3"
        music_lullaby = "assets/music/Orangebeat - Daily Life Suite_Loop_2_lullaby.mp3"
        music_romance = "assets/music/Orangebeat - Daily Life Suite_Loop_3_romancing.mp3"
        music_tension = "assets/music/Orangebeat - Romantic Tension.mp3"
        music_love = "assets/music/Orangebeat - Love.mp3"
        music_silly = "assets/music/Orangebeat - Silliness.mp3"

    # -- Simple transforms ---------------------------------------------
    transform resize_sprite:
        zoom 0.6

    transform speak:
        linear .2 yanchor .9
        linear .2 zoom 1.15

    transform endspeak:
        parallel:
            linear .2 zoom 1
            linear .2 yanchor .99
        parallel:
            yoffset 100

    transform center_alone:
        zoom 1.3
        xanchor 0.5
        yalign 1.0
        xpos .5 yoffset 300

    transform center_alone2:
        zoom 1.3
        xanchor 0.5
        yalign 1.0
        xpos .5 yoffset 350

        
    transform left:
        xanchor 0.5
        yalign 1.0
        xpos .2 yoffset 100

    transform right:
        xanchor 0.5
        yalign 1.0
        xpos .75 yoffset 100

    transform center:
        xanchor 0.5
        yalign 1.0
        xpos .5 yoffset 100

    transform center_group:
        zoom 1
        xanchor 0.5
        yalign 1.0
        xpos .5 yoffset 100

    transform mright_alone2:
        xanchor 0.5
        yalign 1.0
        xpos .6 yoffset 350

    transform logo_center:
        anchor (0.5, 0.5)
        xpos .5
        ypos .5


    # When there are 4 characters on screen at once
    transform left4:
        zoom 1
        xanchor 0.5
        yalign 1.0
        xpos .18 yoffset 100

    transform mleft4:
        zoom 1
        xanchor 0.5
        yalign 1.0
        xpos .37 yoffset 100

    transform mright4:
        zoom 1
        xanchor 0.5
        yalign 1.0
        xpos .6 yoffset 100

    transform right4:
        zoom 1
        xanchor 0.5
        yalign 1.0
        xpos .8 yoffset 100

    # Chibi CGs position
    transform chibi_scene:
        xanchor .5
        xpos .5
        ypos .07

    # -- Animation transforms ------------------------------------------
    # Heartbeat for the CTC
    transform heartbeat:
        easeout 0.5 zoom 0.6 
        easein 0.2 zoom 1.0
        repeat

    # Move from side to side once
    transform sway:
        linear 0.3 xoffset 20
        linear 0.3 xoffset -20
        linear 0.3 xoffset 0

    # Shaking character
    transform shaking:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        repeat

    # Moves fastly to the right and then returns to original position        
    transform bounce_right: 
        easeout 0.1 xoffset 50
        easein 0.3 xoffset 0
    
    # Moves fastly to the left and then returns to original position
    transform bounce_left:
        easeout 0.1 xoffset -50
        easein 0.3 xoffset 0

    # Little excited jump!        
    transform bounce_up: 
        easeout 0.2 yoffset 70
        easein 0.2 yoffset 100

    transform bounce_up_alone: 
        easeout 0.2 yoffset 270
        easein 0.2 yoffset 300

    transform bounce_up_alone2: 
        easeout 0.2 yoffset 310
        easein 0.2 yoffset 350

    # Taken aback! :P        
    transform bounce_down: 
        easeout 0.2 yoffset 120
        easein 0.4 yoffset 100

    transform bounce_down_alone2: 
        easeout 0.2 yoffset 380
        easein 0.4 yoffset 350

    #Pan for the group sex scene
    transform panpan:
        subpixel True
        parallel:
            yalign 1.0
            linear 8.0 yalign 0.05
        parallel:
            xalign 0.0
            linear 8.0 xalign 0.7




    # -- Images --------------------------------------------------------
    python:
        # -- Claire ----------------------------------------------------
        claire_base = StateMachineDisplayable(
            "claire_base", "default",
            {
                "default": "assets/sprites/claire/cl_base_clothed.png",
                "lazy": "assets/sprites/claire/cl_base_lazy.png",
                "chemise": "assets/sprites/claire/cl_base_chemise.png",
                "bra": "assets/sprites/claire/cl_base_bra.png",
                "naked": naked("assets/sprites/claire/cl_base_naked{0}.png") 
            }
        )

        claire_emotion_base = StateMachineDisplayable(
            "claire_emotion_base", "default",
            {
                "default": Null(),
                "large blush": "assets/sprites/claire/cl_emob_blushL.png",
                "small blush": "assets/sprites/claire/cl_emob_blushS.png",
                "dark": "assets/sprites/claire/cl_emob_dark.png",
                "no nose": "assets/sprites/claire/cl_emob_nonose.png"
            }
        )

        claire_emotion = StateMachineDisplayable(
            "claire_emotion", "default",
            {
                "default": Null(),
                "flowers": "assets/sprites/claire/cl_emo_flowers.png",
                "heart": "assets/sprites/claire/cl_emo_heart.png",
                "lll": "assets/sprites/claire/cl_emo_lll.png",
                "note": "assets/sprites/claire/cl_emo_note.png",
                "panic": "assets/sprites/claire/cl_emo_panic.png",
                "shiver": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_emo_shiver.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shiver2.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shiver.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shiver3.png", 0.1, None
                ),
                "shock": "assets/sprites/claire/cl_emo_shock4.png",
                "sigh": "assets/sprites/claire/cl_emo_sigh.png",
                "steam": "assets/sprites/claire/cl_emo_steam.png",
                "sweat": "assets/sprites/claire/cl_emo_sweat.png",
                "sweat lots": "assets/sprites/claire/cl_emo_swtlots.png"
            }
        )

        claire_eyebrows = StateMachineDisplayable(
            "claire_eyebrows", "default",
            {
                "default": "assets/sprites/claire/cl_eyb_normal.png",
                "deep frown": "assets/sprites/claire/cl_eyb_deepfrown.png",
                "flat": "assets/sprites/claire/cl_eyb_flat.png",
                "frown": "assets/sprites/claire/cl_eyb_frown.png",
                "inwards": "assets/sprites/claire/cl_eyb_inwards.png",
                "up": "assets/sprites/claire/cl_eyb_up.png"
            }
        )

        claire_eyes = StateMachineDisplayable(
            "claire_eyes", "default",
            {
                "big": "assets/sprites/claire/cl_eyes_big.png",
                "bug cry": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_bugcry.png", 0.2, None,
                    "assets/sprites/claire/cl_eyes_bugcry2.png", 0.2, None,
                    ),
                "clench": "assets/sprites/claire/cl_eyes_clench.png",
                "clench tear": "assets/sprites/claire/cl_eyes_clenchtear.png",
                "closed": "assets/sprites/claire/cl_eyes_closed.png",
                "cry": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_cry.png", 0.2, None,
                    "assets/sprites/claire/cl_eyes_cry2.png", 0.2, None,
                    ),
                "dizzy": "assets/sprites/claire/cl_eyes_dizzy.png",
                "dots": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_dots.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_dots_blink.png", 0.3, None,
                    "assets/sprites/claire/cl_eyes_dots.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_dots_blink.png", 0.3, None,
                    "assets/sprites/claire/cl_eyes_dots.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_dots_blink.png", 0.3, None,
                    ),
                "down": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_down.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_down_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_down.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_down_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_down.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_down_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
                "flat": "assets/sprites/claire/cl_eyes_flat.png",
                "fun front": "assets/sprites/claire/cl_eyes_funfront.png",
                "fun side": "assets/sprites/claire/cl_eyes_funside.png",
                "happy": "assets/sprites/claire/cl_eyes_happy.png",
                "mortified": "assets/sprites/claire/cl_eyes_mortified.png",
                "default": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_open.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_open.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_open.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
                "semi open": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_semi.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_semi_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_semi.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_semi_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_semi.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_semi_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
                "shock": "assets/sprites/claire/cl_eyes_shock.png",
                "starry": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_starry1.png", 0.2, None,
                    "assets/sprites/claire/cl_eyes_starry2.png", 0.2, None,
                    ),
                "tender": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_tender.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_tender.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_tender.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_open_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
                "tender side": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_tenderside.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_tenderside_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_tenderside.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_tenderside_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_tenderside.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_tenderside_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
                "wide": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_wide.png", 1.2, None,
                    "assets/sprites/claire/cl_eyes_wide_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_wide.png", 3.0, None,
                    "assets/sprites/claire/cl_eyes_wide_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_wide.png", 2.0, None,
                    "assets/sprites/claire/cl_eyes_wide_blink.png", 0.1, None,
                    "assets/sprites/claire/cl_eyes_closed.png", 0.1, None,
                    ),
            }
        )

        claire_mouth = StateMachineDisplayable(
            "claire_mouth", "default",
            {
                "default": "assets/sprites/claire/cl_mouth_neutral.png",
                "ehh": "assets/sprites/claire/cl_mouth_ehh.png",
                "fun ah": "assets/sprites/claire/cl_mouth_fun_ah.png",
                "fun ah2": "assets/sprites/claire/cl_mouth_fun_ah2.png",
                "grin": "assets/sprites/claire/cl_mouth_grin.png",
                "happy": "assets/sprites/claire/cl_mouth_happy.png",
                "kissy": "assets/sprites/claire/cl_mouth_kissy.png",
                "kitty": "assets/sprites/claire/cl_mouth_kitty.png",
                "lip bite": "assets/sprites/claire/cl_mouth_lipbite.png",
                "low": "assets/sprites/claire/cl_mouth_low.png",
                "oh": "assets/sprites/claire/cl_mouth_oh.png",
                "pout": "assets/sprites/claire/cl_mouth_pout.png",
                "smile": "assets/sprites/claire/cl_mouth_smile.png",
                "uh": "assets/sprites/claire/cl_mouth_uh.png",
                "uhh": "assets/sprites/claire/cl_mouth_uhh.png",
                "v": "assets/sprites/claire/cl_mouth_v.png",
                "vhappy": "assets/sprites/claire/cl_mouth_vhappy.png",
                "wah": "assets/sprites/claire/cl_mouth_wah.png",
                "wavy": "assets/sprites/claire/cl_mouth_wavy.png"
            }
        )

        claire = ComposedSprite(
            (360, 504),
            ("base", (0, 0), claire_base),
            ("emotion_base", (0, 0), claire_emotion_base),
            ("eyes", (0, 0), claire_eyes),
            ("eyebrows", (0, 0), claire_eyebrows),
            ("mouth", (0, 0), claire_mouth),
            ("emotion", (0, 0), claire_emotion)
        )


        # -- Akki ------------------------------------------------------
        ak_sprite = lambda x: sprite("akki", "ak_", x)

        akki_base = StateMachineDisplayable(
            "akki_base", "default",
            {
                "default" : ak_sprite("base_clothed"),
                "human"   : ak_sprite("base_human"),
                "naked"   : naked(ak_sprite("base_naked{0}"))
            }
        )

        akki_emotion_base = StateMachineDisplayable(
            "akki_emotion_base", "default",
            {
                "default": Null(),
                "large blush": ak_sprite("emob_blushL"),
                "small blush": ak_sprite("emob_blushS"),
                "dark": ak_sprite("emob_dark"),
                "no nose": ak_sprite("emob_nonose")
            }
        )

        akki_emotion = StateMachineDisplayable(
            "akki_emotion", "default",
            {
                "default"    : Null(),
                "bars"       : ak_sprite("emo_bars"),
                "flowers"    : ak_sprite("emo_flowers"),
                "heart"      : ak_sprite("emo_heart"),
                "lll"        : ak_sprite("emo_lll"),
                "note"       : ak_sprite("emo_note"),
                "panic"      : ak_sprite("emo_panic"),
                "shiver"     : ak_sprite("emo_shiver"),
                "shock"      : ak_sprite("emo_shock"),
                "sigh"       : ak_sprite("emo_sigh"),
                "starry"     : ak_sprite("emo_starry"),
                "steam"      : ak_sprite("emo_steam"),
                "sweat"      : ak_sprite("emo_sweat"),
                "sweat lots" : ak_sprite("emo_swtlots"),
                "vein"       : ak_sprite("emo_vein")
            }
        )

        akki_eyebrows = StateMachineDisplayable(
            "akki_eyebrows", "default",
            {
                "frown"   : ak_sprite("eyb_frown"),
                "inwards" : ak_sprite("eyb_inwards"),
                "default" : ak_sprite("eyb_normal"),
                "one up"  : ak_sprite("eyb_oneup"),
                "tender"  : ak_sprite("eyb_tender"),
                "up"      : ak_sprite("eyb_up")
            }
        )

        akki_eyes = StateMachineDisplayable(
            "akki_eyes", "default",
            {
                "big"       : ak_sprite("eyes_big"),
                "bugteary"  : anim.TransitionAnimation(
                    ak_sprite("eyes_bugteary"), 0.2, None,
                    ak_sprite("eyes_bugteary2"), 0.2, None,
                    ),
                "clench"    : ak_sprite("eyes_clench"),
                "closed"    : ak_sprite("eyes_closed"),
                "cry"       : anim.TransitionAnimation(
                    ak_sprite("eyes_cry"), 0.2, None,
                    ak_sprite("eyes_cry2"), 0.2, None,
                    ),
                "dizzy"     : ak_sprite("eyes_dizzy"),
                "dots"      : anim.TransitionAnimation(
                    ak_sprite("eyes_dots"), 1.5, None,
                    ak_sprite("eyes_dots_blink"), 0.3, None,
                    ak_sprite("eyes_dots"), 2.6, None,
                    ak_sprite("eyes_dots_blink"), 0.3, None,
                    ak_sprite("eyes_dots"), 3.0, None,
                    ak_sprite("eyes_dots_blink"), 0.3, None,
                    
                    ),
                "flat"      : ak_sprite("eyes_flat"),
                "fun front" : ak_sprite("eyes_funfront"),
                "fun side"  : ak_sprite("eyes_funside"),
                "happy"     : ak_sprite("eyes_happy"),
                "mortified" : ak_sprite("eyes_mortified"),
                "default"   : anim.TransitionAnimation(
                    ak_sprite("eyes_open"), 1.5, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_open"), 2.6, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_open"), 3.0, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ),
                "shock"     : ak_sprite("eyes_shock"),
                "starry": anim.TransitionAnimation(
                    ak_sprite("eyes_starry1"), 0.2, None,
                    ak_sprite("eyes_starry2"), 0.2, None
                ),
                "tender"      : anim.TransitionAnimation(
                    ak_sprite("eyes_tender"), 1.5, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_tender"), 2.6, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_tender"), 3.0, None,
                    ak_sprite("eyes_open_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ),
                "tender side" : anim.TransitionAnimation(
                    ak_sprite("eyes_tenderside"), 1.5, None,
                    ak_sprite("eyes_tenderside_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_tenderside"), 2.6, None,
                    ak_sprite("eyes_tenderside_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_tenderside"), 3.0, None,
                    ak_sprite("eyes_tenderside_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ),
                "twitch"      : anim.TransitionAnimation(
                    ak_sprite("eyes_twitch"), 0.2, None,
                    ak_sprite("eyes_twitch2"), 0.2, None
                ),
                "wide"        : anim.TransitionAnimation(
                    ak_sprite("eyes_wide"), 1.5, None,
                    ak_sprite("eyes_wide_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_wide"), 2.6, None,
                    ak_sprite("eyes_wide_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ak_sprite("eyes_wide"), 3.0, None,
                    ak_sprite("eyes_wide_blink"), 0.1, None,
                    ak_sprite("eyes_closed"), 0.1, None,
                    ),
                "wink"        : ak_sprite("eyes_wink")
            }
        )

        akki_mouth = StateMachineDisplayable(
            "akki_mouth", "default",
            {
                "default": ak_sprite("mouth_smile"),
                "ah": ak_sprite("mouth_ah"),
                "drool": ak_sprite("mouth_drool"),
                "ehh": ak_sprite("mouth_ehh"),
                "fun ah": ak_sprite("mouth_fun_ah2"),
                "fun grin": ak_sprite("mouth_fun_grin"),
                "grin": ak_sprite("mouth_grin"),
                "happy": ak_sprite("mouth_happy"),
                "kissy": ak_sprite("mouth_kissy"),
                "low": ak_sprite("mouth_low"),
                "neutral": ak_sprite("mouth_neutral"),
                "oh": ak_sprite("mouth_oh"),
                "smile": ak_sprite("mouth_smile"),
                "tiny": ak_sprite("mouth_tiny"),
                "uh": ak_sprite("mouth_uh"),
                "uhh": ak_sprite("mouth_uhh"),
                "vhappy": ak_sprite("mouth_vhappy"),
                "wah": ak_sprite("mouth_wah"),
                "wavy": ak_sprite("mouth_wavy")
            }
        )

        akki = ComposedSprite(
            (817, 1501),
            ("base", (0, 0), akki_base),
            ("emotion_base", (0, 0), akki_emotion_base),
            ("eyes", (0, 0), akki_eyes),
            ("eyebrows", (0, 0), akki_eyebrows),
            ("mouth", (0, 0), akki_mouth),
            ("emotion", (0, 0), akki_emotion)
        )
        akki.set_state(base="default")


        # -- Mirari ----------------------------------------------------
        mi_sprite = lambda x: sprite("mirari", "mi_", x)

        mirari_base = StateMachineDisplayable(
            "mirari_base", "default",
            {
                "default": mi_sprite("base_clothed"),
                "human": mi_sprite("base_human"),
                "baby doll": mi_sprite("base_bbdoll"),
                "panties": naked(mi_sprite("base_panties{0}")),
                "naked": naked(mi_sprite("base_naked{0}"))
            }
        )

        mirari_emotion = StateMachineDisplayable(
            "mirari_emotion", "default",
            {
                "default": Null(),
                "bars": mi_sprite("emo_bars"),
                
                "flowers": mi_sprite("emo_flowers"),
                "heart": mi_sprite("emo_heart"),
                "lll": mi_sprite("emo_lll"),
                "note": mi_sprite("emo_note"),
                "panic": mi_sprite("emo_panic"),
                "shiver": mi_sprite("emo_shiver"),
                "shock": mi_sprite("emo_shock"),
                "sigh": mi_sprite("emo_sigh"),
                "starry": mi_sprite("emo_starry"),
                "sweat": mi_sprite("emo_sweat"),
                "sweat lots": mi_sprite("emo_swlots"),
                "vein": mi_sprite("emo_vein"),
            }
        )

        mirari_emotion_base = StateMachineDisplayable(
            "mirari_emotion_base", "default",
            {
                "default": Null(),
                "small blush": mi_sprite("emob_blushS"),
                "dark": mi_sprite("emob_dark"),
                "no nose": mi_sprite("emob_nonose")
            }
        )

        mirari_eyebrows = StateMachineDisplayable(
            "mirari_eyebrows", "default",
            {
                "default": mi_sprite("eyb_normal"),
                "frown": mi_sprite("eyb_frown"),
                "inwards": mi_sprite("eyb_inwards"),
                "up": mi_sprite("eyb_up")
            }
        )

        mirari_eyes = StateMachineDisplayable(
            "mirari_eyes", "default",
            {
                "default": anim.TransitionAnimation(
                    mi_sprite("eyes_open"), 1.7, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_open"), 2.4, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_open"), 2.8, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    ),
                "angry": mi_sprite("eyes_angry"),
                "big": mi_sprite("eyes_big"),
                "bugteary": anim.TransitionAnimation(
                    mi_sprite("eyes_bugteary"), 0.2, None,
                    mi_sprite("eyes_bugteary2"), 0.2, None
                ),
                "clench": mi_sprite("eyes_clench"),
                "closed": mi_sprite("eyes_closed"),
                "cry": anim.TransitionAnimation(
                    mi_sprite("eyes_cry"), 0.2, None,
                    mi_sprite("eyes_cry2"), 0.2, None
                ),
                "dizzy": mi_sprite("eyes_dizzy"),
                "dots":  anim.TransitionAnimation(
                    mi_sprite("eyes_dots"), 1.7, None,
                    mi_sprite("eyes_dots_blink"), 0.3, None,
                    mi_sprite("eyes_dots"), 2.4, None,
                    mi_sprite("eyes_dots_blink"), 0.3, None,
                    mi_sprite("eyes_dots"), 2.8, None,
                    mi_sprite("eyes_dots_blink"), 0.3, None,
                    ),
                "flat": mi_sprite("eyes_flat"),
                "fun front": mi_sprite("eyes_funfront"),
                "fun side": mi_sprite("eyes_funside"),
                "happy": mi_sprite("eyes_happy"),
                "mortified": mi_sprite("eyes_mortified"),
                "shock": mi_sprite("eyes_shock"),
                "starry": anim.TransitionAnimation(
                    mi_sprite("eyes_starry1"), 0.2, None,
                    mi_sprite("eyes_starry2"), 0.2, None
                ),
                "tender": anim.TransitionAnimation(
                    mi_sprite("eyes_tender"), 1.7, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_tender"), 2.4, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_tender"), 2.8, None,
                    mi_sprite("eyes_open_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    ),
                "wide":   anim.TransitionAnimation(
                    mi_sprite("eyes_wide"), 1.7, None,
                    mi_sprite("eyes_wide_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_wide"), 2.4, None,
                    mi_sprite("eyes_wide_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    mi_sprite("eyes_wide"), 2.8, None,
                    mi_sprite("eyes_wide_blink"), 0.1, None,
                    mi_sprite("eyes_closed"), 0.1, None,
                    ),
                "wink": mi_sprite("eyes_wink")
            }
        )

        mirari_mouth = StateMachineDisplayable(
            "mirari_mouth", "default",
            {
                "default": mi_sprite("mouth_smile"),
                "ehh": mi_sprite("mouth_ehh"),
                "fun ah": mi_sprite("mouth_funah"),
                "fun smile": mi_sprite("mouth_funsmile"),
                "grin": mi_sprite("mouth_grin"),
                "happy": mi_sprite("mouth_happy"),
                "kissy": mi_sprite("mouth_kissy"),
                "kitty": mi_sprite("mouth_kitty"),
                "low": mi_sprite("mouth_low"),
                "neutral": mi_sprite("mouth_neutral"),
                "oh": mi_sprite("mouth_oh"),
                "pout": mi_sprite("mouth_pout"),
                "smile": mi_sprite("mouth_smile"),
                "tongue": mi_sprite("mouth_tongue"),
                "uh": mi_sprite("mouth_uh"),
                "happy": mi_sprite("mouth_happy"),
                "vhappy": mi_sprite("mouth_vhappy"),
                "wah": mi_sprite("mouth_wah"),
                "v": mi_sprite("mouth_v"),
                "wavy": mi_sprite("mouth_wavy")
            }
        )

        mirari = ComposedSprite(
            (910, 1280),
            ("base", (0, 0), mirari_base),
            ("emotion_base", (0, 0), mirari_emotion_base),
            ("eyes", (0, 0), mirari_eyes),
            ("eyebrows", (0, 0), mirari_eyebrows),
            ("mouth", (0, 0), mirari_mouth),
            ("emotion", (0, 0), mirari_emotion)
        )
        mirari.set_state(base="default")


        # -- Kael ------------------------------------------------------
        ka_sprite = lambda x: sprite("kael", "ka_", x)

        kael_base = StateMachineDisplayable(
            "kael_base", "default",
            {
                "default": ka_sprite("base_clothed"),
                "apron": ka_sprite("base_apron"),
                "human": ka_sprite("base_human"),
                "naked": naked(ka_sprite("base_naked{0}"))
            }
        )

        kael_emotion_base = StateMachineDisplayable(
            "kael_emotion_base", "default",
            {
                "default": Null(),
                "small blush": ka_sprite("emob_blushS"),
                "dark": ka_sprite("emob_dark"),
                "no nose": ka_sprite("emob_nonose")
            }
        )

        kael_emotion = StateMachineDisplayable(
            "kael_emotion", "default",
            {
                "default"    : Null(),
                "bars"       : ka_sprite("emo_bars"),
                "flowers"    : ka_sprite("emo_flowers"),
                "heart"      : ka_sprite("emo_heart"),
                "lll"        : ka_sprite("emo_lll"),
                "note"       : ka_sprite("emo_note"),
                "panic"      : ka_sprite("emo_panic"),
                "shiver"     : ka_sprite("emo_shiver"),
                "shock"      : ka_sprite("emo_shock"),
                "sigh"       : ka_sprite("emo_sigh"),
                "starry"     : ka_sprite("emo_starry"),
                "sweat"      : ka_sprite("emo_sweat"),
                "sweat lots" : ka_sprite("emo_swtlots"),
                "vein"       : ka_sprite("emo_vein")
            }
        )

        kael_eyebrows = StateMachineDisplayable(
            "kael_eyebrows", "default",
            {
                "frown"   : ka_sprite("eyb_frown"),
                "inwards" : ka_sprite("eyb_inwards"),
                "default" : ka_sprite("eyb_normal"),
                "one up"  : ka_sprite("eyb_oneup"),
                "up"      : ka_sprite("eyb_up")
            }
        )

        kael_eyes = StateMachineDisplayable(
            "kael_eyes", "default",
            {
                "bigcry": ka_sprite("eyes_bigcry"),
                "big"       : ka_sprite("eyes_big"),
                "clench"    : ka_sprite("eyes_clench"),
                "closed"    : ka_sprite("eyes_closed"),
                "cry"       : anim.TransitionAnimation(
                    ka_sprite("eyes_cry"), 0.2, None,
                    ka_sprite("eyes_cry2"), 0.2, None
                    ),
                "dizzy"     : ka_sprite("eyes_dizzy"),
                "dots"      : anim.TransitionAnimation(
                    ka_sprite("eyes_dots"), 2.3, None,
                    ka_sprite("eyes_dots_blink"), 0.3, None,
                    ka_sprite("eyes_dots"), 2.0, None,
                    ka_sprite("eyes_dots_blink"), 0.3, None,
                    ka_sprite("eyes_dots"), 2.5, None,
                    ka_sprite("eyes_dots_blink"), 0.3, None,    
                    ),
                "flat"      : ka_sprite("eyes_flat"),
                "fun front" : ka_sprite("eyes_funfront"),
                "fun side"  : ka_sprite("eyes_funside"),
                "happy"     : ka_sprite("eyes_happy"),
                "default"   : anim.TransitionAnimation(
                    ka_sprite("eyes_open"), 2.3, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_open"), 2.0, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_open"), 2.5, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ),
                "shock"     : ka_sprite("eyes_shock"),
                "sparkly": anim.TransitionAnimation(
                    ka_sprite("eyes_sparkly"), 0.2, None,
                    ka_sprite("eyes_sparkly2"), 0.2, None
                    ),
                "tender"      : anim.TransitionAnimation(
                    ka_sprite("eyes_tender"), 2.3, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_tender"), 2.0, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_tender"), 2.5, None,
                    ka_sprite("eyes_open_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ),
                "tender side" : anim.TransitionAnimation(
                    ka_sprite("eyes_tenderside"), 2.3, None,
                    ka_sprite("eyes_tenderside_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_tenderside"), 2.0, None,
                    ka_sprite("eyes_tenderside_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_tenderside"), 2.5, None,
                    ka_sprite("eyes_tenderside_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ),
                "up": anim.TransitionAnimation(
                    ka_sprite("eyes_up"), 2.3, None,
                    ka_sprite("eyes_up_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_up"), 2.0, None,
                    ka_sprite("eyes_up_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_up"), 2.5, None,
                    ka_sprite("eyes_up_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ),
                "wide"        : anim.TransitionAnimation(
                    ka_sprite("eyes_wide"), 2.3, None,
                    ka_sprite("eyes_wide_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_wide"), 2.0, None,
                    ka_sprite("eyes_wide_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ka_sprite("eyes_wide"), 2.5, None,
                    ka_sprite("eyes_wide_blink"), 0.1, None,
                    ka_sprite("eyes_closed"), 0.1, None,
                    ),
                "wink"        : ka_sprite("eyes_wink")
            }
        )

        kael_mouth = StateMachineDisplayable(
            "kael_mouth", "default",
            {
                "default": ka_sprite("mouth_smile"),
                "ah": ka_sprite("mouth_ah"),
                "ehh": ka_sprite("mouth_ehh"),
                "fun smile": ka_sprite("mouth_funsmile"),
                "grin": ka_sprite("mouth_grin"),
                "happy": ka_sprite("mouth_happy"),
                "low": ka_sprite("mouth_low"),
                "neutral": ka_sprite("mouth_neutral"),
                "smile": ka_sprite("mouth_smile"),
                "vhappy": ka_sprite("mouth_vhappy"),
                "wah": ka_sprite("mouth_wah"),
                "wavy": ka_sprite("mouth_wavy")
            }
        )

        kael_glasses = StateMachineDisplayable(
            "kael_glasses", "default",
            {
                "on"   : ka_sprite("glasses"),
                "default" : Null(),
            }
        )

        kael = ComposedSprite(
            (817, 1501),
            ("base", (0, 0), kael_base),
            ("emotion_base", (0, 0), kael_emotion_base),
            ("eyes", (0, 0), kael_eyes),
            ("eyebrows", (0, 0), kael_eyebrows),
            ("mouth", (0, 0), kael_mouth),
            ("emotion", (0, 0), kael_emotion),
            ("glasses", (0, 0), kael_glasses)
        )
        kael.set_state(base="default")

        
        # -- Orias ------------------------------------------------------
        ori_sprite = lambda x: sprite("orias", "ori_", x)

        orias_base = StateMachineDisplayable(
            "orias_base", "default",
            {
                "default": ori_sprite("base_clothed"),
                "jacketless": ori_sprite("base_jacketless"),
                "tea": ori_sprite("base_tea"),
                "human" : ori_sprite("base_human"),
                "naked": naked(ori_sprite("base_naked{0}"))
            }
        )

        orias_emotion_base = StateMachineDisplayable(
            "orias_emotion_base", "default",
            {
                "default": Null(),
                "small blush": ori_sprite("emob_blushS"),
                "dark": ori_sprite("emob_dark"),
                "no nose": ori_sprite("emob_nonose")
            }
        )

        orias_emotion = StateMachineDisplayable(
            "orias_emotion", "default",
            {
                "default"    : Null(),
                "bars"       : ori_sprite("emo_bars"),
                "flowers"    : ori_sprite("emo_flowers"),
                "heart"      : ori_sprite("emo_heart"),
                "lll"        : ori_sprite("emo_lll"),
                "note"       : ori_sprite("emo_note"),
                "panic"      : ori_sprite("emo_panic"),
                "shiver"     : ori_sprite("emo_shiver"),
                "shock"      : ori_sprite("emo_shock"),
                "sigh"       : ori_sprite("emo_sigh"),
                "starry"     : ori_sprite("emo_starry"),
                "sweat"      : ori_sprite("emo_sweat"),
                "sweat lots" : ori_sprite("emo_swtlots"),
                "vein"       : ori_sprite("emo_vein")
            }
        )

        orias_eyebrows = StateMachineDisplayable(
            "orias_eyebrows", "default",
            {
                "frown"   : ori_sprite("eyb_frown"),
                "inwards" : ori_sprite("eyb_inwards"),
                "default" : ori_sprite("eyb_neutral"),
                "tender": ori_sprite("eyb_tender"),
                "up"      : ori_sprite("eyb_up")
            }
        )

        orias_eyes = StateMachineDisplayable(
            "orias_eyes", "default",
            {
                "default": anim.TransitionAnimation(
                    ori_sprite("eyes_open"), 1.8, None,
                    ori_sprite("eyes_open_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_open"), 2.5, None,
                    ori_sprite("eyes_open_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_open"), 1.7, None,
                    ori_sprite("eyes_open_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ),
                "closed"    : ori_sprite("eyes_closed"),
                "dizzy"     : ori_sprite("eyes_dizzy"),
                "dots"      : anim.TransitionAnimation(
                    ori_sprite("eyes_dots"), 1.8, None,
                    ori_sprite("eyes_dots_blink"), 0.3, None,
                    ori_sprite("eyes_dots"), 2.5, None,
                    ori_sprite("eyes_dots_blink"), 0.3, None,
                    ori_sprite("eyes_dots"), 1.7, None,
                    ori_sprite("eyes_dots_blink"), 0.3, None,    
                    ),
                "flat"      : ori_sprite("eyes_flat"),
                "fun front" : ori_sprite("eyes_funfront"),
                "fun side"  : ori_sprite("eyes_funside"),
                "happy"     : ori_sprite("eyes_happy"),
                "shock"     : ori_sprite("eyes_shock"),
                "side": anim.TransitionAnimation(
                    ori_sprite("eyes_side"), 1.8, None,
                    ori_sprite("eyes_side_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_side"), 2.5, None,
                    ori_sprite("eyes_side_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_side"), 1.7, None,
                    ori_sprite("eyes_side_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ),
                "squint": ori_sprite("eyes_squint"),
                "wide": anim.TransitionAnimation(
                    ori_sprite("eyes_wide"), 1.8, None,
                    ori_sprite("eyes_wide_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_wide"), 2.5, None,
                    ori_sprite("eyes_wide_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ori_sprite("eyes_wide"), 1.7, None,
                    ori_sprite("eyes_wide_blink"), 0.1, None,
                    ori_sprite("eyes_closed"), 0.1, None,
                    ),
                "wink"        : ori_sprite("eyes_wink")                
            }
        )

        orias_mouth = StateMachineDisplayable(
            "orias_mouth", "default",
            {
                "default": ori_sprite("mouth_neutral"),
                "ah": ori_sprite("mouth_ah"),
                "ehh": ori_sprite("mouth_ehh"),
                "fun smile": ori_sprite("mouth_funsmile"),
                "grin": ori_sprite("mouth_grin"),
                "happy": ori_sprite("mouth_happy"),
                "low": ori_sprite("mouth_low"),
                "neutral": ori_sprite("mouth_neutral"),
                "oh": ori_sprite("mouth_oh"),
                "smile": ori_sprite("mouth_smile"),
                "uhh": ori_sprite("mouth_uhh"),
                "wavy": ori_sprite("mouth_wavy")
            }
        )

        orias_glasses = StateMachineDisplayable(
            "orias_glasses", "default",
            {
                "on"   : ori_sprite("glasses"),
                "default" : Null(),
            }
        )

        orias = ComposedSprite(
            (817, 1501),
            ("base", (0, 0), orias_base),
            ("emotion_base", (0, 0), orias_emotion_base),
            ("eyes", (0, 0), orias_eyes),
            ("eyebrows", (0, 0), orias_eyebrows),
            ("mouth", (0, 0), orias_mouth),
            ("emotion", (0, 0), orias_emotion),
            ("glasses", (0, 0), orias_glasses)
        )
        orias.set_state(base="default")


    image akki = At(akki.displayable(), resize_sprite)
    image mirari = At(mirari.displayable(), resize_sprite)
    image kael = At(kael.displayable(), resize_sprite)
    image orias = At(orias.displayable(), resize_sprite)

    image warning = "assets/bgs/warning.png"
    image black = "#000000"
    image white = "#ffffff"
    image logo = "assets/ui/logo.png"
    image sugarlogo = "assets/ui/mm-group-logo.png"
    
    # -- Backgrounds ---------------------------------------------------
    image bg bedroom_candles = "assets/bgs/bedroom candles.png"
    image bg bedroom_day = "assets/bgs/bedroom day.png"
    image bg bedroom_night = "assets/bgs/bedroom night.png"
    image bg garden = "assets/bgs/garden.png"
    image bg hallway_day = "assets/bgs/hallway day.png"
    image bg hallway_night = "assets/bgs/hallway night.png"
    image bg kitchen = "assets/bgs/kitchen.png"
    image bg living_room = "assets/bgs/living.png"
    image bg street = "assets/bgs/street.png"


    # --- Chibis  and items --------------------------------------------
    image chibi_akki01 = "assets/chibis/akki_hug.png"
    image chibi_akki02 = "assets/chibis/akki_sit.png"
    
    image chibi_orias01 = "assets/chibis/orias_tea.png"
    image chibi_orias02 = "assets/chibis/orias_read.png"

    image chibi_mira01 = "assets/chibis/mirari_hair.png"
    image chibi_mira02 = "assets/chibis/mirari_flowers.png"

    image chibi_kael01 = "assets/chibis/kael_laundry.png"
    image chibi_kael02 = "assets/chibis/kael_cut.png"

    image item sock: 
        "assets/items/item_sock1.png"
        pause 0.2
        "assets/items/item_sock2.png"
        pause 0.2
        repeat

    image item parfait: 
        "assets/items/item_parfait.png"
        pause 0.2
        "assets/items/item_parfait2.png"
        pause 0.2
        repeat

    image item bacon: 
        "assets/items/item_bacon1.png"
        pause 0.2
        "assets/items/item_bacon2.png"
        pause 0.2
        repeat

    image item pizza: 
        "assets/items/item_pizza1.png"
        pause 0.2
        "assets/items/item_pizza2.png"
        pause 0.2
        repeat

    image item tea: 
        "assets/items/item_tea1.png"
        pause 0.2
        "assets/items/item_tea2.png"
        pause 0.2
        repeat

    image item toast: 
        "assets/items/item_toast1.png"
        pause 0.2
        "assets/items/item_toast2.png"
        pause 0.2
        repeat

    image item pancakes = "assets/items/item_pancakes.png"
       

    # -- CGs and cut-ins------------------------------------------------
    image portal = "assets/CGs/portal.png"

    ##-- The Mastermind game
    image mastermind = LiveComposite((438,460),
        (0, 0), "assets/CGs/mastermind.png",
        (0, 0), "assets/CGs/mm_cl_code.png",
        (0, 0), "assets/CGs/mm_mi_code_hidden.png",
            
        )
    image mmturn_1 = "assets/CGs/mm_1.png"
    image mmturn_2 = "assets/CGs/mm_2.png"
    image mmturn_3 = "assets/CGs/mm_3.png"
    image mmturn_4 = "assets/CGs/mm_4.png"
    image mmturn_5 = "assets/CGs/mm_5.png"
    image mmturn_6 = "assets/CGs/mm_6.png"
    image mmturn_7 = "assets/CGs/mm_7.png"
    image mmturn_8 = "assets/CGs/mm_8.png"
    image mmturn_9 = "assets/CGs/mm_9.png"
    image mmturn_10 = "assets/CGs/mm_10.png"
    image mmturn_11 = "assets/CGs/mm_11.png"
    image mmturn_12 = "assets/CGs/mm_12.png"
    image mmturn_13 = "assets/CGs/mm_13.png"
    image mmturn_14 = "assets/CGs/mm_14.png"
    image mmturn_15 = "assets/CGs/mm_15.png"

    image mmscore_2 = "assets/CGs/mm_2_score.png"
    image mmscore_4 = "assets/CGs/mm_4_score.png"
    image mmscore_6 = "assets/CGs/mm_6_score.png"
    image mmscore_8 = "assets/CGs/mm_8_score.png"
    image mmscore_9 = "assets/CGs/mm_9_score.png"
    image mmscore_10 = "assets/CGs/mm_10_score.png"
    image mmscore_11 = "assets/CGs/mm_11_score.png"
    image mmscore_12 = "assets/CGs/mm_12_score.png"
    image mmscore_13 = "assets/CGs/mm_13_score.png"
    image mmscore_14 = "assets/CGs/mm_14_score.png"
    image mmscore_15 = "assets/CGs/mm_15_score.png"

    
    image mastermind mid = LiveComposite((438,460),
        (0, 0), "mastermind",
        (0, 0), "mmturn_1",
        (0, 0), "mmturn_2",
        (0, 0), "mmturn_3",
        (0, 0), "mmturn_4",
        (0, 0), "mmturn_5",
        (0, 0), "mmturn_6",
        (0, 0), "mmturn_7",
        (0, 0), "mmscore_2",
        (0, 0), "mmscore_4",
        (0, 0), "mmscore_6",
        (0, 0), "mmscore_8",
        (0, 0), "mmscore_9",
        (0, 0), "mmturn_8",
        (0, 0), "mmturn_9",
        (0, 0), "mmturn_10",
        (0, 0), "mmscore_10",
        )
    image mastermind end = "assets/CGs/mm_end.png"

    ##-- No Sex Ending
    image nosex01 = "assets/chibis/NoOneEnd_01.png"
    image nosex02 = "assets/chibis/NoOneEnd_02.png"

    ##-- Akki
    image akki_kiss A = "assets/CGs/akki_kissA.jpg"
    image akki_kiss B = "assets/CGs/akki_kissB.jpg"

    python:
        akki_foreplay_bottom = StateMachineDisplayable(
            "akkifp_bottom", "on",
            {
                "on": "assets/CGs/akki01_akbottomon.png",
                "off": naked("assets/CGs/akki01_akbottomoff{0}.png")
            }
        )

        akki_foreplay_claire_arm = StateMachineDisplayable(
            "akkifp_clarm", "down",
            {
                "down": "assets/CGs/akki01_clarm_down.png",
                "chest": "assets/CGs/akki01_clarm_chest.png",
                "crotch": "assets/CGs/akki01_clarm_crotch.png",
                "handjob": naked("assets/CGs/akki01_clarm_handjob{0}.png")
            }
        )

        akki_foreplay_claire_bottom = StateMachineDisplayable(
            "akkifp_clbottom", "on",
            {
                "on": "assets/CGs/akki01_clbottomon.png", 
                "off": Null(width=1),                
            }
        )

        akki_foreplay_claire_top = StateMachineDisplayable(
            "akkifp_cltop", "on",
            {
                "on": "assets/CGs/akki01_cltop_shirt.png", 
                "bra": "assets/CGs/akki01_cltop_bra.png",
                "off": naked("assets/CGs/akki01_cltop_boobs{0}.png"),
            }
        )

        akki_foreplay_akki_arm = StateMachineDisplayable(
            "akkifp_akarm", "down",
            {
                "down": "assets/CGs/akki01_akarm_down.png", 
                "breast": "assets/CGs/akki01_akarm_breast.png",
                #"tummy": "assets/CGs/akki01_akarm_tummy.png",
                "finger": "assets/CGs/akki01_akarm_finger.png",
            }
        )

        akki_foreplay_ac_heads = StateMachineDisplayable(
            "akkifp_acheads", "kiss",
            {
                "apart": "assets/CGs/akki01_heads_apart.png", 
                "kiss": "assets/CGs/akki01_heads_kiss.png",
            }
        )

        akki_foreplay_claire_face = StateMachineDisplayable(
            "akkifp_clface", "none",
            {
                "none": Null(width=1), 
                "surprised": "assets/CGs/akki01_clface_surprised.png",
                "embarrassed": "assets/CGs/akki01_clface_embarrased.png", 
                "smile": "assets/CGs/akki01_clface_smile.png",
                "happy": "assets/CGs/akki01_clface_happy.png", 
                "pleasure": "assets/CGs/akki01_clface_pleasure.png",
                "O": "assets/CGs/akki01_clface_O.png",
            }
        )

        akki_foreplay_akki_face = StateMachineDisplayable(
            "akkifp_akface", "none",
            {
                "none": Null(width=1), 
                "happy": "assets/CGs/akki01_akface_happy.png", 
                "nervous": "assets/CGs/akki01_akface_nervous.png",
                "pleasure": "assets/CGs/akki01_akface_pleasure.png",
                "D:": "assets/CGs/akki01_akface_hesitant.png",
            }
        )

        akki_foreplay = ComposedSprite(
            (1280, 800),
            (None, (0, 0), "assets/CGs/akki01_bg.jpg"),
            (None, (0, 0), "assets/CGs/akki01_akkibase.png"),
            ("akki_bottom", (0, 0), akki_foreplay_bottom),
            ("claire_arm", (0, 0), akki_foreplay_claire_arm),
            (None, (0, 0), naked("assets/CGs/akki01_clbase{0}.png")),
            ("claire_bottom", (0, 0), akki_foreplay_claire_bottom),
            ("claire_top", (0, 0), akki_foreplay_claire_top),
            ("akki_arm", (0, 0), akki_foreplay_akki_arm),
            ("heads", (0, 0), akki_foreplay_ac_heads),
            ("claire_face", (0, 0), akki_foreplay_claire_face),
            ("akki_face", (0, 0), akki_foreplay_akki_face)
        )

    image akkiforeplay = akki_foreplay.displayable()

    
#    image akkiforeplay = LiveComposite((1280, 800),
#        (0, 0), "assets/CGs/akki01_bg.jpg",
#        (0, 0), "assets/CGs/akki01_akkibase.png",
#        (0, 0), ConditionSwitch(
#            "ak_bottom == 'on'", "assets/CGs/akki01_akbottomon.png", 
#            "ak_bottom == 'off'", naked("assets/CGs/akki01_akbottomoff{0}.png"), 
#            ),
#        (0, 0), ConditionSwitch(
#            "cl_arm == 'down'", "assets/CGs/akki01_clarm_down.png", 
#            "cl_arm == 'chest'", "assets/CGs/akki01_clarm_chest.png",
#            "cl_arm == 'crotch'", "assets/CGs/akki01_clarm_crotch.png",
#            "cl_arm == 'handjob'", naked("assets/CGs/akki01_clarm_handjob{0}.png"),
#            ),
#        (0, 0), naked("assets/CGs/akki01_clbase{0}.png"),
#        (0, 0), ConditionSwitch(
#            "cl_bottom == 'on'", "assets/CGs/akki01_clbottomon.png", 
#            "cl_bottom == 'off'", Null(width=1),
#            ),
#        (0, 0), ConditionSwitch(
#            "cl_top == 'on'", "assets/CGs/akki01_cltop_shirt.png", 
#            "cl_top == 'bra'", "assets/CGs/akki01_cltop_bra.png",
#            "cl_top == 'off'", naked("assets/CGs/akki01_cltop_boobs{0}.png"),
#            
#            ),
#        (0, 0), ConditionSwitch(
#            "ak_arm == 'down'", "assets/CGs/akki01_akarm_down.png", 
#            "ak_arm == 'breast'", "assets/CGs/akki01_akarm_breast.png",
#            #"ak_arm == 'tummy'", "assets/CGs/akki01_akarm_tummy.png",
#            "ak_arm == 'finger'", "assets/CGs/akki01_akarm_finger.png",
#            
#            ),
#        (0, 0), ConditionSwitch(
#            "ac_heads == 'apart'", "assets/CGs/akki01_heads_apart.png", 
#            "ac_heads == 'kiss'", "assets/CGs/akki01_heads_kiss.png",
#            
#            ),
#        (0, 0), ConditionSwitch(
#            "cl_face == None", Null(width=1), 
#            "cl_face == 'surprised'", "assets/CGs/akki01_clface_surprised.png",
#            "cl_face == 'embarrassed'", "assets/CGs/akki01_clface_embarrased.png", 
#            "cl_face == 'smile'", "assets/CGs/akki01_clface_smile.png",
#            "cl_face == 'happy'", "assets/CGs/akki01_clface_happy.png", 
#            "cl_face == 'pleasure'", "assets/CGs/akki01_clface_pleasure.png",
#            "cl_face == 'O'", "assets/CGs/akki01_clface_O.png",
#            
#            ),
#        (0, 0), ConditionSwitch(
#            "ak_face == None", Null(width=1), 
#            "ak_face == 'happy'", "assets/CGs/akki01_akface_happy.png", 
#            "ak_face == 'nervous'", "assets/CGs/akki01_akface_nervous.png",
#            "ak_face == 'pleasure'", "assets/CGs/akki01_akface_pleasure.png",
#            "ak_face == 'D:'", "assets/CGs/akki01_akface_hesitant.png",
#            
#            ),
#
#        )
    image akkiforeplay start = LiveComposite((1280, 800),
        (0, 0), "assets/CGs/akki01_bg.jpg",
        (0, 0), "assets/CGs/akki01_akkibase.png",
        (0, 0), "assets/CGs/akki01_akbottomon.png",
        (0, 0), "assets/CGs/akki01_clbase.png",
        (0, 0), "assets/CGs/akki01_clbottomon.png", 
        (0, 0), "assets/CGs/akki01_clarm_down.png", 
        (0, 0), "assets/CGs/akki01_cltop_shirt.png",
        (0, 0), "assets/CGs/akki01_akarm_down.png",
        (0, 0), "assets/CGs/akki01_heads_kiss.png",
        )

    python:
        akki_missionary_claire = StateMachineDisplayable(
            "akki_lay_cface", 1,
            {
                1: "assets/CGs/akki_lay_cface1.png", 
                2: "assets/CGs/akki_lay_cface2.png", 
                3: "assets/CGs/akki_lay_cface3.png"
            }
        )

        akki_missionary_akki = StateMachineDisplayable(
            "akki_lay_aface", 1,
            {
                1: "assets/CGs/akki_lay_aface1.png", 
                2: "assets/CGs/akki_lay_aface2.png", 
                3: "assets/CGs/akki_lay_aface3.png", 
                4: "assets/CGs/akki_lay_aface4.png", 
                5: "assets/CGs/akki_lay_aface5.png", 
                6: "assets/CGs/akki_lay_aface6.png"
            }
        )

        akki_missionary_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), naked("assets/CGs/akki_lay01{0}.jpg")),
            ("claire", (0, 0), akki_missionary_claire),
            ("akki", (0, 0), akki_missionary_akki)
        )
        

    image akki_missionary = akki_missionary_sprite.displayable()
        
#    image akki_missionary = LiveComposite((1280, 800),
#        (0, 0), naked("assets/CGs/akki_lay01{0}.jpg"),
#        (0, 0), ConditionSwitch(
#            "lay_cface == '1'", "assets/CGs/akki_lay_cface1.png", 
#            "lay_cface == '2'", "assets/CGs/akki_lay_cface2.png", 
#            "lay_cface == '3'", "assets/CGs/akki_lay_cface3.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "lay_aface == '1'", "assets/CGs/akki_lay_aface1.png", 
#            "lay_aface == '2'", "assets/CGs/akki_lay_aface2.png", 
#            "lay_aface == '3'", "assets/CGs/akki_lay_aface3.png", 
#            "lay_aface == '4'", "assets/CGs/akki_lay_aface4.png", 
#            "lay_aface == '5'", "assets/CGs/akki_lay_aface5.png", 
#            "lay_aface == '6'", "assets/CGs/akki_lay_aface6.png",
#            ),
#
#        )

    python:
        akki_cuddle_base = StateMachineDisplayable(
            "akki_cuddle_base", "naked",
            {
                "naked": "assets/CGs/akki_cuddle_n.jpg",
                "clothed": "assets/CGs/akki_cuddle_cl.jpg"
            }
        )

        akki_cuddle_claire = StateMachineDisplayable(
            "akki_cuddle_claire", 1,
            {
                1: "assets/CGs/akki_cuddle_claire1.png", 
                2: "assets/CGs/akki_cuddle_claire2.png", 
                3: "assets/CGs/akki_cuddle_claire3.png"
            }
        )

        akki_cuddle_akki = StateMachineDisplayable(
            "akki_cuddle_akki", 1,
            {
                1: "assets/CGs/akki_cuddle_akki1.png", 
                2: "assets/CGs/akki_cuddle_akki2.png", 
                3: "assets/CGs/akki_cuddle_akki3.png"
            }
        )

        akki_cuddle_sprite = ComposedSprite(
            (1280, 800),
            ("base", (0, 0), akki_cuddle_base),
            ("claire", (0, 0), akki_cuddle_claire),
            ("akki", (0, 0), akki_cuddle_akki)
        )

    image akkicuddle = akki_cuddle_sprite.displayable()
        
#    image akkicuddle = LiveComposite((1280, 800),
#        (0, 0), ConditionSwitch(
#            "akki_sex_choices.missionary == True", "assets/CGs/akki_cuddle_n.jpg", 
#            "True", "assets/CGs/akki_cuddle_cl.jpg",
#            ),
#        (0, 0), ConditionSwitch(
#            "cuddle_cface == '1'", "assets/CGs/akki_cuddle_claire1.png", 
#            "cuddle_cface == '2'", "assets/CGs/akki_cuddle_claire2.png", 
#            "cuddle_cface == '3'", "assets/CGs/akki_cuddle_claire3.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "cuddle_aface == '1'", "assets/CGs/akki_cuddle_akki1.png", 
#            "cuddle_aface == '2'", "assets/CGs/akki_cuddle_akki2.png", 
#            "cuddle_aface == '3'", "assets/CGs/akki_cuddle_akki3.png", 
#            ),
#
#        )

    ##-- Mirari

    image mira_foot = "assets/CGs/mirari_massage_leg.jpg"
    image mira_foot nibble = "assets/CGs/mirari_nibble_foot.png"
    image mira_back = "assets/CGs/mirari_massage_back.jpg"
    image mira_back nibble = "assets/CGs/mirari_nibble_ear.png"
    image mira_breast = naked("assets/CGs/mirari_breasts{0}.jpg")
    #image mira_cuddle = "assets/CGs/mirari_cuddling.jpg"

    python:
        mirari_cuddle_mface = StateMachineDisplayable(
            "mirari_cuddle_mface", 1,
            { 
                1: "assets/CGs/mirari_cuddling_mface1.png",
                2: "assets/CGs/mirari_cuddling_mface2.png",
                3: "assets/CGs/mirari_cuddling_mface3.png",
            }
        )

        mirari_cuddle_cface = StateMachineDisplayable(
            "mirari_cuddle_cface", 1,
            {
                1: "assets/CGs/mirari_cuddling_cface1.png",
                2: "assets/CGs/mirari_cuddling_cface2.png",
            }
        )

        mirari_cuddle_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), "assets/CGs/mirari_cuddling_base.jpg"),
            ("mirari", (0, 0), mirari_cuddle_mface),
            ("claire", (0, 0), mirari_cuddle_cface)
        )

        mirari_cuddle_initial = {
            "mirari": 1,
            "claire": 1
        }

    image mira_cuddle = mirari_cuddle_sprite.displayable()
        
#    image mira_cuddle = LiveComposite((1280,800),
#        (0, 0), "assets/CGs/mirari_cuddling_base.jpg",
#        #Mirari face
#        (0, 0), ConditionSwitch(
#            "mcuddle_mface == '1'", "assets/CGs/mirari_cuddling_mface1.png",
#            "mcuddle_mface == '2'", "assets/CGs/mirari_cuddling_mface2.png",
#            "mcuddle_mface == '3'", "assets/CGs/mirari_cuddling_mface3.png",
#            ), 
#        #Claire face
#        (0,0), ConditionSwitch(
#            "mcuddle_cface == '1'", "assets/CGs/mirari_cuddling_cface1.png",
#            "mcuddle_cface == '2'", "assets/CGs/mirari_cuddling_cface2.png",
#            ), 
#        )

    python:
        mirari_lying_panties = StateMachineDisplayable(
            "mirari_lying_panties", "on",
            {
                "on": "assets/CGs/mirari04_panties.png", 
                "off": naked("assets/CGs/mirari04_nopan{0}.png")
            }
        )

        mirari_lying_marm = StateMachineDisplayable(
            "mirari_lying_marm", "breast",
            {
                "breast": "assets/CGs/mirari04_marm_breast.png", 
                "touch": "assets/CGs/mirari04_marm_touch.png", 
                "lick": "assets/CGs/mirari04_marm_lick.png"
            }
        )

        mirari_lying_clarm = StateMachineDisplayable(
            "mirari_lying_carm", "fold",
            {
                "breast": "assets/CGs/mirari04_clarm_breast.png", 
                "touch": "assets/CGs/mirari04_clarm_touch.png", 
                "fold": "assets/CGs/mirari04_clarm_fold.png"
            }
        )

        mirari_lying_mface = StateMachineDisplayable(
            "mirari_lying_mface", "tender",
            {
                "happy": "assets/CGs/mirari04_mface_happy.png", 
                "tease": "assets/CGs/mirari04_mface_tease.png", 
                "pleasure": "assets/CGs/mirari04_mface_pleasure.png", 
                "tender": "assets/CGs/mirari04_mface_tender.png"
            }
        )

        mirari_lying_clface = StateMachineDisplayable(
            "mirari_lying_clface", "oh",
            {
                "O": "assets/CGs/mirari04_clface_O.png", 
                "oh": "assets/CGs/mirari04_clface_oh.png", 
                "pleasure": "assets/CGs/mirari04_clface_pleasure.png", 
                "smile": "assets/CGs/mirari04_clface_smile.png", 
                "shock": "assets/CGs/mirari04_clface_shock.png", 
            }
        )

        mirari_lying_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), naked("assets/CGs/mirari04{0}.jpg")),
            ("panties", (0, 0), mirari_lying_panties),
            ("mirari_arm", (0, 0), mirari_lying_marm),
            ("claire_arm", (0, 0), mirari_lying_clarm),
            ("mirari_face", (0, 0), mirari_lying_mface),
            ("claire_face", (0, 0), mirari_lying_clface)
            )

        mirari_lying_initial = {
            "panties": "on",
            "mirari_arm": "breast",
            "claire_arm": "fold",
            "mirari_face": "tender",
            "claire_face": "oh"
        }

    image mira_lying = mirari_lying_sprite.displayable()
        
#    image mira_lying = LiveComposite((1280, 800),
#        (0, 0), naked("assets/CGs/mirari04{0}.jpg"),
#        (0, 0), ConditionSwitch(
#            "mlay_panties == 'on'", "assets/CGs/mirari04_panties.png", 
#            "mlay_panties == 'off'", naked("assets/CGs/mirari04_nopan{0}.png"), 
#            ),
#        (0, 0), ConditionSwitch(
#            "mlay_marm == 'breast'", "assets/CGs/mirari04_marm_breast.png", 
#            "mlay_marm == 'touch'", "assets/CGs/mirari04_marm_touch.png", 
#            "mlay_marm == 'lick'", "assets/CGs/mirari04_marm_lick.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "mlay_clarm == 'breast'", "assets/CGs/mirari04_clarm_breast.png", 
#            "mlay_clarm == 'touch'", "assets/CGs/mirari04_clarm_touch.png", 
#            "mlay_clarm == 'fold'", "assets/CGs/mirari04_clarm_fold.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "mlay_mface == 'happy'", "assets/CGs/mirari04_mface_happy.png", 
#            "mlay_mface == 'tease'", "assets/CGs/mirari04_mface_tease.png", 
#            "mlay_mface == 'pleasure'", "assets/CGs/mirari04_mface_pleasure.png", 
#            "mlay_mface == 'tender'", "assets/CGs/mirari04_mface_tender.png", 
#            ), 
#        (0, 0), ConditionSwitch(
#            "mlay_clface == 'O'", "assets/CGs/mirari04_clface_O.png", 
#            "mlay_clface == 'oh'", "assets/CGs/mirari04_clface_oh.png", 
#            "mlay_clface == 'pleasure'", "assets/CGs/mirari04_clface_pleasure.png", 
#            "mlay_clface == 'smile'", "assets/CGs/mirari04_clface_smile.png", 
#            "mlay_clface == 'shock'", "assets/CGs/mirari04_clface_shock.png", 
#            ),      
#        )

    ##-- orias
    image orias_play cold ="assets/CGs/orias_play_cold.png"
    image orias_play nipple =naked("assets/CGs/orias_play_nipple{0}.png")
    image orias_play nipple_ice =naked("assets/CGs/orias_play_nipple_ice{0}.png")
    image orias_play nipple_suck =naked("assets/CGs/orias_play_nipple_suck{0}.png")
    
    image orias_play hot ="assets/CGs/orias_play_hot.png"
    image orias_play wax_pour ="assets/CGs/orias_play_wax_pour.png"
    image orias_play wax_rub ="assets/CGs/orias_play_wax_rub.png"
    image orias_play wax_scratch ="assets/CGs/orias_play_wax_scratch.png"

    image orias_play tickle ="assets/CGs/orias_play_tickle.png"
    image orias_play nipple_tickle =naked("assets/CGs/orias_play_nipple_tickle{0}.png")
    image orias_play tickle_armpit ="assets/CGs/orias_play_tickle_armpit.png"
    image orias_play tickle_body ="assets/CGs/orias_play_tickle_body.png"
    image orias_play tickle_foot ="assets/CGs/orias_play_tickle_foot.png"
    image orias_play tickle_thighs ="assets/CGs/orias_play_tickle_thighs.png"
    
    image orias_play lick ="assets/CGs/orias_play_lick.png"
    image orias_play kiss ="assets/CGs/orias_play_kiss.png"
    image orias_play kiss_blind ="assets/CGs/orias_play_kiss_blind.png"

    python:
        orias_bed_naked = StateMachineDisplayable(
            "orias_bed_naked", False,
            {
                True: Null(width=1),
                False: "assets/CGs/orias01_orias_clothes.png"
            }
        )

        orias_bed_oriface = StateMachineDisplayable(
            "orias_bed_oriface", "smile",
            {
                "laught": "assets/CGs/orias01_oriface_laugh.png",
                "smile": "assets/CGs/orias01_oriface_smile.png",
                "smile2": "assets/CGs/orias01_oriface_smile2.png",
                "neutral": "assets/CGs/orias01_oriface_neutral.png",
                "default": "assets/CGs/orias01_oriface_neutral.png"
            }
        )

        orias_bed_panties = StateMachineDisplayable(
            "orias_bed_panties", "on",
            {
                "off": naked("assets/CGs/orias01_claire_nopan{0}.png"),
                "on": "assets/CGs/orias01_claire_panties.png"
            }
        )

        orias_bed_tiedup = StateMachineDisplayable(
            "orias_bed_tiedup", False,
            {
                True: "assets/CGs/orias01_clarms_tied.png",
                False: "assets/CGs/orias01_clarms_free.png"
            }
        )

        orias_bed_clface = StateMachineDisplayable(
            "orias_bed_clface", "happy",
            {
                "worried": "assets/CGs/orias01_clface_worried.png",
                "content": "assets/CGs/orias01_clface_content.png",
                "happy": "assets/CGs/orias01_clface_happy.png",
                "laughing": "assets/CGs/orias01_clface_laughing.png",
                "pleasure": "assets/CGs/orias01_clface_pleasure.png",
                "shiver": "assets/CGs/orias01_clface_shiver.png",
                "O": "assets/CGs/orias01_clface_O.png",
                "default": "assets/CGs/orias01_clface_content.png"
            }
        )

        orias_bed_blindfold = StateMachineDisplayable(
            "orias_bed_blindfold", False,
            {
                True: "assets/CGs/orias01_blindfold.png",
                False: Null(width=1),
            }
        )

        orias_bed_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), "assets/CGs/orias01.jpg"),
            (None, (0, 0), "assets/CGs/orias01_orias.png"),
            ("naked", (0, 0), orias_bed_naked),
            ("orias_face", (0, 0), orias_bed_oriface),
            (None, (0, 0), "assets/CGs/orias01_claire.png"),
            ("panties", (0, 0), orias_bed_panties),
            ("tiedup", (0, 0), orias_bed_tiedup),
            (None, (0, 0), naked("assets/CGs/orias01_claire_breasts{0}.png")),
            ("claire_face", (0, 0), orias_bed_clface),
            ("blindfold", (0, 0), orias_bed_blindfold)
        )

        orias_bed_initial = {
            "naked": False,
            "orias_face": "smile",
            "panties": "on",
            "tiedup": False,
            "claire_face": "happy",
            "blindfold": False
        }

    image orias_bed = orias_bed_sprite.displayable()

    
#    image orias_bed =LiveComposite((1280, 800),
#        (0, 0), "assets/CGs/orias01.jpg",
#        (0, 0), "assets/CGs/orias01_orias.png",
#        (0, 0), ConditionSwitch(
#            "orias_naked == True", Null(width=1),
#            "True", "assets/CGs/orias01_orias_clothes.png",
#            ),
#        (0, 0), ConditionSwitch (
#            "orilay_oriface == 'laugh'", "assets/CGs/orias01_oriface_laugh.png",
#            "orilay_oriface == 'smile'", "assets/CGs/orias01_oriface_smile.png",
#            "orilay_oriface == 'smile2'", "assets/CGs/orias01_oriface_smile2.png",
#            "orilay_oriface == 'neutral'", "assets/CGs/orias01_oriface_neutral.png",
#            "True", "assets/CGs/orias01_oriface_neutral.png",
#            ),
#        (0, 0), "assets/CGs/orias01_claire.png",
#        (0, 0), ConditionSwitch(
#            "orilay_panties == 'off'", naked("assets/CGs/orias01_claire_nopan{0}.png"),
#            "True", "assets/CGs/orias01_claire_panties.png",
#            ),
#        (0, 0), ConditionSwitch(
#            "orilay_tiedup == True", "assets/CGs/orias01_clarms_tied.png",
#            "True", "assets/CGs/orias01_clarms_free.png",
#            
#            ),
#        (0, 0), naked("assets/CGs/orias01_claire_breasts{0}.png"),
#        (0, 0), ConditionSwitch(
#            "orilay_clface== 'worried'", "assets/CGs/orias01_clface_worried.png",
#            "orilay_clface== 'content'", "assets/CGs/orias01_clface_content.png",
#            "orilay_clface== 'happy'", "assets/CGs/orias01_clface_happy.png",
#            "orilay_clface== 'laughing'", "assets/CGs/orias01_clface_laughing.png",
#            "orilay_clface== 'pleasure'", "assets/CGs/orias01_clface_pleasure.png",
#            "orilay_clface== 'shiver'", "assets/CGs/orias01_clface_shiver.png",
#            "orilay_clface== 'O'", "assets/CGs/orias01_clface_O.png",
#            "True", "assets/CGs/orias01_clface_content.png",
#            ),
#        (0, 0), ConditionSwitch(
#            "orilay_blindfold == True","assets/CGs/orias01_blindfold.png",
#            "True", Null(width=1),
#            ),
#
#        
#        )
    
    image orias_finish oral =LiveComposite((1280,800),
        (450,0), ConditionSwitch(
            "orias_naked == True", Null(width=1),
            "True", "assets/CGs/orias_finish_oral_clothes.png",
            ),
        (450,0),
        naked("assets/CGs/orias_finish_oral{0}.png"),
        )
    image orias_finish fingers =LiveComposite((1280,800),
        (450,0), ConditionSwitch(
            "orias_naked == True", Null(width=1),
            "True", "assets/CGs/orias_finish_fingers_clothes.png",
            ),
        (450,0), naked("assets/CGs/orias_finish_fingers{0}.png"),
        )


    python:
        orias_cuddles_naked = StateMachineDisplayable(
            "orias_cuddles_naked", True,
            {
                True: Null(width=1),
                False: "assets/CGs/orias_cuddles_oriasclothes.png", 
            }
        )

        orias_cuddles_clnaked = StateMachineDisplayable(
            "orias_cuddles_clnaked", True,
            {
                True: Null(width=1), 
                False: "assets/CGs/orias_cuddles_chemise.png", 
            }
        )

        orias_cuddles_clface = StateMachineDisplayable(
            "orias_cuddles_clface", 1,
            {
                1: "assets/CGs/orias_cuddles_cface1.png", 
                2: "assets/CGs/orias_cuddles_cface2.png", 
                3: "assets/CGs/orias_cuddles_cface3.png", 
                4: "assets/CGs/orias_cuddles_cface4.png", 
                5: "assets/CGs/orias_cuddles_cface5.png", 
            }
        )

        orias_cuddles_oriface = StateMachineDisplayable(
            "orias_cuddles_oriface", 1,
            {
                1: "assets/CGs/orias_cuddles_oface1.png", 
                2: "assets/CGs/orias_cuddles_oface2.png", 
                3: "assets/CGs/orias_cuddles_oface3.png", 
                4: "assets/CGs/orias_cuddles_oface4.png", 
            }
        )

        orias_cuddles_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), ("assets/CGs/orias_cuddles.jpg")),
            ("orias_naked", (0, 0), orias_cuddles_naked),
            ("claire_naked", (0, 0), orias_cuddles_clnaked),
            ("claire_face", (0, 0), orias_cuddles_clface),
            ("orias_face", (0, 0), orias_cuddles_oriface)
        )

        orias_cuddles_initial = {
            "orias_naked": False,
            "claire_naked": False,
            "claire_face": 3,
            "orias_face": 1
        }

    image orias_cuddles = orias_cuddles_sprite.displayable()
    
#    image orias_cuddles = LiveComposite((1280, 800),
#        (0, 0), ("assets/CGs/orias_cuddles.jpg"),
#        (0, 0), ConditionSwitch(
#            "orias_naked == True", Null(width=1),
#            "True", "assets/CGs/orias_cuddles_oriasclothes.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "orias_clnaked == True", Null(width=1), 
#            "True", "assets/CGs/orias_cuddles_chemise.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "orias_cuddles_clface == '1'", "assets/CGs/orias_cuddles_cface1.png", 
#            "orias_cuddles_clface == '2'", "assets/CGs/orias_cuddles_cface2.png", 
#            "orias_cuddles_clface == '3'", "assets/CGs/orias_cuddles_cface3.png", 
#            "orias_cuddles_clface == '4'", "assets/CGs/orias_cuddles_cface4.png", 
#            "orias_cuddles_clface == '5'", "assets/CGs/orias_cuddles_cface5.png", 
#            ),
#        (0, 0), ConditionSwitch(
#            "orias_cuddles_oriface == '1'", "assets/CGs/orias_cuddles_oface1.png", 
#            "orias_cuddles_oriface == '2'", "assets/CGs/orias_cuddles_oface2.png", 
#            "orias_cuddles_oriface == '3'", "assets/CGs/orias_cuddles_oface3.png", 
#            "orias_cuddles_oriface == '4'", "assets/CGs/orias_cuddles_oface4.png", 
#            ),    
#        )

    #-- Kael

    image kael_start = "assets/CGs/kael_start_kneel.jpg"
    image kael_start hand = "assets/CGs/kael_start_kneel2.jpg"
    image kael_start kiss = "assets/CGs/kael_start_kiss.jpg"
    image kael_start pillow = "assets/CGs/kael_start_pillow.jpg"

    image kael_leaning = "assets/CGs/kael_leaning.jpg"
    image kael_leaning b= "assets/CGs/kael_leaning2.jpg"

    image kael_kissing A1 = "assets/CGs/kael_kissing_a1.png"
    image kael_kissing A2 = "assets/CGs/kael_kissing_a2.png"
    image kael_kissing B = "assets/CGs/kael_kissing_b.png"

    python:
        kael_warmup_clface = StateMachineDisplayable(
            "kael_warmup_clface", 1,
            {
                1: "assets/CGs/kael_warmup_clface1.png",
                2: "assets/CGs/kael_warmup_clface2.png"
            }
        )

        kael_warmup_kael = StateMachineDisplayable(
            "kael_warmup_kael", 1,
            {
                1: "assets/CGs/kael_warmup_kael1.png",
                2: naked("assets/CGs/kael_warmup_kael2{0}.png"),
                3: naked("assets/CGs/kael_warmup_kael3{0}.png")
            }
        )

        kael_warmup_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), naked("assets/CGs/kael_warmup_base{0}.jpg")),
            ("claire", (0, 0), kael_warmup_clface),
            ("kael", (0, 0), kael_warmup_kael)
        )

        kael_warmup_initial = {
            "claire": 1,
            "kael": 1
        }

    image kael_warmup = kael_warmup_sprite.displayable()
        
#    image kael_warmup = LiveComposite((1280,800),
#        #base
#        (0, 0), naked("assets/CGs/kael_warmup_base{0}.jpg"),
#        #Claire face
#        (0, 0), ConditionSwitch(
#            "kael_warmup_clface == '1'","assets/CGs/kael_warmup_clface1.png",
#            "kael_warmup_clface == '2'","assets/CGs/kael_warmup_clface2.png",
#            ),
#        #Kael position
#        (0, 0), ConditionSwitch(
#            "kael_warmup_kael == '1'", "assets/CGs/kael_warmup_kael1.png",
#            "kael_warmup_kael == '2'", naked("assets/CGs/kael_warmup_kael2{0}.png"),
#            "kael_warmup_kael == '3'", naked("assets/CGs/kael_warmup_kael3{0}.png"),
#            ),
#
#        )

    python:
        kael_missionary_clface = StateMachineDisplayable(
            "kael_missionary_clface", 1,
            {
                1: "assets/CGs/kael_missionary_clface1.png",
                2: "assets/CGs/kael_missionary_clface2.png",
                3: "assets/CGs/kael_missionary_clface3.png",
                4: "assets/CGs/kael_missionary_clface4.png",
                5: "assets/CGs/kael_missionary_clface5.png",
                6: "assets/CGs/kael_missionary_clface6.png",
            }
        )

        kael_missionary_kface = StateMachineDisplayable(
            "kael_missionary_kface", 1,
            {
                1: "assets/CGs/kael_missionary_kface1.png",
                2: "assets/CGs/kael_missionary_kface2.png",
                3: "assets/CGs/kael_missionary_kface3.png",
                4: "assets/CGs/kael_missionary_kface4.png",
            }
        )

        kael_missionary_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), naked("assets/CGs/kael_missionary{0}.jpg")),
            ("claire", (0, 0), kael_missionary_clface),
            ("kael", (0, 0), kael_missionary_kface)
        )

        kael_missionary_initial = {
            "claire": 1,
            "kael": 1
        }

    image kael_missionary = kael_missionary_sprite.displayable()

    
#    image kael_missionary = LiveComposite((1280,800),
#        #base
#        (0, 0), naked("assets/CGs/kael_missionary{0}.jpg"),
#        #claire face
#        (0, 0), ConditionSwitch(
#            "kael_mis_clface == '1'","assets/CGs/kael_missionary_clface1.png",
#            "kael_mis_clface == '2'","assets/CGs/kael_missionary_clface2.png",
#            "kael_mis_clface == '3'","assets/CGs/kael_missionary_clface3.png",
#            "kael_mis_clface == '4'","assets/CGs/kael_missionary_clface4.png",
#            "kael_mis_clface == '5'","assets/CGs/kael_missionary_clface5.png",
#            "kael_mis_clface == '6'","assets/CGs/kael_missionary_clface6.png",
#            ),
#        #kael face
#          (0, 0), ConditionSwitch(
#            "kael_mis_kface == '1'","assets/CGs/kael_missionary_kface1.png",
#            "kael_mis_kface == '2'","assets/CGs/kael_missionary_kface2.png",
#            "kael_mis_kface == '3'","assets/CGs/kael_missionary_kface3.png",
#            "kael_mis_kface == '4'","assets/CGs/kael_missionary_kface4.png",
#            ),
#        )

    python:
        kael_cuddles_clface = StateMachineDisplayable(
            "kael_cuddles_clface", 2,
            {
                1: "assets/CGs/kael_cuddles_cface1.png",
                2: "assets/CGs/kael_cuddles_cface2.png"
            }
        )

        kael_cuddles_kface = StateMachineDisplayable(
            "kael_cuddles_kface", 2,
            {
                1: "assets/CGs/kael_cuddles_kface1.png",
                2: "assets/CGs/kael_cuddles_kface2.png"
            }
        )

        kael_cuddles_knaked = StateMachineDisplayable(
            "kael_cuddles_knaked", False,
            {
                True: Null(width=1),
                False: "assets/CGs/kael_cuddles_kclothes.png"
            }
        )

        kael_cuddles_clnaked = StateMachineDisplayable(
            "kael_cuddles_clnaked", False,
            {
                True: Null(width=1),
                False: "assets/CGs/kael_cuddles_chemise.png",
            }
        )

        kael_cuddles_sprite = ComposedSprite(
            (1280, 800),
            (None, (0, 0), "assets/CGs/kael_cuddles_base.jpg"),
            ("claire_face", (0, 0), kael_cuddles_clface),
            ("kael_face", (0, 0), kael_cuddles_kface),
            ("kael_naked", (0, 0), kael_cuddles_knaked),
            ("claire_naked", (0, 0), kael_cuddles_clnaked)
        )

        kael_cuddles_initial = {
            "claire_face": 2,
            "kael_face": 2,
            "kael_naked": False,
            "claire_naked": False
        }

    image kael_cuddles = kael_cuddles_sprite.displayable()
        
#    image kael_cuddles = LiveComposite((1280,800),
#        #base
#        (0, 0), "assets/CGs/kael_cuddles_base.jpg",
#        #claire face
#        (0, 0), ConditionSwitch(
#            "kael_cuddle_clface == '1'","assets/CGs/kael_cuddles_cface1.png",
#            "kael_cuddle_clface == '2'","assets/CGs/kael_cuddles_cface2.png",
#            ),
#        #kael face
#        (0, 0), ConditionSwitch(
#            "kael_cuddle_kface == '1'","assets/CGs/kael_cuddles_kface1.png",
#            "kael_cuddle_kface == '2'","assets/CGs/kael_cuddles_kface2.png",
#            ),
#        #kael clothes
#        (0,0), ConditionSwitch(
#            "kael_naked == True", Null(width=1),
#            "True", "assets/CGs/kael_cuddles_kclothes.png",
#            ),
#        #caire clothes
#        (0,0), ConditionSwitch(
#            "kael_claire_naked == True", Null(width=1),
#            "True", "assets/CGs/kael_cuddles_chemise.png",
#            ),
#        )

    image group = naked("assets/CGs/orgy{0}.jpg")


    # -- CG Test
    python:
        #Orias Cuddles
        orias_cuddles_base = StateMachineDisplayable(
            "orias_cuddle_base", "default",
            {
                "default": "assets/CGs/orias_cuddles.jpg"
            }
        )
        orias_cuddles_orias_clothes = StateMachineDisplayable(
            "orias_cuddles_orias_clothes", "default",
            {
                "default": "assets/CGs/orias_cuddles_oriasclothes.png",
                "naked": Null(),
            }
        )
        orias_cuddles_claire_clothes = StateMachineDisplayable(
            "orias_cuddles_claire_clothes", "default",
            {
                "default": "assets/CGs/orias_cuddles_chemise.png",
                "naked": Null(),
            }
        )
        orias_cuddles_orias_face = StateMachineDisplayable(
            "orias_cuddles_orias_face", "default",
            {
                "default": "assets/CGs/orias_cuddles_oface1.png",
                "1": "assets/CGs/orias_cuddles_oface1.png",
                "2": "assets/CGs/orias_cuddles_oface2.png",
                "3": "assets/CGs/orias_cuddles_oface3.png",
                "4": "assets/CGs/orias_cuddles_oface1.png",
            }
        )
        orias_cuddles_claire_face = StateMachineDisplayable(
            "orias_cuddles_claire_face", "default",
            {
                "default": "assets/CGs/orias_cuddles_cface1.png",
                "1": "assets/CGs/orias_cuddles_cface1.png",
                "2": "assets/CGs/orias_cuddles_cface2.png",
                "3": "assets/CGs/orias_cuddles_cface3.png",
                "4": "assets/CGs/orias_cuddles_cface1.png",
                "4": "assets/CGs/orias_cuddles_cface1.png",
            }
        )
        orias_cuddles_test = ComposedSprite(
            (1280,800),
            ("base", (0, 0), "assets/CGs/orias_cuddles.jpg"),
            ("o_clothes", (0, 0), orias_cuddles_orias_clothes),
            ("cl_clothes", (0, 0), orias_cuddles_claire_clothes),
            ("o_face", (0, 0), orias_cuddles_orias_face),
            ("cl_face", (0, 0), orias_cuddles_claire_face)
        )
        orias_cuddles_test.set_state(o_clothes="default")

    image orias_cuddles_test = At(orias_cuddles_test.displayable())




    # -- Characters ----------------------------------------------------
    define narrator = make_character(what_style="say_thought")
    define name_only = make_character()
    define cl = make_character('claire_name',
                               dynamic=True,
                               show_side_image=At(claire.displayable(), say_image), color="#bdff14")
    define ak = make_character(name='akki_name', dynamic=True, color="#ff8575")
    define mi = make_character(name='mirari_name', dynamic=True, color="#ffc2d9")
    define ka = make_character(name='kael_name', dynamic=True, color="#9ebbff")
    define ori = make_character(name='orias_name', dynamic=True, color="#e29eff")
    define cla = make_character('claire_name', dynamic=True, color="#bdff14")
