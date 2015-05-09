label kael_hangout1:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_kael
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    scene bg hallway_day with dissolve
    $claire.set_state(eyebrows="up", mouth="uh")
    cl "What is he doing...?"
    if current_day == 1:
        cl "Cooking and now cleaning..."
    cl "Kael?" 
    show kael at center_alone2 with dissolve   
    "He pauses and adjusts the overflowing laundry basket in his arms."
    show kael at bounce_up_alone2
    ka "[claire_name], can I help you?"
    $claire.set_state(eyebrows="flat", emotion="sweat", mouth="smile")
    cl "Um... I was wondering why you were doing the laundry."
    $kael.set_state(with_dissolve, emotion="bars", mouth="ah", eyebrows="up")
    ka "Oh."
    "He sets the basket down, and pulls out a note tucked by his hip. I accept it, instantly recognizing the handwriting."
    $kael.set_state(with_dissolve,**Emotion.normal())
    "'PLEASE PLEASE do your laundry while we're gone! Love, Mom'"
    $claire.set_state(emotion="lll", emotion_base="dark", eyes="flat")
    cl "..."
    "Now I remember. My parents left a few (too many) memos posted on the fridge. I guess he noticed when he made breakfast..."
    $kael.set_state(with_dissolve,emotion="default", eyebrows="default", eyes="happy", mouth="smile")
    ka "I thought, since we're here and all, I could help out since you've fallen behind."
    $kael.set_state(with_dissolve, eyebrows="inwards", eyes="default", mouth="neutral")
    ka "How long have your parents been gone? Over a week I assume from the clothes."
    $claire.set_state(mouth="smile", eyes="fun side")    
    cl "They left only a few days ago."
    $kael.set_state(with_dissolve, emotion_base="dark", eyes="fun front", mouth="low", eyebrows="default")
    ka "..."
    $claire.set_state(eyes="flat", mouth="uhh", eyebrows="inwards", emotion="sigh")
    cl "I know, I know, I've been a slob."
    $kael.set_state(with_dissolve, eyes="closed", emotion_base="default", eyebrows="one up", mouth="fun smile")
    ka "Being genuinely lazy or has something been bothering you?"
    $claire.set_state(eyes="tender side", mouth="low", emotion_base="default", emotion="default")
    cl "I shouldn't excuse my behaviour, but yea it's a bit of the latter..."
    $claire.set_state(with_dissolve, eyes="down", mouth="oh")
    cl "I've mostly been studying and neglecting the chores." 
    $claire.set_state(with_dissolve, eyes="flat", mouth="low")
    cl "I feel all I've been doing lately is hitting the books..."
    $kael.set_state(with_dissolve, eyes="default", emotion_base="default", mouth="low", eyebrows="up")
    ka "Hm?"
    $claire.set_state(emotion="sweat", eyes="happy", mouth="smile")
    cl "Ah, sorry, it's, well... University hasn't been turning out as fun as I hoped. And now all my friends are out there, dating or meeting people this spring break." 
    $claire.set_state(with_dissolve, eyes="fun front", eyebrows="flat", mouth="uhh", emotion_base="dark")
    $kael.set_state(with_dissolve, eyebrows="inwards")
    cl "I thought maybe I just need a little family time instead. Of course as soon as I come back, my parents are on a lovely-dovely trip to Mexico and my brother's at baseball camp with his teammates." 
    $kael.set_state(with_dissolve, eyes="happy", mouth="smile", emotion="sweat")
    $claire.set_state(with_dissolve, eyes="fun side", mouth="pout")
    cl "Everyone has plans but me."
    "I let out a self-deprecating laugh, but it comes out more bitter than I expect."
    "I shove the note into my pocket and Kael gives a thoughtful nod."
    $kael.set_state(with_dissolve, eyes="tender", emotion="default", mouth="neutral")
    ka "I can't say I know much about this university or spring break thing... but I know what it's like to feel alone."
    $kael.set_state(with_dissolve, emotion="note", eyes="default", mouth="smile", eyebrows="default")
    ka "It's not much, but I'll do what I can to get you back on your feet at least. Maybe you'll feel better once the house is clean and it gives you a peace of mind." 
    $kael.set_state(with_dissolve, emotion="default", eyes="wink", mouth="happy")
    ka "Besides, you have four people hanging around. Can't be that lonely now, right?"
    $kael.set_state(with_dissolve, eyes="closed", mouth="ah", eyebrows="up")
    ka "Of course, I expect you to pick up the slack. I'm an incubus, not your mom." 
    $claire.set_state(mouth="vhappy", eyes="happy", emotion_base="default", emotion="flowers", eyebrows="inwards")
    cl "...Hahaha. I never thought I'd hear an incubus say that."
    $kael.set_state(with_dissolve, eyes="up", mouth="low")
    ka "...Believe me, that's not the first or last time I'll say those words to someone. Blame my being a stickler for cleanliness." 
    $claire.set_state(emotion="default", eyes="tender", eyebrows="flat", mouth="uh")
    cl "You're not trying to butter me up or earn points or something, right?"
    $kael.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="closed")
    "He shakes his head, then picks up a discarded sock forgotten in the hallway. Why is there only one sock, though...?"
    $kael.set_state(with_dissolve, eyes="tender")
    stop music fadeout 2
    ka "I'm simply being me. We all are. We'd like you to feel comfortable around us; there's no point in being dishonest about who we are." 
    hide kael with dissolve
    show chibi_kael01 at chibi_scene with dissolve
    $ gallery.unlock("chibi_kael01")
    play music music_silly fadein 2
    "He picks up the basket, and it's then I spot some lacy underwear on the pile."
    cla "Ah, I'll wash those!"
    "I grab my unmentionables, and Kael looks at me in surprise."
    ka "Really? Well, if you dig through the pile there's more—"
    cla "WHAT!?"
    cla "I-I'll do my personal load! Come back in a few minutes once I gather them. I can at least do that!"
    ka "Deal."
    hide chibi_kael01 with dissolve
    stop music fadeout 2

    jump next_day


