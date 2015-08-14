#CG variables
define mira_epilong = False




label mirari_hangout1:
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    play music music_mirari
    $renpy.pause(0.4)
    $claire.set_state(**Emotion.normal())
    $mirari.set_state(**Emotion.normal())
    scene bg garden with dissolve
    play music music_mirari

    cl "Will Mirari be all right in the garden...?"
    voice "m_s09"
    "Scanning the backyard, I hear faint humming and I spot Mirari watering the flowers near the fence."
    show mirari at center_alone with dissolve
    $claire.set_state(eyebrows="up", mouth="uh")
    cl "Are you taking care of them?"
    $mirari.set_state(eyes="happy", emotion="note")
    show mirari at bounce_up_alone
    voice "m_w08"
    mi "Oh, hi, [claire_name]! And yes. The poor things were nearly wilting."
    "She reaches into her barely-there shirt and pulls out a memo. I accept it and recognize the handwriting."
    "'I want my garden alive when I return. Love, Dad.'" 
    $claire.set_state(eyebrows="inwards", emotion="lll", eyes="flat", emotion_base="dark", mouth="ehh")
    cl "Ah... Yeah, I sorta forgot about that..."
    $mirari.set_state(with_dissolve, eyes="default", emotion="default", mouth="happy")
    voice "m_s01"
    mi "I can take care of that while I'm here; I love being outside."
    "I glance over at the fence."
    $claire.set_state(eyebrows="inwards", eyes="default", mouth="oh", emotion_base="default", emotion="sweat")
    cl "Um, have the neighbors noticed you? Did they question you?"
    $mirari.set_state(eyes="wink", mouth="smile", emotion="note")
    show mirari at bounce_up_alone
    voice "m_s08"
    mi "Oh yes, but I told them I was a 'cause-player' and they ate it right up! Teehee, I fooled them good, so my identity is safe~"
    $claire.set_state(eyes="happy", mouth="smile")
    cl "..."
    $mirari.set_state(with_dissolve, eyes="default", eyebrows="inwards", mouth="oh", emotion="default")
    voice "m_w09"
    mi "You okay, hon?"
    $claire.set_state(eyes="default", mouth="low")
    cl "Can I ask you a question? Um, why me?"
    voice "m_s15"
    $mirari.set_state(with_dissolve, mouth="uh", eyebrows="up")
    mi "You mean how I found you?"
    $claire.set_state(eyes="happy", mouth="smile")
    cl "That, too."
    stop music fadeout 1
    $mirari.set_state(eyes="happy", mouth="smile", emotion="flowers")
    voice "m_w10"
    mi "Your scent of course."
    $claire.set_state(eyebrows="up", mouth="uh", eyes="default", emotion="default")
    play music music_silly fadein 1
    cl "Huh?"
    $mirari.set_state(with_dissolve,eyes="wink", emotion="note")
    voice "m_s09"
    mi "We can detect when a human is releasing sexual energy. I was on my usual hunt when I sensed you and went to investigate." 
    $claire.set_state(emotion_base="large blush",eyes="wide", mouth="low")
    cl "..."
    $mirari.set_state(eyes="happy", emotion="heart", mouth="happy")
    show mirari at sway
    voice "m_s10"
    mi "You have a really delicious smell~" 
    $claire.set_state(emotion="steam", eyes="big")
    cl "...."
    $claire.set_state(emotion="panic", eyes="clench", mouth="fun ah2")
    stop music fadeout 1
    cl "Oh my god, how embarrassing."
    play music music_mirari fadein 3
    $mirari.set_state(with_dissolve,emotion="default", eyebrows="inwards", mouth="smile", eyes="default")
    voice "m_w11"
    mi "Don't be! It's something only we sex demons can pick up. Not only that, that was when I heard you wishing you could experience a fling. I thought I could help you out."
    $mirari.set_state(with_dissolve,eyes="happy", emotion="sweat")
    mi "I created the portal so the others could arrive and here we are! I'm sorry we startled you." 
    $mirari.set_state(with_dissolve, eyes="default")
    mi "Thanks for not siccing the police on us; it's been a reoccurring event in recent decades."
    $claire.set_state(emotion="sweat", eyes="happy", emotion_base="default", eyebrows="inwards", mouth="smile")
    cl "It was a huge shock but I see there's good intentions behind your visit. It's kind of you to offer, even if I can't promise I'll even take up on it."
    $mirari.set_state(with_dissolve, emotion="default", mouth="neutral")
    voice "m_w12"
    mi "That's fine! No pressure. You do seem a little insecure about sex in general."
    $claire.set_state(eyes="down", mouth="low", emotion="default", emotion_base="small blush")
    cl "Ah, yeah... On one hand I'd like to experience sex, but I don't want to get intimate with just anyone."
    $claire.set_state(with_dissolve, eyes="tender", mouth="oh")
    cl "I'm not even talking about the 'true love' thing. Just someone who'd care and treat me well, if that makes sense?"
    $mirari.set_state(emotion="default", mouth="smile", eyes="happy", eyebrows="up")
    show mirari at bounce_up_alone
    voice "m_s14"
    mi "It does! Incubi and succubi can't form romantic relationships like you humans can – it's our nature after all – but we can still develop deep bonds with others. It's more akin to a friendship or attachment."
    $mirari.set_state(with_dissolve, eyes="tender")
    mi "Whoever you choose, I promise they'd treat you kindly and make sure you're happy and secure." 
    voice "m_s10"
    $mirari.set_state(with_dissolve, eyes="wink", emotion="note", eyebrows="default", mouth="happy")
    mi "Hehe, after all, we get our nourishment from positive sexual energy. It doesn't do anything if our lover is unhappy, and we like making them feel good." 
    $mirari.set_state(with_dissolve, eyes="happy", emotion="default", eyebrows="up")
    mi "Does that clear everything up for you?"
    $claire.set_state(emotion="default", eyes="happy", mouth="happy", eyebrows="default", emotion_base="default")
    cl "It does, thank you, Mirari." 
    $mirari.set_state(with_dissolve, emotion="default", eyes="happy", mouth="default")
    voice "m_w13"
    mi "Anytime~" 
    stop music fadeout 2
    jump next_day
    


