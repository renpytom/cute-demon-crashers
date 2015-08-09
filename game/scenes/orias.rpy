#temporary sex variables
define coldplay = False
define warmplay = False
define tiedup = False
define blindfolded = False
define nothanks = False
define tickleattack = False
define halfwayyay = False
define chocolatemouth = False
define oraltime = False

#CG variables
define orilay_oriface = "smile"
define orilay_panties = "on"
define orilay_tiedup = False
define orilay_clface = "happy"
define orilay_blindfold = False
define orias_naked = False
define orias_clnaked = False
define orias_cuddles_clface = "3"
define orias_cuddles_oriface = "1"

define orias_cg = False
define orias_cutin = False



label orias_hangout1:
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_orias
    scene bg kitchen with dissolve
    $claire.set_state(**Emotion.normal())
    $orias.set_state(**Emotion.normal())
    $orias.set_state(glasses="default")

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
    show item tea at chibi_scene with dissolve
    "He blows gently on a dainty cup, then offers it to me. I take it, and bring it up to my nose, inhaling softly."
    $claire.set_state(mouth="grin", emotion="heart")
    cl "It smells nice..."
    hide item with dissolve
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
    voice "k_s08"
    ka "Akki, stop making a ruckus - oh - pffffft, I'm sorry, Orias. This is a rare sight. Mirari, Mirari, you need to see this."
    voice "m_s10"
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
    $orias.set_state(glasses="default")
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
    show item toast at chibi_scene with dissolve
    "He places a small tray with jam toast and tea on the desk. When I lift the cup, he shies away."
    $claire.set_state(eyes="happy", eyebrows="inwards", mouth="ehh", emotion="sweat")
    hide item with dissolve
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
    $orias.set_state(with_dissolve,eyes="closed", eyebrows="default", mouth="oh", emotion="default", emotion_base="default")
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
    $orias.set_state(glasses="default")
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
    hide orias with dissolve
    show chibi_orias02 at chibi_scene with dissolve
    ori "I apologize for going off topic. Ahem. 'Dorothy lived in the midst...'"
    stop music fadeout 1
    jump next_day


label orias_sex:
    $ in_sex = True

    if _in_replay:
        $ sex_stop_label = "orias_stoppingnow"
        show screen replay_controls()

    if not _in_replay:
        $ persistent.orias_claire_name = claire_name
        $ persistent.orias_scenes = orias_scenes
    
    stop music fadeout 2
    scene black with dissolve
    $renpy.choice_for_skipping()
    pause(0.5)
    play music music_tension
    scene bg hallway_night with dissolve
    $orias.set_state(base="jacketless",**Emotion.normal())
    $orias.set_state(glasses="default")
    $claire.set_state(**Emotion.normal())
    $ claire.set_state(base="chemise", emotion_base="large blush", mouth="wavy", eyebrows="inwards")
    cl "..."
    play sound "assets/sfx/knock.ogg"
    "I knock on the door."
    cl "Can I come in?"
    ori "Everything is ready."
    scene bg bedroom_candles with dissolve
    "I open and step into the dim bedroom. Yellow candles are scattered around, their flicking seemingly off."
    "Next to my bed is an assortment of items, but all are cleverly covered under a silk cloth, leaving me to speculate."
    $claire.set_state(emotion_base="small blush", eyebrows="up", mouth="uh")
    cl "How nice..."
    $claire.set_state(with_dissolve,eyes="wide", mouth="low")
    cl "Wait, the candles are LED? How current."
    show orias at center with dissolve
    show orias at center_alone2 with dissolve
    $claire.set_state(**Emotion.normal())
    ori "After a certain incident, Mirari swears by them and I simply followed suit." 
    $claire.set_state(eyes="happy", emotion="sweat", mouth="ehh")
    cl "That sounds like a story and a half..."
    "It's then I finally register that he has removed his jacket, exposing more of the leather he has around his chest."
    "I tug on the strap of my chemise."
    $claire.set_state(eyes="down", eyebrows="default", mouth="wavy", emotion_base = "large blush", emotion="default")
    cl "Do I look okay...?"
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="squint", emotion="default")    
    ori "Exquisite." 
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="happy")
    "I feel my face heat up. I never been described as exquisite before..." 
    $orias.set_state(with_dissolve, eyebrows="default", mouth="smile", eyes="side")
    "He takes my hand and guides me to my bed."
    $claire.set_state(eyes="tender side", eyebrows="default", mouth="wavy", emotion_base = "small blush")
    cl "Um, when Akki mentioned 'red' earlier..."
    $orias.set_state(with_dissolve, eyebrows="default", mouth="oh", eyes="default")
    ori "Ah, yes... I was about to go over what I have planned for you, and the use of a safeword. A safeword is basically something you say to stop completely."
    $orias.set_state(with_dissolve, mouth = "neutral")
    $claire.set_state(eyes="default", eyebrows="default", mouth="uh", emotion_base = "default")
    cl "Wouldn't just saying stop work in this situation?"
    $orias.set_state(with_dissolve, eyebrows="default", mouth="oh", eyes="side")
    ori "How to say this... In my line of practices, 'stop' doesn't always mean what it should." 
    $orias.set_state(with_dissolve, eyes="closed")
    ori "To avoid confusion, we agree on a word that normally wouldn't be said during sex."
    $orias.set_state(with_dissolve, eyebrows="default", mouth="neutral", eyes="default")
    $claire.set_state(eyes="happy", eyebrows="default", mouth="happy", emotion_base = "default")
    cl "Oh! So like, uh... cucumber!" 
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="fun side")
    ori "You'll be surprised..."
    $claire.set_state(eyes="mortified", eyebrows="default", mouth="uhh", emotion = "lll")
    cl "..."
    #empty eye claire expression all =_=
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="default")
    ori "Heh, I was kidding. I found in recent decades 'red' is commonly used. When I hear it, all activity will cease. Is that agreeable?"
    $claire.set_state(eyes="happy", eyebrows="default", mouth="wavy", emotion_base = "small blush", emotion = "sweat")
    cl "Sounds good to me, but now I'm a little nervous... What are you planning?"
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="happy", emotion="heart")
    ori "Nothing advanced. Sensation play. I'll tease your senses using temperatures or textures. Possibly with some light restraints."
    if orias_scenes >= 1:
        $orias.set_state(with_dissolve, eyebrows="tender", mouth="oh", eyes="side", emotion="default")
        ori "Remember when you closed your eyes to detect the vanilla in the tea?"
        $claire.set_state(eyes="happy", eyebrows="default", mouth="happy", emotion_base = "default", emotion = "flowers")
        $orias.set_state(with_dissolve, mouth="neutral")
        cl "O-oh! Yes." 
        $orias.set_state(with_dissolve, eyebrows="tender", mouth="grin", eyes="wink", emotion="note")
        ori "It's the same idea."
    else:
        $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="happy", emotion="note")
        ori "When you close your eyes, or are subject to certain sensations, your senses heighten and you become more aware." 
    $claire.set_state(eyes="default", eyebrows="default", mouth="uh", emotion_base = "default", emotion = "default")    
    cl "And is there anything I have to do?"
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="default", emotion="default")
    ori "Since this is your first time... You can relax. Everything will be carefully controlled."
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="side")
    "He glances at the bed, and my eyes follow. There's a large towel spread out, and in its center lies a silk scarf and a sleep mask." 
    $ blindfolded = False
    $ tiedup = False
    $ nothanks = False
    $ orias_cuddles_sprite.set_state(**orias_cuddles_initial)
    $ orias_bed_sprite.set_state(**orias_bed_initial)
    $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="default")
    ori "How would you like to start? Blindfolded or with bound wrists?"
    stop music fadeout 2
    menu:
        "Nothing yet.":
            play music music_love fadein 3
            $ nothanks = True
            $claire.set_state(eyes="down", eyebrows="default", mouth="uh", emotion_base = "small blush", emotion = "default")    
            cl "Can I see how it plays out first before we go ahead with that?"
            ori "Of course. Make yourself comfortable."
            ori "Also, it'd be best to remove your chemise. It looks beautiful on you and I'd hate for it to be stained. Your underwear can stay on."
            "He removes the items while I undress, then I crawl over the towel to lie on my back. Sensing some of the techniques might be a little messy, I decide to raise my arms out of the way." 
            scene orias_bed with dissolve
            $ orias_cuddles_sprite.set_state(claire_naked=True)
            $orias_clnaked = True
            ori "If possible, closing your eyes at certain times might make the activity more fun."
            $claire.set_state(base="naked")
            cla "I'll keep that in mind."
        "Blindfolded.":
            $ blindfolded = True
            play music music_love fadein 3
            $claire.set_state(eyes="default", eyebrows="default", mouth="smile", emotion_base = "default", emotion = "default")    
            cl "I'll try blindfolds first."
            ori "Perfect. Also, it'd be ideal to remove your chemise. It looks beautiful on you and I'd hate for it to be stained. Your underwear can stay on."
            "He removes the items while I undress and instructs me to lie on my back. I close my eyes as I feel the soft fabric slide down my forehead and rest on the bridge of my nose." 
            $ orias_bed_sprite.set_state(blindfold=True)
