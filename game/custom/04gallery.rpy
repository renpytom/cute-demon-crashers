init -100 python:

    class Gallery(StoreBackedObject):
        def __init__(self, *folders):
            self.folders = folders
            self.slot_name = "gallery_state__unlocked"

        def __getitem__(self, key):
            for folder in self.folders:
                if folder.name == key:
                    return map(self._wrap_images, folder)
            return []

        def unlock(self, id):
            self.store(self.load(set()).add(id))

        def _wrap_images(self, bundle):
            def is_locked(x): return x.id in self.load(set())
            def negate(f): return lambda a: not f(a)

            unlocked = filter(negate(is_locked), bundle)
            return GalleryBundle(bundle, unlocked)


    class GalleryBundle(object):
        def __init__(self, bundle, unlocked):
            def is_locked(x): return x in unlocked
            def branch(p, f, g): return lambda a: f(a) if p(a) else g(a)

            self.total = len(bundle)
            self.unlocked = len(unlocked)
            self.thumbnail = unlocked[0].image if len(unlocked) > 0 else Null(width=1, height=1)
            self.images = map(branch(is_locked, GalleryLocked, GalleryUnlocked), bundle)


    class GalleryFolder(object):
        def __init__(self, name, *args):
            self.images = args
            self.name = name

        def __iter__(self):
            return self.images.__iter__()


    class CG(object):
        def __init__(self, id, image):
            self.id = id
            self.image = image

    class GalleryImage(object):
        pass


    class GalleryLocked(GalleryImage):
        def __init__(self, cg):
            self.image = cg.image


    class GalleryUnlocked(GalleryImage):
        def __init__(self, cg):
            self.image = cg.image