label mirari_hangout2:
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    play music music_mirari
    $renpy.pause(0.4)
    $mirari.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    scene bg garden with dissolve
    $mirari.set_state(mouth="happy", eyebrows="up", emotion="bars")
    show mirari at center_alone with dissolve
    show mirari at bounce_up_alone
    voice "m_w16"
    mi "[claire_name]! [claire_name]! Would you like to play a game with me?"
    $claire.set_state(mouth="smile")
    cl "A game? Sure, what is it?"
    $claire.set_state(with_dissolve, eyes="happy", eyebrows="inwards", mouth="ehh", emotion="sweat")
    cl "I hope it's not strip poker."
    $mirari.set_state(with_dissolve, emotion="sweat", eyes="happy", eyebrows="inwards")
    voice "m_s05"
    mi "Haha, if it was, I'd already be at a huge disadvantage."
    $mirari.set_state(with_dissolve, **Emotion.normal())
    mi "It's the newest game that's all the rage! Or was... I can't keep track of human time."
    "She points to a board game with various pegs and holes in the wood. We take a seat around the low table."
    $mirari.set_state(mouth="happy", emotion="note", eyebrows="up")
    show mirari at bounce_up_alone
    voice "m_s01"
    mi "Have you played Mastermind?"
    $claire.set_state(mouth="smile", emotion_base="dark")  
    cl "(This looks like a board game older than I am...)"
    $claire.set_state(eyes="default", emotion_base="default", eyebrows="default", emotion="default")  
    cl "No. How does this work?"
    $mirari.set_state(with_dissolve, eyes="happy", emotion="default")
    voice "m_s15"
    mi "You gotta break the code! You need to guess the pattern the codemaker created by placing coloured pegs in a row. You get ten tries to break the code."
    $claire.set_state(mouth="uh", eyebrows="up")
    cl "And how will I know I'm on the right track?"
    $mirari.set_state(eyes="wink", mouth="smile")
    show mirari at bounce_up_alone
    voice "m_s10"
    mi "From my feedback. A red key indicates you got a correct colored peg in the correct position. A white one is a correct color but in an incorrect spot. Bah, explaining is hard, you'll learn as you go."
    $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="note")
    voice "m_w17"
    mi "Let's start! Create your code, [claire_name]."
    $claire.set_state(eyebrows="frown", mouth="smile", emotion="note")
    cl "Okay... Let's see..."
    hide mirari with dissolve
    show mastermind at chibi_scene with dissolve
    "Orange, white, black, brown. Sure, why not. Once we finish, it's my first turn to guess her code."
    #all white pegs
    show mmturn_1 at chibi_scene with dissolve
    $claire.set_state(emotion="default", mouth="uh")
    cl "There."
    voice "m_s10"
    mi "Haha, you play like Akki. No pegs, dear."
    $claire.set_state(with_dissolve, mouth="default", eyes="semi open")
    cl "So no white at all..." 
    show mmturn_2 at chibi_scene with dissolve
    show mmscore_2 at chibi_scene with dissolve

    "Mirari must possess extreme luck since she nails two of my pegs correctly. Well, the game doesn't point out {i}which{/i} are correct, so she still needs to figure it out."
    show mmturn_3 at chibi_scene with dissolve
    show mmturn_4 at chibi_scene 
    show mmscore_4 at chibi_scene 
    show mmturn_5 at chibi_scene 
    with dissolve
    show mastermind mid with dissolve
    "We continue playing. She decodes mine on the fifth turn."
    hide mmturn_1
    hide mmturn_2
    hide mmturn_3
    hide mmturn_4
    hide mmturn_5
    hide mmscore_4
    hide mmscore_2
    with None

    hide mastermind mid with dissolve
    show mirari at center_alone with dissolve
    show mirari at bounce_up_alone
    ##Oh gee, I wasn't following before but are they playing as codemaker and breaker at once? Is... is that how you play?
    voice "m_w18"
    mi "I win! But you still have five chances to guess mine."
    "And I only found one correct colour! While I strain my brain, she gets up to tend to the flowers."
    hide mirari with dissolve
    $claire.set_state(mouth="wavy", eyes="clench")
    cl "(She's watering the flowers while waiting on me!? Come on, think. Use your shivered up brain cells, [claire_name].)"
    show mastermind mid at chibi_scene
    with dissolve
    show mmturn_11 at chibi_scene with dissolve
    $claire.set_state(mouth="oh", eyes="default", eyebrows="up")
    cl "Are there similar flowers in the demon world?"
    #6th guess
    "She returns to her seat and rejoins the game."
    show mmscore_11 at chibi_scene with dissolve
    mi "A few. Earth flowers are nice because they don't fight back or try to eat the house in a day. It's a relaxing change of pace, but it can get boring."
    show mmturn_12 at chibi_scene with dissolve
    $claire.set_state(mouth="uhh", eyes="flat", eyebrows="flat", emotion="sweat")
    cl "If, uh, the flowers in your world are rather feisty, why do you grow them?"
    show mmscore_12 at chibi_scene with dissolve

    #7th guess
    voice "m_s10"
    mi "I love a challenge! Plus some of them are useful and can be harvested"
    show mmturn_13 at chibi_scene with dissolve
    mi "Orias and I formed a little partnership surrounding that. I punch the flowers into submission and he brews a lovely cup from them." 
    show mmscore_13 at chibi_scene with dissolve
    #8th guess
    #$claire.set_state(mouth="oh", eyes="dots", eyebrows="up", emotion="default")
    show chibi_mira02 at chibi_scene with dissolve
    $ gallery.unlock("chibi_mira02")
    cla "...Interesting." 
    voice "m_w19"
    mi "They are! Would you like me to bring a flower from our world for you as a gift?"
    hide chibi_mira02 with dissolve
    show mmturn_14 at chibi_scene with dissolve
    $claire.set_state(mouth="smile", eyes="happy", eyebrows="inwards", emotion_base="dark", emotion="sweat")
    cl "No, it's okay. It'll be hard to explain to my parents why there's a rose bush devouring their fence."
    show mmscore_14 at chibi_scene with dissolve
    $claire.set_state(mouth="wavy", eyes="clench", eyebrows="frown", emotion_base="default")
    cl "Arg, this game is hard as well!"
    voice "m_s14"
    mi "You're almost there."
    #9th guess
    $claire.set_state(mouth="oh", eyebrows="up", emotion="default", eyes="wide")
    cl "Wait... I got it!"
    show mmturn_15 at chibi_scene with dissolve
    #10th guess
    show mmscore_15 at chibi_scene with dissolve
    show mastermind end with dissolve
    hide mmturn_11
    hide mmturn_12
    hide mmturn_13
    hide mmturn_14
    hide mmturn_15
    hide mmscore_11
    hide mmscore_12
    hide mmscore_13
    hide mmscore_14
    hide mmscore_15
    voice "m_w20"
    mi "Wow, you cracked the code. Congratulations!"
    hide mastermind with dissolve
    $mirari.set_state(emotion="default")
    show mirari at center_alone with dissolve
    $claire.set_state(emotion="sigh", eyes="flat", mouth="uhh", eyebrows="inwards")
    cl "Phew. I feel I pulled a brain muscle there." 
    $mirari.set_state(with_dissolve, **Emotion.normal())
    voice "m_s10"
    mi "Would you like to play again?"
    $claire.set_state(emotion_base="default", emotion="default", eyes="happy", mouth="smile", eyebrows="default")
    cl "Maybe later. Thanks though, it was fun!"
    $mirari.set_state(with_dissolve, eyes="happy")
    voice "m_w13"
    mi "Anytime."
    stop music fadeout 2
    jump next_day


label mirari_hangout3:
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    play music music_mirari
    $renpy.pause(0.4)
    $mirari.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    scene bg garden with dissolve

    $claire.set_state(eyes="flat", mouth="wavy", eyebrows="frown", emotion="sweat")
    cl "Ugh my hair turned up again... Maybe if I let it naturally dry outside..."
    $claire.set_state(with_dissolve, mouth="pout")
    cl "These tangles are a pain..."
    $mirari.set_state(emotion="note")
    show mirari at center_alone with dissolve
    show mirari at bounce_up_alone
    voice "m_w27"
    mi "Want me to help with that?"
    $claire.set_state(eyes="default", eyebrows="default", mouth="uh", emotion="default")
    cl "Will you?"
    $mirari.set_state(with_dissolve, eyes="happy", mouth="happy", emotion="heart")
    voice "m_w24"
    mi "Of course! Take a seat and I'll comb your hair for you."
    hide mirari with dissolve
    show chibi_mira01 at chibi_scene with dissolve
    $ gallery.unlock("chibi_mira01")
    "Grateful for the tempting offer, I sit down on the grass in front of her lawn chair. She leans in, running her fingers through my hair as she brushes it."
    "I close my eyes and let out a little happy hum. It feels soooo good."
    cla "It's been a while since someone pampered me like this..."
    voice "m_s09"
    mi "Were you going for a new hairstyle?"
    cla "Trying. I can't tame my hair at all."
    cla "I get a little worried about my appearance sometimes, but I guess that's normal."
    cla "I hope whoever I sleep with doesn't get disappointed by my looks."
    hide chibi_mira01
    $mirari.set_state(emotion="default", eyes="default", eyebrows="frown", mouth="uh")
    show mirari at center_alone with dissolve
    voice "m_w28"
    mi "Hon, if the person truly cares for you, they'd never ever be disappointed by your appearance in bed. If they make you feel inadequate, they aren't worth your time."
    $mirari.set_state(with_dissolve, eyes="closed", eyebrows="default", mouth="smile")
    mi "You deserve to be with someone who makes you feel beautiful."
    $claire.set_state(eyebrows="inwards", eyes="tender side", emotion_base="small blush")
    cl "I never thought about that. I admit I've been overthinking things, like how because I'm inexperienced, I'll disappoint my partner..."
    $mirari.set_state(eyebrows="frown", eyes="default", mouth="pout", emotion="vein")
    show mirari at bounce_left
    "I feel a flick at the back of my head."
    $mirari.set_state(with_dissolve, eyes="wink", mouth="uh", emotion="default")
    voice "m_w29"
    mi "I know it sounds odd coming from a succubus, but, surprise, sex isn't about 'mind-blowing experiences'. There's more to it than impressing your lover."
    $mirari.set_state(with_dissolve, eyes="closed", mouth="happy", eyebrows="up")
    mi "It's about willingness to explore, practice and being okay if things don't go as planned."
    $mirari.set_state(with_dissolve, eyes="tender", mouth="default", eyebrows="default")
    voice "m_s12"
    mi "I've had many - many - partners over the years, but I still learn new things. Everyone is different and has their own needs and, yes, insecurities."
    $mirari.set_state(with_dissolve, eyes="happy")
    mi "Basically, you'll know when you feel ready, [claire_name]. Don't try to rush it." 
    $claire.set_state(eyes="happy", emotion_base="default", mouth="smile" )
    cl "...Thank you. I really needed this little pep talk."
    $mirari.set_state(mouth="uh", eyebrows="frown")
    show mirari at bounce_up_alone
    voice "m_s08"
    mi "It's not a problem. And if I ever hear someone saying you're uncute, I'll toss spiders through their bedroom window." 
    $claire.set_state(mouth="happy")
    stop music fadeout 2
    cl "Heh, thanks."
    play music music_romance fadein 2
    $claire.set_state(with_dissolve, eyes="down", emotion_base="large blush", mouth="smile")
    $mirari.set_state(with_dissolve, emotion="default", eyes="tender", mouth="smile", eyebrows="default")
    cl "I never considered whether I'm attracted to women or not, but I think you're really beautiful, too."
    $mirari.set_state(emotion="flowers", eyes="default", eyebrows="inwards", mouth="smile", emotion_base="small blush")
    show mirari at bounce_up_alone
    voice "m_s17"
    mi "You do!? Aw, you're adorable, [claire_name]!"
    "She hugs me tightly from behind."
    $mirari.set_state(with_dissolve, emotion="heart", eyes="tender", emotion_base="default")
    mi "I know we've only been together for a few days, but I think you're a sweet person. I hope whoever you choose down the road makes you very happy."
    $mirari.set_state(emotion="note", eyes="happy", eyebrows="up")
    show mirari at sway
    voice "m_s09"
    mi "There, hair's done! Where's that mirror... What do you think?"
    $claire.set_state(emotion="sweat", emotion_base="default", eyebrows="flat", eyes="default", mouth="low")
    cl "I don't look any different?"
    $mirari.set_state(with_dissolve, emotion="default", eyes="default", eyebrows="default")
    voice "m_s08"
    mi "It's because I love your hair the way it is." 
    $mirari.set_state(with_dissolve, emotion="heart", eyes="wink", mouth="tongue")
    mi "Although... later tonight, I'd love to give it a cute disheveled appearance, too." 
    $claire.set_state(emotion_base="large blush", emotion="steam", eyes="dots", eyebrows="up", mouth="wavy")
    cl "R-really?"
    $mirari.set_state(with_dissolve, emotion="default", eyes="happy", mouth="smile", emotion_base="small_blush")
    voice "m_s01"
    mi "Kidding aside... but if you do pick me... I promise you won't disappoint me, and I'd make it a fun, relaxing, experience for you."
    $claire.set_state(emotion="default", eyes="tender", mouth="smile", eyebrows="default")
    stop music fadeout 3
    cl "Thank you." 
    jump next_day