#            $orilay_blindfold = True
            $orias.set_state(base="jacketless")
            $ orias_cuddles_sprite.set_state(claire_naked=True)
            $orias_clnaked = True
            scene orias_bed with dissolve
            ori "Not too tight?"
            $claire.set_state(base="naked")
            cla "No, and it won't fall off either."
            ori "Good. I also recommend keeping your arms up and out of the way." 
        "Wrists tied.":
            $ tiedup = True
            play music music_love fadein 3
            $ orias_bed_sprite.set_state(tiedup=True)
#            $ orilay_tiedup = True
            $claire.set_state(eyes="happy", eyebrows="default", mouth="ehh", emotion_base = "small blush", emotion = "sweat") 
            cl "This sounds so kinky but... tie me up."
            $claire.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="uh", emotion_base = "small blush", emotion = "default") 
            cl "Will you chain me to something?"
            ori "No, not for the first session. I'm simply restricting your arm movements, but I'll keep the knot loose."
            $claire.set_state(eyes="default", eyebrows="default", mouth="smile", emotion_base = "small blush", emotion = "default") 
            cl "Thank you."
            ori "Also, it'd be best to remove your chemise now since we won't be able to remove it once you're bound."
            $orias.set_state(base="jacketless")
            $ orias_cuddles_sprite.set_state(claire_naked=True)
            $orias_clnaked = True
            scene orias_bed with dissolve
            "After I'm exposed, he instructs me to lie on my back, and I lift my arms above my head. He leans over and ties my wrists deftly with the silk scarf, the sensation cool against my skin."
            "After wriggling a finger into the knot, he tugs it slightly."
            $claire.set_state(base="naked")
            ori "How does this feel?"
            cla "Perfect."
            "I rub my wrists together to demonstrate I have a healthy circulation and he nods in approval."
        "Red.":
            play music music_tension fadein 1
            $claire.set_state(eyes="dots", eyebrows="default", mouth="ehh", emotion_base = "small blush", emotion = "default")   
            cl "Um... Red..."
            $orias.set_state(with_dissolve, eyebrows="inwards", mouth="low", eyes="side")
            ori "I apologize if I came off as too intimidating."
            $orias.set_state(with_dissolve, eyebrows="inwards", mouth="low", eyes="default")
            $claire.set_state(eyes="clench", eyebrows="inwards", mouth="oh", emotion_base = "default", emotion = "panic")   
            cl "No, it's not that. I think I'm not ready for this sort of thing after all." 
            $claire.set_state(with_dissolve, eyes="down", eyebrows="inwards", mouth="low", emotion_base = "default", emotion = "default") 
            cl "I'm sorry, and you already went ahead and prepared everything."
            $orias.set_state(with_dissolve, eyebrows="inwards", mouth="neutral", eyes="default")
            $claire.set_state(with_dissolve, eyes="default", eyebrows="default", mouth="uh", emotion_base = "default", emotion = "default") 
            cl "And I can't expect you to do things you're not used to, either. I'm guessing vanilla isn't your specialty." 
            $orias.set_state(with_dissolve, eyebrows="inwards", mouth="neutral", eyes="closed")
            "He shakes his head."
            $orias.set_state(with_dissolve, eyebrows="tender", mouth="smile", eyes="default")
            ori "No, however, I enjoy aftercare."
            $claire.set_state(eyes="default", eyebrows="up", mouth="uhh", emotion_base = "default", emotion = "default") 
            cl "Aftercare?"
            $orias.set_state(with_dissolve, eyebrows="tender", mouth="grin", eyes="wink", emotion="heart")
            ori "Cuddling, serving tea, making sure my partner is alright after the session, no matter how intense or... non-existent." 
            stop music fadeout 2
            $claire.set_state(eyes="tender", eyebrows="default", mouth="smile", emotion_base = "small blush", emotion = "heart") 
            cl "Heh, I'd like that."
            play music music_lullaby fadein 2
            scene orias_cuddles with dissolve
            "A few minutes later, I'm leaning against Orias who is sitting up and occasionally sipping tea. The chamomile blend works wonders and I start to doze off." 
            "My head finds a comfortable spot on his shoulder, and I close my eyes..."
            call credits
            jump orias_epilogue
        
    cla "Now what?"  
    show screen sex_stop_red("orias_stoppingnow")  
    $ firsthalf = True
    ori "Your choice. What would you like to experience first? Something cold, something warm, or something ticklish?" 
    cla "I..."
    menu:
        "Cold":
            cla "Let's try cold." 
            ori "Alright."
            if orilay_blindfold == False:
                ori "No peeking; that's half the fun."
                $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                $orilay_clface = "content"
            "I hear something clink together as it's brought over, something like glass. The bed shifts from Orias' weight, and I inhale in anticipation."
            "He's nearby but I don't sense anything. What is he planning...?"
            show orias_play cold with dissolve
            $orias_cutin = True
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="shiver")
            $orilay_clface = "shiver"
            cla "Ee-heh!"
            $ coldplay = True
            "A drop of cold liquid hits the center of my torso and slides down the side of my stomach, causing me to shiver and get goosebumps on my arms."
            if orilay_tiedup == True:
                "My bound wrists prevent me from automatically wiping it away, letting the sensation linger even longer." 
            else:
                "I resist wiping the liquid away."
            "Another drop follows, thicker than the previous one. Before it trails down my body, a few more follow suit. The pattern is unpredictable and I find myself wondering when the next drop will come."
            ori "How is it?"
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
            $orilay_clface = "content"
            cla "Cold but not unbearable..."
            show orias_play lick with dissolve
            $orias_cutin = True
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
            $orilay_clface = "pleasure"
            "I sense his body heat as he leans down, and his breath tickles my stomach. Something moist glides along, lapping up the liquid paths and warming my skin. It's just his body temperature but it feels unusually hot thanks to the initial coldness."
            ori "There, to balance it out."
            "I shiver, but not from the temperature play." 
            hide orias_play with dissolve
            $orias_cutin = False
            ori "Would you like it if my mouth explored more as well?"
            "His fingers brush just below my breast to clarify."
            menu:
                "Yes.":
                    cla "I would."
                    show orias_play cold with dissolve
                    $orias_cutin = True
                    cla "Eee."
                    "I feel something cold brush above my navel, and I squirm a bit from the sensation. All I feel is wetness, cold, and a bit of sharpness." 
                    show orias_play lick with dissolve
                    "The shock wears off as quickly as Orias' tongue slides where the ice cube touched, his fingers still guiding the ice higher and higher, toward my sternum. As it melts, he laps up the water, creating a wet and sensual suction against my skin." 
                    "His face moves away from my body, and I hear another click in a glass as he presumingly grabs a fresh cube." 
                    show orias_play nipple_ice with dissolve
                    $orilay_clface ="pleasure"
                    "I gasp as something frigid circles one of my nipples, causing it to feel numb and sending chills down my spine."
                    show orias_play nipple_suck with dissolve
                    extend " Immediately I'm greeted by something hot, and I realize Orias has taken my nipple into this mouth, his tongue rolling over the nub."
                    cla "Oh..."
                    "While he's warming it up, the ice cube teases my other breast, creating a slight sharp sensation, which he quickly remedies with his mouth again." 
                    hide orias_play with dissolve
                    $orias_cutin = False
                    "When he's done, I hear him wipe his mouth."
                    ori "Not so cold anymore?"
                    cla "No..."
                    $ coldplay = False
                "It's fine as it is.":
                    $orilay_clface = "content"
                    cla "I like what you're doing now."
                    ori "I understand."
                    cla "Eee."
                    "I feel something cold brush above my navel, and I squirm a bit from the sensation. All I feel is wetness, cold, and a bit of sharpness." 
                    show orias_play cold with dissolve
                    $orias_cutin = True
                    "I can feel the liquid pool in my navel, while excess water travels down my side."
                    show orias_play lick with dissolve
                    "The shock wears off as quickly as Orias' tongue slides where the ice cube touched, then descends to my navel. He drinks up the water, creating a wet and sensual suction against my skin." 
                    hide orias_play with dissolve
                    $orias_cutin = False
                    ori "Not so cold anymore?"
                    cla "No..."
                    $ coldplay = False
                "Red":
                    jump orias_stoppingnow
        "Warm.":
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried")
            $orilay_clface="worried"
            cla "Warm... Is it like warm-warm or hot-warm?"
            ori "Just above your body temperature warm. Don't worry, I always test on myself before I pour the candle wax on someone else."
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="smile2")
            $orilay_oriface ="smile2"
            ori "Everything about the product is organic, but I'd like to also test a small area to make sure your skin doesn't have a bad reaction."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
            $orilay_clface="content"
            ori "We'll start with your back since its not as sensitive as your front." 
            if orilay_tiedup == True:
                "It feels a little silly with my restraints, but I roll over."
            else:
                "I obey and roll over, making myself comfortable." 
            "A pleasant sugary vanilla scent fills the air, and I inhale it."
            cla "Is that the wax? It smells lovely."
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="smile")
            $orilay_oriface ="smile"
            ori "Yes, I thought it'd delight your senses. Even if I'm far from vanilla myself."
            cla "Heh, this has been a relaxing, uh, BDSM session so far." 
            ori "You're new to this, so I'm doing my best to make this an inviting experience for you."
            ori "Ah, perfect temperature."
            if blindfolded == True:
                ori "However, your sight is restricted so you might be more sensitive to the heat than I am. Please let me know if it's too hot or uncomfortable."
            else:
                ori "However, your sensitivity will be different from mine. Please let me know if it's too hot or uncomfortable."
            ori "This is the test, so no surprises from me just yet. I'll pour a bit on your shoulder."    
            show orias_play hot with dissolve
            $orias_cutin = True
            "Vanilla invades my senses again and a spoonful of the mildly warm wax drips onto my skin." 
            $ warmplay = True
            cla "Ah... kinda hot but not... scalding..."
            show orias_play wax_rub with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
            $orilay_clface="pleasure"
            "He disperses the wax by rubbing it, and I moan happily."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
            $orilay_clface="content"
            cla "Oh... I like that. It starts hot then spreads out juuust in time so it doesn't hurt." 
            ori "I'll let it cool a bit more than so I can let the drops linger too." 
            ori "It doesn't itch or anything?"
            cla "Nope!"
            ori "And your skin doesn't appear irritated. We'll go with this then." 
            cla "You're... very thorough and caring."
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="neutral")
            $orilay_oriface ="neutral"
            ori "I wouldn't do anything to a submissive I wouldn't perform on myself." 
            show orias_play hot with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="smile")
            $orilay_oriface ="smile"
            "He drips more wax between my shoulder blades, and the warm sensation continues down my back. Half the fun is guessing where, when and how much he applies."
            "Whenever I think I have the pattern down, Orias changes it up."
            hide orias_play hot with dissolve
            $orias_cutin = False
            ori "Would you like to turn over? It'll be a bit more sensitive on your stomach and chest."
            menu:
                "Yes.":
                    cla "I trust you."
                    "I roll over, thankful for the towel keeping the bed untouched." 
                    if blindfolded == True:
                        "I can sense the weight of the bed shift again as Orias adjusts to my position."
                    else:
                        $ orias_bed_sprite.set_state(with_dissolve, claire_face="happy")
                        $orilay_clface = "happy"
                        "I open my eyes briefly, seeing Orias holding a small tin, with a little spoon sticking out. Ah, that's how he did it... I close my eyes again."
                        $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                        $orilay_clface = "content"
                    ori "I'll keep this part short, since your skin is probably very sensitive now..." 
                    show orias_play hot with dissolve
                    $orias_cutin = True
                    "I gasp when wax dribbles between my breasts and rolls down my stomach. It's not as warm as it was previously, but it still feels mild against my skin."
                    $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
                    $orilay_clface="pleasure"
                    "The 'burning' sensation only lasts a second, like sticking your toe in a hot tub before you submerge completely. My muscles tighten only briefly, then relax once the wax cools against my skin, and Orias occasionally dilutes the wax with his rubs." 
                    ori "There, done. Anymore and this would take longer to do..."
                    cla "What would take— Oh."
                    show orias_play wax_scratch with dissolve
                    "Gentle nails dig into my skin, peeling off the hardened wax. I sigh as his fingers graze up and down before massaging my stomach fully to show it's wax-free."
                    hide orias_play with dissolve
                    $orias_cutin = False
                    $ warmplay = False
                    
                "I'm happy like this.":
                    cla "I like what you're doing right now..."
                    ori "Of course."
                    show orias_play hot with dissolve
                    $orias_cutin = True
                    "He continues dripping the wax, going up and down my spine, making sure not to get too close to my hair, which he brushes aside." 
                    show orias_play wax_rub with dissolve
                    "With each drop, I feel my senses heightened and... more aware of the touch? I can feel the wax slide down, or when it starts to pool, which Orias rubs down." 
                    ori "There. I'm going to remove it."
                    show orias_play wax_scratch with dissolve
                    "Nails dig into my skin and gently travel up and down as pieces of wax fall beside me."
                    $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
                    $orilay_clface="pleasure"
                    cla "Ah, if the wax was nice, this is heaven..." 
                    ori "I only poured on a small area too, otherwise this would take a while."
                    $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                    $orilay_clface="content"
                    "He teasingly pinches my spine, causing me to giggle, before he continues. When he's done, I can feel his hands stroke up and down my back to show it's completely wax-free. My skin also feels silkier under his touch." 
                    hide orias_play with dissolve
                    $orias_cutin = False
                    ori "There, done. You can turn over again." 
                    $ warmplay = False
                      
                "Red.":
                    jump orias_stoppingnow
            
        "Ticklish.":
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried")
            $orilay_clface="worried"
            cla "I guess ticklish... Is it like tickle torture?"
            ori "Not that extreme, but I'll make featherlight movements on your body, seeing what you like." 
            if blindfolded == False:
                $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                $orilay_clface="content"
                ori "No peeking; that's half the fun."
                "I close my eyes, and the weight on the bed disappears briefly before returning."
            else: 
                "The weight on the bed disappears briefly, before returning."
                $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                $orilay_clface="content"
            "The bed shifts under him, and I feel my body tense up, wondering where he'll start first."
            cla "Hehe..."
            $ tickleattack = True
            show orias_play tickle with dissolve
            $orias_cutin = True
            "I feel something oh-so-subtle trail up my stomach above my navel. Unsurprisingly, it's ticklish."
            ori "Your reactions are cute."
            cla "Eee."
            show orias_play tickle_foot with dissolve
            "The feather(?) attacks the sole of my foot, and I automatically bend my leg, trying to get away."
            cla "I guess I could give you an uncute reaction if you wanted."
            ori "I doubt it's possible from you."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="laughing")
            $orilay_clface = "laughing"
            cla "WAHHAHA."
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="laugh")
            $orilay_oriface = "laugh"
            ori " What... Hahaha."
            "His voice cracks and, for once, I hear a genuine laugh from him."
            ori "It was a manner of speech, I wasn't putting forth a challenge..." 
            show orias_play tickle_armpit with dissolve
            "My giggles are uncontrollable as he brushes against my armpits."
            if tiedup == True:
                "My bound wrists make it impossible to wriggle away and I writhe under the touch."
            else: 
                "I roll to my side, then to my other side, as he alternates between my armpits."
            "I thought BDSM was supposed to be all serious...?"
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
            $orilay_clface = "content"
            hide orias_play with dissolve
            $orias_cutin = False
            $ orias_bed_sprite.set_state(with_dissolve, orias_face="smile")
            $orilay_oriface = "smile"
            ori "If you like, I could make it more sensual than ticklish now..."
            menu:
                "Sure.":
                    cla "Sure, hehe... Go for it..."
                    "I didn't expect the next sense to be what Orias promised. Suddenly, I feel a firmer, yet still airy, brush just under my breast."
                    $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
                    $orilay_clface = "pleasure"
                    show orias_play nipple_tickle with dissolve
                    $orias_cutin = True
                    "Any laughter I still suppressed leaves my body with a gasp, and I sink into the bed further."
                    "The feather flirts under the next breast then travels upward to my sternum. I writhe ever so slightly as he keeps it up."
                    "The feather traces around my breasts like a spiral, circling closer and closer to my nipple. After it grazes it, he does the same to my other breast but counterclockwise to change it up."
                    "The sensation vanishes, and my body tenses up, anticipating the next touch."
                    show orias_play tickle_thighs with dissolve
                    "I feel something tickle my inner thighs, and the pit of my stomach plummets."
                    cla "Ah..."
                    ori "Feel surprisingly good?"
                    cla "I didn't expect that..."
                    "The feather darts against the lace of my panties, then travels upward to my navel then glides back down with more pressure." 
                    "The feather vanishes, leaving me with a lingering desire."
                    hide orias_play with dissolve
                    $orias_cutin = False
                    ori "That should do. I don't want to warm you up too much yet."
                    $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
                    $orilay_clface = "content"
                    cla "You're a tease."
                    $ tickleattack = False
                "Keep up the tickle torture.":
                    cla "This is good... I'm really enjoying this."
                    $ orias_cuddles_sprite.set_state(orias_face=1)
                    $orias_cuddles_oriface = "1"
                    ori "Oh, really now?"
                    show orias_play tickle with dissolve
                    $orias_cutin = True
                    "The feather brushes up my neck, and I turn toward my shoulder, exposing the other side. The tip grazes my shoulder, then travels down my torso. It's less ticklish with the constant contact, but I still giggle slightly." 
                    "The movement continues down my body, then darts under my knees, and I squeal again."
                    "The feather dances around my knees then vanishes instantly."
                    if blindfolded == False:
                        "It takes all my willpower not to open my eyes to see where it went."
                    "I feel a light brush against my nose, causing it to wriggle, and I snort before Orias withdraws."
                    $ orias_bed_sprite.set_state(with_dissolve, orias_face="smile2")
                    $orilay_oriface = "smile2"
                    hide orias_play with dissolve
                    $orias_cutin = False
                    ori "There, I think I found most of your sensitive spots." 
                "Red.":
                    $ tickleattack = False
                    jump orias_stoppingnow    
            
    label halfwaypoint:
        $ firsthalf = False
        $ halfwayyay = True
        ori "How do you feel so far?"
        $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
        $orilay_clface = "content"
        if orilay_blindfold == True and orilay_tiedup == False:
            "He gently adjusts the blindfold, making sure it didn't become crooked during the session."
            ori "Would you like me to tie up your wrists?"
            menu:
                "Yes.":
                    cla "Sure, let's try that."
                    $ orias_bed_sprite.set_state(with_dissolve, tiedup=True)
                    $orilay_tiedup = True
                    "I feel the smooth silk wrap around my wrists as he ties some kind of knot. He wriggles a finger between it to make sure there's enough room for circulation."
                    ori "How do you feel?"
                    cla "It's perfect. I got wiggle room." 
                "No.":
                    cla "I'm good. I'm happy having the blindfold."
                    ori "I'm glad you're content with that."
                "Red.":
                     jump orias_stoppingnow
        if orilay_tiedup == True and orilay_blindfold == False:
            "He wriggles a finger between the knotted scarf, making sure it isn't cutting my circulation."
            ori "Would you like your eyes covered?" 
            menu:
                "Yes.":
                    cla "Let's go the whole way."
                    ori "I love your enthusiasm."
                    $ orias_bed_sprite.set_state(with_dissolve, blindfold=True)
                    $orilay_blindfold = True
                    "I close my eyes as I feel the sleep mask slide over my head."
                    ori "How is that?"
                    cla "Comfortable and not too tight, but it won't fall off either."
                    ori "Good."
                "No.":
                    cla "I'm good with this."
                    ori "I understand."
                "Red.":
                    jump orias_stoppingnow
        if nothanks == True:
            ori "Would you like to try being blindfolded or having your wrists bound?"
            menu:
                "Blindfold.":
                    cla "I'll try being blindfolded. I feel more comfortable with the idea now."
                    ori "I'm glad."
                    $ orias_bed_sprite.set_state(with_dissolve, blindfold=True)
                    $ orilay_blindfold = True
                    "I close my eyes and I feel the sleep mask slip down my head."
                    ori "How does that feel?"
                    cla "Good, comfy, but not too tight."
                    ori "Excellent."
                "Wrists tied.":
                    cla "I'll be comfortable with my wrists tied up."
                    $ orias_bed_sprite.set_state(with_dissolve, tiedup=True)
                    $ orilay_tiedup = True
                    "The smooth silk wraps around my wrists as he ties some kind of knot. He wriggles a finger between it to make sure there's enough room for circulation."
                    ori "How do you feel?"
                    cla "It's perfect. I got wiggle room." 
                "I'm good.":
                    cla "I don't think I'm ready for those steps quite yet."
                    ori "I understand."
                "Red.":
                    jump orias_stoppingnow
                    
    ori "I think your body is quite warmed up now... So I have one last thing to try with you..."
    menu:
        "Ask him to strip, too.":
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried")
            $orilay_clface="worried"
            cla "Wait."
            ori "Hm?"
            cla "I've been practically naked the whole time and... well, you're still in your window-pants."
            ori "Heh, that's a new term..."
            ori "I'm guessing you'll feel better if I took them off?"
            "I nod."
            hide screen sex_stop_red

            scene bg bedroom_candles with dissolve
            $orias.set_state(mouth="default")
            show orias at center_alone2 with dissolve
            $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender")
            ori "I guess it's only fair..."
            if orilay_blindfold == True:
                "I feel the sleep mask lift up to my forehead before he steps back."
            show orias at center_group with dissolve
            $orias.set_state(with_dissolve, base="naked")
            $ orias_bed_sprite.set_state(naked=True)
            $ orias_cuddles_sprite.set_state(orias_naked=True)
            $orias_naked = True
            "He starts by unbuckling the strap around his chest, letting it slide down his body before removing it completely. With one swift motion, he loosens the belt and removes his pants." 
            $orias.set_state(with_dissolve, eyes="default", mouth="smile")
            $claire.set_state(eyes="dots", emotion_base="large blush", eyebrows="up", emotion="steam", mouth="v")
            cl "..."
            $claire.set_state(with_dissolve, eyes="down", eyebrows="up", mouth="low", emotion_base = "small blush", emotion = "default") 
            cl "That piercing must've hurt."
            $orias.set_state(with_dissolve, eyes= "fun front", mouth = "grin")
            ori "Which one?"
            $orias.set_state(with_dissolve, eyes= "happy", mouth = "smile")
            "He smirks and I chuckle while my eyes travel over his frame."
            $claire.set_state(eyes="tender side", eyebrows="default", mouth="uh", emotion_base = "small blush", emotion = "default")
            $orias.set_state(with_dissolve, eyes= "wide", eyebrows = "up", mouth = "uhh", emotion_base = "small blush")
            cl "And... you're cute...."
            $orias.set_state(with_dissolve, eyes="side", mouth="default", emotion_base="small blush", eyebrows="tender")
            ori "Cute? I admit I've been described as many things but 'cute' wasn't one of them."
            $orias.set_state(with_dissolve, eyes= "wide", eyebrows = "up", mouth = "low", emotion_base = "small blush")
            $claire.set_state(eyes="happy", eyebrows="default", mouth="happy", emotion_base = "small blush", emotion = "flowers")
            cl "Well, you're cute now. If you can call me exquisite, I can call you cute."
            $orias.set_state(with_dissolve, eyes= "default", eyebrows = "tender", mouth = "smile", emotion_base = "small blush")
            show orias at center_alone2 with dissolve
            ori "I'm honored to be seen as cute in your eyes then." 
            if orilay_blindfold == True:
                $orias.set_state(with_dissolve, eyes= "default", eyebrows = "tender", mouth = "smile",emotion = "heart", emotion_base = "default")
                "He winks then places the sleep mask over my eyes again."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="content")
            $orilay_clface="content"
            scene orias_bed with dissolve
            $orias_cg = True
            show screen sex_stop_red("orias_stoppingnow")  
                
        "Enjoy the next session.":
            "What is he planning...?"
       
    if orilay_blindfold == False:
        "Orias approaches a candle that was subtly hidden on the bookcase. I close my eyes again since I have a feeling it'll be more fun this way."
    else:
        "I hear footsteps away, followed by the sound of tin scraping against wood. Is he at my bookcase?"
    "He returns, and the bed shifts under his weight again."
    ori "Ready? It's a surprise this time."
    "I inhale, wondering what part of my body he'll touch next."
    $ halfwayyay = False
    $ chocolatemouth = True
    show orias_play hot with dissolve
    "I feel something... thick drizzle between my breasts, warm and gooey. A sweet scent fills the air, but before I can identify it, he starts licking me sensually."
    $ orias_bed_sprite.set_state(with_dissolve, claire_face="pleasure")
    $orilay_clface="pleasure"
    cla "Ng..."
    "I can sense his face hovering close before me, then his lips brush against mine."
    if orilay_blindfold == True:
        show orias_play kiss_blind
    else:
        show orias_play kiss
    "The kiss is deep, and I inhale in response. The taste of chocolate floods my mouth. I moan from the realization."
    "His tongue darts to the corners of my mouth before traveling back down between my chest."
    hide orias_play with dissolve
    $ chocolatemouth = False
    $ oraltime = True
    "Once all of the chocolate has been removed, he flutters downward, alternating between warm kisses and hot breaths."
    "When he reaches my navel, his lips close around it and I feel an incredible suction and nothing else. It's then I know what he's trying to hint..."
    ori "Should I keep going...?"
    menu:
        "Let him continue.":
            cla "Yes..."
            "He plants a firm kiss under my navel before resuming his destination. His fingers touch the lace of my panties, then gently pulls them down."
            $ orias_bed_sprite.set_state(with_dissolve, panties="off")
            $orilay_panties = "off"
            "My stomach coils from the closing distance, and his lips brush the tips of my pubic hair. After a deep breath, I widen my legs a little, and he begins massaging my inner thighs."
            ori "I'm glad you enjoyed the sensational play..."
            show orias_finish oral with dissolve
            "With long broad strokes, he parts my lower lips, licking each side tenderly. I turn my head to the side, my body highly sensitive to every movement." 
            "The coiling sensation tightens like a spring, and every stroke and lick sends jolts up and down my body. His tongue narrows and traces along my entrance, and I start to squirm, my hips unable to keep still."
            "Orias continues his up-and-down motions, gradually increasing his movements, and applies more pressure against me."
            hide screen sex_stop_red

            "I feel the lightest suction as his mouth brushes upward towards my clit, and I inhale in anticipation."
            if orilay_tiedup == True:
                "Being binded only adds a sweet layer of pleasure – unable to adjust myself or clutch onto the sheets. Instead, my fingers tighten into fists in response."
            "Orias flattens his tongue and teases my clit with unhurried licks. I moan softly depending on his angles."
            cla "...Ah..."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="O")
            $orilay_clface="O"
            "Eventually I'm unable to pick up the subtle touches as my mind becomes hazy from the increasing pleasure. My legs shift and my pelvis arches against him, not wanting him to let up the rhythm."
            "Flashes of heat radiate from my core all the way to my trembling fingers and down to my curled toes. I moan, my head pushing against my raised arms."
            "I shudder and feel release, my body shivering and I take in a deep gulp of air. I can't tell if I'm sinking into the bed or if the bed vanished. I feel so light..."
            hide orias_finish with dissolve
            if orilay_blindfold == True:
                $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried")
                $orilay_clface ="worried"
                cla "Orias...?"
                ori "I'm here, and I'll remove everything."
            "I feel a hand caress my forehead, wiping away the sweat."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="happy")
            $orilay_clface ="happy"
            ori "Enjoyed yourself?"
            cla "Did I ever..."
            if orilay_blindfold and orilay_tiedup == True:
                "Chuckling, he carefully removes the bindings and blindfold, making sure my wrists are okay."
            elif orilay_blindfold == True:
                "Chuckling, he carefully removes the blindfold. I open my eyes and blink until my vision clears."
            elif orilay_tiedup == True:
                "Chuckling, he carefully removes the silk knot, making sure my wrists are okay."
            scene bg bedroom_candles with dissolve
            $orias_cg = False
            $orias.set_state(eyes= "default", mouth="smile", eyebrows="tender", emotion="default", emotion_base="default")  
            show orias at center_alone2 with dissolve
            ori "I'll clean you up now, so you can relax."
            stop music fadeout 2
            $claire.set_state(eyes="happy", eyebrows="inwards", mouth="wavy", emotion_base = "small blush", emotion = "default")
            cl "Honestly, I think that's all I can do at this point..."
            
        "Request fingers instead.":
            cla "Um, is it okay if you use your fingers... once you get there?"
            ori "I can do that."
            "He plants one last firm kiss just above my pubic hair, and I can subtly feel his fingers replace where his mouth was. Wriggling under the lace, he then pulls down my underwear."
            $orilay_panties = "off"
            "His finger travels through my hair, then dips into the already moist parting. I widen my legs slightly to make it easier for him."
            show orias_finish fingers with dissolve
            ori "I'm glad you enjoyed the sensation play."
            "One hand massages my inner thigh while the other begins stroking my outer lips. With each motion, his fingers explore deeper, tracing the sides and around my entrance." 
            if orilay_blindfold == True:
                "My eyes flutter under the mask and my breathing quickens from his touch."
            else:
                "My eyes flutter, and my breathing quickens from his touch."    
            #remove stop button
            "Encouraged by my reaction, he continues to stroke me while his other hand caresses my thigh."
            "One finger dips into me, and I feel a jolt up my body. After withdrawing, he lingers around my entrance again before traveling upward."
            "Gradually, he brushes over my clit, and I let out a little moan. The pressure I had felt for a while starts to disperse, making my body warm and pleasant throughout."
            hide screen sex_stop_red

            cla "Mm..."
            "My legs squirm as he increases his vigor, his fingers first making circular motions over my clit before settling on up and down movements." 
            if orilay_tiedup == True:
                "Having my wrists bound adds a new layer of pleasure. I'm unable to balance myself or clutch the sheets beside me, instead my arms harmlessly quiver along with my body."
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="O")
            $orilay_clface ="O"
            "Soon I'm unable to distinguish Orias' movements, and I feel a pleasant sensation building and intensifying. Hot streaks radiate from my body, causing me to shudder and arch."
            "My muscles suddenly seize up, and I let out one final moan. I buck against his hand, then sink into the bed."
            "A calm feeling slowly takes over, although I still feel occasional tingles and the soft throbbing between my thighs."
            "Orias affectionately rubs my leg, bringing me back to reality."
            hide orias_finish with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="happy")
            $orilay_clface ="happy"
            ori "Enjoyed yourself?"
            cla "Heh, you'd think so after that..."
            cla "Wow..."
            if orilay_blindfold == True and orilay_tiedup == False:
                "A light-headed sensation washes over me as Orias carefully removes the blindfold. I open my eyes, then blink, allowing my vision to return."
            if orilay_tiedup == True and orilay_blindfold == False:
                "A light-headed sensation washes over me as Orias removes the scarf, making sure my wrists are unharmed." 
            if orilay_blindfold and orilay_tiedup == True:
                "A light-headed sensation washes over me as Orias carefully removes the blindfold and scarf, making sure my wrists are alright."    
            scene bg bedroom_candles with dissolve
            $orias.set_state(eyes= "default", mouth="smile", eyebrows="tender", emotion="default", emotion_base="default")
            show orias at center_alone2 with dissolve
            ori "I'll clean you up now, so you can relax."
            stop music fadeout 2
            $claire.set_state(eyes="happy", eyebrows="inwards", mouth="wavy", emotion_base = "small blush", emotion = "default")
            cl "I think that's all I'm capable of doing now..." 
               
        "Red.":
            jump orias_stoppingnow
            
    play music music_lullaby fadein 2
    scene orias_cuddles with dissolve
    "A few minutes later, I'm leaning against Orias who is sitting up and occasionally sipping tea. Myself, I have water to help stay hydrated. Orias carefully guides me through 'aftercare', making sure I feel mentally and physically fine after an intense session."
    $ orias_cuddles_sprite.set_state(with_dissolve, claire_face=1)
    $orias_cuddles_clface = "1"
    cla "Was all this really sex?"
    ori "Well, what do you think we did?"
    $ orias_cuddles_sprite.set_state(with_dissolve, claire_face=2, orias_face=2)
    $orias_cuddles_clface = "2"
    $orias_cuddles_oriface = "2"
    "I think about it, then feel my face heat up, reflecting over the activities. I sip my water, and Orias chuckles softly at my reaction."
    $ orias_cuddles_sprite.set_state(with_dissolve, orias_face=1)
    $orias_cuddles_oriface = "1"
    ori "Moreover, I got well nourished from you."
    if orias_scenes >= 3:
        ori "Also, was there anything I could do better? If there's ever a next time..."
    else:
        ori "Any feedback that I can keep in mind?"
    $ orias_cuddles_sprite.set_state(with_dissolve, claire_face=1)
    $orias_cuddles_clface = "1"
    cla "Hrm, well..."
    $ orias_cuddles_sprite.set_state(with_dissolve, claire_face=4)
    $orias_cuddles_clface = "4"
    cla "You were great but at the same time... it felt distant."
    $ orias_cuddles_sprite.set_state(with_dissolve, orias_face=3)
    $orias_cuddles_oriface = "3"
    ori "Distant? For me, the ultimate form of pleasure is being able to satisfy my partner." 
    cla "..."
    $ orias_cuddles_sprite.set_state(with_dissolve, orias_face=4)
    $orias_cuddles_oriface = "4"
    ori "Ah, then..."
    "He places a hesitant kiss on my forehead, then pulls away. I wonder if he's not used to affection outside of sex..."
    $ orias_cuddles_sprite.set_state(with_dissolve, claire_face=3)
    $orias_cuddles_clface = "3"
    cla "Thank you..."
    "I'm still exhausted from the session and I feel myself sag against him. Sensing I'm ready to pass out, Orias takes my mug and places it on the nightstand."
    $ orias_cuddles_sprite.set_state(with_dissolve, orias_face=1)
    $orias_cuddles_oriface = "1"
    "My head finds a comfortable spot on his shoulder and I close my eyes..."
    "Before sleep overtakes me, I feel a hand wrap around me..."
    call credits
    jump orias_epilogue
            