label kael_hangout2:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    scene bg living_room with dissolve
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    $renpy.pause(0.4)
    
    scene bg living_room with dissolve
    play sound "assets/sfx/glass_crash.ogg"
    "Crash!"
    $claire.set_state(eyes="wide", eyebrows="up", mouth="wavy", emotion="shock")
    cl "What was that?"
    play music music_kael fadein 2
    $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="low" )
    show kael at center_alone with dissolve
    "I hurry to the living room and spot Kael staring at the floor with wide eyes."
    $kael.set_state(eyebrows="inwards", emotion="panic", mouth="ehh")
    "There's a shattered picture frame, with pieces of glass scattered before the fireplace. Kael kneels down, his hands hovering over the mess, wondering what to do." 
    $claire.set_state(eyebrows="inwards", mouth="oh", emotion="default", eyes="default")
    cl "What happened?"
    show kael at sway
    $kael.set_state(eyes="bigcry", mouth="wah", emotion_base="no nose")
    ka "[claire_name], I apologize! I was dusting the mantle and this frame tipped over..."
    show kael at sway
    $kael.set_state(with_dissolve, eyes="clench")
    ka "Careful, I don't want you to cut yourself."
    $kael.set_state(with_dissolve,emotion="default", mouth="wavy", eyes="default", emotion_base="default")
    "I crouch down beside him and gingerly pluck out the photograph. It's an old picture of my family standing in front of a twisty arbutus tree from some park." 
    $kael.set_state(with_dissolve,eyebrows="default", mouth="low")
    "Kael peers at it curiously."
    $kael.set_state(with_dissolve,mouth="ah", emotion="bars", eyebrows="up", eyes="wide")
    ka "Is... that... you?"
    $claire.set_state(eyebrows="inwards", mouth="smile", eyes="tender")
    cl "Yes, when I was ten. This is my mom, dad, and the one in the dinosaur jacket is my little brother when he was four." 
    $kael.set_state(with_dissolve, emotion="default", eyes="default", eyebrows="default", mouth="happy")
    ka "Fascinating... You look so different. Smaller frame and knobby knees."
    $claire.set_state(eyebrows="flat", mouth="uh", eyes="default")
    cl "Huh? Well yea, I was a kid. Then I grew up. Is it the same for incubi and succubi?"
    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
    ka "Not at all. When we're, um, 'born', we're already as we are. I've always found the human nuclear family interesting since we don't have our own."
    $kael.set_state(with_dissolve, eyes="tender")
    ka "We also live alone for the most part. It's rare for our kind to stay together."
    $claire.set_state(eyebrows="up")
    cl "Then... what about you, Akki, Orias and Mirari? How did you all get acquainted?" 
    $kael.set_state(with_dissolve,eyes="closed", mouth="happy")
    ka "I found Orias and Mirari passed out and injured while I was exploring a forest in the demon world."
    $claire.set_state(mouth="uhh", emotion="sweat")
    cl "What happened? Were they okay?"
    $kael.set_state(with_dissolve, eyes="happy", emotion="sweat", eyebrows="inwards", mouth="smile")
    ka "Yes. As soon as I patched them up, they jumped into the fray again... They were, uh, rather vehement in taking down a monstrous flower."  
    $claire.set_state(eyes="dots", mouth="oh", eyebrows="inwards")
    cl "Mirari I can imagine, but Orias?"
    $kael.set_state(with_dissolve, eyes="wink", mouth="grin")
    ka "He can be stubborn when it comes to creating new tea blends... Of course, I didn't know that at the time." 
    $kael.set_state(with_dissolve, **Emotion.normal())
    ka "We stuck together after that. Someone has to make sure those two stay out of trouble." 
    $claire.set_state(eyes="happy", eyebrows="default", mouth="smile", emotion="default")
    cl "Hehe, and Akki?"
    $kael.set_state(with_dissolve, emotion="default", mouth="ah", eyebrows="up")
    ka "He's the youngest incubi I know of. When we're born, aside from basic knowledge of our identity and how to survive, we're essentially a blank slate."
    $kael.set_state(with_dissolve, eyes="wink", mouth="smile", eyebrows="default")
    ka "After we found him, we took him under our wing. He's still learning how to use his powers and it's his first time in the human world. Keep it a secret, but he's easier to manage than the other two."
    $kael.set_state(with_dissolve, eyes="happy", emotion="note")
    ka "That's my 'family' for you."
    cl "Aw, it's a wonderful family. I'm pretty close to my parents, although my brother can be a brat when he hogs all the video games and saves over my files." 
    "Still, I glance fondly at the photograph."
    $kael.set_state(with_dissolve, eyebrows="inwards", eyes="dots", mouth="low", emotion="lll", emotion_base="dark")
    ka "Again, sorry about the mess..."    
    $claire.set_state(eyebrows="inwards", emotion="sweat", eyes="default")
    cl "Don't worry, it'd be believable that I accidentally knocked it over. I think my parents will be more surprised over a tidy room than a broken frame."
    $claire.set_state(with_dissolve, eyes="happy", emotion="default", eyebrows="default")
    cl "I can buy another one later, anyway. I'll grab a broom."

    jump next_day