label mirari_sex:
    $ in_sex = True

    if _in_replay:
        $ sex_stop_label = "mirari_stop_now"
        show screen replay_controls()

    if not _in_replay:
        $ persistent.mirari_claire_name = claire_name
        $ persistent.mirari_scenes = mirari_scenes
        $ persistent.mirari_sex_stop = None
    
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    pause(0.5)
    play music music_tension
    scene bg hallway_night with dissolve
    $mirari.set_state(**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    $ claire.set_state(base="chemise", emotion_base="large blush", mouth="wavy", eyebrows="inwards")
    cl "Do I look okay...?"
    "I tug the strap of my chemise then take a deep breath. The bedroom door is open ajar, and I see it as a cue that Mirari's preparations are complete."
    $claire.set_state(mouth="low")
    cl "Can I come in?"
    play sound "assets/sfx/knock.ogg"
    "I knock lightly on the door."
    voice "m_w24"
    mi "Of course!"
    scene bg bedroom_candles with dissolve
    "I step in. The room is dim, save for yellow candles scattered around on the table and bookcase."
    "On the bed are a few towels, folded and placed behind a fluffed-up pillow. Next to the bed are bottles, a water-filled basin and a handcloth organized on the floor."
    $ mirari.set_state(base="baby doll")
    show mirari at center with dissolve
    "Mirari straightens up and eagerly looks me over."
    show mirari at center_alone with dissolve
    $mirari.set_state(eyes="happy", emotion_base="small blush", emotion="flowers", mouth="happy")
    show mirari at bounce_up_alone
    voice "m_s01"
    mi "You look adorable!"
    $claire.set_state(mouth="smile", emotion_base="small blush", eyebrows="default")
    cl "S-so do you..."
    $mirari.set_state(with_dissolve, eyes="wink", mouth="smile", emotion="note", emotion_base="default")
    voice "m_s12"
    mi "I thought it'd be fun if I dressed for the occasion, too."
    $claire.set_state(mouth="uh")
    cl "And the candles are a nice touch... Wait, they're LED? How surprisingly modern."
    if mirari_scenes >= 3:
        $mirari.set_state(with_dissolve, emotion="sweat", eyes="happy", eyebrows="inwards")
        voice "m_s06"
        mi "Hehe, remember how I told you how, uh, sex doesn't always go as planned?"
        $claire.set_state(emotion_base="dark", eyes="fun side", emotion="sweat", eyebrows="flat", mouth="smile")
        cl "Ah... smart move."
    else:
        $mirari.set_state(with_dissolve, emotion_base="default", eyes="happy", eyebrows="inwards")
        mi "I find them to be less of a hassle. And safer."    
    $mirari.set_state(with_dissolve, eyebrows="default", eyes="wink", emotion="default")
    mi "Have you ever experienced a full body massage before?"
    $claire.set_state(emotion_base="small blush", eyebrows="up", eyes="default", mouth="oh", emotion="default")
    cl "Um, no..." 
    "She takes my hand and guides me to the bed, and we sit on the edge together."
    $mirari.set_state(with_dissolve,eyes="happy", mouth="happy")
    voice "m_s01"
    mi "That's fine! I thought I could help you feel relaxed with a massage, and you can decide if you'd like to go beyond that." 
    $mirari.set_state(with_dissolve,eyes="tender", mouth="smile")
    mi "I won't try anything you wouldn't want me to, hon."
    $claire.set_state(mouth="smile", eyebrows="default")
    cl "Thank you... Is there anything I need to do?"
    $mirari.set_state(with_dissolve,eyes="happy", emotion="note")
    voice "m_sex01"
    mi "Nope! Just lie down and relax. I could begin with your shoulders, or I could start with something less intimate, like your feet, if you prefer." 
    $mirari.set_state(with_dissolve,emotion="default", eyes="default")
    mi "Whatever feels more comfortable to you." 
    stop music fadeout 2
    cl "Then..."
    menu:
        "A shoulder massage.":
            $ mirari_sex_choices.top_choice = True
            play music music_love fadein 3
            cl "When I think of a massage, I always think of shoulders and back first, so... That sounds like a good starting point."
            $mirari.set_state(emotion="note", eyes="wink", mouth="grin")
            voice "m_sex07"
            mi "Of course! I hope you don't mind removing your chemise already~"
            "I blush, but disrobe, leaving only my panties."
            $ claire.set_state(base="naked")
            "I lie down on the towel, my upper body on top of the pillow. Mirari covers my lower back and rear with a towel, and I don't feel as exposed anymore."
            "She applies oil to her hands and starts rubbing them together. The soft scent of jasmine now lingers in the air, relaxing me."
            hide mirari with dissolve
            show mira_back with dissolve
            $ gallery.unlock("mira_back")
            "She straddles my rear and lightly sits on me, supporting most of her weight on her knees."         
            show screen sex_stop("mirari_stop_now")
            $ mirari_sex_choices.shoulder_massage = True
            "Her fingers lightly touch my neck, below my hairline. Her hands are warm from the oil and easily glide over my skin."
            "All it takes are small, circular motions to send shivers down my spine and I moan in approval."
            cla "That feels heavenly..."
            cla "How are you so good at this?"
            voice "m_sex13"
            mi "Hehe, it doesn't take much for the neck area. You're pretty tense up here... Stressed?"
            cla "Uh, a bit of that and hunching over my desk..."
            voice "m_sex14"
            mi "That'll do it."
            "She travels outside, kneading my shoulders before stroking back to my neck, increasing pressure each time."
            mi "Your skin is so smooth! I love how it feels."
            cla "Ee..."
            voice "m_sex15"
            mi "You make the cutest sounds! Can I nibble you too?"
            menu:
                "Go for it.":
                    $ mirari_sex_choices.nibbles = True
                    cla "Sure, although what would you even nib—"
                    show mira_back nibble with dissolve
                    $ gallery.unlock("mira_back nibble")
                    "Her tongue trails up my ear rim, then she blows lightly on it, creating a cooling sensation. I gasp as she leans in and nibbles my earlobe. I feel my face go warm from the gesture." 
                    cla "Ng..."
                    voice "m_sex16"
                    mi "You're adorable..."
                    "Her breath tickles my ear, and she does the same to the other side, her hands still massaging my neck."

                "No nibbling.":
                    $ mirari_sex_choices.nibbles = False
                    cla "Your hands are enough, they feel amazing."
                    voice "m_sex10"
                    mi "Roger~"

                "I'd like to stop...":
                    jump mirari_stop_now
            if mirari_sex_choices.nibbles == True:
                show mira_back with dissolve
                $ gallery.unlock("mira_back")
            "When she gets to my shoulder blade, I cringe when her fingers push against what feels like a cluster of nerves."
            cla "Ouch..."
            mi "A knot?"
            cla "F-feels like it... Ow..."
            voice "m_sex11"
            mi "I can loosen it up. Tell me where it's most tender."
            "The corner of my eyes scrunch up as she travels over a tight area."
            cla "There."
            voice "m_sex19"
            mi "Okay. Take a deep breath, and I'll massage it out. Ready?" 
            "My chest heaves heavily against the bed, and I roll my shoulders a bit, preparing myself." 
            "Her fingers prod against my skin, then press harder right into the sore knot. I clutch my pillow and grit my teeth, only able to describe it as 'sweet pain'."
            voice "m_sex20"
            mi "You okay? Should I keep going?"
            cla "It feels good... painful yet it's... nice..." 
            "I can feel the stress leave my body as she starts massaging the middle, radiating toward the edge as my muscle unwinds under her touch." 
            "I let out a happy sigh, my face burying into the pillow."
            cla "W-wow, I really needed that..."
            "I feel giddy from the release, and giggle, mindful not to accidentally kick Mirari as my legs bend." 
            voice "m_sex21"
            mi "Better?"
            cla "Much. I'm trying not to melt into the bed." 
            voice "m_sex22"
            mi "Wonderful."
            "Her hands travel down my back and stop at its base."
            voice "m_sex23"
            mi "Hrm, would you like me to massage your cute butt, too?"
            jump mirari_butt_choice
            
        "Feet first.":
            play music music_love fadein 3
            $ mirari_sex_choices.top_choice = False
            $ mirari_sex_choices.foot_massage = True
            cl "A foot massage sounds nice..."
            $mirari.set_state(emotion="note", eyes="wink", mouth="grin")
            show mirari at bounce_up_alone
            voice "m_sex08"
            mi "Leave it to me. You can keep sitting like so."
            show screen sex_stop("mirari_stop_now")
            hide mirari with dissolve
            show mira_foot with dissolve
            $ gallery.unlock("mira_foot")
            "She kneels down in front of me, and I raise one foot. She applies some oil to her hands and starts rubbing them together. A light jasmine scent fills the air."
            "Cupping my foot gently in her hands, she begins rubbing the top, then looks up to gauge my reaction."
            voice "m_sex09"
            mi "How does it feel?"
            cla "Feels lovely... You're an expert at this?"
            mi "Well, there's no real wrong way to do this, it's more paying attention to your lover's cues and feedback than anything."
            "She winks and increases pressure on my heel, sending shivers up my leg. My eyes flutter from the sensation and I wonder how long my feet needed this treatment."
            cla "Amazing..." 
            "I lift up my leg and her thumbs rub down my heel, making circular motions before kneading my arch." 
            voice "m_sex15"
            mi "I love the sounds you make~ Can I nibble you, too?"
            menu:
                "Nibble away.":
                    cla "Sure."
                    $ mirari_sex_choices.nibbles = True
                    "Her fingers lightly tug my toes, one by one. She looks up at me with a teasing glint in her eye, then carefully bites my big toe."
                    show mira_foot nibble with dissolve
                    $ gallery.unlock("mira_foot nibble")
                    "I can sense my face heat up. I didn't expect the gesture to feel - or appear - so erotic." 
                    cla "...Ng..."
                    "Her fingers keep working my arch while her moist lips suck and nibble my toes and the top of my foot." 
                    voice "m_sex17"
                    mi "So cute..."
                    show mira_foot with dissolve
                    $ gallery.unlock("mira_foot")

                "No nibbling.":
                    $ mirari_sex_choices.nibbles = False
                    cla "Your hands are already working wonders."
                    voice "m_sex10"
                    mi "Roger~"
                    "Her fingers keep working my arch, her thumbs making long, languid, strokes up and down." 

                "Actually I'd like to stop now...":
                    jump mirari_stop_now
                  
            "She gives my other foot the same treatment, leaving no muscle or spot untreated. Everything about her movements are calm and unhurried."
            $ mirari_sex_choices.foot_massage = False
            $ mirari_sex_choices.leg_massage = True
            mi "I'll start moving upward now..."      
            "She squeezes my ankle, pushing upward with a pressured stroke. Whenever her fingers go a little higher, I find myself anticipating more, and I grip the sheets."
            voice "m_s01"
            "Seeing my reaction, she giggles then switches to my other foot, back to its ankle. Clearly she loves teasing." 
            mi "If you'd like, you can lie down and I can massage your whole leg. It'll be easier to in that position." 
            hide mira_foot with dissolve
            "I move to my stomach and make myself comfortable on the towel. I rest my upper body on the soft pillow and hug it close."
            "Mirari sits beside me, and I can hear her rubbing her hands again, presumingly with more jasmine oil."
            $mirari.set_state(emotion="default", eyes="tender", eyebrows="inwards", mouth="oh")
            show mirari at center with dissolve
            voice "m_sex11"
            mi "Ah, you're never supposed to break contact during a massage... It loses momentum. I'll make up for it." 
            $mirari.set_state(eyes="closed", eyebrows="default", mouth="smile")
            show mirari at center_alone with dissolve
            "She continues her long, spine-tingling strokes, her thumbs pressing into the middle of my legs while her fingers carefully brush the sides." 
            "Easing the pressure near my knees, she then glides her hands all the way from my calf to my upper thighs." 
            $claire.set_state(eyes="closed", eyebrows="inwards")
            cl "Ah... it feels like you're getting all the kinks out of my legs..."
            $mirari.set_state(with_dissolve, eyes="wink")
            voice "m_sex13"
            mi "That's the idea."
            $claire.set_state(mouth="happy")
            cl "I'm gonna melt into the bed..." 
            "All the tension and soreness from my daily walks have disappeared, and my legs feel like jelly now."
            $mirari.set_state(with_dissolve, eyes="happy",mouth="happy")
            voice "m_sex23"
            mi "I'm glad. Hrm, would you like me to massage your adorable butt, too?"
            jump mirari_butt_choice
            
        "I'd like to stop now...":
            play music music_tension
            $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat")
            $mirari.set_state(with_dissolve, eyebrows="inwards")
            cl "Actually... I don't think I'm ready for this after all."
            $claire.set_state(with_dissolve, eyes="bug cry", mouth="uhh", emotion="default", emotion_base="default")
            cl "I'm sorry, especially since you set everything up for the massage." 
            $mirari.set_state(with_dissolve, mouth="happy")
            voice "m_sex02"
            mi "Aw, it's okay. You know yourself best."
            $mirari.set_state(with_dissolve, eyes="happy")
            mi "Plus, it can be seen as a rather personal activity, sexual or not."
            $mirari.set_state(with_dissolve, eyes="default", mouth="smile", eyebrows="default")
            voice "m_sex06"
            mi "Would cuddling be too intimate for you?" 
            $claire.set_state(with_dissolve, mouth="smile", eyes="tender")
            stop music fadeout 2
            cl "No, a cuddle sounds nice."
            $ mirari_cuddle_sprite.set_state(**mirari_cuddle_initial)
            scene mira_cuddle with dissolve
            play music music_lullaby fadein 2
            $ mirari_cuddle_sprite.set_state(with_dissolve, mirari=3)
#            $mcuddle_mface ="3"
            "We curl up on the bed, our fingers intertwined between us. She smiles and gives my hand an affectionate squeeze before closing her eyes."
            cla "Thank you, Mirari..."
            "The candles flicker softly, creating a cozy atmosphere."
            $ mirari_cuddle_sprite.set_state(with_dissolve, claire=2)
#            $mcuddle_cface ="2"
            "Her closeness and warmth is more soothing than any blanket, and I find myself drifting off to sleep as well..."
            call credits from _call_credits
            jump mirari_epilogue


label mirari_butt_choice:
    menu: 
        "That sounds great.":
            if mirari_sex_choices.shoulder_massage == True:
                cla "I never had one before..."
                $ mirari_sex_choices.shoulder_massage = False
                $ mirari_sex_choices.butt_massage = True
                mi "It'll make your lower back muscles feel so much better, too~"
                "Her fingers glide over my body, careful not to break contact, and her palms rest at the small of my back."
                voice "m_sex24"
                mi "Don't worry, it'll only be a surface massage, no surprises for your first time."
                cla "Oh, uh, thanks. I didn't even consider it."
                "Her palms cup the roundness and she starts massaging in circular motions, occasionally fanning to my lower back again." 
                "After kneading thoroughly, she presses against my upper thighs. I feel my stomach coil from her touch, and my breathing deepens." 
                "My heart beats wildly against the towel, and I try not to squirm too much under Mirari's magic." 
                "Her fingers trace the frills of my panties."
                voice "m_sex25"
                mi "How do you feel? A little warmed up?"
                cla "Getting there..."
                voice "m_sex23"
                mi "Would you like it even better if I massaged your breasts?"
            else:
                $claire.set_state(eyes="default", mouth="uh", eyebrows="up")
                cl "I never had one before..."
                $ mirari_sex_choices.leg_massage = False
                $ mirari_sex_choices.butt_massage = True
                $mirari.set_state(with_dissolve, eyes="wink", emotion="note", mouth="smile")
                mi "It'll make your lower back muscles feel so much better, too~"
                "Her fingers glide over my body, careful not to break contact, and her palms rest at the small of my back."
                $mirari.set_state(with_dissolve, eyes="closed", emotion="default", eyebrows="up")
                voice "m_sex24"
                mi "Don't worry, it'll only be a surface massage, no surprises for your first time."
                $claire.set_state(eyes="dots", mouth="uhh", emotion_base="large blush", eyebrows="default")
                cl "Oh, uh, thanks. I didn't even consider it."
                "Her palms cup the roundness and she starts massaging in circular motions, occasionally fanning to my lower back again." 
                "After kneading thoroughly, she presses against my upper thighs. I feel my stomach coil from her touch, and my breathing deepens." 
                "My heart beats wildly against the towel, and I try not to squirm too much under Mirari's magic." 
                "Her fingers trace the frills of my panties."
                $mirari.set_state(eyes="tender", emotion_base="small_blush", emotion="heart")
                voice "m_sex25"
                mi "How do you feel? A little warmed up?"
                $claire.set_state(eyes="tender", emotion_base="small blush", mouth="smile")
                cl "Getting there..."
                voice "m_sex23"
                mi "Would you like it even better if I massaged your breasts?"
            menu:
                "Yes.":
                    cla "I'd love that..."
                    voice "m_sex29"
                    mi "Here, I can reach you better if you sit up for this one."
                    scene bg bedroom_candles with dissolve
                    $ claire.set_state(base="naked")
                    $ mirari_sex_choices.butt_massage = False
                    $ mirari_sex_choices.breast_massage = True
                    "I obey and rest on my knees. I raise my arms, and she tugs the chemise over my body."
                    jump mirari_breast_massage_scene
                "I'd like to stop now.":
                    jump mirari_stop_now
                
        "I'd prefer a back massage..." if not mirari_sex_choices.top_choice:
            $claire.set_state(eyes="default", eyebrows="inwards", mouth="smile")
            cl "I don't know if I'd feel comfortable with that. Maybe a back massage instead?"
            $mirari.set_state(with_dissolve, eyes="wink", emotion="note", mouth="smile")
            voice "m_sex07"
            mi "Of course~ I'll get all the tension out of your muscles." 
            $claire.set_state(eyes="tender side", mouth="low", emotion="sweat")
            cl "Um, thanks... I'm sorry if I'm being a stick-in-the-mud or anything..."
            $mirari.set_state(with_dissolve, eyes="tender", emotion="default", mouth="happy")
            voice "m_sex27"
            mi "You're not. It's good to be clear about your boundaries, and I respect them." 
            $mirari.set_state(with_dissolve, eyebrows="up", eyes="closed", mouth="smile")
            voice "m_sex13"
            mi "I want you to feel happy and secure, not guilty that you're not enjoying something but too afraid to speak up." 
            hide mirari with dissolve
            show mira_back with dissolve
            $ gallery.unlock("mira_back")
            $ claire.set_state(base="naked")
            $ mirari_sex_choices.butt_massage = True
            "She lifts up my chemise and starts working on my lower back, kneading it lightly with her knuckles." 
            voice "m_sex12"
            mi "Besides, this is your first time. Sometimes you don't even know what you like or dislike until you get there. Be as fussy as you want, I'll do my best to adjust~"
            voice "m_sex28"
            mi "In return, be honest with me, okay? You're doing great, hon."
            cla "Promise."
            jump mirari_back_massage_scene
                
        "Continue with the back massage..." if mirari_sex_choices.top_choice:
            cla "I don't know if I'd feel comfortable with that. Maybe continue the back massage?"
            $ mirari_sex_choices.shoulder_massage = False
            $mirari_sex_choices.butt_massage = True
            voice "m_sex07"
            mi "Of course~ I'll get the rest of those pesky knots out of your back."
            cla "Um, thanks... I hope I'm not sounding like a wet blanket."
            voice "m_sex27"
            mi "You're not. I'm happy you're being honest about your boundaries, and I respect them."
            "She starts working on my lower muscles, careful not to press directly on my spine."
            mi "I want you to enjoy yourself, not pretend you are when you'd wish I'd rather stop the activity." 
            voice "m_sex28"
            mi "You're doing great, hon."
            cla "Thank you." 

            jump mirari_back_massage_scene
            
        "I'd like to stop now.":
            jump mirari_stop_now    


label mirari_back_massage_scene:
    $ mirari_sex_choices.butt_massage = True
    "She fans her hands out like a butterfly and guides them up and down my back."
    $claire.set_state(eyes="tender", mouth="smile", emotion="default", eyebrows="default")
    voice "m_sex13"
    mi "Aw, even your little spine is cute."
    if mirari_sex_choices.nibbles:
        "I feel her lips against my spine and her teeth grazes the skin."
        cla "Hehe, that feels so weird." 
    else: 
        "To prove it, she playfully pinches my spine, rolling the bone under her fingers. I giggle." 
    "Her hands spread out and start to drop along my sides to trace over my hip bone." 
    "The featherlight touch causes my heart to beat wildly, and my breathing deepens. Whenever she rubs closer to my stomach, I feel a rush of warmth spreading to my thighs." 
    voice "m_sex23"
    mi "Would you like it if I massaged your breasts?"
        
    menu:
        "Yes.":
            $ claire.set_state(base="naked")
            cla "I'd love that..."
            voice "m_sex29"
            mi "Here, I can reach you better if you sit up for this one."
            $ mirari_sex_choices.butt_massage = False
            $ mirari_sex_choices.breast_massage = True
            scene bg bedroom_candles with dissolve
            "I obey, sitting on my knees as she scoots closer behind me."
            jump mirari_breast_massage_scene

        "I'd like to stop now.":
            jump mirari_stop_now


label mirari_breast_massage_scene:
    #$ mirari_sex_choices.back_massage = False
    show mira_breast with dissolve
    $ gallery.unlock("mira_breast")
    "Her arms wrap around, and she places her hands right below my chest. I can feel my heart beat against her fingers, and she seems content rubbing there first." 
    cla "T-they're not too small or anything...?"
    voice "m_sex24"
    mi "Don't worry about your size. They're beautifully shaped and fill my hands nicely, see?"
    "Opening her palms, she fondles them gently in circular motions with her thumbs above my nipples." 
    "Mirari leans against me and I can feel how soft she is, her front playfully pressing into my back." 
    if mirari_sex_choices.nibbles:
        "Her nose nuzzles the outer rim of my ear as she seeks my earlobe. She nibbles the tip lightly, tenderly brushing it against her teeth and lips." 

    "She applies pressure, squeezing my chest firmly without causing any discomfort, her pointer fingers tracing down my sternum after each motion."
    "The multiple sensations are amazing, and I lean my head back, taking in a deep breath. I shift my thighs slightly to maintain a little friction below." 
    "Her thumbs brush closer and closer to my nipples after each caress until finally I feel them graze the top."
    voice "m_sex15"
    mi "Feel okay?"
    cla "Wonderful... It makes sense you'd know my body."
    voice "m_sex30"
    mi "I try~"
    "She gently pinches my nipples and rolls them between her fingers. I cover her hands with mine to encourage her." 
    "Tiny kisses flutter over my shoulder and travel to the back of my neck, sending more shivers down my body and raising goosebumps on my arms." 
    "Finally, I turn, tilting my head for another kiss that she eagerly accepts. Our lips meet firmly and she cradles me close before we break away."
    voice "m_sex31"
    mi "Would you like to keep going?"
    menu:
        "Yes.":
            stop music fadeout 2
            cla "I would."
            scene bg bedroom_candles with dissolve
            "Mirari pushes the towels away and grabs the pillow, dropping it in its original spot. After removing her babydoll, we both lie down, facing each other on our sides." 
            $mirari.set_state(base="panties")
            show mirari at center_alone with dissolve
            voice "m_sex32"
            mi "There we go. We'll start with an easy position. Now, where was I~?"
            $ mirari_lying_sprite.set_state(**mirari_lying_initial)
            scene mira_lying with dissolve
            play music music_romance

            $ mirari_sex_choices.on_sides = True

            voice "m_s01"
            "Giggling, she cups the underside of my breast, then starts traveling down my side, running her fingers along my curves."
            menu:
                "Mutually touch her back.":
                    $ mirari_sex_choices.mutual_touching = True
                    cla "I'd like to return the favor somehow..."
                    $ mirari_lying_sprite.set_state(with_dissolve, claire_arm="breast")
#                    $ mlay_clarm = "breast"
                    "Hesitantly, I bring up my hand to her breasts, and she raises an eyebrow in surprise."
                    voice "m_sex33"
                    mi "Oh~? You'd like to?"
                    cla "I-if it's okay with you..."
                    $ mirari_lying_sprite.set_state(with_dissolve, mirari_face="happy")
#                    $mlay_mface = "happy"
                    voice "m_sex07"
                    mi "Of course. Go easy on me."
                    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="smile")