label orias_stoppingnow:
        if not _in_replay:
            $ persistent.orias_sex_stop = last_statement
        hide screen sex_stop_red

        if firsthalf == True and halfwayyay == False:
            if orias_cutin == True:
                hide orias_play with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried", orias_face="neutral")
            $orilay_clface= "worried"
            $orilay_oriface = "neutral"
            cla "Red. I'd like to stop."
            ori "I understand."
            scene bg bedroom_candles with dissolve
            if orilay_blindfold == True:
                "He gently touches the back of my head and removes the sleep mask."
            if orilay_tiedup == True:
                "He carefully unties my wrists and gives them a rub to make sure they're unharmed." 
            if coldplay == True or warmplay == True:    
                "Orias gently wipes my body down with a damp handcloth."
                jump oriasstopearly 
        elif halfwayyay == True and firsthalf == False:
            if orias_cutin == True:
                hide orias_play with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried", orias_face="neutral")
            $orilay_clface= "worried"
            $orilay_oriface = "neutral"
            cla "Red. I'm done."
            ori "I understand."
            scene bg bedroom_candles with dissolve
            if orilay_blindfold == True:
                "He then gently touches the back of my head and removes the sleep mask."
            if orilay_tiedup == True:
                "He then carefully unties my wrists and gives them a rub to make sure they're unharmed."
            "Orias gently wipes my body down with a damp handcloth, making sure nothing is missed from our sessions."
            $orias.set_state(eyes="default", eyebrows="tender", mouth="default", emotion="default", emotion_base="default")
            show orias at center_alone2 with dissolve
            ori "There."
            jump oriasstopmiddle
            
        elif chocolatemouth == True:
            hide orias_play with dissolve
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried", orias_face="neutral")
            $orilay_clface= "worried"
            $orilay_oriface = "neutral"
            cla "Red. I'm done."
            ori "I understand."
            scene bg bedroom_candles with dissolve
            if orilay_blindfold == True and orilay_tiedup == False:
                "He gently touches the back of my head and removes the sleep mask."
            if orilay_tiedup == True and orilay_blindfold == False:
                "He carefully unties my wrists and gives them a rub to make sure they're unharmed."
            if orilay_tiedup == True and orilay_blindfold == True:   
                "He carefully removes the sleep mask then unties my wrists, giving them a rub to make sure they're unharmed."
            if coldplay == True or warmplay == True:
                "Orias gently wipes my body down with a damp handcloth, making sure nothing is missed from our sessions."
            $orias.set_state(eyes="default", eyebrows="tender", mouth="default", emotion="default", emotion_base="default")
            show orias at center_alone2 with dissolve
            ori "There."    
            jump oriasstoplate
            
        elif oraltime == True:
            $ orias_bed_sprite.set_state(with_dissolve, claire_face="worried", orias_face="neutral")
            $orilay_clface= "worried"
            $orilay_oriface = "neutral"
            cla "Red. Red."
            hide orias_finish with dissolve
            "He halts, then removes himself from my body."
            ori "Of course."
            scene bg bedroom_candles with dissolve
            if orilay_blindfold == True:
                "He gently touches the back of my head and removes the sleep mask."
            if orilay_tiedup == True:
                "He carefully unties my wrists and gives them a rub to make sure they're unharmed."
            if coldplay == True or warmplay == True:
                "Orias then gently wipes my body down with a damp handcloth, making sure nothing is missed from our sessions."
            else:
                jump oriasstoplate
            $orias.set_state(eyes="default", eyebrows="tender", mouth="default", emotion="default", emotion_base="default")    
            show orias at center_alone2 with dissolve
            ori "There."  
            jump oriasstoplate

                
