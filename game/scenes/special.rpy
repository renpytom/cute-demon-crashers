label choose_a_place_to_hangout:
    $ _return = house_map.show()

    if _return == "mirari":
        $ mirari_scenes += 1
        jump expression "mirari_hangout{0}".format(mirari_scenes)
        
    elif _return == "orias":
        $ orias_scenes += 1
        jump expression "orias_hangout{0}".format(orias_scenes)
        
    elif _return == "kael":
        $ kael_scenes += 1
        jump expression "kael_hangout{0}".format(kael_scenes)
        
    elif _return == "akki":
        $ akki_scenes += 1
        jump expression "akki_hangout{0}".format(akki_scenes)
        
    elif _return == "room":
        #had to add a pause here to avoid Claire's dialogue from just skipping >_o
        pause (1.0)
        cl "I'd rather spend time with one of them..."
        jump choose_a_place_to_hangout



label next_day:
    $ scenes_seen += 1

    if scenes_seen == 1:
        jump day1_afternoon
    elif scenes_seen ==2:
        jump day2_morning
    else:
        jump sex_choice



label credits:
    if _in_replay:
        return
    
    # [TODO]
    scene white with dissolve
    pause(1)
    $ renpy.block_rollback()
    show text "{color=#000}Credits{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    hide text with dissolve
    show text "{color=#ff70b0}Original Concept{/color}\n \n{color=#000}Pudding Fluff \nToffee Cake{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Scenario Writing{/color}\n \n{color=#000}Toffee Cake{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Editing{/color}\n \n{color=#000}Caramel Glaze{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Character Designs{/color}\n \n{color=#000}Pudding Fluff{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Art{/color}\n \n{color=#000}Pudding Fluff (sprites and CGs)\nMint Cookie (chibi scenes)\n Chocolate Berry (additional art) {/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Backgrounds{/color}\n \n{color=#000}Chocolate Berry{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}GUI{/color}\n \n{color=#000}Honey Bun{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Music{/color}\n \n{color=#000}Orangebeat{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}SFX sourcing{/color}\n \n{color=#000}Caramel Glaze{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}SFX by{/color}\n \n{color=#000}SmartWentCody\n Corsica_S\nSamKolber\nProject_Trident\nplasterbrain\nTimbre\nzeuss\nguitarguy1985\nAdam_N\nsoundscalpel.com\ncreapersound{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Core Programming{/color}\n \n{color=#000}Fruit Muffin{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Scene directing and additional Programming{/color}\n \n{color=#000}Pudding Fluff{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Voices{/color}\n \n{color=#000}Akki: Red Velvet\nMirari: Anairis Quinones\nOrias: EdwardVapid\nKael: Three Berry Scone{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Voice equalizing{/color}\n \n{color=#000}Ziassan{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#ff70b0}Special Thanks to{/color}\n \n{color=#000}PyTom\n Other friends that would rather not be named :P{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    show text "{color=#000}Made with{/color}{color=#ff70b0} Ren'Py{/color}" with dissolve
    $renpy.pause(2.0, hard=True)
    hide text with dissolve
    show sugarlogo at logo_center with dissolve
    $renpy.pause(2.0, hard=True)
    hide sugarlogo with dissolve
    show logo at logo_center with dissolve
    $renpy.pause(2.0, hard=True)
    hide logo with dissolve
    show text "{color=#000}Thank you so much for playing! :D{/color}" with dissolve
    stop music fadeout 2
    $renpy.pause()
    return

    pass
return