#                    $mlay_clface = "smile" 
                    "She winks and I blush heavily, resting an open palm on the center of her chest, not sure what I'm doing."
                    voice "m_sex13"
                    mi "Hehe, we're pretty similar. Just think about what makes you feel good, and do the same to me." 
                    cla "But if what we like are different...?"
                    mi "Then I'll give you feedback."
                    $mlay_mface = "tender"
                    if mirari_scenes >= 3:
                        mi "Sex is about exploring and learning about each other's bodies, right?" 
                    cla "Right..."
                    voice "m_sex15"
                    "I glide a finger down her sternum, and she lets out a happy hum of approval. Gaining some confidence, I move my hand sideways and fondle her breast, massaging it lightly."
                    cla "That feel okay...?"
                    voice "m_sex26"
                    mi "Yes. You can apply a bit more pressure, too."
                    "After squeezing more firmly, I watch her reaction and she nods contently before resuming her hand on my hip."
                    jump continuing_to_end

                "Enjoy the moment.":
                    $ mirari_sex_choices.mutual_touching = False
                    jump continuing_to_end
                    
                "I'd like to stop now.":    
                    jump mirari_stop_now    
                    
        "I'd like to stop now.":    
            jump mirari_stop_now    
                    
label continuing_to_end:                     
    "Her fingers flirt with the lace of my panties, and she makes eye contact with me. I reach down and tug them off, and she does the same. I notice she sports a heart-shaped trim."
    $mirari.set_state(base="naked")
    $ mirari_lying_sprite.set_state(with_dissolve, panties="off")