label kael_hangout3:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $kael.set_state(base="default",**Emotion.normal())
    $claire.set_state(**Emotion.normal())
    $renpy.pause(0.4)
    play music music_kael
    scene bg kitchen with dissolve
    play sound "assets/sfx/chopping.ogg"
    $claire.set_state(eyes="flat", mouth="pout", emotion_base="dark", eyebrows="frown", emotion="lll")
    cl "Twenty minute stir-fry my butt. It's taking me ten for chopping veggies." 
    "I glance at the directions saved on my phone and continue slicing a large carrot." 
    $kael.set_state(eyebrows="up", mouth="ah")
    show kael at center_alone2 with dissolve
    ka "Oh? This is a surprise. You can cook?"
    $claire.set_state(eyebrows="inwards", mouth="low", eyes="tender side", emotion="sweat", emotion_base="small blush")
    cl "Not at all, but when I see you doing all my chores around the house... I couldn't just laze around doing nothing."
    $claire.set_state(with_dissolve, eyes="default", mouth="smile", emotion_base="default")
    cl "I thought maybe I could step in and cook a decent meal at least."
    $claire.set_state(with_dissolve, mouth="happy", eyebrows="default", eyes="happy")
    cl "Um, thanks for that. I think it was the push I needed to start being more proactive." 
    $kael.set_state(with_dissolve, emotion="flowers", mouth="happy", eyes="happy")
    ka "I'm glad. Do you want me to help you prep the ingredients at least?"
    cl "Nah, I got this, honest I—"
    stop music fadeout 3
    "Do carrots normally ooze red juice when cut?"
    $claire.set_state(eyes="dots")
    cl "..."
    play music music_silly fadein 2
    $claire.set_state(with_dissolve, eyes="big", mouth="fun ah", emotion="shock", eyebrows="inwards", emotion_base="dark")
    cl "OW! FRICK!" 
    $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
    ka "Are you okay?"
    "He rushes to my side as I examine my injured finger. He reaches to have a look at it, but I hold the wound close to my chest."
    $kael.set_state(emotion="panic", mouth="wah", eyes="big", eyebrows="inwards", emotion_base="dark")
    show kael at center_group with dissolve
    "Kael seems confused but steps back to give me room. If anything, he's panicking more than me."
    $kael.set_state(with_dissolve, eyes="dots", mouth="wavy", emotion="sweat lots")
    ka "It's okay, I know how human bodies work. One minor cut and it's fatal unless treated. Do you have a medical kit? "
    $claire.set_state(emotion="sweat", eyes="happy", mouth="smile", emotion_base="default")
    stop music fadeout 2
    cl "I don't think it's that serious... but the first-aid kit should be beside the fridge." 
    play music music_kael fadein 2
    $kael.set_state(with_dissolve, eyes="default", emotion="default", mouth="low", emotion_base="default")
    "He urges me toward the counter, and I sit on its surface while he rummages through the kit."
    "He pokes around the supplies and selects what he needs."
    $claire.set_state(eyebrows="up", eyes="default", mouth="uh", emotion="default")
    cl "You seem familiar with human medicine; I'm impressed."
    $kael.set_state(mouth="neutral")
    show kael at center_alone2 with dissolve
    "He applies a clean disinfecting wipe to my finger, and I bite my lip from the slight pain."
    $kael.set_state(with_dissolve, mouth="smile", eyes="tender")
    ka "It's something I picked up whenever I stay in the human world."
    $kael.set_state(with_dissolve, eyebrows="default")
    ka "The med— first-aid kits may change appearances over the years, but the contents and uses are roughly the same." 
    $kael.set_state(with_dissolve, eyebrows="inwards", mouth="grin", eyes="happy")
    ka "Although the band-aids usually don't have dinosaur patterns." 
    $kael.set_state(with_dissolve, emotion="note", eyebrows="up", eyes="default", mouth="happy")
    ka "Ta-da, you're good to go."
    "I wiggle my newly bandaged finger."
    $claire.set_state(eyebrows="inwards", mouth="smile")
    $kael.set_state(with_dissolve, **Emotion.normal())
    cl "Thanks... Sorry about keeping my hand away from you earlier."
    $claire.set_state(emotion="sweat", eyes="happy")
    cl "I thought you were gonna do something weird like suck the blood or stick it in your mouth, being a demon and all."
    $kael.set_state(with_dissolve, eyebrows="one up", eyes="fun front", mouth="ah")
    ka "I'm not a vampire. I don't go around sticking bloody, onion-smelling fingers into my mouth. It's not sanitary." 
    $kael.set_state(with_dissolve, eyes="closed", mouth="smile")
    "He holds up my hand and teasingly nibbles a knuckle, causing me to giggle."
    $claire.set_state(mouth="happy", eyes="clench", emotion_base="small blush")
    cl "I'm sorry."
    $kael.set_state(with_dissolve, eyes="tender", eyebrows="frown")
    ka "And I guess you expected me to do this next, right?"
    "He leans in, then delivers a cold puff of air to my neck. The ticklishness catches me by surprise and I squeal, falling back." 
    stop music fadeout 2
    $claire.set_state(eyes="wide", eyebrows="up", mouth="oh", emotion="default")
    cl "Oh—"
    play music music_romance fadein 2
    show kael at bounce_down_alone2
    $kael.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="shock")
    ka "Whoa—"
    "He wraps his arms around my back and pulls me close. My chin rests on his shoulder and I can feel my face warming up from the contact."
    $kael.set_state(with_dissolve, emotion="sweat", eyes="tender", eyebrows="inwards", mouth="smile")
    ka "Um, I apologize. I went too far with that joke..."
    $claire.set_state(emotion_base="large blush", eyes="down", eyebrows="inwards", mouth="smile")
    cl "I-it's okay..."
    hide kael with dissolve
    "We separate, and Kael immediately busies himself by packing up the kit. I hop off the counter and resume cutting veggies, albeit cautiously." 
    $kael.set_state(**Emotion.normal())
    $kael.set_state(eyes="wink")
    show kael at center_alone2 with dissolve
    ka "Want me to help with your meal? You'll learn faster that way. You'll still do most of the work, of course."
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion_base="default", emotion="sweat")
    cl "Deal. I don't want to have four demons keel over from food poisoning; it'd be improper hosting." 
    $kael.set_state(with_dissolve, eyes="happy", mouth="happy")
    "He laughs and starts washing the broccoli. For a few minutes, there's a comfortable silence between us."
    $kael.set_state(with_dissolve, eyes="tender", emotion="heart", mouth="smile", emotion_base="small blush")
    ka "[claire_name], if you happen to pick me tonight... I'd like that. I promise to make your spring break a memorable one." 
    $claire.set_state(emotion_base="large blush", eyes="tender", eyebrows="inwards", mouth="smile", emotion="default")
    cl "Thank you..."

    jump next_day
    

