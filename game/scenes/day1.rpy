label day1_morning:
    $current_day = 1
    scene black with dissolve
    play music music_claire
    play sound "assets/sfx/bird_chirp.ogg"
    pause (1.2)
    scene bg hallway_day with dissolve
    show portal with dissolve
    play sound "assets/sfx/portal_hum3.ogg"
    pause (0.5)
    $claire.set_state(mouth="low")
    cl "..."
    $claire.set_state(with_dissolve, mouth="uhh", emotion="sweat lots")
    cl "It's still here."
    play sound "assets/sfx/portal_whoop.ogg"
    "Hesitantly, I pick up a dirty, discarded sock and toss it into the purple portal. It vanishes into the void." 
    $claire.set_state(mouth="wavy", emotion="lll", eyebrows="inwards")
    cl "...I must still be tired. I should eat. I hope there's cereal left."
    scene bg kitchen with dissolve

    #kitchen
    $claire.set_state(emotion_base="small blush", emotion="flowers", mouth="kitty")
    cl "Something smells good... but why?"
    $kael.set_state(base="apron", eyes="default")
    show kael at center with dissolve
    ka "Good morning, [claire_name]. Did you have a restful sleep?" 
    $claire.set_state(emotion="sweat", eyes="dots", mouth="low", emotion_base="default")
    cl "...G-good morning..."
    "I slump down in my usual chair at the table."
    
    $kael.set_state(emotion="flowers", mouth="happy", eyebrows="up", eyes="happy" )
    show kael at speak
    ka "I thought the whole 'demons showing up in your house' must've taken a lot out of you, so I made breakfast. Look, it's even happy to see you."
    "He places a plate down before me and a smiley face made out of sunny-side up eggs and three strips of bacon stares back. The dish matches the demon's grin." 
    cl "Uh... thank you... Um..."
    $kael.set_state(**Emotion.normal())
    ka "Kael. Akki is the young redhead and Orias is the long-haired one. I think you'll remember Mirari since you met her first."
    hide kael with dissolve
    "He maneuvers back to the stove, and I slowly pick up my fork to poke at the fried yolk."
    $claire.set_state(emotion="default")
    cl "...It's... a dream, right?"
    "I pinch my cheek hard."
    $claire.set_state(eyes="clench tear", mouth="uhh")
    cl "Nnng, ow."
    "I scoop some of the egg onto my fork, then give it a cautious sniff before sampling it."
    $claire.set_state(emotion="flowers", emotion_base="small blush", eyes="wide", eyebrows="up", mouth="uh")
    cl "It's... good."
    stop music fadeout 4
    "The texture, the smell, the tinge of salt and pepper, it fills my mouth. I feel the weight as I chew, then swallow it."
    "There's no way this isn't real..."
    $claire.set_state(with_dissolve, emotion="default", eyes="bug cry", mouth="wavy")
    cl "I wasn't dreaming...?"
    $claire.set_state(eyebrows="inwards")
    cl "I..."

    $ claire.set_state(with_dissolve, eyes="cry")
    cl "I..."

    #SOBBING HARD
    ##Come back to this
    play music music_silly fadein 1
    "Tears splatter onto my plate as I continue eating."
    $claire.set_state(mouth="uhh")
    cl "It's better than cereal..."
    $kael.set_state(emotion="panic", eyebrows="inwards", mouth="wah", eyes="wide")
    show kael at center_alone with dissolve
    ka "A-are you okay? I never made someone cry over my cooking before. Does it taste that bad?"
    $claire.set_state(mouth="oh")
    cl "No, it's heavenly. Thank you for making this for me. I'm just overwhelmed at the moment. It's all real. You're real..."
    $claire.set_state(with_dissolve, mouth="wah")
    cl "...Waaaah..." 
    play sound "assets/sfx/cutlery_drop.ogg"
    "The fork clatters as I bury my head in my hands. For a few minutes I'm sobbing uncontrollably before my emotions quiet down into a soft sniffle."
    $ claire.set_state(eyes="closed", mouth="wavy", emotion_base="default")
    stop music fadeout 1
    cl "I think I'm good now. Seriously, sex demons..."
    play music music_daily
    $kael.set_state(with_dissolve, emotion="default", mouth="low", eyes="default")
    $claire.set_state(with_dissolve, eyes="semi open")
    cl "Sex demons who make breakfasts with happy faces..."
    $claire.set_state(with_dissolve, eyebrows="flat", eyes="default")
    cl "... while wearing my dad's apron."
    $kael.set_state(with_dissolve, eyes="happy", emotion="sweat", mouth="default")
    ka "It's a lot to take in, but I assure you you're safe with us. It'll only be for two days. Until then, please relax and enjoy yourself." 
    $kael.set_state(with_dissolve, eyes="default", eyebrows="default", emotion="default", mouth="default")
    ka "However you enjoy yourself is up to you."
    $claire.set_state(mouth="default", eyes="tender side", eyebrows="inwards")
    cl "Right..."

    show kael at center_group with dissolve
    show kael at mleft4 with move
    $orias.set_state(**Emotion.normal())
    show orias at right with moveinright
    
    ori "Feeling better? Here, some tea that'll help calm your nerves." 
    "Orias appears and gently sets down a fancy, unfamiliar tea cup and a flowery aroma fills the air. With slightly trembling hands, I take it."
    $claire.set_state(eyes="default", eyebrows="up", mouth="oh")
    cl "What kind of tea is it?"
    $orias.set_state(with_dissolve, mouth="oh", eyebrows="tender")
    show orias at speak
    ori "It's similar to your earth passionflower. I promise it's safe for humans; I've been brewing this type for centuries." 
    $claire.set_state(eyes="closed", mouth="smile", emotion="flowers")
    cl "Mm, smells like a meadow after the rain... It tastes amazing, too."
    $orias.set_state(with_dissolve, eyes="closed", mouth="default", eyebrows="inwards", emotion="sweat")
    ori "I'm glad to be of assistance. Your crying was, uh, quite alarming. I hope Kael didn't upset you."
    #kael =< =< =<
    $kael.set_state(emotion="panic", eyebrows="inwards", mouth="ah", eyes="clench", emotion_base="no nose")
    show kael at bounce_up
    ka "I'd never!" 
    $claire.set_state(emotion="default", mouth="uh", eyes="default", eyebrows="default")
    cl "Okay, if this isn't a dream... where are the others?"
    $orias.set_state(with_dissolve, eyes="side", eyebrows="default")
    $kael.set_state(with_dissolve,  eyes="happy", emotion="sweat", mouth="default", emotion_base="default")
    stop music
    with hpunch
    "???" "THESE GODDAMN BLUE SHELLS!"
    play music music_daily
    ka "Akki's in the living room, Mirari's in the garden." 
    $orias.set_state(with_dissolve, emotion="default", eyes="default", mouth="smile")
    ori "And I'll be returning to the miniature library. I've never seen so many books on modern human law before, it's fascinating."
    $claire.set_state(mouth="smile")
    cl "Oh, my dad's a lawyer so... And that's his office..."
    $orias.set_state(with_dissolve, eyebrows="inwards", mouth="default")
    ori "Would it be rude to continue browsing?"
    $claire.set_state(eyes="happy")
    cl "Nah, it's okay. He probably hasn't touched those books in years anyway. Just put it back when you're finished."
    $orias.set_state(eyes="closed", eyebrows="default", mouth="smile")
    ori "I will. Thank you."
    
    #orias leaves
    hide orias with dissolve
    show kael at center with move
    show kael at speak
    $kael.set_state(**Emotion.normal())
    ka "Sounds like you're much calmer now."
    cl "The tea helped and... you guys seem nice. I haven't had people dote on me in a long time."
    $claire.set_state(with_dissolve, emotion_base="small blush", eyes="tender side", eyebrows="inwards", mouth="low")
    cl "Um... do I still have to... you know..."
    $kael.set_state(with_dissolve, eyes="closed")
    ka "Only if you're comfortable. We wouldn't pressure you to do something you'd rather not."
    $claire.set_state(eyes="happy", mouth="smile", emotion="sweat")
    cl "I see. I mean it's still bizarre that there's mystical beings crashing at my house, but I promise I won't freak out anymore. Or pinch myself."
    $claire.set_state(with_dissolve, emotion="default", emotion_base="default", eyes="default", eyebrows="default")
    cl "Thanks again for the breakfast, Kael."
    $kael.set_state(with_dissolve, eyes="happy", mouth="happy")
    ka "Anytime."
    hide kael with dissolve
    "He takes the dishes, and I stand up, wondering what to do now."
    cl "(Who should I spend time with?)"

    jump choose_a_place_to_hangout

   

label day1_afternoon:
    play music music_claire fadein 1
    scene black with dissolve
    scene bg hallway_day with dissolve
    $claire.set_state(emotion="default", eyes="default", mouth="smile", eyebrows="default", emotion_base="default")
    "I had a nice lunch... Now what?"
    cl "(Who should I spend time with?)"
    jump choose_a_place_to_hangout
   