#    $mlay_panties = "off"
    cla "That's cute..."
    $ mirari_lying_sprite.set_state(with_dissolve, mirari_face="happy")
#    $mlay_mface = "happy"
    voice "m_sex34"
    mi "Aw, thank you. You're cute as well."
    $ mirari_lying_sprite.set_state(with_dissolve, mirari_face="tender", mirari_arm="touch")
#    $mlay_mface = "tender"
#    $mlay_marm = "touch"
    "She shifts her weight closer, her fingers tickling the edge of my pubic hair. My body heightens in anticipation, and I can feel heat radiating between my thighs as her hand covers my front." 
    if mirari_sex_choices.mutual_touching:
        $ mirari_lying_sprite.set_state(with_dissolve, claire_arm="touch")
#        $mlay_clarm = "touch"
        "I clumsily mimic her movements, careful not to push her arm away as I brush toward her inner thighs." 
    voice "m_sex13"
    mi "I'm glad the massage felt this good.."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="pleasure")
#    $mlay_clface = "pleasure"
    "Her fingers stroke my lips, using my wetness to further lubricate me as she explores." 
    if mirari_sex_choices.mutual_touching:
        $ mirari_lying_sprite.set_state(with_dissolve, mirari_face="pleasure")
#        $mlay_mface = "pleasure"
        "After tracing her heart, I gently wedge my fingers between the cleft of her thighs, feeling the slick wetness between my fingers."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="smile")