# label kael_sex:

#     show screen sex_stop("kael_stop_now")

#     cl "Here I go..."
#     "I knock on the bedroom door, which is already slightly open." 
#     cl "Kael, are you in there? Can I enter?"
#     ka "Feel free."
#     "Inside, I can hear soft classical music as a soothing backdrop. I guess he figured out how to work my neglected CD player..." 
#     ka "You look adorable, [claire_name]."
#     "I approach him and he takes my hand, raising it over my head. Coupled with the music, I take the cue and give a little twirl." 
#     ka "Blue is a lovely colour on you, but that could just be my bias." 
#     cl "Thank you, Kael..." 
#     "He guides me to the bed, and he makes himself comfortable on his side, and I hesitantly follow suit."
#     ka "Still nervous?"
#     cl "Yeah. I think it's mostly the, uh, experience gap."
#     ka "If it helps, since this is your first time, we'll focus on you. There's no right or wrong way to this and we can stop at anytime."
#     ka "Just be honest about how you feel, and I'll do my best. If there's anything you want to try or do, let me know."
#     cl "W-well since this is my first experience... I'm not even sure what I'd like or dislike, myself..."
#     ka "Trial and error is part of the process. We'll take everything slow."
#     ka "Besides, we still need to warm you up first."
#     "He leans in and gives me a gentle kiss on the forehead, his hand seeking mine, intertwining our fingers together."
#     ka "Ready?"
#     menu:
#         "Yes.":
#             cl "Yes. Thanks for easing my mind."
#             ka "No problem. I want it to be a fun experience for you."
#             $ kael_sex_choices.kissing = True
#             "His hand moves to cup my cheek, stroking it sensually with his thumb. He gazes tenderly at me before closing the distance, his lips meeting mine." 
#             "At first the kisses are quick tastes, lightly brushing the surface, then gradually deepen once I tilt my head and welcome a firmer approach. When our lips lock, I inhale sharply, taking note of his earthy scent." 
#             "I wrap my arm around him, cradling my hand under his head to encourage him and he responds mutually by running his fingers through my hair."
#             "His hand travels down my arm, leaving behind goosebumps, then stops at my elbow. He breaks the kiss to gauge my flushed expression."
#             ka "Feeling okay? Should I keep going?" 
#             "I feel a finger linger over the side of my torso, then stop under my chest." 
#             menu:
#                 "Yes.":
#                     cl "I'd like that."
#                     $ kael_sex_choices.kissing = False
#                     $ kael_sex_choices.foreplay = True
#                     "He resumes kissing me passionately, his hand moving upward before cupping one breast. He fondles me in circular motions, applying an occasional light squeeze before moving to the other breast. After he repeats the actions, his thumb brushes over my erect nipple."
#                     "Even through the sheer fabric, his touch stirs something within me and I breathe in a longing sigh."
#                     "Kael's foot touches mine, playfully rubbing against me before brushing my farthest leg. After another kiss, his leg slowly moves over mine, closing the distance between us."
#                     "Something hard presses against my hip and I move my hand to his lower back. He shuffles closer until our hips touch. I break off the kiss with a gasp, nuzzling my face against his shoulder."
#                     ka "Would you feel comfortable with your chemise off?"
#                     "His fingers tease my chemise strap, giving it a little tug, looking at me for approval. I respond by pulling it off as he helps lift it up. After undressing, his hands freeze at his collar when he sees my exposed front."
#                     cl "How do I look?"
#                     ka "Really beautiful..."
#                     "He fumbles with the collar briefly, causing me to giggle, and I assist him. Once it's removed, he playfully embraces me close, ruffling my hair and kissing my forehead. Our legs intertwine again, with his weight slightly over me."
#                     ka "Would you like me to lie on top of you, or would you prefer to be on top?"
#                     menu:
#                         "Kael on top.":
#                             $ kael_sex_choices.before_pillow = True
#                             $ kael_sex_choices.foreplay = False
#                             $ kael_sex_choices.top_first = True
#                             cl "I'd like you on top."
#                             ka "Alright."
#                             "Untangling our legs, he shifts his weight until he straddles over me. Holding my hand, he kisses me deeply as he slowly lowers himself on top of me."
#                             ka "Not too heavy?"
#                             cl "No."
#                             "We resume kissing, and he adjusts his elbows until he finds his ideal position. His chest heaves against mine, and I can feel my heartbeat race from our proximity."
#                             "His hardness presses into my thighs, sending shivers up my spine and a warmth radiating from my lower belly. Gradually my legs open, and he moves his knees between them. I feel a moan in my throat when his hip aligns against mine."
#                             "My underwear clings to me from the moisture as he teasingly dips into me before continuing with long, unhurried strokes."
#                             "We break the kiss with a laboured gasp and Kael gazes at me. His hand travel down my side, then slips a finger under the lace of my panties."
#                             ka "Would you feel comfortable if we took this further?"
#                             $ kael_sex_choices.before_pillow = False
#                             $ kael_sex_choices.undressing = True
#                             menu:
#                                 "Yes.":
#                                     cl "I would."
#                                     "I sit up as he withdraws, giving him easier access .When he brushes over my pubic hair, my face goes warm."
#                                     $ kael_sex_choice.undressing_scene_top = False
#                                     jump kael_undressing_scene
                                    