label oriasstopearly:
        $orias.set_state(eyes="default", eyebrows="tender", mouth="default", emotion="default", emotion_base="default")
        show orias at center_alone2 with dissolve
        $claire.set_state(eyes="down", mouth="low", eyebrows="inwards", emotion="default", emotion_base="small blush")
        cl "I'm sorry for stopping the session so soon..."
        $orias.set_state(with_dissolve, eyes="closed", eyebrows="inwards", mouth="smile")
        ori "No, don't be. You don't need to force yourself to do anything you're not comfortable with."
        $claire.set_state(eyes="tender", mouth="smile")
        $orias.set_state(with_dissolve, eyes="default", eyebrows="tender" )
        cl "Thank you, Orias." 
        $claire.set_state(eyes="tender side", mouth="low")
        cl "Um, would it be too vanilla to ask for a cuddle at least?"
        $orias.set_state(with_dissolve, mouth="happy", eyebrows="up")
        ori "Oh, I enjoy aftercare."
        $claire.set_state(mouth="oh", eyebrows="up", eyes="default")
        $orias.set_state(with_dissolve, mouth="smile", eyebrows="tender" )
        cl "Aftercare?"
        $orias.set_state(with_dissolve, eyes="wink", mouth="smile", eyebrows="tender", emotion="heart")
        ori "Cuddling, serving tea, making sure my partner is alright after the session, no matter how intense or... short." 
        stop music fadeout 2
        $claire.set_state(mouth="grin", eyebrows="default", eyes="happy")
        cl "Heh, I'd like that."
        play music music_lullaby fadein 2
        scene orias_cuddles with dissolve
        "A few minutes later, I'm leaning against Orias who is sitting up and occasionally sipping tea. The chamomile blend works wonders and I start to doze off." 
        "My head finds a comfortable spot on his shoulder, and I close my eyes..."
        call credits
        jump orias_epilogue 
        