#    $mlay_clface = "smile"
    cla "I'm glad you're enjoying yourself too..." 
    voice "m_s01"
    $ mirari_lying_sprite.set_state(with_dissolve, mirari_face="happy")
#    $mlay_mface = "happy"
    "She gauges my awkward expression and giggles." 
    mi "Of course. I'm with you."
    "Her motions turn circular once she finds my budding clit and begins rubbing it. My legs squirm under her touch, and I try not to trap her fingers between my thighs." 
    hide screen sex_stop
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="pleasure")
#    $mlay_clface = "pleasure"
    "Tension builds below my stomach as she presses against me, alternating between her fingers quickly."
    if mirari_sex_choices.mutual_touching:
        "My hand between her thighs turns limp as I lose concentration."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="O")
#    $mlay_clface = "O"
    "I let out a little moan and wriggle my face into the pillow. It feels like there's bursts of white lights in my mind, and I close my eyes to focus on the sensation." 
    "My body seizes up briefly and I feel contractions through my stomach. After one final shudder, I exhale deeply and relax."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="smile")
#    $mlay_clface = "smile"
    "Mirari hugs me close, keeping her touch light as she smothers my sweaty forehead with kisses."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_arm="fold", mirari_face="happy")
#    $mlay_clarm = "fold"
#    $mlay_mface = "happy"
    voice "m_sex35"
    mi "You did great, hon."
    cla "...That was intense... I never experienced that on my own."
    mi "It's thanks to the lengthly massage keeping you nice and ready throughout."
    voice "m_sex13"
    mi "I could tell. You smelled so delicious and..."
    $ mirari_lying_sprite.set_state(with_dissolve, mirari_arm="lick", mirari_face="tease")
#    $mlay_marm = "lick"
#    $mlay_mface = "tease"
    "She removes her hand from my thigh and licks her fingers."
    $ mirari_lying_sprite.set_state(with_dissolve, claire_face="shock")
#    $mlay_clface = "shock"
    cla "JLKFDKLDSA?"
    voice "m_sex15"
    mi "...you taste lovely, too."
    cla "...Do I even have a flavor?"
    voice "m_sex23"
    mi "Hrm... I'd say, tangy yogurt?"
    cla "Now you're just pulling my leg."
    mi "Perhaps. Maybe you'll remember this when you eat your parfait tomorrow."
    cla "Omigod."
    voice "m_sex13"
    mi "Hehe, you're so fun to tease."
    mi "I know you're going to have a wonderful sleep tonight." 
    stop music fadeout 2
    
    scene bg bedroom_candles with dissolve

    "She takes a damp handcloth and playfully wipes me down, the cool dampness a blessing against my aching warm body."
    play music music_lullaby fadein 2
    $ mirari_cuddle_sprite.set_state(**mirari_cuddle_initial)
    scene mira_cuddle with dissolve
    $ claire.set_state(base="chemise")
    "Once she's done, we both settle into the bed facing each other, my hand in hers. I can still smell the faint jasmine, further relaxing me." 
    if mirari_scenes >= 3:
        $ persistent.mirari_complete = True
        mi "Hope you feel a little better about yourself. I enjoyed this and you didn't disappoint me in the least."
        $ mirari_cuddle_sprite.set_state(with_dissolve, mirari=2)
#        $mcuddle_mface = "2"
        voice "m_sex15"
        mi "Ah, the disheveled hair look {i}is{/i} cute on you after all."
        "I use a free hand to at least pat down my bangs."
        cla "T-thank you... for making me feel beautiful."
        $ mirari_cuddle_sprite.set_state(with_dissolve, mirari=1)
#        $mcuddle_mface = "1"
        voice "m_sex36"
        mi "You {i}are{/i} beautiful."
        "She giggles and we exchange a small kiss. After that, she closes her eyes and gives my hand a comforting squeeze."
    $ mirari_cuddle_sprite.set_state(with_dissolve, mirari=3, claire=2)
#    $mcuddle_mface = "3"
#    $mcuddle_cface = "2"
    "Mirari's closeness and warmth is more soothing than any blanket, and I find myself drifting off to sleep as well..."
    $mira_epilong = True
    call credits from _call_credits_1
    jump mirari_epilogue


