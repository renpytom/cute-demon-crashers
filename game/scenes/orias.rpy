label orias_hangout1:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_orias
    scene bg kitchen with dissolve
    $claire.set_state(**Emotion.normal())
    $orias.set_state(**Emotion.normal())

    $claire.set_state(eyebrows="up", mouth="uh")
    cl "(What is he doing?)"
    "Orias is sitting at the table, scooping what looks like a tea blend into silk bags. Once he's done, he skillfully ties it up and places it in a growing pile."
    show orias at center_alone2 with dissolve
    if current_day == 1:
        cl "Is that the tea you served me earlier?"
        $orias.set_state(mouth="oh", eyes="default")
        ori "Hm? Ah, this is something entirely different. It's ginger peach with vanilla."
    else:
        cl "Preparing tea bags? What blend is it?"
        $orias.set_state(mouth="oh", eyes="default")
        ori "Yes, and it's ginger peach with vanilla."
    $orias.set_state(with_dissolve,eyebrows="up", mouth="oh",  eyes="default")    
    ori "Would you like to try one?"
    $claire.set_state(eyebrows="default", mouth="smile")
    cl "Sure."
    $orias.set_state(with_dissolve,eyebrows="tender", mouth="smile",  eyes="closed") 
    "Nodding, he closes the jar containing the blend, and heads over to the kitchen counter with one of the tea bags."
    "I glance at the pile. Many of them are simple white ones, but a few are embroidered with lattice patterns."
    $claire.set_state(eyes="happy")
    cl "When did you pick up your tea hobby?"
    $orias.set_state(with_dissolve,eyebrows="default", mouth="oh",  eyes="side") 
    ori "When did I... Ah, Paris. Tea was becoming popular in Paris centuries ago. Many of the nobles I had trysts with drank it."
    $orias.set_state(with_dissolve, mouth="smile",  eyes="default") 
    ori "Once its popularity spread to England, that was when I became interested in its different preparations and flavors." 
    $orias.set_state(with_dissolve,eyebrows="tender", mouth="smile",  eyes="happy") 
    ori "Many of those tea bags are gifts and souvenirs from my travels."
    $orias.set_state(with_dissolve,eyebrows="tender", mouth="smile",  eyes="default") 
    ori "Here you go."
    "He blows gently on a dainty cup, then offers it to me. I take it, and bring it up to my nose, inhaling softly."
    $claire.set_state(mouth="grin", emotion="heart")
    cl "It smells nice..."
    "Orias props his elbows on the table, observing my movements. After the tea cools down, I take a sip."
    $claire.set_state(mouth="uh", eyes="default", emotion="default")
    cl "Ah, I can taste the peach with the hint of spicy ginger but... I can't taste the vanilla?"
    
    $orias.set_state(with_dissolve,eyes="closed")
    ori "Try closing your eyes." 
    "I do so and continue to drink. It's then I detect the creamy smoothness that lingers."
    $claire.set_state(emotion="flowers", eyes="closed", mouth="happy")
    cl "Oh, I can taste it now! It's very subtle, but it's there."
    $orias.set_state(with_dissolve,eyes="default")
    ori "When you block out one sense, the others heighten."
    $orias.set_state(with_dissolve,eyebrows="default", eyes="closed") 
    ori "I'm still balancing out the proportions; thank you for your feedback."
    $claire.set_state(emotion="default", eyes="happy", mouth="smile")
    cl "Nah, you're more attuned to this than I am."
    "He returns to preparing the tea bags, and I curiously watch his nimble fingers work."
    $claire.set_state(with_dissolve,eyes="default")
    cl "You're really good at tying."
    $orias.set_state(with_dissolve,eyebrows="up",  eyes="wink") 
    stop music
    play sound "assets/sfx/scratch.ogg"
    ori "Thank you. It's probably from all the experience of binding my lovers."
    hide orias at center with dissolve
    show chibi_orias01 at chibi_scene with dissolve
    $ gallery.unlock("chibi_orias01")
    play music music_silly
    cla "Pffffffffft."
    "I cover my mouth when I realize I showered Orias' face with my tea."
    $claire.set_state(emotion="panic", eyes="big", mouth="fun ah", eyebrows="inwards", emotion_base="dark")
    cl "Oh god... I'm so sorry. I'm SO, SO sorry."
    hide chibi_orias01 with dissolve
    $orias.set_state(with_dissolve,eyebrows="inwards", eyes="flat",mouth="low", emotion="lll", base="tea")
    show orias at center_alone2 with dissolve 
    ori "It's quite all right. My timing was off."
    $orias.set_state(with_dissolve, eyes="side", mouth="neutral")
    ori "I wanted to find a way to be upfront about my sexual interests, in case you were considering me."
    $orias.set_state(with_dissolve,eyebrows="tender",emotion="default", eyes="default")
    ori "I'm not trying to... dissuade you, but it's something to be mindful of when weighing your options."
    $orias.set_state(with_dissolve,eyes="closed")
    ori "Excuse me, I'll go wash myself off now."
    $claire.set_state(mouth="wavy", eyes="clench") 
    cl "O-of course. Sorry about that..."
    hide orias with moveoutright
    "He gets up and leaves, and I sip my tea with a guilty conscience. A few moments later I hear a roar in the other room."
    ak "HAHAHAHA, what happened to you? New technique?"
    ka "Akki, stop making a ruckus - oh - pffffft, I'm sorry, Orias. This is a rare sight. Mirari, Mirari, you need to see this."
    mi "What is everyone babbling about-  teehee, that's a whole new look for you!"
    ori "I'm delighted that you're all highly amused by this."
    $claire.set_state(emotion="lll", eyes="dots")
    cl "..."
    "Face beet-red, I gulp my tea down."
    $claire.set_state(emotion="steam", eyes="clench", emotion_base="large blush")
    cl "Good job, [claire_name]."
    $orias.set_state(base="default")
    stop music fadeout 1
    jump next_day