label oriasstopmiddle:
        $orias.set_state(eyes="default", eyebrows="inwards", mouth="smile", emotion="default", emotion_base="default")
        ori "There you go. Do you feel better, [claire_name]?"
        $claire.set_state(eyes="tender", mouth="smile", eyebrows="inwards", emotion="default", emotion_base="small blush")
        cl "Yes... Um, sorry for ending it after we had a good mood going... I felt I had enough."
        if coldplay == True:
            $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile", emotion="note", emotion_base="default")
            ori "I'm proud of you. You got to experiment a bit with ice play."
        elif warmplay == True:
            $orias.set_state(with_dissolve,eyes="wink", eyebrows="tender", mouth="smile", emotion="note", emotion_base="default")
            ori "I'm proud of you. Wax play is usually considered an advanced session... and you enjoyed yourself."
        elif tickleattack == True:
            $orias.set_state(with_dissolve,eyes="happy", eyebrows="tender", mouth="smile", emotion="note", emotion_base="default")
            ori "I'm proud of you. You got to experiment with the senses."
        if orilay_tiedup == True:
            $orias.set_state(with_dissolve,eyes="default", eyebrows="default", emotion="default")
            ori "And you got to feel what it was like to be restrained."
        if orilay_blindfold == True and orilay_tiedup == False:
            $orias.set_state(with_dissolve,eyes="default", eyebrows="default", emotion="default")
            ori "And you got to feel what it was like to be deprived of your sight." 
        if orilay_blindfold == True and orilay_tiedup == True:  
            $orias.set_state(with_dissolve,mouth="grink", eyebrows="default", emotion="default")
            "And you got to experience light BDSM."
        $orias.set_state(with_dissolve,eyes="closed", eyebrows="tender", mouth="smile", emotion="default")
        ori "It's definitely not entry-level stuff, and you still gave it a chance." 
        $orias.set_state(with_dissolve,eyes="happy", eyebrows="tender", mouth="smile", emotion="heart")
        ori "You did well on your first session. I even got nourished during it."
        $claire.set_state(eyes="dots", eyebrows="default", mouth="smile", emotion="default")
        cl "Ah... then I'm glad it worked out..."
        $orias.set_state(with_dissolve,eyes="default", eyebrows="tender", mouth="smile", emotion="default")
        $claire.set_state(eyes="tender side", mouth="low")
        cl "Um... would it be too vanilla if I asked for a cuddle now...?"
        $orias.set_state(with_dissolve, mouth="happy", eyebrows="up", eyes="closed")
        ori "Of course not. Aftercare is extremely important, no matter how intense or light the session is."
        $claire.set_state(mouth="oh", eyebrows="up", eyes="default")
        $orias.set_state(with_dissolve, mouth="smile", eyebrows="tender", eyes="default" )
        cl "Aftercare?"
        $orias.set_state(with_dissolve, eyes="wink", mouth="smile", eyebrows="tender", emotion="heart")
        ori "Where I get to spoil you with cuddles and tea and make sure you're alright."
        stop music fadeout 2
        $claire.set_state(mouth="grin", eyebrows="default", eyes="happy")
        cl "Ah, I'd like that..."
        play music music_lullaby fadein 2
        scene orias_cuddles with dissolve
        "A few minutes later, I'm leaning against Orias who is sitting up and occasionally sipping tea. The chamomile blend works wonders and I start to doze off." 
        "My head finds a comfortable spot on his shoulder, and I close my eyes..."
        call credits
        jump orias_epilogue 
        
