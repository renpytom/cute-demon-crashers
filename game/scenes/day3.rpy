# label day3_morning:
#     jump choose_a_place_to_hangout

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
    mi "Remember, the portal closes around midnight, so it should give you plenty of time with whoever you pick." 
    $mirari.set_state(eyes="default")
    show mirari zorder 0 at endspeak
    $kael.set_state(eyes="wink")
    show kael zorder 3 at speak
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
                    mi "Aw, but it's probably for the best."
                    show kael zorder 3
                    $kael.set_state(with_dissolve,eyes="closed")
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
                    ka "Ah, can't be helped..."
                elif orias_scenes >= 3:
                    $mirari.set_state(eyes="happy", emotion="note")
                    show mirari at bounce_up
                    mi "How wonderful!"
                    show kael zorder 3
                    $kael.set_state(with_dissolve, eyes="closed")
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
            mi "Already bridal carrying her to the bedroom! How passionate."
            $kael.set_state(with_dissolve, emotion="sweat", eyebrows="inwards", mouth="grin", eyes="happy")
            ka "So much for not getting too excited."
            $orias.set_state(with_dissolve, mouth="smile", eyebrows="tender", eyes="default")
            ori "Still, this will be a good experience. He would need to be nourished sooner or later, and it's ideal it's happening now."
            $kael.set_state(with_dissolve, **Emotion.normal())
            ka "And with someone he's comfortable with."
            $mirari.set_state(mouth="vhappy", emotion="flowers")
            show mirari at bounce_up
            mi "We should find a way to celebrate when he gets back! I say we bake a cake!"
            $kael.set_state(mouth="happy", eyes="happy", emotion="note")
            show kael at bounce_up
            ka "I like that suggestion. Should we write something on it?"
            $orias.set_state(with_dissolve, mouth="happy", eyes="closed", emotion="note", eyebrows="up")
            ori "Something like... 'Congratulations On Your Copulation' followed by three exclamation marks."
            $kael.set_state(with_dissolve, emotion="sweat", eyebrows="inwards", mouth="smile", eyes="happy")
            ka "How big a cake are we talking about...? We could shorten the writing to um... 'congrats on the sex'?"
            $orias.set_state(with_dissolve,eyes="default", emotion="default", mouth="smile")
            $mirari.set_state(with_dissolve, eyes="happy", mouth="happy")
            show mirari at bounce_up
            mi "I love it! I have a feeling it'll go successfully for the both of them~" 
            jump akki_sex
        #transition to sex scene
               
        # "Kael.":
        #     if kael_scenes >= 3:
        #         "Kael and I exchange looks and he gives an encouraging nod."
        #         cl "Kael. If you don't mind someone as inexperienced as me..."
        #         ka "I'd be honored."
        #     else:
        #         cl "Then, I choose Kael. Is that okay with you?"
        #         ka "Of course it is."
        #         if akki_scenes >= 3:
        #             mi "How wonderful! Kael's very gentle, [claire_name]."
        #             ori "It will be a good first-time experience."
        #             ak "Can't beat experience..."
        #         if mirari_scenes >= 3:
        #             ori "It will be a good first-time experience."
        #             ak "You'll learn a lot from him. (I still do...)"
        #             mi "He is a good cook after all..."
        #         if orias_scenes >= 3:
        #             mi "How wonderful! Kael's very gentle, [claire_name]."
        #             ak "You'll learn a lot from him. (I still do...)"
        #             ori "He would be more compatible..."
        #         else:    
        #             mi "How wonderful! Kael's very gentle, [claire_name]."
        #             ori "It will be a good first-time experience."
        #             ak "You'll learn a lot from him. (I still do...)"
        #     mi "Then we'll let you two be~"
        #     ori "We'll take our leave, then."
        #     ak "Later!"
        #     cl "Take care."
        #     #3 leave
        #     cl "..."
        #     ka "Nervous?"
        #     cl "A bit..."
        #     ka "I don't blame you. Feel free to refreshen up with a shower or whatever you need to do. I'll meet you in the bedroom."
        #     cl "Sounds good."
        #     ka "Oh and..."
        #     cl "Hm?"
        #     ka "If it gets to that point... would you prefer if I use a condom?"
        #     cl "..."
        #     ka "I thought it'd be better to discuss this beforehand than during the moment." 
        #     cl "I see... Do demons usually use condoms?"
        #     ka "For us, we don't need them. We can't get humans pregnant, and we're naturally immune. However, I know partners may want them for aesthetic reasons or it 'feels proper' to them."
        #     cl "Then..."
        #     menu:
        #         "Yes please.":
        #             $ kael_sex_choices.condom = True
        #             cl "Considering how much safe sex ed I've had ingrained into me during high school... I'd feel at ease if you used a condom."
        #         "We'll be fine.":
        #             $ kael_sex_choices.condom = False
        #             cl "If it's not needed, then we'll be okay. I trust you, Kael."
        #     ka "Got it. Thank you."
        #     cl "No, thank you for bringing it up. Um, I'll see you after my shower."

        #     jump kael_sex

                 
        # "Orias.":
        #     if orias_scenes >= 3:
        #         "Orias averts his eyes, not expecting my answer."
        #         cl "I... pick Orias."
        #         ori "..."
        #         ak "Wow."
        #         ka "It's rare for him to be picked for their first time."
        #         mi "Aw, look, he's secretly pleased~"
        #         ori "A-anyway..."
        #     else:
        #         cl "I choose Orias."
        #         ori "M-me?"
        #         if akki_scenes >= 3:
        #             ak "She picked expert mode..."
        #             mi "You do know what he's into, right?"
        #             ka "You feel comfortable with your choice?"
        #             cl "Was I not supposed to pick Orias?"
        #             mi "Oh, it's not that, it's more um... a pleasant surprise."
        #         if mirari_scenes >= 3:
        #             ak "You sure?"
        #             ka "You feel comfortable with your choice?"
        #             mi "I didn't see that coming..."
        #             cl "Was I not supposed to pick Orias?"
        #             mi "Oh, it's not that, it's more um... a pleasant surprise."
        #         if kael_scenes >= 3:
        #             ak "You sure?"
        #             mi "You do know what he's into, right?"
        #             ka "Wonder if it's the tea..."
        #             cl "Was I not supposed to pick Orias?"
        #             mi "Oh, it's not that, it's more um... a pleasant surprise."
        #         else:
        #             ak "You sure?"
        #             mi "You do know what he's into, right?"
        #             ka "You feel comfortable with your choice?"
        #             cl "Was I not supposed to pick Orias?"
        #             mi "Oh, it's not that, it's more um... a pleasant surprise."
        #     ori "To be honest, I didn't expect to be a potential suitor, let alone picked."
        #     ori "However, thank you. I promise to give you a memorable experience."
        #     mi "He may seem cold, but he's very sweet. He'll treat you well."
        #     ka "I guess it's time to let you two be, then."
        #     ak "Later, [claire_name]."
        #     ak "Remember, the safeword is 'red' with him."
        #     cl "Huh, what?"
        #     ori "Please don't say things like that so suddenly. I'll explain later."
        #     # 3 leave
        #     cl "So..."
        #     ori "Foremost, this would be an opportune time for you to relax and prepare. I highly suggest a bath, considering what I already have planned for tonight."
        #     cl "You sure thought this out thoroughly for someone who didn't expect to be picked."
        #     if orias_scenes >= 3:
        #         ori "..."
        #         ori "I had a slim hope you would..."
        #     else:
        #         ori "I like being prepared."
        #     ori "Since you're new to this, everything we'll do will be extremely tame under my usual standards." 
        #     ori "I promise you can feel safe with me." 
        #     cl "Thank you, Orias. I'll take your advice, then. See you in a bit."
        #     ori "Oh, before I forget... Any allergies I should be aware of?"
        #     cl "Unless you plan to bring bees into the bedroom, I should be okay."
        #     ori "Heh, duly noted."

        #     jump orias_sex
                
                
        "Mirari.":
            if mirari_scenes >= 3:
                $mirari.set_state(with_dissolve, eyes="wink", emotion="heart")
                "My eyes dart to Mirari, and she gives me a sly wink, already knowing my answer."
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "I'd like to be with you, Mirari."
                show mirari zorder 3 at bounce_up
                $mirari.set_state(eyes="happy", emotion="flowers", mouth="happy")
                mi "Yay! I promise we'll have a great time together."
            else:
                $claire.set_state(eyebrows="inwards", mouth="smile")
                cl "If you're okay with me, Mirari..."
                show mirari at bounce_up
                $mirari.set_state(eyes="happy", emotion="flowers", mouth="smile")
                mi "Of course, hon."
            if akki_scenes >= 3:
                $kael.set_state(with_dissolve,eyes="happy")
                show kael zorder 3 at bounce_up
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
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            elif kael_scenes >= 3:
                show orias zorder 4
                $orias.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="tender")
                ori "She'll treat you well, [claire_name]."
                $kael.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                ka "So that's your preference..."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            elif orias_scenes >= 3:
                $kael.set_state(with_dissolve,eyes="happy")
                show kael zorder 3 at bounce_up
                ka "This is a good arrangement."
                $orias.set_state(with_dissolve, eyebrows="inwards", eyes="closed")
                ori "It'd be more relaxing with Mirari, I admit..."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            else:
                $kael.set_state(eyes="happy")
                show kael zorder 3 at bounce_up
                ka "This is a good arrangement."
                show orias zorder 4
                $orias.set_state(with_dissolve, eyes="closed", mouth="smile", eyebrows="tender")
                ori "She'll treat you well, [claire_name]."
                $akki.set_state(eyes="happy", mouth="grin")
                show akki zorder 4 at bounce_up
                ak "Mirari can be surprisingly gentle when she's not punching things."
                $mirari.set_state(emotion_base="dark",emotion="vein", mouth="fun smile", eyebrows="default")
                show mirari at sway
                mi "I heard that, Akki~"
                $akki.set_state(with_dissolve, emotion="panic", eyes="wide", mouth="ehh", eyebrows="up")
                ak "T-that's our cue to give you two privacy now."
            $orias.set_state(with_dissolve, eyes="default", eyebrows="tender", mouth="smile")
            ori "Then excuse us."
            $kael.set_state(with_dissolve, **Emotion.normal())
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
            mi "I already planned out the whole thing. I promise you'll love it."
            $claire.set_state(eyes="tender")
            cl "Think so?"
            if mirari_scenes >= 3:
                $mirari.set_state(with_dissolve, eyes="tender", mouth="kitty", eyebrows="up")
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
            ka "We understand. None of us would want you to feel pressured or uncomfortable."
            $claire.set_state(emotion="default", eyes="bug cry", mouth="low")
            cl "I'm sorry. You guys have been good to me. You've made me feel like a guest in my own home. You've fed me, helped me with chores and I can't return the favour..."
            $kael.set_state(eyes="default")
            show kael zorder 0 at endspeak
            $mirari.set_state(eyes="clench", mouth="kissy")
            show mirari zorder 3 at speak
            mi "Aw, sweetie, it's okay. This is your body and wellbeing we're talking about here."
            "She steps in and gives me a hug."
            $mirari.set_state(with_dissolve, eyes="closed", mouth="default")
            mi "Thank you for your honesty; that's all we can ask for."
            $mirari.set_state(eyes="default")
            show mirari zorder 0 at endspeak
            $kael.set_state(eyes="closed", mouth="default", eyebrows="inwards", emotion="sweat")
            show kael zorder 3 at speak
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
            play music music_silly fadein 2
            ak "AW YEA FIRST PLACE! Last lap here I come!"
            cla "Ugh, how did you improve so fast? I'm right behind you, Akki."
            play sound "assets/sfx/race_start.ogg"
            ori "Mirari, you're going the wrong way again."
            mi "I-I knew that! I was taking a shortcut!"
            ka "At least you can see where you're going... I can't seem to get away from this wall."
            cla "B, hit B, Kael."
            ka "B...? What is this— Ooh, I'm going backwards!"
            play sound "assets/sfx/screeches.ogg"
            ka "Well now I fell off a cliff, but at least I can see in front again!" 
            mi "Yaaay, I finally hit one of those item thingies!"
            mi "What does this blue shell do?"
            ak "It does nothing, don't use it."
            cla "LAUNCH IT, LAUNCH IT NOW."
            mi "How do I do that? I'm hitting every—"
            ori "This one."
            mi "Oh!"
            scene nosex02 with dissolve
            play sound "assets/sfx/ded.ogg"
            ak "NOOOOOOO!"
            cla "First place is mine! Hahaha!"
            ak "Best two out of three!"
            "I ended up not having sex after all, but I still had a memorable spring break..."
            jump credits
                
        #"All of them." if persistent.sexcomplete:
        #   cl "This is going to sound crazy but I pick all of you."
        #   mi "A-all of us!?"
        #    ka "Like... a giant orgy?"
        #    ori "This is quite the request..." 
        #    ak "You sure?"
        #    cl "Definitely. I trust you guys."
        #    mi "Why not, sounds like fun!"
        #    ka "I haven't participated in one in a long time..."
        #    ori "It has been ages..."
        #    mi "It's strange, I pegged you for a virgin but... I feel there's something about you, [claire_name]..."
        #    ka "Are you sure you haven't experienced sex before?"
        #    cl "Hehe... it's a little complicated to explain."
        #    mi "No matter. However, we'll go easy on you just the same. And Akki."
        #    ak "H-hey, you don't need to worry about me. Let's go, [claire_name]."
        #    cl "Okay!"
        #    "And then we had mind-blowing sex."
        #    #silly 'everyone sleeping in bed' picture then credits I guess?
                