label orias_hangout2:
    stop music fadeout 1
    scene black with dissolve
    $renpy.pause(0.4)
    $renpy.choice_for_skipping()
    play music music_orias
    $claire.set_state(**Emotion.normal())
    $orias.set_state(**Emotion.normal())
    $orias.set_state(glasses="off")
    scene bg bedroom_day with dissolve
    "As much as I'd like to spend more time with them... I can't ignore my studies."
    "I crack open my textbook and find the required chapter."
    $claire.set_state(eyes="closed", eyebrows="inwards", mouth="oh", emotion="sigh", emotion_base="dark")
    cl "I know there'll be a pop quiz the day I get back..."
    play sound "assets/sfx/knock.ogg"
    "The minutes melt away as I jot down notes. A knock on the door frame jolts me out of my trance."
    $claire.set_state(eyes="default", eyebrows="up", mouth="uh", emotion="default", emotion_base="default")
    cl "Yes? Come in."
    $orias.set_state(with_dissolve,mouth="smile",emotion="default", eyes="default")
    show orias at center_alone2 with dissolve
    ori "We've noticed that you've been absorbed for quite some time. I thought you'd appreciate a pick-me-up."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="default", mouth="low", emotion="sweat")
    show orias at center_group with dissolve
    "He places a small tray with jam toast and tea on the desk. When I lift the cup, he shies away."
    $claire.set_state(eyes="happy", eyebrows="inwards", mouth="ehh", emotion="sweat")
    cl "I promise I won't spray you in the face this time."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="default")
    ori "And I won't speak while you're drinking." 
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="default")
    $claire.set_state(eyes="default", eyebrows="default", mouth="happy", emotion="default")
    cl "Deal."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="oh")
    show orias at center_alone2 with dissolve
    ori "What are you studying? Is it related to your education?"
    $claire.set_state(eyes="semi open", eyebrows="default", mouth="smile", emotion="default")
    cl "History. I haven't declared a major yet, so I'm picking courses that sound interesting and then go from there."
    $orias.set_state(with_dissolve, mouth="default")
    $claire.set_state(eyes="happy", mouth="grin", emotion="note")
    cl "I find I like factual stuff. Right now I'm studying the French Revolution."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender",mouth="oh")
    ori "Has it really been that long...? How nostalgic."
    $claire.set_state(eyes="default", eyebrows="up", mouth="uhh", emotion="default")
    cl "Wait, were you there during that time?"
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default",mouth="neutral")
    ori "I left prior to the events and stayed in London. However, news did spread."
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile")
    ori "We incubi and succubi try to avoid getting entangled in human affairs. Although Mirari likes to claim she had nothing to do with the free love movement during the Victorian Era." 
    $claire.set_state(eyes="default", eyebrows="up", mouth="vhappy", emotion="flowers")
    cl "What was France like while you stayed there? What did you do there?"
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="oh", emotion="sweat")
    ori "Well... I set a bedroom on fire to help a noblewoman fake her death and escape her arranged marriage."
    $claire.set_state(eyes="fun front", eyebrows="default", mouth="kitty", emotion="default")
    cl "And I thought you avoided human affairs."
    $orias.set_state(with_dissolve, eyes="wink", eyebrows="default", mouth="smile", emotion="default")
    ori "'Try' is the keyword."
    $orias.set_state(with_dissolve, eyes="closed", eyebrows="default", mouth="smile")
    "Orias sits on the edge of my bed, recalling events and memories. I scribble down the tidbits related to the pre-Revolution." 
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="note")
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile")
    cl "Thanks for that. It's pretty surreal to talk to someone who lived during that time." 
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile")
    ori "I'm glad to be of assistance. It's been a while since I remembered the past; I hope my stories made sense." 
    $claire.set_state(eyes="semi open", eyebrows="inwards", mouth="oh", emotion="sweat")
    cl "Also..."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="default")
    ori "Hm?"
    $claire.set_state(eyes="semi open", eyebrows="default", mouth="wavy", emotion="default")
    cl "Er, I want to apologize. Not just for the tea incident, but for getting the wrong idea about your interests."
    $claire.set_state(with_dissolve, eyes="closed", eyebrows="inwards", mouth="wavy", emotion="sweat")
    cl "Before, I thought people who were into, uh, kinky stuff were all cruel sadists who loved dominating people against their will. Whips and dungeons, the whole shebang."
    $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="low", emotion="lll", emotion_base="dark")
    ori "..."
    #thought bubble with a little chibi of evil looking Orias cackling and holding a whip? XD
    $orias.set_state(with_dissolve, eyes="flat", eyebrows="default", mouth="ehh", emotion="sweat", emotion_base="dark")
    ori "Ah... no, it's nothing like that."
    $orias.set_state(eyes="closed", eyebrows="default", mouth="oh", emotion="default", emotion_base="default")
    ori "There are misconceptions surrounding my practices, yes, but I assure you that is completely untrue." 
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile")
    ori "My role as a Dominant includes responsibility and being considerate of my partners. Nothing pleases me more than fulfilling their needs." 
    $orias.set_state(with_dissolve, eyes="wink", eyebrows="up", emotion="note")
    ori "My partners have the real power. If they request dungeons and whips, I'd be happy to provide, though."
    $claire.set_state(eyes="dots", eyebrows="up", mouth="oh", emotion="default")
    cl "I can't believe you have a dungeon on standby."
    $orias.set_state(with_dissolve, eyes="fun side", eyebrows="up", mouth="smile", emotion="default")
    ori "What can I say, my partners' desires can be... unconventional." 
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="default")
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="default")
    cl "Haha. Thanks for clearing things up."
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile", emotion="default")
    ori "My pleasure. I don't want people to be repulsed due to a misunderstanding." 
    "He takes the empty plate and drained teacup."
    $orias.set_state(with_dissolve, eyes="default", mouth="smile")
    ori "I'll leave you to your studies."
    $claire.set_state(eyes="default", eyebrows="default", mouth="smile")
    cl "Thank you."
    stop music fadeout 1
    jump next_day