#                                 "I'd like to stop now.":
#                                     jump kael_stop_now
                                 
#                         "Be on top.":
#                             $ kael_sex_choices.claire_top = True
#                             $ kael_sex_choices.foreplay = False
#                             $ kael_sex_choices.top_first = False
#                             cl "I'd like to be on top."
#                             "He rolls to his back, and I wait until he's ready. He extends a hand, I take it, and he guides me to his hips. I crawl over him, hovering awkwardly."
#                             cl "..."
#                             "I gently lower myself down until my chest rests on his, with my hands beside his shoulders. His heart races against mine, and his entire body feels warm to the touch."
#                             cl "I'm not heavy?"
#                             ka "No, this feels great." 
#                             "He embraces me and we resume kissing, his legs rubbing against mine playfully. The friction causes my body to heat up, and I shift ever so slightly against him, his hardness pressing against my belly." 
#                             "One hand rubs my back, while the other caresses my head, his fingers combing through my hair. While we kiss, I find my hips inching higher and higher, until he's between my legs."
#                             "He pushes against me, and even through the damp fabric I can feel a slight throb, sending pleasant shivers from my core. I squirm, wanting to become even closer to him."
#                             "Kael separates from our kiss, and gives me a tender look. His hand travels from my shoulder blade down to my thigh, then traces his fingers over the lace of my panties."
#                             ka "Would you like to go further?"
#                             $ kael_sex_choices.claire_top = False
#                             menu:
#                                 "Yes.":
#                                     $ kael_sex_choices.undressing = True
#                                     cl "I would."
#                                     "We both sit up to make this easier, and Kael slowly pushes my underwear down, his fingers brushing the edge of my pubic hair."  
#                                     jump kael_undressing_scene
                                    
#                                 "I'd like to stop now.":
#                                     jump kael_stop_now
                            
#                         "I'd like to stop now.":
#                             jump kael_stop_now
                            
#                 "I'd like to stop now.":
#                     jump kael_stop_now
               
#         "I'd like to stop.":
#             "My hand goes limp in his, and I glance away."
#             cl "Um, I don't think I am..."
#             cl "Sorry."
#             ka "That's okay. You shouldn't force yourself if you feel you're not ready."
#             ka "Would a cuddle suffice?"
#             cl "Yeah... I'd like that."
#             "I roll over and Kael hugs me from behind, his body pressing against mine. His breath warms the base of my neck, and the soft music drifts through the room." 
#             "Relaxed, and secure in his arms, I close my eyes and fall into a restful sleep." 
#             jump credits



# label kael_undressing_scene:
#     cl "Um, sorry, I didn't really... shave down there...only trimmed..."
#     "I curl up my legs so he can remove my panties, and he sets them aside."
#     ka "I wouldn't worry about that, I think you're cute the way you are."
#     ka "Besides, I'm not one to judge."
#     "Winking, he unties the sash around his waist, loosening the loincloth. After removing it, I peek down then shyly look away. Our eyes meet, and we both let out an amused chuckle."
#     cl "Ah, no wonder... I like the way you are, too."
#     ka "Thank you."
#     if kael_sex_choices.condom:
#         "He reaches over for the condom wrapper on the nightstand, and I politely glance away until he's done."        
#     $ kael_sex_choices.undressing = True
#     ka "Before we continue, would you like to switch positions?"
#     if kael_sex_choices.top_first:
#         ka "In case you'd like me on top this time."
#     else:
#         ka "In case you'd like to be on top this time."
#     cl "I..."
#     menu:
#         "Switch positions.":
#             $ kael_sex_choices.switched_positions = True
#             if kael_sex_choices.top_first:
#                 cl "Sure, sounds like fun."
#                 ka "I understand, and you'll have more control this way." 
#                 jump kael_claire_bottom
#             else:
#                 cl "Sure, let's change it up."
#                 ka "I understand. Oh, before we start..."
#                 jump kael_claire_top
                    
#         "I'm good.":
#             $ kael_sex_choies.switched_positions = False
#             cl "I'm good, thanks for asking."
#             ka "No problem then. Now..."
#             if kael_sex_choices.top_first:
#                 jump kael_claire_top
#             else:
#                 jump kael_claire_bottom
                
#         "I'd like to stop now.":
#             jump kael_stop_now


