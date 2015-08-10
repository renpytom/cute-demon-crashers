#- Gallery and Replay --------------------------------------------------
# 
# The Cute Demon Crashers! gallery has to support a few different kinds
# of items. Scene replays, pannable images, regular images, and
# character outfits look similar in the gallery, but require different
# ways of displaying or unlocking.
#
# With that in mind, this file provides the basic functionality for
# capturing all of these different types of images into a single,
# well-defined interface, with which the Gallery screen can interact
# without being aware of the differences. This simplifies a lot of the
# work.
init -100 python:

    #-- State ----------------------------------------------------------
    
    #### data: persistent.unlocked_gallery
    # @type: set(any)
    #
    # A set of items that have been unlocked in the gallery. These
    # account for sprites not having a distinct tag for each variation,
    # in which case we can't use Ren'Py's internal `seen_image()`
    # function.
    if persistent.unlocked_gallery is None:
        persistent.unlocked_gallery = set()


    #-- Image representation -------------------------------------------

    #### class: GalleryItem(object)
    # 
    # The common interface for each individual item in the gallery. An
    # item can be an image, or anything else we show to the user. Items
    # can only be parts of a separate bundle.
    class GalleryItem(object):
        ##### method: is_unlocked(self)
        # @type: () -> bool
        #
        # True if this item is unlocked in the gallery, since items
        # might diverge on when they're considered unlocked. Bundles
        # compute the amount of unlocked images based on this.
        def is_unlocked(self):
            return False

        ##### method: get_displayable(self)
        # @type: () -> Displayable
        #
        # Returns a displayable for showing this item on the screen.
        def get_displayable(self):
            return None

        ##### method: get_items(self)
        # @type: () -> [GalleryItem]
        #
        # Some gallery items might be just a convenient way of defining
        # several other gallery items. In order to flatten all of them
        # into a single list of items, the bundle uses this method.
        def get_items(self):
            return [self]


    #### class: RenpyImage(GalleryItem)
    # 
    # Represents images that are shown and tracked by Ren'Py's standard
    # API.
    class RenpyImage(GalleryItem):

        ##### method: __init__(self, id)
        # @type: str -> RenpyImage
        #
        # Initialises a Ren'Py image. `id` should be the full name of
        # the image, e.g.: "RenpyImage('akki kiss')"
        def __init__(self, id):
            self.id = id

        ##### method: is_unlocked(self)
        # @type: () -> bool
        def is_unlocked(self):
            return renpy.seen_image(self.id)

        ##### method: get_displayable(self)
        # @type: () -> Displayable
        def get_displayable(self):
            return renpy.display.image.ImageReference(self.id)


    #### class: SpriteImage(GalleryItem)
    # 
    # Sprite images are single objects that represent a snapshot of a
    # particular `ComposedSprite`.
    def SpriteImage(GalleryItem):

        ##### method: __init__(self, id, image)
        # @type: any, Displayable -> SpriteImage
        def __init__(self, id, image):
            self.id = id
            self.image = image

        ##### method: is_unlocked(self)
        # @type: () -> bool
        def is_unlocked(self):
            return self.id in persistent.unlocked_gallery

        ##### method: get_displayable(self)
        # @type: () -> Displayable
        def get_displayable(self):
            return self.image
        
        

    #### class: SpriteImageSet(GalleryItem)
    # 
    # Sprite image sets are collections of images formed by a sequence
    # of state transformations over a `ComposedSprite` object. They
    # particularly make it simpler for us to define image galleries by
    # just providing states, rather than getting a complete snapshot.
    def SpriteImageSet(GalleryItem):
        ##### method: __init__(self, id, sprite, initial_state, *states)
        # @type: str, ComposedSprite, dict(a, b), dict(a, b)... -> SpriteImageSet
        def __init__(self, id, sprite, initial_state, *states):
            self.id = id
            self.sprite = sprite
            self.initial_state = initial_state
            self.states = states

        ##### method: get_items(self)
        # @type: () -> [GalleryItem]
        def get_items(self):
            def to_item(st):
                return SpriteImage(
                    (self.id, self.sprite.dict_to_state_tuple(st)),
                    self.sprite.snapshot(**st)
                )

            return map(to_item, scan(merge, self.initial_state, self.states))


    #-- Bundles of images ----------------------------------------------

    #### class: GalleryBundle(object)
    #
    # Bundles define groups of images or other items, and are displayed
    # as a single entity in the Gallery.
    class GalleryBundle(object):

        ##### method: __init__(self, idle_thumb, hover_thumble)
        # @type: Displayable, Displayable -> GalleryBundle
        def __init__(self, idle_thumb, hover_thumb, **kwargs):
            ##### data: idle_thumb
            # @type: Displayable
            #
            # The thumbnail to show in the gallery when idle.
            self.idle_thumb = idle_thumb

            ##### data: hover_thumb
            # @type: Displayable
            #
            # The thumbnail to show in the gallery when hovered.
            self.hover_thumb = hover_thum


        ##### method: is_unlocked(self)
        # @type: () -> bool
        #
        # True if at least one of the images are unlocked.
        def is_unlocked(self):
            return len(self.get_unlocked()) > 0
            
        ##### method: get_unlocked(self)
        # @type: () -> [GalleryItem]
        #
        # Returns a list of unlocked gallery items in this bundle.
        def get_unlocked(self):
            return []

        ##### method: show(self)
        # @type: () -> () -> unit
        #
        # Shows the bundle to the player.
        def show(self):
            return lambda: None


    #### class: ImageBundle(GalleryBundle)
    #
    # A bundle of regular images.
    class ImageBundle(GalleryBundle):

        ##### method: __init__(self, *images, **kwargs)
        # @type: GalleryItem..., **any -> ImageBundle
        def __init__(self, *images, **kwargs):
            super(ImageBundle, self).__init__(**kwargs)
            self.images = flatten(map(lambda x: x.to_items(), images))

        ##### method: get_unlocked(self)
        # @type: () -> [GalleryItem]
        def get_unlocked(self):
            return filter(lambda x: x.is_unlocked(), self.images)

        ##### method: show(self)
        # @type: () -> () -> unit
        def show(self):
            def run():
                images = map(lambda x: x if x.is_unlocked() else None, self.images)
                renpy.show_screen("gallery_view", images, transition=dissolve)

            return run


    #### class: ReplayBundle(GalleryBundle)
    #
    # Represents replay items in the gallery.
    class ReplayBundle(GalleryBundle):

        ##### method: __init__(self, label, initialiser, **kwargs)
        # @type: str, (() -> dict(a, b)), **any -> ReplayBundle
        def __init__(self, label, initialiser, **kwargs):
            self.label = label
            self.initialiser = initialiser

        ##### method: is_unlocked(self)
        # @type: () -> bool
        def is_unlocked(self):
            return renpy.seen_label(self.label)

        ##### method: show(self)
        # @type: () -> () -> unit
        def show(self):
            return Replay(self.label, self.initialiser())
        

    #-- Folders --------------------------------------------------------

    #### class: GalleryFolder(object)
    # 
    # A gallery folder represents any of the divisions in the
    # gallery. It must have a name and a `select` method that handles
    # selection in the gallery.
    class GalleryFolder(object):
        def __init__(self, name, thumb):
            self.name = name
            self.thumb = thumb

        def select(self):
            return lambda: None


    #### class: TutorialFolder(object)
    #
    # A gallery folder that shows the tutorial screen.
    class TutorialFolder(GalleryFolder):
        def select(self):
            return Show("tutorial", transition=dissolve, action_=Hide("tutorial"))


    #### class: ImageFolder(object)
    #
    # A gallery folder that only shows images.
    class ImageFolder(GalleryFolder):
        def __init__(self, name, *bundles, **kwargs):
            super(ImageFolder, self).__init__(name, **kwargs)
            self.bundles = bundles

            

    #### class: CharacterFolder(ImageFolder)
    #
    # A gallery folder for a character, that supports showing
    # characters' outfits.
    class CharacterFolder(GalleryFolder):
        def __init__(self, name, sprite, *bundles, **kwargs):
            super(CharacterFolder, self).__init__(name, *bundles, **kwargs)
            self.sprite = sprite



    #### class: ReplayFolder(GalleryFolder)
    #
    # A gallery folder that contains Replay bundles.
    class ReplayFolder(GalleryFolder):
        def __init__(self, name, *bundles, **kwargs):
            super(ReplayFolder, self).__init__(name, **kwargs)
            self.bundles = bundles

    

        
    #-- Gallery --------------------------------------------------------

    #### class: Gallery(object)
    # 
    # The gallery object holds the definition of the images in the
    # gallery, and provides an interface for unlocking items that can't
    # use Ren'Py's built-in tools.
    class Gallery(object):

        ##### method: __init__(self, *folders)
        # @type: GalleryFolder... -> Gallery
        def __init__(self, *folders):
            self.folders = folders
            self.sprite_map = {}

        ##### method: __getitem__(self, key)
        # @type: any -> [GalleryBundle]
        def __getitem__(self, key):
            for folder in self.folders:
                if folder.name == key:
                    return folder
            raise KeyError(key)

        ##### method: add_unlockable_sprite(self, sprite, name)
        # @type: ComposedSprite, str -> unit
        #
        # Modifies a ComposedSprite such that for each state transition
        # the relevant state ID is unlocked in the gallery
        # automatically.
        def add_unlockable_sprite(self, sprite, name):
            def wrap_unlock(f):
                def apply(*args, **kwargs):
                    result = f(*args, **kwargs)
                    self.unlock_sprite(sprite)
                    return result
                return apply
            
            setattr(sprite, "set_state", wrap_unlock(sprite.set_state))
            self.sprite_map[sprite] = name


        ##### method: unlock_sprite(self, sprite)
        # @type: ComposedSprite -> unit
        #
        # Unlocks the current state of a previously registered
        # ComposedSprite.
        def unlock_sprite(self, sprite):
            self.unlock((self.sprite_map[sprite], sprite.state()))


        ##### method: unlock(self, id)
        # @type: any -> unit
        #
        # Unlocks the given ID in the gallery.
        def unlock(self, id):
            persistent.unlocked_gallery.add(id)