label orias_hangout3:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_orias
    scene bg bedroom_day with dissolve
    $claire.set_state(**Emotion.normal())
    $orias.set_state(**Emotion.normal())
    $orias.set_state(glasses="off")
    $orias.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="oh")
    show orias at center_alone2 with dissolve
    ori "Studying again?"
    $claire.set_state(eyes="happy", eyebrows="default", mouth="smile")
    cl "Finishing up. Thanks for the coffee earlier. I know it's not your forte, but I really needed it."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="default")
    "I spot a book in his hand."
    $claire.set_state(eyes="default", eyebrows="up", mouth="oh")
    cl "Reading as well?"
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="up", mouth="smile", emotion="sweat")
    ori "Yes. As much as I enjoy reading through your father's miniature library, the subjects are becoming a little monotonous."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="default", mouth="oh", emotion="default")
    ori "I noticed your bookshelf here earlier... May I browse?"
    $claire.set_state(eyes="happy", eyebrows="default", mouth="wavy", emotion="sweat")
    cl "Of course. Uh, just keep in mind I rarely read so..."
    $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="ah", emotion="bars")
    ori "They're all children's books!"
    $claire.set_state(eyes="flat", eyebrows="default", mouth="wavy", emotion="sweat")
    cl "...the selection hasn't changed in years."
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile", emotion="note")
    ori "I remember when many of these were first released. {i}The Wonderful Wizard of Oz{/i}, {i}Heidi{/i}, {i}Treasure Island{/i}..." 
    $claire.set_state(eyes="default", eyebrows="default", mouth="smile", emotion="sweat")
    cl "My parents love classical literature and would buy those for me every year."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="neutral", emotion="default")
    $claire.set_state(eyes="happy", eyebrows="inwards", mouth="grin", emotion="default")
    cl "I'd remember asking 'Why couldn't Dorothy just use the GPS on her cell phone to find Emerald City?' and mom declared modern technology ruined everything." 
    $orias.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="oh")
    ori "Did they read to you a lot?"
    $claire.set_state(eyes="default", eyebrows="up", mouth="oh")
    cl "Not really, I preferred video games. Yourself? Did you always love reading?"
    $orias.set_state(with_dissolve, eyes="squint", eyebrows="tender", mouth="smile", emotion="heart")
    "He pulls out {i}The Wonderful Wizard of Oz{/i} and looks over it fondly."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="smile", emotion="default")
    ori "One of my previous partners was an actor in a playing company back in London. Before we made love, he'd practice reciting lines for me."
    $orias.set_state(with_dissolve, eyes="closed")
    ori "His voice was soothing but captivating and you'd hang onto every word. He'd also read books out loud." 
    $orias.set_state(with_dissolve, eyes="closed", eyebrows="up", mouth="oh", emotion="default")
    ori "I know many people consider reading a solitary pastime, but I find it just as enjoyable sharing them."
    $claire.set_state(eyes="happy", eyebrows="up", mouth="happy", emotion="flowers")
    cl "Since I'm done studying, would you like to read to me?"
    $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="uhh", emotion="bars")
    ori "Me?"
    $claire.set_state(eyes="default", eyebrows="default", mouth="smile", emotion="note")
    cl "Of course you. I think you have a lovely voice, and you have a relaxing presence." 
    $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender", mouth="smile", emotion="default")
    ori "I may not have the acting talent, but I'll do my best."
    "I climb into bed, then pat the spot next to me."
    $orias.set_state(with_dissolve, eyes="wide", eyebrows="up", mouth="oh", emotion="default")
    ori "You want me beside you?"
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="default")
    cl "There's illustrations in the book, after all."
    $orias.set_state(with_dissolve, eyes="wink", eyebrows="up", mouth="happy", emotion="default")
    stop music fadeout 2
    ori "So that's your excuse."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile")
    play music music_romance fadein 2
    "However, he acquiesces and climbs into bed. Once we make ourselves cozy, Orias opens to the first page."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="oh", emotion_base="small blush")
    ori "Are you okay with this arrangement?" 
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile", emotion="default")
    "I lean in as an answer, and he chuckles."
    $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile", emotion_base="default")
    ori "I'm glad you're comfortable around me."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="smile", emotion="sweat")
    ori "It's rare that I interact with humans outside of copulation nowadays. Forgive me if I seem rusty or aloof."
    $claire.set_state(eyes="default", eyebrows="up", mouth="oh", emotion="default")
    cl "Why is that? Er, the whole interaction thing. From what you've told me, you sound very involved with your past lovers."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="neutral", emotion="default")
    ori "I was, until I left someone brokenhearted. We possess feelings, but as incubi, we're unable to experience love in the romantic sense."
    $orias.set_state(with_dissolve, eyes="closed", eyebrows="inwards", mouth="wavy")
    ori "Therefore, when someone starts getting too attached, I stop seeing them. I don't want them to end up hurt."
    $claire.set_state(eyes="semi open", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "I understand. If it helps, I respect your wishes. Um, would it be too much to consider you a friend?"
    $orias.set_state(with_dissolve, eyes="side", eyebrows="tender", mouth="oh", emotion_base="small blush")
    ori "No, I quite like that. I've enjoyed spending time with you."
    $orias.set_state(with_dissolve, eyes="default", eyebrows="tender", mouth="smile", emotion_base="small blush")
    ori "If you decide to... pick me tonight, I promise I'll give you a wonderful experience. You can trust me." 
    $claire.set_state(eyes="happy", eyebrows="default", mouth="grin")
    cl "...Aw, thank you..."
    $orias.set_state(with_dissolve, eyes="side", eyebrows="default", mouth="neutral", emotion_base="small blush")
    "I shyly glance down at the book and he does the same."
    $orias.set_state(with_dissolve, eyes="closed", eyebrows="default", mouth="oh", emotion_base="default", glasses="on")
    ori "I apologize for going off topic. Ahem. 'Dorothy lived in the midst...'"
    stop music fadeout 1
    jump next_day


label orias_sex:
    # [TODO]
    pass
# label orias_epilogue:
#     #orias epilogue
#     $ claire.set_state(eyes="closed", eyebrows="frown", mouth="neutral", emotion="default", emotion_base="default")
#     cl "Mm..."
#     "I groggily open my eyes. When I roll over, I realize the bed is empty and I place an arm out to confirm I'm indeed alone."
#     $ claire.set_state(eyes="semi open", eyebrows="default", mouth="oh")
#     cl "...Was it a dream?"
#     "I sit up and reach for my phone as part of my routine. But there's something different about it. Next to my phone is a note. Curious, I pick it up."
#     "'Salutations, I hope you had a good night's sleep. I want to thank you for accommodating us; it was a delight browsing the miniature library. If, on the off chance, you would like to see me again, I provided my symbol and incantation on the back of this note. Sincerely, Orias.'"
#     "'P.S. I left a chai tea blend for you. Please enjoy.'"
#     $ claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="note")
#     cl "Aw... how sweet."
#     $ claire.set_state(eyes="default", eyebrows="default", mouth="grin", emotion="default")
#     cl "Thanks, Orias."
