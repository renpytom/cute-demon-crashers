# House map
init:
    transform garden_chibi:
        anchor (0.5, 0.5)
        xpos 600
        ypos 430

    transform kitchen_chibi:
        anchor (0.5, 0.5)
        xpos 500
        ypos 290

    transform bedroom_chibi:
        anchor (0.5, 0.5)
        xpos 350
        ypos 100

    transform living_room_chibi:
        anchor (0.5, 0.5)
        xpos 700
        ypos 300

    transform hallway_chibi:
        anchor (0.5, 0.5)
        xpos 640
        ypos 80

    transform chibi_button:
        anchor (0.5, 0.5)

        on hover:
            linear 0.2 zoom 1.2 rotate 15

        on idle:
            linear 0.4 zoom 1.0 rotate 0
       

init python:
    class HouseMap(object):
        def __init__(self):
            self.selection = None

        def show(self):
            return renpy.call_screen("housemap", self)

        def reset(self):
            if self.selection is not None:
                self.selection = None
                renpy.restart_interaction()

    house_map = HouseMap()

    class UIComponent(object):
        def ImageButton(self, *args, **kwargs):
            ui.detached()
            return ui.imagebutton(*args, **kwargs)


    class OneAt(UIComponent):
        def __init__(self, context, selection, transform, character):
            self.context = context
            self.selection = selection
            self.transform = transform
            self.character = character

        def render(self):
            (image, action) = self.character
            
            return At(
                self.ImageButton(
                    idle=image,
                    hover=image,
                    hovered=SetField(self.context, "selection", self.selection),
                    unhovered=SetField(self.context, "selection", None),
                    action=[action]
                ),
                chibi_button,
                self.transform
            )

    class TwoAt(UIComponent):
        def __init__(self, context, selection, transform, left, right):
            self.context = context
            self.selection = selection
            self.transform = transform
            self.left = left
            self.right = right

        def render_one(self, character, xoffset, yoffset):
            (image, action) = character

            return At(
                self.ImageButton(
                    idle=image,
                    hover=image,
                    hovered=SetField(self.context, "selection", self.selection),
                    unhovered=SetField(self.context, "selection", None),
                    action=[action],
                    xoffset=xoffset,
                    yoffset=yoffset
                ),
                chibi_button
            )
            
        def render(self):
            return At(
                Fixed(
                    self.render_one(self.left, -30, -30),
                    self.render_one(self.right, 30, 30),
                    xfill=False,
                    yfill=False,
                    xsize=130,
                    ysize=130,
                    xoffset=70,
                    yoffset=50
                ),
                self.transform
            )


screen housemap(ctx):
    python:
        def img(x): return "assets/ui/map/house-{0}-hover.png".format(x)
        def noop(): pass
        def show_menu(ctx):
            def _do():
                ctx.reset()
                return ShowMenu("save")()
            return _do

        housemap_data = {
            "garden": (img("garden"), _("Dad loves his gardening.")),
            "hallway": (img("hallway"), _("Now with a purple portal...?")),
            "kitchen": (img("kitchen"), _("Where the food is.")),
            "living": (img("living"), _("Where the video games are.")),
            "room": (img("room"), _("Where all my textbooks are.")),
        }

        orias_chibi = ("assets/ui/map/chibi-orias.png", Return("orias"))
        mirari_chibi = ("assets/ui/map/chibi-mirari.png", Return("mirari"))
        kael_chibi = ("assets/ui/map/chibi-kael.png", Return("kael"))
        akki_chibi = ("assets/ui/map/chibi-akki.png", Return("akki"))

        location_map = [
            #no scenes
            [
                OneAt(ctx, "garden", garden_chibi, mirari_chibi),
                OneAt(ctx, "kitchen", kitchen_chibi, orias_chibi),
                OneAt(ctx, "hallway", hallway_chibi, kael_chibi),
                OneAt(ctx, "living", living_room_chibi, akki_chibi)
            ],
            [
                OneAt(ctx, "garden", garden_chibi, mirari_chibi),
                OneAt(ctx, "kitchen", kitchen_chibi, orias_chibi),
                TwoAt(ctx, "living", living_room_chibi, kael_chibi, akki_chibi)
            ],
            [
                OneAt(ctx, "garden", garden_chibi, mirari_chibi),
                TwoAt(ctx, "kitchen", kitchen_chibi, kael_chibi, orias_chibi),
                OneAt(ctx, "living", living_room_chibi, akki_chibi)
            ],
            [
                OneAt(ctx, "garden", garden_chibi, mirari_chibi),
                OneAt(ctx, "room", bedroom_chibi, orias_chibi),
                OneAt(ctx, "hallway", hallway_chibi, kael_chibi),
                OneAt(ctx, "living", living_room_chibi, akki_chibi)
            ],
            [
                OneAt(ctx, "garden", garden_chibi, mirari_chibi),
                OneAt(ctx, "room", bedroom_chibi, orias_chibi),
                TwoAt(ctx, "living", living_room_chibi, kael_chibi, akki_chibi)
            ]

        ]
            
    modal True
    zorder 2

    window:
        style_group "housemap"

        fixed:
            key "game_menu" action show_menu(ctx)
            add "assets/ui/map/house-bg.png" align (0, 0)

            # Location selection
            showif ctx.selection is not None:
                python:
                    (map_hover, map_desc) = housemap_data.get(ctx.selection, (Null(), ""))

                add map_hover align (0, 0)

                text map_desc style "housemap_description"


            # Character selection
            if scenes_seen == 0 or (kael_scenes==0 and orias_scenes==0):
                for layout in location_map[0]:
                    add layout.render()
            elif (kael_scenes==1) and (orias_scenes==0):
                for layout in location_map[1]:
                    add layout.render()
            elif (kael_scenes==2) and (orias_scenes==0):
                for layout in location_map[2]:
                    add layout.render()
            elif(kael_scenes==0) and (orias_scenes>0):
                for layout in location_map[3]:
                    add layout.render()
            else:
                for layout in location_map[4]:
                    add layout.render()
            