#TODO -> Faces    
label oriasstoplate:
        $orias.set_state(eyes="default", eyebrows="tender", mouth="default", emotion="default", emotion_base="default")
        $claire.set_state(eyes="down", eyebrows="inwards", mouth="low", emotion="sweat", emotion_base="small blush")
        show orias at center_alone2 with dissolve
        cl "..."
        $orias.set_state(with_dissolve, eyes="default", eyebrows="inwards", emotion="default", emotion_base="default")
        ori "Are you alright?"
        $claire.set_state(eyes="closed", eyebrows="inwards", mouth="low", emotion="sweat", emotion_base="small blush")
        cl "Yeah... I'm sorry. We were pretty far, and I suddenly felt like I had to stop."
        $orias.set_state(with_dissolve, eyes="closed", eyebrows="tender", mouth="neutral")
        ori "I understand. It's not always easy having someone in control for that long."
        $claire.set_state(eyes="bug cry", eyebrows="inwards", mouth="low", emotion_base="small blush")
        $orias.set_state(with_dissolve, eyes="default", eyebrows="up", mouth="default")
        cl "I apologize for ruining everything..."
        $orias.set_state(with_dissolve, eyes="happy", eyebrows="tender", mouth="smile")
        ori "You didn't ruin anything. If anything, I'm proud of you. You got to experiment in something that's... not exactly easy for beginners."
        $claire.set_state(eyes="happy", eyebrows="inwards", mouth="smile", emotion="sweat", emotion_base="small blush")
        cl "Yeah... Maybe I went over my head a bit... but I'm glad I got to try it with you, Orias."
        $claire.set_state(eyes="tender", emotion="default")
        cl "Can we do something more, uh, tame? Like a cuddle?"
        $orias.set_state(with_dissolve, mouth="happy", eyebrows="up", eyes="closed")
        ori "Of course. Aftercare is extremely important, no matter how intense or light the session is."
        $claire.set_state(mouth="oh", eyebrows="up", eyes="default")
        $orias.set_state(with_dissolve, mouth="smile", eyebrows="tender", eyes="default" )
        cl "Aftercare?"
        $orias.set_state(with_dissolve, eyes="wink", mouth="smile", eyebrows="tender", emotion="heart")
        ori "Where I get to spoil you with cuddles and tea and make sure you're alright."
        stop music fadeout 2
        $claire.set_state(mouth="grin", eyebrows="default", eyes="happy")
        cl "Ah, I'd like that..."
        play music music_lullaby fadein 2
        scene orias_cuddles with dissolve
        "A few minutes later, I'm leaning against Orias who is sitting up and occasionally sipping tea. The chamomile blend works wonders and I start to doze off." 
        "My head finds a comfortable spot on his shoulder, and I close my eyes..."
        call credits
        jump orias_epilogue 
        