# label kael_claire_top:
#     if kael_sex_choices.switched_positions:
#         "He rests on his back, extending a hand. I take it, and he guides me to his hips. I crawl over him, hovering awkwardly."
#         $ kael_sex_choices.claire_top = True
#         cl "..."
#         "Gingerly, I straddle over his hips, resting on my knees. I can't help but glance downward before I lower myself onto him."
#     else:
#         "Once he's on his back, I straddle over him, pausing briefly to glance downward, before I lower myself again."
#         $ kael_sex_choices.claire_top = True
#     ka "Like what you see?"
#     cl "I... couldn't see under that hair."
#     ka "Oh, getting cheeky are we?"
#     "He lightly pinches my cheek, and I giggle in response."
#     cl "O-okay, I like what I see..."
#     "He shifts his head until I feel his hot breath against my ear and lowers his voice to a sultry tone."
#     ka "I like what I see, too." 
#     "My face flushes and he ruffles my hair."
#     if kael_sex_choices.switched_positions:
#         cl "And I'm not too heavy?"
#         ka "Not at all."
#     "He playfully hugs me close, smothering my forehead with adoring kisses before seeking my mouth, and I happily accept the kiss."
#     "Kael guides my hips until his shaft presses against my lower lips, then places his hands on my back, encouraging me to move how I'd like." 
#     "I experiment with a side to side motion until I settle on a sensual back-and-forth, rubbing my clit against his tip."
#     "A moan escape my lips as the initial ticklish sensation becomes deeper, wetter, more pleasurable. My hips migrate higher until he's pressing against my entrance, and he gently breaks off the passionate kiss."

#     ka "Would you like to keep going?"
#     menu:
#         "Yes.":
#             cl "Yes... although..."
#             cl "Um... how would I go about this...?"
#             jump kael_claire_top_sex
#         "I'd like to stop now.":
#             jump kael_stop_now


# label kael_claire_bottom:
#     "Kael grabs a pillow next to me."
#     ka "Here, it'll ease your back, and make you more comfortable since I'm bigger..."
#     cl "Bigger?"
#     ka "Ah, height. My stature. I was only referring to that, I swear."
#     "A rare blush spreads across his face as I lift my back and he slides the pillow underneath."
#     $ kael_sex_choices.kael_on_top = True
#     $ kael_sex_choices.before_pillow = False
#     "Once I'm settled, he crawls over me and repositions himself. He catches me staring and he teasingly leans in to block my view."
#     ka "Like what you see?"
#     cl "I... couldn't see under that hair."
#     ka "Oh, getting cheeky are we?"
#     "He lightly pinches my cheek, and I giggle as he tickles my forehead with adoring air kisses."
#     cl "O-okay, I like what I see..."
#     "He shifts his head until I feel his hot breath against my ear and lowers his voice to a sultry tone."
#     ka "I like what I see, too." 
#     if kael_sex_choices.switched_positions:
#         "I feel my face flush, and he lowers until his chest touches, and aligns his hips against mine."
#         ka "I'm not too heavy?"
#         cl "No."
#         "With my pelvis elevated, he settles between my moist thighs then glides back and forth."
#     else:    
#         "I feel my face flush, and he lowers until his chest touches, and aligns his hips against mine. With my pelvis elevated, he settles between my moist thighs then glides back and forth."

#     "A soft moan escapes my lips as Kael delves deeper with each stroke, until I can feel a gentle pressure against my entrance. I embrace him and relax my head on the pillow, closing my eyes." 
#     ka "How does that feel? Should I keep going?"
#     menu:
#         "Yes.":
#             cl "Feels wonderful. You can keep going, just um..."
#             "He gropes for my hand then gives it a tender squeeze."
#             ka "I'll take it slow. Ready?"
#             cl "Yes."
#             jump kael_claire_bottom_sex
                
#         "I'd like to stop now.":
#             jump kael_stop_now


# label kael_claire_top_sex:
#     ka "I'll help. Here, lift your hips a bit..."
#     "He grabs himself, and I can feel his tip deliberately rub against my clit before he continues. He gently nudges against my entrance but doesn't apply any firm pressure."
#     ka "I've got you. Slowly lower,and take your time."
#     $ kael_sex_choices.claire_top = False
#     $ kael_sex_choices.claire_top_inside = True
#     "His other hand rests on my thigh for support, and I sturdy my arms next to his shoulders. After a deep breath, I press down gingerly, feeling him nudge into me."
#     "Kael removes his hand from under me and I gasp when I feel him slide deeper, and pause to recover from the sensation."
#     ka "Everything alright?"
#     cl "Yea... I'll take my time..."
#     "It's tight but I continue, letting him slowly fill me. I pause to adjust, but now the initial shock is over and it becomes easier. Kael starts stroking my thighs softly to help me relax as my chest meets his."
#     "I open my eyes when I realize our hips are connected. For a moment we gaze at each other, saying nothing and I wonder what I can say regarding this physical milestone."
#     cl "That... didn't hurt like I thought it would."
#     ka "I'd never do that. Who do you think you're with?" 
#     if kael_scenes >= 3:
#         cl "True, considering how you panicked when I cut myself earlier."
#         ka "I was worried about you, alright?"
#     "He pouts and tickles my sides, causing me to giggle."        
#     cl "I thought sexytimes were all about serious intimate moments?" 
#     ka "How do you think people react when they see my bush?" 
#     "I laugh and it causes my stomach muscles to twitch, making me very aware that he's inside me."
#     cl "Don't make me laugh... that felt good."
#     ka "That's a promising sign. Think you'll be okay moving around?"
#     cl "Yeah... I might try some weird angles or something so I apologize in advance..."
#     ka "Everyone's different. You'll find what feels good."
#     "Curiously, I subtly rock back and forth. At first there's nothing, but gradually I feel a pleasant sensation welling up. Kael's fingers massage my breast while his other hand helps guide my hips, keeping up with my rhythm."
#     "I experiment side to side, up and down, but soon I find a tempo my body loves, and continue the pattern. His pubic bone rubs against my clit, making me moan whenever I press against him, and Kael responds by cupping and teasing my other breast as well."
#     # [TODO]
#     #remove stop button until menu
#     "The multiple sensations merge into one, and my mind clouds over in a blissful haze. My thighs burn, but I endure it until I feel the first shudder. I buck, my arms unable to support myself anymore."
#     "Like a wave, the intensity slowly ebbs away, leaving a few pleasurable jolts up and down my limbs." 
#     cl "... wow..."
#     ka "Looks like you enjoyed it."
#     cl "Looks...?"
#     ka "Seeing you climax on top of me was quite the sight."
#     cl "... Omigosh..."
#     "I cover my face and Kael chuckles, leaning in."
#     ka "You were fine."
#     jump kael_sex_final