label mirari_stop_now:
    if not _in_replay:
        $ persistent.mirari_sex_stop = last_statement
    hide screen sex_stop
    if mirari_sex_choices.on_side:
        "I squirm a bit."
        cla "Actually... I'd like to stop."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $mirari.set_state(with_dissolve, eyes="happy", emotion_base="small blush")
        show mirari at center_alone with dissolve
        "Her hand freezes and she removes it from my body."
        voice "m_sex18"
        mi "All done for tonight?"
        jump mirari_stop_late

    elif mirari_sex_choices.breast_massage:
        cla "I'd like to stop now."
        "Mirari removes her hands from my body."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $mirari.set_state(with_dissolve, eyes="happy")
        show mirari at center_alone with dissolve
        voice "m_sex07"
        mi "Of course. Did you have enough?"
        $claire.set_state(eyes="tender", emotion_base="large blush", mouth="smile")
        cl "Yes."
        jump mirari_stop_middle

    elif mirari_sex_choices.butt_massage:
        cla "I'd like to stop now..."
        "She removes her hands from my body and I sit up."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="tender", eyebrows="inwards", mouth="smile", emotion_base="small blush")
        $mirari.set_state(with_dissolve, eyebrows="inwards")
        show mirari at center_alone with dissolve
        voice "m_sex20"
        mi "You okay, hon?"
        cl "I am. I just feel this is a good stopping point for me."
        $mirari.set_state(with_dissolve, eyebrows="default", eyes="happy")
        voice "m_sex05"
        mi "I understand. Hold still, I'm going to wipe the oil off you."
        "She takes a damp handcloth and attentively cleans the back of my body." 
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat")
        cl "Sorry about that. I feel I spoiled the mood, especially since you've given me a wonderful massage."
        $mirari.set_state(with_dissolve, eyes="default", mouth="happy")
        voice "m_sex11"
        mi "Aw, you didn't ruin anything. I'm glad you enjoyed what you did." 
        "She places the cloth down, then takes my hand and gives it a squeeze."
        $mirari.set_state(with_dissolve, eyes="happy", mouth="default")
        mi "I think this was a great step for you! You got to experience intimate contact." 
        $claire.set_state(eyes="down", eyebrows="default", mouth="smile", emotion_base="large blush")
        cl "True... I never had someone touch me like that before..."
        $claire.set_state(with_dissolve, eyes="tender", emotion="default", mouth="smile", emotion_base="small blush")
        cl "If it's okay with you... can we cuddle for the rest of the night?"
        jump mirari_stop_early

    elif mirari_sex_choices.leg_massage:
        cla "I'd like to stop now..."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat", emotion_base="small blush")
        $mirari.set_state(with_dissolve, eyebrows="inwards")
        show mirari at center_alone with dissolve
        voice "m_sex07"
        mi "Of course. Was it too much?"
        cl "No... not exactly. I realized I'm not ready to go further. Sorry for changing my mind."
        $mirari.set_state(with_dissolve, eyebrows="default", eyes="happy")
        voice "m_sex03"
        mi "That's alright! You know your body more than anyone else, you don't need to force yourself."
        "She takes a damp handcloth and washes my legs and feet of the oil."
        $mirari.set_state(eyes="tender")
        voice "m_sex04"
        mi "There you go, all clean. Anything else I can do you for?"
        $claire.set_state(eyes="tender", emotion="default", mouth="smile")
        cl "A... cuddle would feel nice..."
        jump mirari_stop_early

    elif mirari_sex_choices.foot_massage:
        "My toes curl and I glance away."
        cla "I'd like to stop now."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat", emotion_base="small blush")
        $mirari.set_state(with_dissolve, eyebrows="inwards")
        show mirari at center_alone with dissolve
        voice "m_sex07"
        mi "Of course. Was it too much to start with?"
        cl "No... I realized I'm not up for this. Sorry for changing my mind early."
        $mirari.set_state(with_dissolve, eyebrows="default", eyes="happy")
        voice "m_sex03"
        mi "That's fine. You know your body more than anyone else, and sometimes it's just not the right time." 
        "She takes the basin and washes my foot of the oil." 
        $mirari.set_state(eyes="tender")
        voice "m_sex04"
        mi "There you go, sweetie. Anything else I can do for you?"
        $claire.set_state(eyes="tender", emotion="default", mouth="smile")
        cl "Um... a cuddle would be nice..."
        jump mirari_stop_early


    elif mirari_sex_choices.shoulder_massage:
        cla "Actually, I'd like to stop."
        "She removes her hands from my body."
        scene bg bedroom_candles with dissolve
        $mirari.set_state(**Emotion.normal())
        $claire.set_state(**Emotion.normal())
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat", emotion_base="small blush")
        $mirari.set_state(with_dissolve, eyebrows="inwards")
        show mirari at center_alone with dissolve
        voice "m_sex07"
        mi "Of course, did I start off too intense...?"
        cl "It's not that, I realized I'm not ready for this after all. Sorry for changing my mind..."
        $mirari.set_state(with_dissolve, eyebrows="default", eyes="happy")
        voice "m_sex03"
        mi "That's fine. You know your body more than anyone, and it just didn't feel like the right time for you." 
        "She takes a damp cloth and wipes my shoulders and neck of the oil."
        $claire.set_state(eyes="tender", emotion="default", mouth="smile")
        voice "m_sex04"
        mi "There you go, hon. Anything else I can do for you?"
        $claire.set_state(eyes="tender", emotion="default", mouth="smile")
        cl "Um... I wouldn't mind a cuddle..."
        jump mirari_stop_early
        

    


label mirari_stop_early:
    hide screen sex_stop
    $mirari.set_state(with_dissolve, eyes="happy", emotion_base="small blush", emotion="default", eyebrows="default", mouth="default")
    stop music fadeout 2
    voice "m_sex07"
    mi "Of course. We can snuggle tonight."
    $ mirari_cuddle_sprite.set_state(mirari=3, claire=2)
#    $mcuddle_mface = "3"
#    $mcuddle_cface = "2"
    scene mira_cuddle with dissolve 
    play music music_lullaby fadein 2
    "We curl up on the bed, our fingers intertwined between us. She smiles and gives my hand an affectionate squeeze before closing her eyes."
    cla "Thank you, Mirari..."
    "The candles flicker softly, creating a cozy atmosphere."
    "Her closeness and warmth is more soothing than any blanket, and I find myself drifting off to sleep as well..."
    call credits from _call_credits_2
    jump mirari_epilogue


label mirari_stop_middle:
    hide screen sex_stop
    $claire.set_state(**Emotion.normal())
    $claire.set_state(eyes="closed", eyebrows="inwards", mouth="low", emotion_base="small blush")
    cl "I apologize, we had a good mood going and everything and suddenly... I felt it was best to stop."
    $mirari.set_state(with_dissolve, eyes="tender", emotion_base="default", emotion="default", eyebrows="default", mouth="default")
    voice "m_sex05"
    mi "I understand. Sometimes you're not ready to go further."
    $mirari.set_state(with_dissolve, eyes="happy", emotion="note", mouth="happy", eyebrows="up")
    mi "I think you did wonderful! You got to experience a lovely massage and you enjoyed yourself. I'm glad you were able to relax with me."
    $claire.set_state(eyes="tender", eyebrows="default", mouth="smile")
    cl "Yes, my body has never felt better in a long time. That was amazing, Mirari."
    $mirari.set_state(with_dissolve, eyes="closed", emotion="default", mouth="smile")
    voice "m_sex12"
    mi "And besides..."
    $mirari.set_state(with_dissolve, eyes="wink", emotion="heart", mouth="grin", emotion_base="small blush")
    voice "m_sex15"
    mi "You were a little aroused, so I did get some nourishment from all this." 
    $claire.set_state(emotion_base="large blush", eyes="dots", mouth="smile", eyebrows="inwards")
    cl "Ah... Um, I'm glad I was able to help a bit..."
    if mirari_scenes >= 1:
        $mirari.set_state(with_dissolve, eyes="happy", mouth="tongue")
        mi "You did, hon. And you still smell delicious too~"
        $claire.set_state(eyes="big", mouth="uhh", emotion="steam")
        cl "W-what? I showered and... the jasmine..."
        $mirari.set_state(with_dissolve, emotion="note", mouth="kitty")
        voice "m_sex13"
        mi "Hehe, you can't mask it." 
    else:
        $mirari.set_state(with_dissolve, eyes="happy", emotion="default", mouth="smile")
        voice "m_s01"
        mi "You did, hon."
    $mirari.set_state(with_dissolve, emotion_base="default", emotion="default", eyes="wink", eyebrows="default", mouth="default")
    voice "m_sex06"
    mi "Up for a cuddle?"
    stop music fadeout 2
    $claire.set_state(eyes="happy", mouth="smile", eyebrows="default", emotion_base="small_blush", emotion="default")
    cl "I'd like that."
    $ mirari_cuddle_sprite.set_state(mirari=3, claire=2)
#    $mcuddle_mface = "3"
#    $mcuddle_cface = "2"
    scene mira_cuddle with dissolve
    play music music_lullaby fadein 2
    "After I retrieve my chemise, I curl up beside Mirari, facing her. Our fingers lace together and we make ourselves comfortable." 
    "I let out a deep breath, watching the flickering candles make shadows dance against the wall. I can still smell the faint jasmine, further relaxing me." 
    "Mirari's closeness and warmth is more soothing than any blanket, and I find myself drifting off to sleep as well..."
    call credits from _call_credits_3
    jump mirari_epilogue