label orias_epilogue:
    #orias epilogue
    if orias_scenes==3:
        jump orias_epilogue_long
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
    "I groggily open my eyes. When I roll over, I realize the bed is empty and I place an arm out to confirm I'm indeed alone."
    $ claire.set_state(with_dissolve,eyes="semi open", eyebrows="default", mouth="oh")
    cl "...Was it a dream?"
    "I sit up and reach for my phone as part of my routine. But there's something different about it. Next to my phone is a note. Curious, I pick it up."
    scene white with dissolve
    show text "{color=#000} 'Salutations, I hope you had a good night's sleep.\n I want to thank you for accommodating us; it was a delight browsing the miniature library.\n If, on the off chance, you would like to see me again, I provided my symbol and incantation on the back of this note.\n Sincerely, Orias.'{/color}" with dissolve
    $renpy.pause()
    show text "{color=#000}'P.S. I left a chai tea blend for you. Please enjoy.'{/color}" with dissolve
    $renpy.pause()
    show bg bedroom_day with dissolve
    $ claire.set_state(eyes="happy", eyebrows="default", mouth="grin", emotion="note")
    cl "Aw... how sweet."
    $ claire.set_state(with_dissolve,eyes="default", eyebrows="default", mouth="grin", emotion="default")
    cl "Thanks, Orias."
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return