# label kael_claire_bottom_sex:
#     $ kael_sex_choices.kael_on_top = False
#     $ kael_sex_choices.kael_inside = True
#     cl "Ah..."
#     "His tip nudges into me and a shock of pleasure radiates from my stomach, along with a stretching sensation."   
#     ka "You okay?"
#     cl "Good... tight but not unpleasant."
#     "He kisses my forehead then increases the pressure just a little bit more, stopping to gauge my reaction. After a sharp inhale, I relax, letting my body get used to the sensation."
#     "Each movement becomes slicker from how wet I've become, and I sense him take a deep breath before continuing."
#     "We both gasp as I feel the expansion within me, massaging me from the inside." 
#     "Our bodies join, and his chest lightly rests against mine as I embrace him. For a moment we say nothing and I wonder what I can say regarding this physical milestone."
#     cl "That... didn't hurt like I thought it would."
#     ka "I'd never do that. Who do you think you're with?" 
#     if kael_scenes >= 3:
#         cl "True, considering how you panicked when I cut myself earlier."
#         ka "I was worried about you, alright?"
#     "He pouts, then teasingly blows an air kiss against my neck, causing me to giggle."
#     cl "I also thought sex was all serious sexytimes and no laughing."
#     ka "I allow moans of ecstasy and giggling here. Even the occasional, 'Oh, god, yes.'"
#     "I burst out laughing from his tone, unwittingly causing my pelvic muscles to contract around him, and I dissolve into a half-chuckle half-gasp."
#     cl "Don't make me laugh... that felt good."
#     ka "I'll take it easy, okay? Let me know if it starts to feel uncomfortable." 
#     "After adjusting his elbows, he begins a deep, sensual stroke followed by shallow thrusts. At first I feel nothing, then the friction and warmth starts to build inside. The base of his shaft rubs against my clit, escalating the sensation."
#     "Whenever it starts to become too intense or monotonous, he senses the cues in my voice and expression then changes angles or tempo. My hips squirm under the constant, but pleasant, pressure in my lower belly."
#     # [TODO]
#     #remove stop button and return for menu
#     "I moan as the overwhelming bliss makes it impossible to distinguish Kael's rhythm anymore, and I feel my muscles clench against him."
#     "It's nothing I ever experienced before - it's feels like a cup that has overflowed and each 'spill' ripples throughout my body in pure ecstasy. The intensity takes a hold of me, stringing me along like a hook, not letting me go."
#     "I shudder after the final release, and sink back into the bed. The warmth slowly fades away, like a receding tide, leaving me relaxed and very satisfied."
#     cl "... wow..."
#     ka "Sounds like you enjoyed it."
#     cl "Sound...?"
#     ka "You made some very cute noises."
#     cl "... I didn't even realize... Oh gosh, I hope I didn't wake the neighbors."
#     "I cover my face and Kael chuckles, leaning in."
#     ka "You were fine."
#     jump kael_sex_final


# label kael_sex_final:
#     "It's then I realize we're covered in sweat, and he's still hard inside me. He makes no movements, and pauses to gauge my response."
#     ka "Sore?"
#     cl "Just a bit."
#     ka "You'll probably feel it in the morning."
#     "We gingerly separate and sit up. He reaches over, grabs a folded dry towel off the floor, and starts to pat me down tenderly."
#     ka "You did great, Claire. I'm glad I got to be a part of this."
#     cl "No, thank you. Um, it's because of you I really enjoyed my first time..." 
#     "I glance downward, but I'm too nervous to actually see, and the towel obscures my view anyway."
#     cl "Er, wait, what about you? I've been so selfish I've only focused on how I felt... Should we keep going? Until..., you know..."
#     ka "Huh? Oh, no, don't worry about that."
#     ka "Did you forget? I'm an incubus."
#     "I feel an unexpected poke against my side, causing me to squeal, and his tail stealthily darts behind him."
#     ka "It's sweet of you to ask, but your nourishment is more than enough. We can finish, and it feels good, but it's not necessary for us."
#     ka "Unless..."
#     "He leans in and until his breath tickles my ear."
#     ka "You enjoyed it so much, *you* would like to keep going?"
#     cl "Again!?"
#     "He chuckles and kisses my forehead."
#     ka "Of course I really mean a cuddle." 
#     cl "I'd like that..."
#     jump kael_late_stop


# label kael_stop_now:
#     if kael_sex_choices.kissing or kael_sex_choices.foreplay:
#         cl "Um, I'd like to stop here..."
#         if kael_sex_choices.kissing:
#             "He removes his hand."
#         if kael_sex_choices.foreplay:
#             "Kael gently withdraws his body from mine."
#         ka "Everything okay?"
#         cl "Yes. Experiencing these sensations... they feel nice, but I don't think I'm ready to go beyond that quite yet."
#         ka "I understand. There's no rule that says you need to go all the way in intimacy." 
#         ka "Would you like to cuddle instead?"
#         cl "I'd like that."
#         jump kael_early_stop

