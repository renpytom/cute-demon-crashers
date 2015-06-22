#- Common Ren'Py/Python utilities --------------------------------------
#
# This file contains common utility functions that are used througout the
# Cute Demon Crashers! source code.

init -100 python:

    #-- Ren'Py definitions / utilities ---------------------------------
    #
    # The functions in this category deal with providing simpler and
    # less repetitive ways of defining some stuff in Ren'Py, as well
    # as giving access for things for which Ren'Py lacks built-in
    # functions for, or the built-in is awkward to use.


    #### function: get_screen_var(name)
    # @type: str -> None | object
    #
    # Returns the value of a screen variable, or None if called from outside
    # of a screen.
    #
    # Ren'Py allows one to define screen-scoped variables (which may even
    # be assigned default values in common screen syntax), but doesn't seem
    # to provide any functionality for accessing them programmatically
    # outside of inline Ren'Py code.
    #
    # This is probably fine for most usages of Screens, but sometimes you
    # want to mix some Python code in your Screen language code in order
    # to make some things less repetitive. The following definition is
    # taken from the internals of `SetScreenVariable`, which might not
    # be the best of the ideas, but works.
    #
    # @example("py"){{{
    #   screen foo:
    #     default x = "foo"
    #     $ ui.text(get_screen_var("x") + "bar")
    # }}}
    def get_screen_var(name):
        cs = renpy.current_screen()
        if cs is not None:
            return cs.scope[name]


    #### function: make_character(*args, **kwargs)
    # @type: any... -> Character
    #
    # Creates a new character with pre-defined options.
    #
    # Usually you'd set up a template character in Ren'Py and then
    # have your other characters inherit from that one.
    def make_character(*args, **kwargs):
        ctc_indicator = LiveComposite((50, 27),
                                      (10, 0), At("assets/ui/ctc.png", heartbeat))

        return Character(ctc=ctc_indicator,
                         ctc_timedpause=Null(),
                         *args, **kwargs)


    #### function: naked(path[, suffix="_cen"])
    # @type: str[, str] -> str
    #
    # Returns a displayable that correctly chooses between the censored and
    # regular versions of an image, given a path to said image.
    #
    # The substring `{0}` in the `path` stands for the place where the suffix
    # will be inserted if the game is running in the censored mode.
    #
    # For this to work, images must be stored in their censored and
    # uncensored versions, and censored images must have a common suffix.
    # As an example, if one were to use this for CGs, the CG folder might
    # look like the following:
    #
    # @code("text"){{{
    #   - akki_cg1.png
    #   - akki_cg1_censored.png
    #   - akki_cg2.png
    #   - akki_cg2_censored.png
    #   - ( ... )
    # }}}
    #
    # In the example above, the suffix chosen was `_censored` (note that it also
    # includes the underscore). So, one would be able to define the CGs in Ren'Py
    # in the following way:
    #
    # @example("py"){{{
    #   image akki_cg1 = naked("cgs/akki_cg1{0}.png")
    #   image akki_cg2 = naked("cgs/akki_cg2{0}.png")
    #   ( ... )
    # }}}
    def naked(path, suffix="_cen"):
        return ConditionSwitch(
            "persistent.censor_18", path.format(suffix),
            True,                   path.format("")
        )


    #### function: sprite(name, prefix, image)
    # @type: str, str, str -> str
    #
    # Constructs a path to a particular sprite image.
    #
    # Sprites in Cute Demon Crashers! are organised into a
    # `[character]/[character abbrev]_[asset type]_[asset variation].png`
    # hierarchy, and this function just makes building that simpler.
    def sprite(name, prefix, image):
        return "assets/sprites/{0}/{1}{2}.png".format(name, prefix, image)

    #### function: sprite_orias(asset)
    def sprite_orias(asset):
        return sprite("orias", "ori_", asset)

    #### function: sprite_kael(asset)
    def sprite_kael(asset):
        return sprite("kael", "ka_", asset)

    #### function: sprite_akki(asset)
    def sprite_akki(asset):
        return sprite("akki", "ak_", asset)

    #### function: sprite_mirari(asset)
    def sprite_mirari(asset):
        return sprite("mirari", "mi_", asset)

    #### function: sprite_claire(asset)
    def sprite_claire(asset):
        return sprite("claire", "cl_", asset)


    #-- Python utilities -----------------------------------------------
    #
    # Python's built-in libraries lack some fairly useful functions.
    # Functions here vary from “this part would be terser if I could
    # write it like this,” to “if we had this, we could reduce the
    # number of possible bugs/catch error earlier,” and everything
    # in between.
    #
    # We define them here so they may be used everywhere else.

    #### function: flatten(xss)
    # @type: list(list(a)) -> list(a)
    #
    # Takes a list of lists and flattens it one level. So, if you have
    # a list `xss` that looks like `[[1, 2], [3, 4]]`, `flatten(xss)`
    # would give you `[1, 2, 3, 4]`.
    def flatten(xss):
        return reduce(lambda r, x: r + x, xss, [])


    #### function: scan(f, initial, xs)
    # @type: (b, a, -> b), b, list(a) -> list(b)
    #
    # Like `reduce`, but accumulates the results, such that
    # `scan(f, 0, [1, 2, 3]) => [f(0, 1), f(f(0, 1), 2), ...]`
    def scan(f, initial, xs):
        def go(r, x):
            (item, ys) = r
            y = f(item, x)
            return (y, ys + [y])
        
        return reduce(go, xs, (initial, []))[1]
    

    #### function: merge(a, b)
    # @type: a, b -> { a | b }
    #
    # Returns a new dictionary that contains items from both given ones.
    #
    # Python's standard library only contains imperative methods for
    # merging dictionaries, which means you can't have a single expression
    # updating a dictionary and returning its new value. So this fixes that,
    # and gets rid of that pesky mutation by explicitly (shallow) copying
    # the dictionary.
    def merge(a, b):
        result = a.copy()
        result.update(b)
        return result


    #### function: enum(*items)
    # @type: str... -> Enum
    #
    # Python 2.x lacks an enumeration type (a weaker form of @link("sum types"))
    # so this, together with the provided custom `Enum` class make up for that.
    #
    # As far as Cute Demon Crashers!'s code goes, this is used for the
    # `SexChoiceSet` object, so choices in the set (which are exposed as
    # attributes in the object) are constrained by the possible choices **and**
    # get to have a unique value.
    #
    # @ref("sum types"): http://en.wikipedia.org/wiki/Tagged_union
    def enum(*items):
        return Enum(**dict(zip(items, range(len(items)))))


    #### class: Enum()
    # @private
    #
    # A class in which instances expose the given initialisation dictionary
    # as attributes. Not to be used directly, but rather through the `enum`
    # function, which accepts a list of names.
    class Enum(object):

        #### method: __init__(**kwargs)
        # @type: dict(a, b)... -> Enum
        #
        # Initialises an `Enum` instance.
        def __init__(self, **kwargs):
            for (key, value) in kwargs.items():
                self.__setattr__(key, value)