label orias_epilogue_long:
    $ persistent.orias_complete = True
    stop music fadeout 1
    scene black with dissolve
    $renpy.choice_for_skipping()
    $renpy.pause(0.4)
    play music music_orias
    scene bg street with dissolve
    $orias.set_state(base="human", glasses="on", **Emotion.normal())
    $ claire.set_state(base="default", **Emotion.normal())
    $claire.set_state(eyes="closed", emotion="sigh", eyebrows="inwards", mouth="uhh", emotion_base="default")
    
    cl "..."
    "I drag my feet as I walk home from university."
    "Even a week after my spring break, I find myself thinking of Orias." 
    "If I close my eyes, I can almost hear his voice..."
    "???" "[claire_name]?"
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="uh", emotion_base="default")
    cl "Huh?"
    $orias.set_state(eyes= "default", mouth="smile", eyebrows="default")
    show orias at center_alone2 with dissolve
    "I spin around and let out a gasp."
    $claire.set_state(eyes="happy", emotion="flowers", eyebrows="default", mouth="happy", emotion_base="default")
    cl "Orias! How did you find me?" 
    $orias.set_state(with_dissolve,eyes= "side", mouth="oh", eyebrows="default", emotion="default", emotion_base="default")
    ori "Considering your house and education, I had a faint idea but I didn't know your schedule. However, I'm glad I was able to see you."
    $orias.set_state(with_dissolve,eyes= "default", mouth="smile", eyebrows="default", emotion="default", emotion_base="default")
    "He holds up a small container tied with a pretty ribbon on top."
    $orias.set_state(with_dissolve,eyes= "wink", mouth="grin", eyebrows="tender", emotion="note", emotion_base="default")
    ori "I thought that you might have missed my specialty tea, so I brought some..." 
    $orias.set_state(with_dissolve,eyes= "happy", mouth="grin", eyebrows="tender", emotion="default", emotion_base="default")
    $claire.set_state(eyes="happy", emotion="flowers", eyebrows="default", mouth="grin", emotion_base="default")
    cl "I have! Your tea's exquisite."
    $claire.set_state(with_dissolve,eyes="down", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    $orias.set_state(with_dissolve,eyes= "wide", mouth="default", eyebrows="up", emotion="default", emotion_base="default")
    cl "I actually have something for you, too."
    $claire.set_state(eyes="tender side", emotion="panic", eyebrows="inwards", mouth="lip bite", emotion_base="default")
    cl "Ah, is it still in my purse...?"
    $orias.set_state(with_dissolve,eyes= "default", mouth="default", eyebrows="default", emotion="default", emotion_base="default")
    $claire.set_state(eyes="happy", emotion="default", eyebrows="default", mouth="grin", emotion_base="default")
    cl "Phew. I carried this around in case I ever saw you again."
    $orias.set_state(with_dissolve,eyes= "side", mouth="default", eyebrows="tender", emotion="default", emotion_base="default")
    "After putting his gift into my bag, I present a small item bundled in tissue paper. He takes it and carefully unwraps it, revealing the silicone leaf lid attached to a tiny steel basket ."
    $orias.set_state(with_dissolve,eyes= "wide", mouth="oh", eyebrows="up", emotion="default", emotion_base="default")
    ori "And this is...?"
    $orias.set_state(with_dissolve,eyes= "wide", mouth="default", eyebrows="up", emotion="default", emotion_base="default")
    $claire.set_state(eyes="happy", emotion="note", eyebrows="default", mouth="happy", emotion_base="default")
    cl "A modern tea infuser. If you put it in your teacup, the leaf will bob up and down."
    $orias.set_state(with_dissolve,eyes= "squint", mouth="neutral", eyebrows="tender", emotion="default", emotion_base="default")
    "He holds it up, scrutinizing it as if he has a profound comment to say, then lowers his hand."
    $orias.set_state(eyes= "happy", mouth="grin", eyebrows="tender", emotion="note", emotion_base="default")
    ori "It's... cute. Thank you."
    $orias.set_state(with_dissolve,eyes= "side", mouth="oh", eyebrows="tender", emotion="default", emotion_base="small blush")
    ori "It appears you... missed something other than my tea." 
    $claire.set_state(eyes="down", emotion="default", eyebrows="default", mouth="smile", emotion_base="small blush")
    cl "Yeah."
    $orias.set_state(with_dissolve,eyes= "default", mouth="smile", eyebrows="tender", emotion="default", emotion_base="small blush")
    ori "I promise that the feeling's mutual."
    $orias.set_state(with_dissolve,eyes= "happy", mouth="smile", eyebrows="tender", emotion="heart", emotion_base="default")
    ori "If you wish... I could visit you more often."
    $claire.set_state(eyes="fun front", emotion="heart", eyebrows="default", mouth="kitty", emotion_base="default")
    cl "I'd like that. However, I have two requests."
    $orias.set_state(with_dissolve,eyes= "default", mouth="oh", eyebrows="up", emotion="default", emotion_base="default")
    ori "And they are...?"
    $orias.set_state(with_dissolve,eyes= "wide", mouth="low", eyebrows="up", emotion="default", emotion_base="small blush")
    "I stand on my tippy toes and deliver a light peck to his cheek."
    $claire.set_state(eyes="default", emotion="default", eyebrows="default", mouth="grin", emotion_base="default")
    cl "I'd like to see a little more affection from you."
    $orias.set_state(with_dissolve,eyes= "side", mouth="smile", eyebrows="tender", emotion="default", emotion_base="default")
    ori "I'm satisfied with that arrangement."
    $claire.set_state(eyes="tender side", emotion="default", eyebrows="default", mouth="uh", emotion_base="small blush")
    cl "Aaaand..."
    $orias.set_state(with_dissolve,eyes= "wide", mouth="default", eyebrows="up", emotion="bars", emotion_base="default")
    $claire.set_state(eyes="down", emotion="steam", eyebrows="default", mouth="low", emotion_base="large blush")
    cl "Can I do things for you in bed?"
    $orias.set_state(with_dissolve,eyes= "wide", mouth="oh", eyebrows="up", emotion="default", emotion_base="default")
    ori "You'd like to? I admit my preferences are... a little unusual so I rarely disclose it to my new partners."
    $claire.set_state(eyes="clench", emotion="panic", eyebrows="default", mouth="oh", emotion_base="large blush")
    cl "Try me."
    $orias.set_state(with_dissolve,eyes= "closed", mouth="uhh", eyebrows="default", emotion="default", emotion_base="small blush")
    "He leans down, his whisper tickling my ear. His answer causes me to blush when he pulls away. I glance at the piercings in his ears, realizing it makes sense."
    $claire.set_state(eyes="dots", emotion="sweat lots", eyebrows="flat", mouth="ehh", emotion_base="large blush")
    cl "W-well, I could always start off with a few simple things..."
    $orias.set_state(with_dissolve,eyes= "wink", mouth="smile", eyebrows="tender", emotion="default", emotion_base="default")
    ori "Remember, there's no rush. We can take our time with these arrangements."
    $orias.set_state(with_dissolve,eyes= "side", mouth="oh", eyebrows="tender", emotion="default", emotion_base="small blush")
    ori "Now regarding the first request..."
    $orias.set_state(with_dissolve,eyes= "closed", mouth="smile", eyebrows="tender", emotion="default", emotion_base="small blush")
    "He hesitantly kisses my forehead, then glances away." 
    $orias.set_state(with_dissolve,eyes= "default", mouth="smile", eyebrows="tender", emotion="default", emotion_base="small blush")
    "I smile and take his hand, content with his sincere attempt."
    $claire.set_state(eyes="tender", emotion="default", eyebrows="default", mouth="grin", emotion_base="small blush")
    cl "Yeah... No rush."
    stop music fadeout 1
    scene white with dissolve
    hide screen replay_controls
    $ renpy.end_replay()
    return