#     if kael_sex_choices.kael_on_top or kael_sex_choices.before_pillow:
#         cl "I'd like to stop."
#         if kael_sex_choices.kael_on_top:
#             "Kael withdraws and I sit up, clutching the pillow that was previously under me."
#         else:
#             "Kael rolls off me and I sit up."
#         ka "Everything okay?"
#         cl "Yes. Sorry for bringing everything to a halt... I just don't think I'm ready for, um, going further..."
#         ka "That's alright. You're allowed to change your mind anytime. Sometimes you don't know your own comfort level until you feel yourself leaving it."
#         ka "We got to try a little foreplay, and I'm sure that was very new to you."
#         if kael_sex_choices.kael_on_top:
#             "I nod, then rest my chin on my pillow." 
#         else: 
#             "I nod."
#         cl "Yea, I never gotten that far with someone before."
#         ka "Would you like me to cuddle with you then?"
#         cl "I'd like that, thanks." 
#         jump kael_early_stop
            
#     if kael_sex_choices.kael_inside:
#         cl "I'd like to stop now."
#         if kael_sex_choices.condom:
#             "He pauses, and gently pulls out, careful of the condom."
#         else:
#             "He pauses, and gently pulls out."
#         ka "All done?"
#         cl "Yes... Sorry for halting everything when we barely started... I just felt it was a good time to end things."
#         ka "That's fine. I enjoyed what we did together. There's nothing wrong with changing your mind and there's no pressure to continue."
#         ka "I hope I was able to make it a good experience for you."
#         cl "You did. Thank you. I guess that makes you my first..."
#         "He leans in and nudges my forehead with his." 
#         ka "If you're up for it, we can cuddle for a while."
#         cl "Thank you. That sounds nice." 
#         jump kael_middle_stop
            
#     if kael_sex_choices.claire_top:
#         cl "I'd like to stop now..."
#         ka "I understand."
#         "I roll off, and Kael sits up."
#         cl "Sorry, didn't mean to halt everything when it was getting good."
#         ka "You don't need to apologize. We got to experiment with foreplay and you tried a position you've never done before." 
#         ka "We could do something more familiar if you'd like. If you're up for cuddling."
#         cl "I'd like that..."
#         jump kael_middle_stop

#     if clairetopinside == "True":
#         cl "I'd like to stop now..."
#         "My movements pause, and Kael removes his hands. I carefully withdraw, and we both sit up."
#         ka "Everything okay?"
#         cl "Yes. It wasn't painful or anything... I just wasn't ready to go beyond that."
#         ka "I understand. If anything I'm proud of you. I'm glad I'm your first."
#         ka "I hope you enjoyed yourself at least?"
#         cl "I did, thank you. I felt comfortable with you the whole time, and still do."
#         ka "I'm glad. Would you like to cuddle for a bit?"
#         cl "Sounds good to me."
#         jump kael_middle_stop    


# label kael_early_stop:    
#     "He gives me a reassuring kiss on the forehead. I roll over, and Kael hugs me from behind, moulding his body against mine." 
#     "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
#     "Relaxed, and secure in his arms, I close my eyes and fall into a restful sleep."

# label kael_middle_stop:
#     "Kael pats me down with a dry towel, then teasingly ruffles my hair."
#     ka "I... also got nourished by you. Thank you."
#     "He gives me a reassuring kiss on the forehead. I roll over, and Kael hugs me from behind, moulding his body against mine." 
#     "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
#     "Relaxed, and secure in his arms, I close my eyes and fall into a restful sleep."

# label kael_late_stop:
#     "He gives me a reassuring kiss on the forehead. I roll over, and Kael hugs me from behind, moulding his body against mine." 
#     if kael_scenes >= 3:
#         ka "I hope you've had a memorable spring break."
#         cl "Ha, I did. It wasn't the least bit lonely. You could say it was unbelievable."
#     "His breath warms the base of my neck, and it's then I realize there's soft music still drifting in the room. Both have a soothing effect on me, along with his comforting embrace."
#     "Relaxed, and secure in his arms, I close my eyes and fall into a restful sleep."
# label kael_epilogue:
#     #kael epilogue
#     $ claire.set_state(eyes="closed", eyebrows="frown", mouth="neutral", emotion="default", emotion_base="default")
#     cl "Mm..."
#     "I groggily open my eyes. When I roll over, I realize the bed is empty and I place an arm out to confirm I'm indeed alone."
#     $ claire.set_state(eyes="semi open", eyebrows="default", mouth="oh")
#     cl "...Was it a dream?"
#     "I sit up and reach for my phone as part of my routine. But there's something different about it. Next to my phone is a note. Curious, I pick it up."
#     "'Sorry for leaving on short notice. I enjoyed my time with you and I hope you have a wonderful spring break. If you ever want to see me again, draw the symbol enclosed at the bottom and repeat the chant on the back of the note. Even if you simply want company, or a nice home-cooked meal, I'd be glad to. - Kael.'"
#     "'P.S. I believe this is yours?'"
#     $ claire.set_state(eyes="dots", eyebrows="up", mouth="ehh")
#     cl "...A dirty sock? Why would..."
#     $ claire.set_state(eyes="default", eyebrows="default", mouth="oh")
#     cl "Oh... Heh."
#     $ claire.set_state(eyes="default", eyebrows="default", mouth="grin")
#     cl "Thanks, Kael."