label mirari_stop_late:
    hide screen sex_stop
    $claire.set_state(emotion_base="large blush", eyes="down", eyebrows="inwards", mouth="uhh", emotion="sweat")
    cl "Yeah... I never gone this far before with someone... It's a little, um... scary?"
    $mirari.set_state(with_dissolve, eyes="tender", emotion_base="small_blush", emotion="default", eyebrows="inwards", mouth="default")
    voice "m_sex05"
    mi "I understand. It's not always easy letting go of control."
    $mirari.set_state(with_dissolve, eyes="happy", emotion="flowers", mouth="happy", eyebrows="up")
    voice "m_sex13"
    mi "I'm really happy though! You experienced a lot."
    $claire.set_state(with_dissolve, mouth="smile", eyes="happy", eyebrows="default", emotion="flowers", emotion_base="small blush") 
    cl "I did. That was the best massage I ever had. Thank you, Mirari."
    $mirari.set_state(with_dissolve, eyes="wink", emotion="heart", mouth="grin")
    voice "m_sex15"
    mi "Not only that... I got nourished a bit from our activities." 
    $claire.set_state(mouth="grin", eyebrows="up", emotion="default") 
    cl "Ah, so it's a win-win situation?"
    $mirari.set_state(with_dissolve, eyes="happy", emotion="note", mouth="smile")
    voice "m_sex26"
    mi "It's always a win-win if you're happy and I obtained some energy." 
    $mirari.set_state(with_dissolve, eyes="tender", emotion="default")
    voice "m_sex06"
    mi "Tired? Would you like to cuddle?"
    $claire.set_state(with_dissolve, eyes="tender", emotion="note")
    stop music fadeout 2
    cl "That sounds perfect right now..."
    $ mirari_cuddle_sprite.set_state(mirari=3, claire=2)
#    $mcuddle_mface = "3"
#    $mcuddle_cface = "2"
    scene mira_cuddle with dissolve
    play music music_lullaby fadein 2
    "We retrieve our lingerie, and I curl up next to Mirari, holding hands." 
    "I sigh happily, still detecting the faint scent of jasmine in the air, while the candles lazily flicker."
    "Her closeness and warmth is more soothing than any blanket, and I find myself drifting off to sleep as well..."
    call credits from _call_credits_4
    jump mirari_epilogue

label mirari_epilogue:

    # smaller epilogues you get if:
    #1) didn't see all three scenes from the same sex demon
    #2)didn't make it ALL the way with sex. 
    if mirari_scenes==3 and mira_epilong == True:
        jump mirari_epilogue_long
    else:
        pass
    scene bg bedroom_day with dissolve 
    play sound "assets/sfx/bird_chirp.ogg"
    pause(0.5)
    if claire_base.current_state == "chemise":
        $claire.set_state(base="chemise")
    else:
        $claire.set_state(base="chemise")
    $ claire.set_state(eyes="closed", eyebrows="frown", mouth="default", emotion="default", emotion_base="default")
    cl "Mm..."
    "I groggily open my eyes. When I roll over, I realize the bed is empty and I stretch an arm out to confirm I'm indeed alone."
    $ claire.set_state(eyes="semi open", eyebrows="default", mouth="oh")
    cl "...Was it a dream?"
    "I sit up and reach for my phone as part of my routine. But there's something different about it. Next to my phone is a note. Curious, I pick it up."
    scene white with dissolve
    voice "mirarinote1"
    show text "{color=#000}'Good morning, sweetie!\n I wish I could've cuddled with you longer, or wake up together and give you a kiss.\n It was so adorable how you fell asleep holding my hand. <3\n If you ever want to see me again, draw the mark at the bottom of the note and say the words on the back.\n Even if you just want a massage, I'd be more than happy to provide.{/color}" with dissolve
    $renpy.pause()
    voice "mirarinote2"
    show text "{color=#000}Take care of yourself, hon! - Mirari.'{/color}" with dissolve
    #content face
    $renpy.pause()
    show bg bedroom_day with dissolve
    $ claire.set_state(eyes="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "..."
    $ claire.set_state(with_dissolve, eyes="happy", eyebrows="default", mouth="grin")
    cl "I might take up on that offer one day... Thanks, Mirari."
    $ persistent.mirari_replay = True
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return

label mirari_epilogue_long:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_mirari
    scene bg street with dissolve
    $ claire.set_state(base="default", **Emotion.normal())
    "..."
    "..."
    $claire.set_state(eyes="down", emotion="default", eyebrows="default", mouth="smile", emotion_base="default")
    cl "Five attempts... I'm getting better at mastermind."
    "I pocket my phone as I walk home from university. Although I'm happy with my little victory, it feels hollow since I can't play it with a certain someone..."
    "Even though it's been a week after spring break, I still find myself missing Mirari. I wonder if she punched out a flower recently."
    voice "m_epi01"
    "???" "[claire_name]! There you are!"
    $mirari.set_state(base="human", **Emotion.normal())
    show mirari at center_alone2 with dissolve
    $claire.set_state(eyes="wide", emotion="default", eyebrows="up", mouth="oh", emotion_base="default")
    cl "M-Mirari!?"
    $mirari.set_state(eyes= "happy", mouth="grin", eyebrows="default", emotion="note", emotion_base="default")
    show mirari at bounce_up_alone2
    voice "m_s01"
    "She envelops me in a tight hug and it takes me a moment to register she's right here in front of me."
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="grin", eyebrows="default", emotion="default", emotion_base="default")
    voice "m_epi02"
    mi "Good! I'm so glad I've been able to find you. I've been excited to give you this present; I collected them myself."
    $mirari.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "She gives me a small packet with a crude drawing of a tulip-like plant on the front. I open up the packet and see tiny little seeds."
    $claire.set_state(with_dissolve, eyes="happy", emotion="sweat", eyebrows="default", mouth="grin", emotion_base="default")
    cl "Oh wow... They won't eat the fence, right?"
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="happy", eyebrows="default", emotion="flowers", emotion_base="default")
    voice "m_epi03"
    mi "Of course not! I took note you didn't want any carnivorous plants. It only needs a little sun and sugar water."
    $mirari.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    mi "Once they bloom, at night they release balls of light that resembles your world's fireflies. I keep one by my bedroom window sill, actually, so I thought..."
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="uh", eyebrows="default", emotion="sweat", emotion_base="default")
    voice "m_epi04"
    mi "It wouldn't be a hassle... I hope? I promise they're super harmless and similar to your earth flowers."
    $claire.set_state(eyes="happy", emotion="default", eyebrows="default", mouth="happy", emotion_base="default")
    cl "No, I love it. And I promise I'll water them."
    $mirari.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    $claire.set_state(with_dissolve, eyes="default", emotion="default", eyebrows="default", mouth="oh", emotion_base="default")
    cl "Is this the only reason you came to see me?"
    $mirari.set_state(with_dissolve, eyes= "closed", mouth="smile", eyebrows="default", emotion="default", emotion_base="small blush")
    "She twirls a strand of her hair, then grabs my hand."
    $mirari.set_state(with_dissolve, eyes= "tender", mouth="grin", eyebrows="default", emotion="default", emotion_base="small blush")
    voice "m_epi05"
    mi "No, I wanted to see you too. I thought, if you wanted to, we could be lovers."
    $mirari.set_state(with_dissolve, eyes= "wink", mouth="smile", eyebrows="default", emotion="default", emotion_base="small blush")
    voice "m_s01"
    mi "I enjoyed our little night together, and I'd love to give you more memories." 
    show mirari at bounce_down_alone2 
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "She leans in and we share a gentle kiss."
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "I'd like that."
    $mirari.set_state(with_dissolve, eyes= "default", mouth="happy", eyebrows="default", emotion="flowers", emotion_base="default")
    voice "m_epi06"
    mi "Wonderful! We should celebrate."
    $mirari.set_state(with_dissolve, eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    voice "m_epi07"
    mi "I think it's time for me to get a new babydoll. Shall we do a little shopping?"
    $claire.set_state(eyes="tender side", emotion="default", eyebrows="default", mouth="low", emotion_base="small blush")
    cl "True... If we're going to see each other often, I think I need more than one outfit..." 
    show mirari at sway
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="kitty", eyebrows="default", emotion="heart", emotion_base="small blush")
    voice "m_s01"
    mi "Ah, I'd love to dress you up in cute lingerie. It'll be a lot of fun. I think something with frills will look super adorable on you."
    $mirari.set_state(with_dissolve, eyes= "happy", mouth="smile", eyebrows="default", emotion="heart", emotion_base="small blush")
    $claire.set_state(eyes="happy", emotion="default", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "Sounds like a plan."
    $ persistent.mirari_replay = True
    stop music fadeout 1
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return
