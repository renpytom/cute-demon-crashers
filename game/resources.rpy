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
                "shock": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_emo_shock.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shock2.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shock3.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shock4.png", 0.1, None,
                    "assets/sprites/claire/cl_emo_shock5.png"
                ),
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
                "bug cry": "assets/sprites/claire/cl_eyes_bugcry.png",
                "clench": "assets/sprites/claire/cl_eyes_clench.png",
                "clench tear": "assets/sprites/claire/cl_eyes_clenchtear.png",
                "closed": "assets/sprites/claire/cl_eyes_closed.png",
                "cry": "assets/sprites/claire/cl_eyes_cry.png",
                "dizzy": "assets/sprites/claire/cl_eyes_dizzy.png",
                "dots": "assets/sprites/claire/cl_eyes_dots.png",
                "down": "assets/sprites/claire/cl_eyes_down.png",
                "flat": "assets/sprites/claire/cl_eyes_flat.png",
                "fun front": "assets/sprites/claire/cl_eyes_funfront.png",
                "fun side": "assets/sprites/claire/cl_eyes_funside.png",
                "happy": "assets/sprites/claire/cl_eyes_happy.png",
                "mortified": "assets/sprites/claire/cl_eyes_mortified.png",
                "default": "assets/sprites/claire/cl_eyes_open.png",
                "semi open": "assets/sprites/claire/cl_eyes_semi.png",
                "shock": "assets/sprites/claire/cl_eyes_shock.png",
                "starry": anim.TransitionAnimation(
                    "assets/sprites/claire/cl_eyes_starry1.png", 0.2, None,
                    "assets/sprites/claire/cl_eyes_starry2.png", 0.2, None
                ),
                "tender": "assets/sprites/claire/cl_eyes_tender.png",
                "tender side": "assets/sprites/claire/cl_eyes_tenderside.png",
                "wide": "assets/sprites/claire/cl_eyes_wide.png"
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
                "bugteary"  : ak_sprite("eyes_bugteary"),
                "clench"    : ak_sprite("eyes_clench"),
                "closed"    : ak_sprite("eyes_closed"),
                "cry"       : ak_sprite("eyes_cry"),
                "dizzy"     : ak_sprite("eyes_dizzy"),
                "dots"      : ak_sprite("eyes_dots"),
                "flat"      : ak_sprite("eyes_flat"),
                "fun front" : ak_sprite("eyes_funfront"),
                "fun side"  : ak_sprite("eyes_funside"),
                "happy"     : ak_sprite("eyes_happy"),
                "mortified" : ak_sprite("eyes_mortified"),
                "default"   : ak_sprite("eyes_open"),
                "shock"     : ak_sprite("eyes_shock"),
                "starry": anim.TransitionAnimation(
                    ak_sprite("eyes_starry1"), 0.2, None,
                    ak_sprite("eyes_starry2"), 0.2, None
                ),
                "tender"      : ak_sprite("eyes_tender"),
                "tender side" : ak_sprite("eyes_tenderside"),
                "twitch"      : ak_sprite("eyes_twitch"),
                "wide"        : ak_sprite("eyes_wide"),
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
                
                "flowers": anim.TransitionAnimation(
                    mi_sprite("emo_flowers"), 0.1, None,
                    mi_sprite("emo_flowers2"), 0.1, None,
                    mi_sprite("emo_flowers3"), 0.1, None,
                    mi_sprite("emo_flowers4"), 0.1, None,
                    mi_sprite("emo_flowers5"), 0.1, None,
                    mi_sprite("emo_flowers6"), 0.1, None,
                    mi_sprite("emo_flowers7"), 0.1, None,
                    Null()
                ),
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
                "default": mi_sprite("eyes_open"),
                "angry": mi_sprite("eyes_angry"),
                "big": mi_sprite("eyes_big"),
                "bugteary": mi_sprite("eyes_bugteary"),
                "clench": mi_sprite("eyes_clench"),
                "closed": mi_sprite("eyes_closed"),
                "cry": mi_sprite("eyes_cry"),
                "dizzy": mi_sprite("eyes_dizzy"),
                "dots": mi_sprite("eyes_dots"),
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
                "tender": mi_sprite("eyes_tender"),
                "wide": mi_sprite("eyes_wide"),
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
                "cry"       : ka_sprite("eyes_cry"),
                "dizzy"     : ka_sprite("eyes_dizzy"),
                "dots"      : ka_sprite("eyes_dots"),
                "flat"      : ka_sprite("eyes_flat"),
                "fun front" : ka_sprite("eyes_funfront"),
                "fun side"  : ka_sprite("eyes_funside"),
                "happy"     : ka_sprite("eyes_happy"),
                "default"   : ka_sprite("eyes_open"),
                "shock"     : ka_sprite("eyes_shock"),
                "sparkly": ka_sprite("eyes_sparkly"),
                "tender"      : ka_sprite("eyes_tender"),
                "tender side" : ka_sprite("eyes_tenderside"),
                "up": ka_sprite("eyes_up"),
                "wide"        : ka_sprite("eyes_wide"),
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
                "default": ori_sprite("eyes_open"),
                "closed"    : ori_sprite("eyes_closed"),
                "dizzy"     : ori_sprite("eyes_dizzy"),
                "dots"      : ori_sprite("eyes_dots"),
                "flat"      : ori_sprite("eyes_flat"),
                "fun front" : ori_sprite("eyes_funfront"),
                "fun side"  : ori_sprite("eyes_funside"),
                "happy"     : ori_sprite("eyes_happy"),
                "shock"     : ori_sprite("eyes_shock"),
                "side": ori_sprite("eyes_side"),
                "squint": ori_sprite("eyes_squint"),
                "wide": ori_sprite("eyes_wide"),
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


    # --- Chibis -------------------------------------------------------
    image chibi_akki01 = "assets/chibis/akki_hug.png"
    image chibi_akki02 = "assets/chibis/akki_sit.png"
    
    image chibi_orias01 = "assets/chibis/orias_tea.png"

    image chibi_mira01 = "assets/chibis/mirari_hair.png"

    image chibi_kael01 = "assets/chibis/kael_laundry.png"


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

    image akkiforeplay = LiveComposite((1280, 800),
        (0, 0), "assets/CGs/akki01_bg.jpg",
        (0, 0), "assets/CGs/akki01_akkibase.png",
        (0, 0), ConditionSwitch(
            "ak_bottom == 'on'", "assets/CGs/akki01_akbottomon.png", 
            "ak_bottom == 'off'", naked("assets/CGs/akki01_akbottomoff{0}.png"), 
            ),
        (0, 0), ConditionSwitch(
            "cl_arm == 'down'", "assets/CGs/akki01_clarm_down.png", 
            "cl_arm == 'chest'", "assets/CGs/akki01_clarm_chest.png",
            "cl_arm == 'crotch'", "assets/CGs/akki01_clarm_crotch.png",
            "cl_arm == 'handjob'", naked("assets/CGs/akki01_clarm_handjob{0}.png"),
            ),
        (0, 0), naked("assets/CGs/akki01_clbase{0}.png"),
        (0, 0), ConditionSwitch(
            "cl_bottom == 'on'", "assets/CGs/akki01_clbottomon.png", 
            "cl_bottom == 'off'", Null(width=1),
            ),
        (0, 0), ConditionSwitch(
            "cl_top == 'on'", "assets/CGs/akki01_cltop_shirt.png", 
            "cl_top == 'bra'", "assets/CGs/akki01_cltop_bra.png",
            "cl_top == 'off'", naked("assets/CGs/akki01_cltop_boobs{0}.png"),
            
            ),
        (0, 0), ConditionSwitch(
            "ak_arm == 'down'", "assets/CGs/akki01_akarm_down.png", 
            "ak_arm == 'breast'", "assets/CGs/akki01_akarm_breast.png",
            #"ak_arm == 'tummy'", "assets/CGs/akki01_akarm_tummy.png",
            "ak_arm == 'finger'", "assets/CGs/akki01_akarm_finger.png",
            
            ),
        (0, 0), ConditionSwitch(
            "ac_heads == 'apart'", "assets/CGs/akki01_heads_apart.png", 
            "ac_heads == 'kiss'", "assets/CGs/akki01_heads_kiss.png",
            
            ),
        (0, 0), ConditionSwitch(
            "cl_face == None", Null(width=1), 
            "cl_face == 'surprised'", "assets/CGs/akki01_clface_surprised.png",
            "cl_face == 'embarrassed'", "assets/CGs/akki01_clface_embarrased.png", 
            "cl_face == 'smile'", "assets/CGs/akki01_clface_smile.png",
            "cl_face == 'happy'", "assets/CGs/akki01_clface_happy.png", 
            "cl_face == 'pleasure'", "assets/CGs/akki01_clface_pleasure.png",
            "cl_face == 'O'", "assets/CGs/akki01_clface_O.png",
            
            ),
        (0, 0), ConditionSwitch(
            "ak_face == None", Null(width=1), 
            "ak_face == 'happy'", "assets/CGs/akki01_akface_happy.png", 
            "ak_face == 'nervous'", "assets/CGs/akki01_akface_nervous.png",
            "ak_face == 'pleasure'", "assets/CGs/akki01_akface_pleasure.png",
            "ak_face == 'D:'", "assets/CGs/akki01_akface_hesitant.png",
            
            ),

        )
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
    
    image akki_missionary = LiveComposite((1280, 800),
        (0, 0), naked("assets/CGs/akki_lay01{0}.jpg"),
        (0, 0), ConditionSwitch(
            "lay_cface == '1'", "assets/CGs/akki_lay_cface1.png", 
            "lay_cface == '2'", "assets/CGs/akki_lay_cface2.png", 
            "lay_cface == '3'", "assets/CGs/akki_lay_cface3.png", 
            ),
        (0, 0), ConditionSwitch(
            "lay_aface == '1'", "assets/CGs/akki_lay_aface1.png", 
            "lay_aface == '2'", "assets/CGs/akki_lay_aface2.png", 
            "lay_aface == '3'", "assets/CGs/akki_lay_aface3.png", 
            "lay_aface == '4'", "assets/CGs/akki_lay_aface4.png", 
            "lay_aface == '5'", "assets/CGs/akki_lay_aface5.png", 
            "lay_aface == '6'", "assets/CGs/akki_lay_aface6.png",
            ),

        )
    
    image akkicuddle = LiveComposite((1280, 800),
        (0, 0), ConditionSwitch(
            "akki_sex_choices.missionary == True", "assets/CGs/akki_cuddle_n.jpg", 
            "True", "assets/CGs/akki_cuddle_cl.jpg",
            ),
        (0, 0), ConditionSwitch(
            "cuddle_cface == '1'", "assets/CGs/akki_cuddle_claire1.png", 
            "cuddle_cface == '2'", "assets/CGs/akki_cuddle_claire2.png", 
            "cuddle_cface == '3'", "assets/CGs/akki_cuddle_claire3.png", 
            ),
        (0, 0), ConditionSwitch(
            "cuddle_aface == '1'", "assets/CGs/akki_cuddle_akki1.png", 
            "cuddle_aface == '2'", "assets/CGs/akki_cuddle_akki2.png", 
            "cuddle_aface == '3'", "assets/CGs/akki_cuddle_akki3.png", 
            ),

        )

    ##-- Mirari

    image mira_foot = "assets/CGs/mirari_massage_leg.jpg"
    image mira_foot nibble = "assets/CGs/mirari_nibble_foot.png"
    image mira_back = "assets/CGs/mirari_massage_back.jpg"
    #image mira_back nibble = "assets/CGs/mirari_nibble_ear.png"
    image mira_breast = naked("assets/CGs/mirari_breasts{0}.jpg")
    image mira_cuddle = "assets/CGs/mirari_cuddling.jpg"

    image mira_lying = LiveComposite((1280, 800),
        (0, 0), naked("assets/CGs/mirari04{0}.jpg"),
        (0, 0), ConditionSwitch(
            "mlay_panties == 'on'", "assets/CGs/mirari04_panties.png", 
            "mlay_panties == 'off'", naked("assets/CGs/mirari04_nopan{0}.png"), 
            ),
        (0, 0), ConditionSwitch(
            "mlay_marm == 'breast'", "assets/CGs/mirari04_marm_breast.png", 
            "mlay_marm == 'touch'", "assets/CGs/mirari04_marm_touch.png", 
            "mlay_marm == 'lick'", "assets/CGs/mirari04_marm_lick.png", 
            ),
        (0, 0), ConditionSwitch(
            "mlay_clarm == 'breast'", "assets/CGs/mirari04_clarm_breast.png", 
            "mlay_clarm == 'touch'", "assets/CGs/mirari04_clarm_touch.png", 
            "mlay_clarm == 'fold'", "assets/CGs/mirari04_clarm_fold.png", 
            ),
        (0, 0), ConditionSwitch(
            "mlay_mface == 'happy'", "assets/CGs/mirari04_mface_happy.png", 
            "mlay_mface == 'tease'", "assets/CGs/mirari04_mface_tease.png", 
            "mlay_mface == 'pleasure'", "assets/CGs/mirari04_mface_pleasure.png", 
            "mlay_mface == 'tender'", "assets/CGs/mirari04_mface_tender.png", 
            ), 
        (0, 0), ConditionSwitch(
            "mlay_clface == 'O'", "assets/CGs/mirari04_clface_O.png", 
            "mlay_clface == 'oh'", "assets/CGs/mirari04_clface_oh.png", 
            "mlay_clface == 'pleasure'", "assets/CGs/mirari04_clface_pleasure.png", 
            "mlay_clface == 'smile'", "assets/CGs/mirari04_clface_smile.png", 
            "mlay_clface == 'shock'", "assets/CGs/mirari04_clface_shock.png", 
            ),      
        )


    # -- Characters ----------------------------------------------------
    define narrator = make_character(what_style="say_thought")
    define name_only = make_character()
    define cl = make_character('claire_name',
                               dynamic=True,
                               show_side_image=At(claire.displayable(), say_image))
    define ak = make_character(name='akki_name', dynamic=True)
    define mi = make_character(name='mirari_name', dynamic=True)
    define ka = make_character(name='kael_name', dynamic=True)
    define ori = make_character(name='orias_name', dynamic=True)
    define cla = make_character('claire_name', dynamic=True)


    # -- Gallery -------------------------------------------------------
    python:
        gallery = Gallery(
            GalleryFolder(
                "Akki",
                [CG("akki01", Solid("#000000"))]
            ),
            GalleryFolder("Orias"),
            GalleryFolder("Kael"),
            GalleryFolder("Mirari"),
            GalleryFolder("Others")
        )