#    class ImageSet(object):
#        def __init__(self, *images):
#            self.images = flatten(map(lambda x: x.to_gallery_items(), images))
#
#        def to_bundle(self):
#            def is_locked(x):
#                return x.is_locked()
#
#            def negate(f):
#                return lambda a: not f(a)
#
#            unlocked = filter(negate(is_locked), self.images)
#            return GalleryBundle(self.images, unlocked)
#
#        
#    class GalleryBundle(object):
#        def __init__(self, bundle, unlocked):
#            def is_locked(x): return x not in unlocked
#            def branch(p, f, g): return lambda a: f(a) if p(a) else g(a)
#
#            self.total = len(bundle)
#            self.unlocked = len(unlocked)
#            self.thumbnail = unlocked[0].image if len(unlocked) > 0 else Null(width=1, height=1)
#            self.images = map(branch(is_locked, GalleryLocked, GalleryUnlocked), bundle)
#
#        def is_unlocked(self):
#            return self.unlocked > 0
#            
#        def display(self):
#            return Show("gallery_view", dissolve, self)
#        
#
#    class ReplayBundle(object):
#        def __init__(self, label_, thumbnail, initialiser):
#            self.thumbnail = thumbnail
#            self.label_ = label_
#            self.initialiser = initialiser
#
#        def is_unlocked(self):
#            return renpy.seen_label(self.label_)
#
#        def display(self):
#            return Replay(self.label_, self.initialiser())
#
#        def to_bundle(self):
#            return self
#        
#
#    class GalleryFolder(object):
#        def __init__(self, name, *args):            
#            self.images = args
#            self.name = name
#
#        def __iter__(self):
#            return self.images.__iter__()
#
#
#    class GalleryItem(object):
#        def __init__(self, id, image):
#            self.id = id
#            self.image = image
#
#        def is_locked(self):
#            return self.id not in persistent.unlocked_gallery
#            
#
#    class CG(object):
#        def __init__(self, id, image):
#            self.id = id
#            self.image = image
#
#        def is_locked(self):
#            return self.id not in persistent.unlocked_gallery
#
#        def to_gallery_items(self):
#            return [GalleryItem(self.id, self.image)]
#
#
#    class RenpyImage(object):
#        def __init__(self, id):
#            self.id = id
#            self.image = renpy.display.image.ImageReference(id)
#
#        def is_locked(self):
#            return not renpy.seen_image(self.id)
#
#        def to_gallery_items(self):
#            return [self]
#        
#        
#    class SpriteCG(CG):
#        def __init__(self, id, sprite, initial_state, *states):
#            self.id = id
#            self.sprite = sprite
#            self.initial_state = initial_state
#            self.states = states
#
#        def to_gallery_items(self):
#            def to_item(st):
#                return GalleryItem(
#                    (self.id, self.sprite.dict_to_state_tuple(st)),
#                    self.sprite.snapshot(**st)
#                    )
#                
#            return map(to_item, scan(merge, self.initial_state, self.states))
#
#
#    class GalleryImage(object):
#        pass
#
#
#    class GalleryLocked(GalleryImage):
#        def __init__(self, cg):
#            self.image = cg.image
#
#        def is_locked(self):
#            return True
#
#    class GalleryUnlocked(GalleryImage):
#        def __init__(self, cg):
#            self.image = cg.image
#
#        def is_locked(self):
#            return False
