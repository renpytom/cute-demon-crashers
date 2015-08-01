init -100 python:

    if persistent.unlocked_gallery is None:
        persistent.unlocked_gallery = set()

    class Gallery(object):
        def __init__(self, *folders):
            self.folders = folders
            self.sprite_map = {}

        def __getitem__(self, key):
            for folder in self.folders:
                if folder.name == key:
                    return map(lambda x: x.to_bundle(), folder)
            return []

        def add_unlockable_sprite(self, sprite, name):
            def wrap_unlock(f):
                def apply(*args, **kwargs):
                    result = f(*args, **kwargs)
                    self.unlock_sprite(sprite)
                    return result
                return apply
            
            setattr(sprite, "set_state", wrap_unlock(sprite.set_state))
            self.sprite_map[sprite] = name

        def unlock_sprite(self, sprite):
            self.unlock((self.sprite_map[sprite], sprite.state()))

        def unlock(self, id):
            persistent.unlocked_gallery.add(id)



    class ImageSet(object):
        def __init__(self, *images):
            self.images = flatten(map(lambda x: x.to_gallery_items(), images))

        def to_bundle(self):
            def is_locked(x):
                return x.is_locked()

            def negate(f):
                return lambda a: not f(a)

            unlocked = filter(negate(is_locked), self.images)
            return GalleryBundle(self.images, unlocked)

        
    class GalleryBundle(object):
        def __init__(self, bundle, unlocked):
            def is_locked(x): return x not in unlocked
            def branch(p, f, g): return lambda a: f(a) if p(a) else g(a)

            self.total = len(bundle)
            self.unlocked = len(unlocked)
            self.thumbnail = unlocked[0].image if len(unlocked) > 0 else Null(width=1, height=1)
            self.images = map(branch(is_locked, GalleryLocked, GalleryUnlocked), bundle)

        def is_unlocked(self):
            return self.unlocked > 0
            
        def display(self):
            return Show("gallery_view", dissolve, self)
        

    class ReplayBundle(object):
        def __init__(self, label_, thumbnail, initialiser):
            self.thumbnail = thumbnail
            self.label_ = label_
            self.initialiser = initialiser

        def is_unlocked(self):
            return renpy.seen_label(self.label_)

        def display(self):
            return Replay(self.label_, self.initialiser())

        def to_bundle(self):
            return self
        

    class GalleryFolder(object):
        def __init__(self, name, *args):            
            self.images = args
            self.name = name

        def __iter__(self):
            return self.images.__iter__()


    class GalleryItem(object):
        def __init__(self, id, image):
            self.id = id
            self.image = image

        def is_locked(self):
            return self.id not in persistent.unlocked_gallery
            

    class CG(object):
        def __init__(self, id, image):
            self.id = id
            self.image = image

        def is_locked(self):
            return self.id not in persistent.unlocked_gallery

        def to_gallery_items(self):
            return [GalleryItem(self.id, self.image)]


    class RenpyImage(object):
        def __init__(self, id):
            self.id = id
            self.image = renpy.display.image.ImageReference(id)

        def is_locked(self):
            return not renpy.seen_image(self.id)

        def to_gallery_items(self):
            return [self]
        
        
    class SpriteCG(CG):
        def __init__(self, id, sprite, initial_state, *states):
            self.id = id
            self.sprite = sprite
            self.initial_state = initial_state
            self.states = states

        def to_gallery_items(self):
            def to_item(st):
                return GalleryItem(
                    (self.id, self.sprite.dict_to_state_tuple(st)),
                    self.sprite.snapshot(**st)
                    )
                
            return map(to_item, scan(merge, self.initial_state, self.states))


    class GalleryImage(object):
        pass


    class GalleryLocked(GalleryImage):
        def __init__(self, cg):
            self.image = cg.image

        def is_locked(self):
            return True

    class GalleryUnlocked(GalleryImage):
        def __init__(self, cg):
            self.image = cg.image

        def is_locked(self):
            return False
