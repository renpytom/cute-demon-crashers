# label day3_morning:
#     jump choose_a_place_to_hangout

define everybody_sex = False

label sex_choice:
    scene black with dissolve 
    play music music_tension
    pause (0.2)
    
    #Resetting everybody's expressions and bases
    $orias.set_state(base="default", glasses="off", **Emotion.normal())
    $kael.set_state(base="default", glasses="off", **Emotion.normal())
    $mirari.set_state(base="default",**Emotion.normal())
    $akki.set_state(base="default", **Emotion.normal())

    scene bg hallway_night with dissolve
    pause (0.2)
    $claire.set_state(eyebrows="frown", emotion="sweat lots", mouth="wavy", eyes="default", emotion_base="small blush")
    cl "(It's time...)"
    show mirari at left4
    show akki at mleft4
    show kael at mright4
    show orias at right4
    with dissolve
    "The others are already gathered in the hallway when I arrive." 
    $mirari.set_state(with_dissolve, eyes="wink")
    show mirari zorder 3 at speak
    voice "m_w30"
    mi "Remember, the portal closes around midnight, so it should give you plenty of time with whoever you pick." 
    $mirari.set_state(eyes="default")
    show mirari zorder 0 at endspeak
    $kael.set_state(eyes="wink")
    show kael zorder 3 at speak
    voice "k_s03"
    ka "And we'll leave you to your privacy as well."
    $kael.set_state(eyes="default")
    show kael zorder 0 at endspeak
    $orias.set_state(eyes="closed")
    show orias zorder 3 at speak
    ori "Once the portal closes, it'll be as if we were never here."
    $orias.set_state(eyes="default")
    show orias zorder 0 at endspeak
    $akki.set_state(eyes="happy")
    show akki zorder 3 at speak
    ak "We'll respect your decision, [claire_name], whatever it is."
    "My heart races a bit. After all, this isn't easy..."
    $claire.set_state(mouth="smile", emotion="default", eyebrows="default", emotion_base="small blush")
    cl "Thank you, everyone."
    $claire.set_state(with_dissolve, eyebrows="frown", mouth="wavy")
    cl "Then..."
    $akki.set_state(eyes="default")
    show akki at endspeak
    "...Who should I pick?"

    if persistent.akki_complete:
        if persistent.orias_complete:
            if persistent.kael_complete:
                if persistent.mirari_complete:
                    $everybody_sex = True


    menu:
        
        "Akki.":
            if akki_scenes >= 3:
                $akki.set_state(with_dissolve, eyes="wink")
                "Akki and I exchange knowing glances."
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "You'd be okay settling for me, Akki?"
                $akki.set_state(eyes="happy", mouth="grin", emotion="starry", emotion_base="small blush")
                show akki at bounce_up
                ak "Settle? I'd be {i}thrilled{/i}, [claire_name]."
            else:
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "Um, Akki, if it's okay with you..."
                $akki.set_state(with_dissolve, eyebrows="up", mouth="happy", emotion="starry", emotion_base="small blush")
                show akki at bounce_up
                ak "M-me? You mean it? Of course!"
                if mirari_scenes >= 3:
                    $mirari.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                    voice "m_s18"
                    mi "Aw, but it's probably for the best."
                    show kael zorder 3
                    $kael.set_state(with_dissolve,eyes="closed")
                    voice "k_s03"
                    ka "Treat her kindly, Akki, and don't get too excited."
                    show orias zorder 4
                    $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender", mouth="smile")
                    ori "It's a good match."
                elif kael_scenes >= 3:
                    $mirari.set_state(eyes="happy", emotion="note")
                    show mirari at bounce_up
                    mi "How wonderful!"
                    show orias zorder 4
                    $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender", mouth="smile")
                    ori "It's a good match."
                    $kael.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                    voice "k_s01"
                    ka "Ah, can't be helped..."
                elif orias_scenes >= 3:
                    $mirari.set_state(eyes="happy", emotion="note")
                    show mirari at bounce_up
                    mi "How wonderful!"
                    show kael zorder 3
                    $kael.set_state(with_dissolve, eyes="closed")
                    voice "k_s03"
                    ka "Treat her kindly, Akki, and don't get too excited."
                    $orias.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                    ori "I guess Akki would be more suitable..."
                else:
                    $mirari.set_state(eyes="happy", emotion="note")
                    show mirari at bounce_up
                    mi "How wonderful!"
                    show kael zorder 3
                    $kael.set_state(with_dissolve,eyes="closed")
                    ka "Treat her kindly, Akki, and don't get too excited."
                    show orias zorder 4
                    $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender", mouth="smile")
                    ori "It's a good match."

            show kael zorder 2
            show orias zorder 1
            show akki zorder 3 at speak
            $akki.set_state(eyebrows="frown",eyes="default", mouth="happy")
            ak "Let's do this! Come on~"
            $claire.set_state(emotion_base="large blush", mouth="wah", eyes="big", emotion="panic", eyebrows="up")
            cl "Eep! Whoa, Akki!"
            hide akki with moveoutright
            #both leave
            show mirari at left 
            show kael at center 
            show orias at right
            with move
            show mirari at bounce_up
            $mirari.set_state(with_dissolve, eyes="clench", mouth="kitty", emotion="heart", eyebrows="up")
            voice "m_s10"
            mi "Already bridal carrying her to the bedroom! How passionate."
            $kael.set_state(with_dissolve, emotion="sweat", eyebrows="inwards", mouth="grin", eyes="happy")
            voice "k_s03"
            ka "So much for not getting too excited."
            $orias.set_state(with_dissolve, mouth="smile", eyebrows="tender", eyes="default")
            ori "Still, this will be a good experience. He would need to be nourished sooner or later, and it's ideal it's happening now."
            $kael.set_state(with_dissolve, **Emotion.normal())
            voice "k_s03"
            ka "And with someone he's comfortable with."
            $mirari.set_state(mouth="vhappy", emotion="flowers")
            show mirari at bounce_up
            voice "m_w31"
            mi "We should find a way to celebrate when he gets back! I say we bake a cake!"
            $kael.set_state(mouth="happy", eyes="happy", emotion="note")
            show kael at bounce_up
            voice "k_w15"
            ka "I like that suggestion. Should we write something on it?"
            $orias.set_state(with_dissolve, mouth="happy", eyes="closed", emotion="note", eyebrows="up")
            ori "Something like... 'Congratulations On Your Copulation' followed by three exclamation marks."
            $kael.set_state(with_dissolve, emotion="sweat", eyebrows="inwards", mouth="smile", eyes="happy")
            ka "How big a cake are we talking about...? We could shorten the writing to um... 'congrats on the sex'?"
            $orias.set_state(with_dissolve,eyes="default", emotion="default", mouth="smile")
            $mirari.set_state(with_dissolve, eyes="happy", mouth="happy")
            show mirari at bounce_up
            voice "m_w33"
            mi "I love it! I have a feeling it'll go successfully for the both of them~" 
            jump akki_sex
        #transition to sex scene

         
        "Kael.":
            if kael_scenes >= 3:
                $kael.set_state( with_dissolve, eyes="closed" )
                "Kael and I exchange looks and he gives an encouraging nod."
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "Kael. If you don't mind someone as inexperienced as me..."
                voice "k_w34"
                show kael zorder 3 at speak
                $kael.set_state(with_dissolve, mouth="smile", eyes= "tender")
                ka "I'd be honored."
                show mirari at sway
                $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="heart")
                voice "m_epi06"
                mi "How wonderful! Kael's very gentle, [claire_name]."
                show orias at bounce_up
                $orias.set_state (with_dissolve, mouth="smile", eyes="closed")
                ori "It will be a good first-time experience."
                show akki at bounce_up
                $akki.set_state (with_dissolve, eyes="happy", mouth ="happy")
                ak "You'll learn a lot from him. (I still do...)"
            else:
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "Then, I choose Kael. Is that okay with you?"
                if akki_scenes >= 3:
                    $akki.set_state(with_dissolve, eyebrows="up", mouth="neutral")
                if mirari_scenes >= 3:
                    $mirari.set_state(with_dissolve, eyebrows="inwards")
                if orias_scenes >= 3:
                    $orias.set_state(with_dissolve, eyebrows="inwards")

                show kael zorder 3 at speak
                $kael.set_state(with_dissolve, mouth="smile", eyes= "tender")
                voice "k_w20"
                ka "Of course it is."
                if akki_scenes >= 3:
                    show mirari at sway
                    $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="heart")
                    voice "m_epi06"
                    mi "How wonderful! Kael's very gentle, [claire_name]."
                    show orias at bounce_up
                    $orias.set_state (with_dissolve, mouth="smile", eyes="closed")
                    ori "It will be a good first-time experience."
                    $akki.set_state(with_dissolve, eyes="closed",mouth="smile", eyebrows="inwards", emotion="sweat" )
                    ak "Can't beat experience..."
                elif mirari_scenes >= 3:
                    show orias at bounce_up
                    $orias.set_state (with_dissolve, mouth="smile", eyes="closed")
                    ori "It will be a good first-time experience."
                    show akki at bounce_up
                    $akki.set_state (with_dissolve, eyes="happy", mouth ="happy")
                    ak "You'll learn a lot from him. (I still do...)"
                    $mirari.set_state (with_dissolve, eyebrows="inwards", emotion="sweat", eyes="closed", mouth="smile")
                    voice "m_s18"
                    mi "He is a good cook after all..."
                elif orias_scenes >= 3:
                    show mirari at sway
                    $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="heart")
                    voice "m_epi06"
                    mi "How wonderful! Kael's very gentle, [claire_name]."
                    show akki at bounce_up
                    $akki.set_state (with_dissolve, eyes="happy", mouth ="happy")
                    ak "You'll learn a lot from him. (I still do...)"
                    $orias.set_state(with_dissolve, eyes="closed", mouth="smile")
                    ori "He would be more compatible..."
                else:    
                    show mirari at sway
                    $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="heart")
                    voice "m_epi06"
                    mi "How wonderful! Kael's very gentle, [claire_name]."
                    show orias at bounce_up
                    $orias.set_state (with_dissolve, mouth="smile", eyes="closed")
                    ori "It will be a good first-time experience."
                    show akki at bounce_up
                    $akki.set_state (with_dissolve, eyes="happy", mouth ="happy")
                    ak "You'll learn a lot from him. (I still do...)"
            $mirari.set_state(with_dissolve, eyes="wink", emotion="default", mouth="smile", eyebrows="default")
            $akki.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="default")
            $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="default")
            show kael at endspeak
            voice "m_s12"
            show mirari at bounce_up
            mi "Then we'll let you two be~"
            show orias at bounce_up
            ori "We'll take our leave, then."
            show akki at bounce_up
            $akki.set_state(with_dissolve, eyes="wink", mouth="grin")
            ak "Later!"
            $claire.set_state(eyes="happy", mouth="happy", eyebrows="default")
            cl "Take care."
            
            #3 leave
            hide orias
            hide mirari
            hide akki
            with moveoutright
            show kael at center with move
            show kael at center_alone2 with dissolve


            $claire.set_state(eyes="tender", mouth="smile", emotion="sweat", eyebrows="inwards")
            cl "..."
            voice "k_w35"
            $kael.set_state(with_dissolve, eyebrows="inwards")
            ka "Nervous?"
            $claire.set_state(eyes="happy")
            cl "A bit..."
            $kael.set_state(with_dissolve, eyes="wink")
            voice "k_s01"
            ka "I don't blame you. Feel free to refreshen up with a shower or whatever you need to do. I'll meet you in the bedroom."
            $claire.set_state(eyes="default", eyebrows="default", emotion="default")
            cl "Sounds good."
            voice "k_w36"
            $kael.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="ah")
            ka "Oh and..."
            $claire.set_state(eyebrows="up", mouth="low")
            cl "Hm?"
            $kael.set_state(with_dissolve,eyes="tender", mouth="smile", emotion="heart")
            voice "k_s12"
            ka "If it gets to that point... would you prefer if I use a condom?"
            $claire.set_state(eyes="dots", emotion_base="large blush", mouth="v", emotion="steam")
            cl "..."
            $kael.set_state(with_dissolve,eyes="happy", eyebrows="inwards", emotion="sweat")
            voice "k_s03"
            ka "I thought it'd be better to discuss this beforehand than during the moment." 
            $claire.set_state(eyes="default", emotion_base="small blush", emotion="default", mouth="uh")
            cl "I see... Do demons usually use condoms?"
            voice "k_s14"
            $kael.set_state(with_dissolve,eyes="default", eyebrows="default", emotion="default")
            ka "For us, we don't need them. We can't get humans pregnant, and we're naturally immune. However, I know partners may want them for aesthetic reasons or it 'feels proper' to them."
            $claire.set_state(eyebrows="flat", mouth="default")
            cl "Then..."
            menu:
                "Yes please.":
                    $ kael_sex_choices.condom = True
                    $claire.set_state(eyes="closed", mouth="uh")
                    cl "Considering how much safe sex ed I've had ingrained into me during high school... I'd feel at ease if you used a condom."
                "We'll be fine.":
                    $ kael_sex_choices.condom = False
                    $claire.set_state(eyes="tender", eyebrows="default", mouth="smile")
                    cl "If it's not needed, then we'll be okay. I trust you, Kael."
            voice "k_w37"    
            $kael.set_state(with_dissolve, eyes="wink")    
            ka "Got it. Thank you."
            $claire.set_state(eyes="happy", emotion="sweat")
            cl "No, thank you for bringing it up. Um, I'll see you after my shower."

            jump kael_sex

                 
        "Orias.":
            if orias_scenes >= 3:
                $orias.set_state(with_dissolve, eyes="side", mouth="default", eyebrows="tender")
                "Orias averts his eyes, not expecting my answer."
                $claire.set_state(eyebrows="default", mouth="smile")
                cl "I... pick Orias."
                $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="oh", emotion="bars")
                $akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="low", emotion="shock")
                $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
                $mirari.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="oh", emotion="shock")
                ori "..."
                $orias.set_state(with_dissolve, emotion="default",emotion_base="small blush", mouth="default")
                $akki.set_state(with_dissolve, mouth="ah", emotion="default")
                $kael.set_state(with_dissolve, emotion="default")
                $mirari.set_state(with_dissolve, emotion="default")
                ak "Wow."
                $kael.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="default")
                voice "k_s03"
                ka "It's rare for him to be picked for their first time."
                $akki.set_state(with_dissolve, mouth="default", eyes="happy", eyebrows="default")
                $mirari.set_state(eyes="happy", mouth="kitty", emotion="note", eyebrows="default")
                $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="smile")
                show mirari at sway
                voice "m_s17"
                mi "Aw, look, he's secretly pleased~"
                $mirari.set_state(with_dissolve, emotion="default", eyes="tender", mouth="default")
                $orias.set_state(with_dissolve, eyes="closed", mouth="oh", emotion="sweat", eyebrows="frown")
                show orias at bounce_up
                ori "A-anyway..."
            else:
                $claire.set_state(eyebrows="flat", mouth="oh", emotion="default", eyes="closed")
                cl "I choose Orias."
                $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="oh", emotion="bars")
                $akki.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="low", emotion="shock")
                $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
                $mirari.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="oh", emotion="shock")
                show orias at bounce_up
                ori "M-me?"
                if akki_scenes >= 3:
                    $orias.set_state(with_dissolve, emotion="default",emotion_base="small blush", mouth="default")
                    $akki.set_state(with_dissolve, mouth="low", emotion="sweat", eyes="dots", eyebrows="inwards")
                    $kael.set_state(with_dissolve, emotion="default", mouth="neutral")
                    $mirari.set_state(with_dissolve, emotion="default",  mouth="neutral")
                    ak "She picked expert mode..."
                    $mirari.set_state(with_dissolve, eyebrows="inwards", mouth="smile", eyes="happy", emotion="sweat")
                    voice "m_s05"
                    mi "You do know what he's into, right?"
                    $kael.set_state(with_dissolve, eyes="default", mouth="smile", eyebrows="inwards", emotion="sweat")
                    voice "k_s12"
                    ka "You feel comfortable with your choice?"
                    $claire.set_state(eyebrows="inwards", mouth="low", eyes="default", emotion="sweat")
                    cl "Was I not supposed to pick Orias?"
                    $mirari.set_state(with_dissolve, mouth="uh", emotion="note", eyebrows="up")
                    voice "m_s15"
                    mi "Oh, it's not that, it's more um... a pleasant surprise."
                elif mirari_scenes >= 3:
                    $orias.set_state(with_dissolve, emotion="default",emotion_base="small blush", mouth="default")
                    $kael.set_state(with_dissolve, emotion="default",  mouth="neutral")
                    $mirari.set_state(with_dissolve, emotion="default", mouth="neutral")
                    $akki.set_state(with_dissolve, eyebrows="default", eyes="default", emotion="sweat", mouth="uhh")
                    ak "You sure?"
                    $kael.set_state(with_dissolve, eyes="default", mouth="smile", eyebrows="inwards", emotion="sweat")
                    voice "k_s12"
                    ka "You feel comfortable with your choice?"
                    $mirari.set_state(with_dissolve, eyes="closed", eyebrows="inwards", emotion="sweat")
                    voice "m_s18"
                    mi "I didn't see that coming..."
                    $claire.set_state( eyebrows="inwards", mouth="low", eyes="default", emotion="sweat")
                    cl "Was I not supposed to pick Orias?"
                    $mirari.set_state(with_dissolve, mouth="uh", emotion="note", eyebrows="up")
                    voice "m_s15"
                    mi "Oh, it's not that, it's more um... a pleasant surprise."
                elif kael_scenes >= 3:
                    $orias.set_state(with_dissolve, emotion="default",emotion_base="small blush", mouth="default")
                    $kael.set_state(with_dissolve, emotion="default",  mouth="neutral")
                    $mirari.set_state(with_dissolve, emotion="default",  mouth="neutral")
                    $akki.set_state(with_dissolve, eyebrows="default", eyes="default", emotion="sweat",mouth="uhh")
                    ak "You sure?"
                    $mirari.set_state(with_dissolve, eyebrows="inwards", mouth="smile", eyes="happy", emotion="sweat")
                    voice "m_s05"
                    mi "You do know what he's into, right?"
                    voice "k_s01"
                    $kael.set_state(with_dissolve, eyes="tender side", eyebrows="inwards", mouth="low", emotion="sweat")
                    ka "Wonder if it's the tea..."
                    $claire.set_state( eyebrows="inwards", mouth="low", eyes="default")
                    cl "Was I not supposed to pick Orias?"
                    $mirari.set_state(with_dissolve, mouth="uh", emotion="note", eyebrows="up")
                    voice "m_s15"
                    mi "Oh, it's not that, it's more um... a pleasant surprise."
                else:
                    $orias.set_state(with_dissolve, emotion="default",emotion_base="small blush", mouth="default")
                    $kael.set_state(with_dissolve, emotion="default", mouth="neutral")
                    $mirari.set_state(with_dissolve, emotion="default", mouth="neutral")
                    $akki.set_state(with_dissolve, eyebrows="default", eyes="default", emotion="sweat", mouth="uhh")
                    ak "You sure?"
                    $mirari.set_state(with_dissolve, eyebrows="inwards", mouth="smile", eyes="happy", emotion="sweat")
                    voice "m_s05"
                    mi "You do know what he's into, right?"
                    $kael.set_state(with_dissolve, eyes="default", mouth="smile", eyebrows="inwards", emotion="sweat")
                    voice "k_s12"
                    ka "You feel comfortable with your choice?"
                    $claire.set_state(eyebrows="inwards", mouth="low", eyes="default", emotion="sweat")
                    cl "Was I not supposed to pick Orias?"
                    $mirari.set_state(with_dissolve, mouth="uh", emotion="note", eyebrows="up")
                    show mirari at bounce_up
                    voice "m_s15"
                    mi "Oh, it's not that, it's more um... a pleasant surprise."
            $mirari.set_state(with_dissolve, **Emotion.normal())
            $orias.set_state(with_dissolve, eyes="side", mouth="oh", eyebrows="tender")
            ori "To be honest, I didn't expect to be a potential suitor, let alone picked."
            $kael.set_state(with_dissolve, **Emotion.normal())
            $akki.set_state(with_dissolve, **Emotion.normal())
            $orias.set_state(with_dissolve, mouth="smile", eyes="default", emotion="default")
            ori "However, thank you. I promise to give you a memorable experience."
            $mirari.set_state(with_dissolve, eyes="happy", mouth="happy")
            voice "m_s12"
            mi "He may seem cold, but he's very sweet. He'll treat you well."
            $kael.set_state(with_dissolve, eyes="happy")
            voice "k_s04"
            ka "I guess it's time to let you two be, then."
            $akki.set_state(with_dissolve, mouth="happy")
            ak "Later, [claire_name]."
            $akki.set_state(with_dissolve, mouth="uh")
            show akki zorder 3 at speak
            ak "Remember, the safeword is 'red' with him."
            $claire.set_state(eyes="dots", eyebrows="up")
            cl "Huh, what?"
            $orias.set_state(with_dissolve, eyebrows="frown", mouth="wavy", eyes="closed")
            show orias at bounce_up
            ori "Please don't say things like that so suddenly. I'll explain later."
            hide mirari
            hide kael
            hide akki
            with moveoutright
            $orias.set_state(**Emotion.normal())
            show orias at center with move
            $claire.set_state(**Emotion.normal())
            $orias.set_state(**Emotion.normal())
            $claire.set_state(eyes="tender side", eyebrows="default", mouth="uh")
            cl "So..."
            show orias at center_alone2 with dissolve
            $orias.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="default")
            ori "Foremost, this would be an opportune time for you to relax and prepare. I highly suggest a bath, considering what I already have planned for tonight."
            $claire.set_state(eyes="happy", emotion_base="small blush", mouth="grin")
            cl "You sure thought this out thoroughly for someone who didn't expect to be picked."
            if orias_scenes >= 3:
                $orias.set_state(with_dissolve, eyebrows="up", mouth="default", eyes="wide")
                ori "..."
                $orias.set_state(with_dissolve, eyebrows="default", mouth="oh", eyes="side", emotion_base = "small blush")
                ori "I had a slim hope you would..."
            else:
                $orias.set_state(with_dissolve, eyebrows="default", mouth="grin", eyes="wink")
                ori "I like being prepared."
            $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="closed", emotion_base = "default")    
            ori "Since you're new to this, everything we'll do will be extremely tame under my usual standards." 
            $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="default", emotion="heart")    
            ori "I promise you can feel safe with me." 
            $claire.set_state(eyes="default", emotion_base="default", mouth="smile")
            cl "Thank you, Orias. I'll take your advice, then. See you in a bit."
            $orias.set_state(with_dissolve, eyebrows="default", mouth="oh", eyes="default", emotion="default")    
            ori "Oh, before I forget... Any allergies I should be aware of?"
            $orias.set_state(with_dissolve, eyebrows="up", mouth="neutral", eyes="wide", emotion="default")    
            $claire.set_state(eyes="happy", emotion="sweat", mouth="ehh")
            cl "Unless you plan to bring bees into the bedroom, I should be okay."
            $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="closed", emotion="default")    
            ori "Heh, duly noted."

            jump orias_sex
                
                
        "Mirari.":
            if mirari_scenes >= 3:
                $mirari.set_state(with_dissolve, eyes="wink", emotion="heart")
                "My eyes dart to Mirari, and she gives me a sly wink, already knowing my answer."
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "I'd like to be with you, Mirari."
                show mirari zorder 3 at bounce_up
                $mirari.set_state(eyes="happy", emotion="flowers", mouth="happy")
                voice "m_w31"
                mi "Yay! I promise we'll have a great time together."
            else:
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "If you're okay with me, Mirari..."
                show mirari at bounce_up
                $mirari.set_state(eyes="happy", emotion="flowers", mouth="smile")
                voice "m_w24"
                mi "Of course, hon."
            if akki_scenes >= 3:
                $kael.set_state(with_dissolve,eyes="happy")
                show kael zorder 3 at bounce_up
                voice "k_w13"
                ka "This is a good arrangement."
                show orias zorder 4
                $orias.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="tender")
                ori "She'll treat you well, [claire_name]."
                $akki.set_state(with_dissolve, eyes="tender side", eyebrows="inwards")
                ak "She does have experience..."
                $akki.set_state(with_dissolve, eyes="happy", mouth="default", eyebrows="default")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                voice "m_s07"
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            elif kael_scenes >= 3:
                show orias zorder 4
                $orias.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="tender")
                ori "She'll treat you well, [claire_name]."
                $kael.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                voice "k_s01"
                ka "So that's your preference..."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                voice "m_s07"
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            elif orias_scenes >= 3:
                $kael.set_state(with_dissolve,eyes="happy")
                show kael zorder 3 at bounce_up
                voice "k_w13"
                ka "This is a good arrangement."
                $orias.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                ori "It'd be more relaxing with Mirari, I admit..."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                voice "m_s07"
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            else:
                $kael.set_state(eyes="happy")
                show kael zorder 3 at bounce_up
                voice "k_w13"
                ka "This is a good arrangement."
                show orias zorder 4
                $orias.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="tender")
                ori "She'll treat you well, [claire_name]."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                voice "m_s07"
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            $orias.set_state(with_dissolve, eyes="default", eyebrows="tender", mouth="smile")
            ori "Then excuse us."
            $kael.set_state(with_dissolve, **Emotion.normal())
            voice "k_w14"
            ka "Take care, [claire_name]."
            $akki.set_state(with_dissolve, eyes="happy", emotion="default", mouth="default", eyebrows="default")
            ak "Later!"
            # 3 gone
            hide orias
            hide kael
            hide akki
            with moveoutright
            $mirari.set_state(eyes="happy", eyebrows="up", mouth="smile", emotion="default", emotion_base="default")
            show mirari at center with move
            "She grabs my hands and holds them up."
            show mirari at center_alone with dissolve
            $mirari.set_state(eyes="wink", emotion="heart")
            voice "m_s12"
            mi "I already planned out the whole thing. I promise you'll love it."
            $claire.set_state(eyes="tender")
            cl "Think so?"
            if mirari_scenes >= 3:
                $mirari.set_state(with_dissolve, eyes="tender", mouth="kitty", eyebrows="up")
                voice "m_s08"
                mi "If you enjoyed my touch when I combed your hair... Well, there's more where that came from."
                $claire.set_state(eyes="clench", emotion_base="large blush")
                cl "..."
            else:
                $mirari.set_state(with_dissolve, eyes="happy")
                mi "Uh-huh. You can just relax with me." 
            $mirari.set_state(with_dissolve, **Emotion.normal())
            mi "I'll be making preparations in your room, so take a bath or whatever that'll help you feel refreshed." 
            $claire.set_state(eyes="happy", emotion_base="small blush", eyebrows="default")
            cl "Thank you."

            jump mirari_sex
                        
                
        "None of them.":

            $claire.set_state(eyes="closed", eyebrows="inwards", emotion="sweat", mouth="default")
            cl "I'm sorry but... I'd like to decline the offer."
            $claire.set_state(with_dissolve, eyes="tender side", emotion_base="default")
            cl "I don't think I'm ready for sex quite yet." 
            $kael.set_state(eyes="happy")
            $mirari.set_state(eyebrows="inwards")
            $akki.set_state(eyebrows="inwards")
            $orias.set_state(eyebrows="tender")
            show kael zorder 3 at speak
            voice "k_sex07"
            ka "We understand. None of us would want you to feel pressured or uncomfortable."
            $claire.set_state(emotion="default", eyes="bug cry", mouth="low")
            cl "I'm sorry. You guys have been good to me. You've made me feel like a guest in my own home. You've fed me, helped me with chores and I can't return the favour..."
            $kael.set_state(eyes="default")
            show kael zorder 0 at endspeak
            $mirari.set_state(eyes="clench", mouth="kissy")
            show mirari zorder 3 at speak
            voice "m_s17"
            mi "Aw, sweetie, it's okay. This is your body and wellbeing we're talking about here."
            "She steps in and gives me a hug."
            $mirari.set_state(with_dissolve, eyes="closed", mouth="default")
            voice "m_s07"
            mi "Thank you for your honesty; that's all we can ask for."
            $mirari.set_state(eyes="default")
            show mirari zorder 0 at endspeak
            $kael.set_state(eyes="closed", mouth="default", eyebrows="inwards", emotion="sweat")
            show kael zorder 3 at speak
            voice "k_s14"
            ka "We did... drop in suddenly after all. I apologize for the trouble we put you through."
            $claire.set_state(eyes="clench", emotion="panic", mouth="oh")
            cl "It wasn't any trouble at all. I enjoyed your company."
            $kael.set_state(**Emotion.normal())
            show kael zorder 0 at endspeak
            $orias.set_state(eyes="side", eyebrows="up")
            show orias zorder 3 at speak
            ori "Although it does beg the question... What should we do in the meantime? Should we simply leave?"
            $orias.set_state(**Emotion.normal())
            show orias zorder 0 at endspeak
            $akki.set_state(eyes="closed", eyebrows="frown", mouth="low")
            show akki zorder 3 at speak
            ak "..."
            $akki.set_state(with_dissolve, emotion="starry", eyes="wink", eyebrows="default", mouth="happy")
            stop music fadeout 2
            ak "I have an idea." 
            #transition to Mario Kart chibi
            scene black with dissolve
            play sound "assets/sfx/rev_up.ogg"
            pause(1.0)
            scene nosex01 with dissolve
            $ gallery.unlock("chibi_nosex01")
            play music music_silly fadein 2
            ak "AW YEA FIRST PLACE! Last lap here I come!"
            cla "Ugh, how did you improve so fast? I'm right behind you, Akki."
            play sound "assets/sfx/race_start.ogg"
            ori "Mirari, you're going the wrong way again."
            voice "m_s13"
            mi "I-I knew that! I was taking a shortcut!"
            voice "k_s02"
            ka "At least you can see where you're going... I can't seem to get away from this wall."
            cla "B, hit B, Kael."
            voice "k_s09"
            ka "B...? What is this— Ooh, I'm going backwards!"
            play sound "assets/sfx/screeches.ogg"
            voice "k_s05"
            ka "Well now I fell off a cliff, but at least I can see in front again!" 
            voice "m_w31"
            mi "Yaaay, I finally hit one of those item thingies!"
            mi "What does this blue shell do?"
            ak "It does nothing, don't use it."
            cla "LAUNCH IT, LAUNCH IT NOW."
            voice "m_s11"
            mi "How do I do that? I'm hitting every—"
            ori "This one."
            mi "Oh!"
            scene nosex02 with dissolve
            $ gallery.unlock("chibi_nosex02")
            play sound "assets/sfx/ded.ogg"
            ak "NOOOOOOO!"
            cla "First place is mine! Hahaha!"
            ak "Best two out of three!"
            "I ended up not having sex after all, but I still had a memorable spring break..."
            jump credits
                
        "All of them." if everybody_sex :
            #[TODO]
            #---------- ADD SPRITE MOVEMENT-------------------------
            $claire.set_state(emotion="sweat", eyes="happy", mouth="grin", emotion_base="default", eyebrows ="inwards")
            cl "This is going to sound crazy but I pick all of you."
            stop music
            play sound "assets/sfx/scratch.ogg"
            $akki.set_state(with_dissolve,emotion="shock", eyes="wide", mouth="ah", emotion_base="default", eyebrows ="up")
            $mirari.set_state(with_dissolve,emotion="default", eyes="wide", mouth="oh", emotion_base="default", eyebrows ="up")
            $kael.set_state(with_dissolve,emotion="default", eyes="wide", mouth="low", emotion_base="default", eyebrows ="up")
            $orias.set_state(with_dissolve,emotion="default", eyes="wide", mouth="low", emotion_base="default", eyebrows ="up")
            mi "A-all of us!?"
            play music music_love fadein 3
            $kael.set_state(with_dissolve,emotion="default", eyes="default", mouth="ah", emotion_base="default", eyebrows ="default")
            ka "Like... a giant orgy?"
            $mirari.set_state(with_dissolve,emotion="default", eyes="default", mouth="default", emotion_base="default", eyebrows ="default")
            $kael.set_state(with_dissolve,emotion="default", eyes="default", mouth="low", emotion_base="default", eyebrows ="default")
            $akki.set_state(with_dissolve,emotion="default", eyes="tender side", mouth="wavy", emotion_base="small blush", eyebrows ="tender")
            $orias.set_state(with_dissolve,emotion="default", eyes="side", mouth="oh", emotion_base="default", eyebrows ="default")
            ori "This is quite the request..." 
            $akki.set_state(with_dissolve,emotion="default", eyes="default", mouth="oh", emotion_base="small blush", eyebrows ="up")
            $orias.set_state(with_dissolve, mouth="default")
            ak "You sure?"
            $akki.set_state(with_dissolve,emotion="default", eyes="default", mouth="default", emotion_base="default", eyebrows ="default")
            $claire.set_state(emotion="default", eyes="default", mouth="grin", emotion_base="small blush", eyebrows ="default")
            cl "Definitely. I trust you guys."
            $kael.set_state(with_dissolve,mouth="smile")
            $mirari.set_state(with_dissolve,emotion="flowers", eyes="happy", mouth="happy", emotion_base="small blush", eyebrows ="up")
            voice "m_s12"
            show mirari zorder 3 at bounce_up
            mi "Why not, sounds like fun!"
            $kael.set_state(with_dissolve,emotion="default", eyes="happy", mouth="smile", emotion_base="default", eyebrows ="default")
            show mirari zorder 0
            show kael zorder 3 at sway
            ka "I haven't participated in one in a long time..."
            $mirari.set_state(with_dissolve,emotion="default")
            $orias.set_state(with_dissolve,emotion="default", eyes="closed", mouth="smile", emotion_base="default", eyebrows ="tender")
            show kael zorder 0
            show orias zorder 3 at bounce_up
            ori "It has been ages..."
            $orias.set_state(with_dissolve,emotion="default", eyes="default", mouth="default", emotion_base="default", eyebrows ="default")
            $mirari.set_state(with_dissolve,emotion="default", eyes="default", mouth="uh", emotion_base="default", eyebrows ="inwards")
            voice "m_s09"
            show orias zorder 0
            show mirari zorder 3 at speak
            mi "It's strange, I pegged you for a virgin but... I feel there's something about you, [claire_name]..."
            $mirari.set_state(with_dissolve,mouth = "default")
            $kael.set_state(with_dissolve,emotion="default", eyes="default", mouth="ah", emotion_base="default", eyebrows ="one up")
            show mirari zorder 0 at endspeak
            show kael zorder 3 at speak
            ka "Are you sure you haven't experienced sex before?"
            $claire.set_state(emotion="sweat", eyes="happy", mouth="ehh", emotion_base="default", eyebrows ="default")
            cl "Hehe... it's a little complicated to explain."
            $mirari.set_state(with_dissolve,emotion="heart", eyes="happy", mouth="grin", emotion_base="default", eyebrows ="default")
            $kael.set_state(with_dissolve,emotion="default", eyes="default", mouth="smile", emotion_base="default", eyebrows ="default")
            voice "m_s08"
            show kael zorder 0 at endspeak
            show mirari zorder 3 at bounce_up
            mi "No matter. We'll go easy on you just the same. And Akki."
            $akki.set_state(with_dissolve,emotion="default", eyes="clench", mouth="ah", emotion_base="small blush", eyebrows ="up")
            show mirari zorder 0
            show akki zorder 3 at speak
            ak "H-hey, you don't need to worry about me. Let's go, [claire_name]."
            $claire.set_state(emotion="default", eyes="happy", mouth="happy", emotion_base="small blush", eyebrows ="default")
            cl "Okay!"
            hide mirari
            hide orias
            hide kael
            hide akki 
            with dissolve
            show group at panpan with dissolve
            "..."
            "And then we had mind-blowing sex."
            jump credits
           #silly 'everyone sleeping in bed' picture then credits I guess?
                

