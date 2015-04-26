.. This file is auto-generated from Dollphie.




Common Ren'Py/Python utilities
******************************

This file contains common utility functions that are used througout the
Cute Demon Crashers! source code.




.. code-block:: py
   
   
   init -100 python:
   






Ren'Py definitions / utilities
==============================

The functions in this category deal with providing simpler and
less repetitive ways of defining some stuff in Ren'Py, as well
as giving access for things for which Ren'Py lacks built-in
functions for, or the built-in is awkward to use.


.. rst-class:: hidden-heading




get_screen_var()
----------------




.. function:: get_screen_var
   
   
   
   
   .. code-block:: haskell
      
      
      str -> None | object
   
   
   
   
   
   
   
   
   Returns the value of a screen variable, or None if called from outside
   of a screen.
   
   
   Ren'Py allows one to define screen-scoped variables (which may even
   be assigned default values in common screen syntax), but doesn't seem
   to provide any functionality for accessing them programmatically
   outside of inline Ren'Py code.
   
   
   This is probably fine for most usages of Screens, but sometimes you
   want to mix some Python code in your Screen language code in order
   to make some things less repetitive. The following definition is
   taken from the internals of ``SetScreenVariable``, which might not
   be the best of the ideas, but works.
   
   
   
   
   .. code-block:: py
      :caption:
        Example
      :linenos:
      
      
      
        screen foo:
          default x = "foo"
          $ ui.text(get_screen_var("x") + "bar")
      
   
   
   
   
   .. code-block:: py
      
      
          def get_screen_var(name):
              cs = renpy.current_screen()
              if cs is not None:
                  return cs.scope[name]
          
      
   
   
   
   


.. rst-class:: hidden-heading




naked()
-------




.. function:: naked(path[, suffix="_cen"])
   
   
   
   
   .. code-block:: haskell
      
      
      str[, str] -> str
   
   
   
   
   
   
   
   
   Returns a displayable that correctly chooses between the censored and
   regular versions of an image, given a path to said image.
   
   
   The substring ``{0}`` in the ``path`` stands for the place where the suffix
   will be inserted if the game is running in the censored mode.
   
   
   For this to work, images must be stored in their censored and
   uncensored versions, and censored images must have a common suffix.
   As an example, if one were to use this for CGs, the CG folder might
   look like the following:
   
   
   
   
   .. code-block:: text
      
      
      
        - akki_cg1.png
        - akki_cg1_censored.png
        - akki_cg2.png
        - akki_cg2_censored.png
        - ( ... )
      
   
   
   
   
   In the example above, the suffix chosen was ``_censored`` (note that it also
   includes the underscore). So, one would be able to define the CGs in Ren'Py
   in the following way:
   
   
   
   
   .. code-block:: py
      :caption:
        Example
      :linenos:
      
      
      
        image akki_cg1 = naked("cgs/akki_cg1{0}.png")
        image akki_cg2 = naked("cgs/akki_cg2{0}.png")
        ( ... )
      
   
   
   
   
   .. code-block:: py
      
      
          def naked(path, suffix="_cen"):
              return ConditionSwitch(
                  "persistent.censor_18", path.format(suffix),
                  True,                   path.format("")
              )
      
          
   
   
   
   


.. rst-class:: hidden-heading




sprite()
--------




.. function:: sprite(name, prefix, image)
   
   
   
   
   .. code-block:: haskell
      
      
      str, str, str -> str
   
   
   
   
   
   
   
   
   Constructs a path to a particular sprite image.
   
   
   Sprites in Cute Demon Crashers! are organised into a
   ``[character]/[character abbrev]_[asset type]_[asset variation].png``
   hierarchy, and this function just makes building that simpler.
   
   
   .. code-block:: py
      
      
          def sprite(name, prefix, image):
              return "assets/sprites/{0}/{1}{2}.png".format(name, prefix, image)
          
   
   
   
   


.. rst-class:: hidden-heading




sprite_orias()
--------------




.. function:: sprite_orias(asset)
   
   
   
   
   
   
   
   
   
   .. code-block:: py
      
      
          def sprite_orias(asset):
              return sprite("orias", "ori_", asset)
      
   
   
   
   


.. rst-class:: hidden-heading




sprite_kael()
-------------




.. function:: sprite_kael(asset)
   
   
   
   
   
   
   
   
   
   .. code-block:: py
      
      
          def sprite_kael(asset):
              return sprite("kael", "ka_", asset)
      
   
   
   
   


.. rst-class:: hidden-heading




sprite_akki()
-------------




.. function:: sprite_akki(asset)
   
   
   
   
   
   
   
   
   
   .. code-block:: py
      
      
          def sprite_akki(asset):
              return sprite("akki", "ak_", asset)
              
   
   
   
   


.. rst-class:: hidden-heading




sprite_mirari()
---------------




.. function:: sprite_mirari(asset)
   
   
   
   
   
   
   
   
   
   .. code-block:: py
      
      
          def sprite_mirari(asset):
              return sprite("mirari", "mi_", asset)
      
   
   
   
   


.. rst-class:: hidden-heading




sprite_claire()
---------------




.. function:: sprite_claire(asset)
   
   
   
   
   
   
   
   
   
   .. code-block:: py
      
      
          def sprite_claire(asset):
              return sprite("claire", "cl_", asset)
      
      
   
   
   
   




Python utilities
================

Python's built-in libraries lack some fairly useful functions.
Functions here vary from “this part would be terser if I could
write it like this,” to “if we had this, we could reduce the
number of possible bugs/catch error earlier,” and everything
in between.


We define them here so they may be used everywhere else.


.. rst-class:: hidden-heading




flatten()
---------




.. function:: flatten(xss)
   
   
   
   
   .. code-block:: haskell
      
      
      list(list(a)) -> list(a)
   
   
   
   
   
   
   
   
   Takes a list of lists and flattens it one level. So, if you have
   a list ``xss`` that looks like ``[[1, 2], [3, 4]]``, ``flatten(xss)``
   would give you ``[1, 2, 3, 4]``.
   
   
   .. code-block:: py
      
      
          def flatten(xss):
              return reduce(lambda: r, x: r + x, xss, [])
      
      
   
   
   
   


.. rst-class:: hidden-heading




merge()
-------




.. function:: merge(a, b)
   
   
   
   
   .. code-block:: haskell
      
      
      a, b -> { a | b }
   
   
   
   
   
   
   
   
   Returns a new dictionary that contains items from both given ones.
   
   
   Python's standard library only contains imperative methods for
   merging dictionaries, which means you can't have a single expression
   updating a dictionary and returning its new value. So this fixes that,
   and gets rid of that pesky mutation by explicitly (shallow) copying
   the dictionary.
   
   
   .. code-block:: py
      
      
          def merge(a, b):
              result = a.copy()
              result.update(b)
              return result
      
      
   
   
   
   


.. rst-class:: hidden-heading




enum()
------




.. function:: enum(*items)
   
   
   
   
   .. code-block:: haskell
      
      
      str... -> Enum
   
   
   
   
   
   
   
   
   Python 2.x lacks an enumeration type (a weaker form of `sum types`_)
   so this, together with the provided custom ``Enum`` class make up for that.
   
   
   As far as Cute Demon Crashers!'s code goes, this is used for the
   ``SexChoiceSet`` object, so choices in the set (which are exposed as
   attributes in the object) are constrained by the possible choices **and**
   get to have a unique value.
   
   
   
   .. _`sum types`: http://en.wikipedia.org/wiki/Tagged_union
   
   
   .. code-block:: py
      
      
          def enum(*items):
              return Enum(**dict(zip(items, range(len(items)))))
          
      
   
   
   
   




Class: ``Enum``
---------------




.. class:: Enum()
   
   
   
   
   
   
   





A class in which instances expose the given initialisation dictionary
as attributes. Not to be used directly, but rather through the ``enum``
function, which accepts a list of names.


.. code-block:: py
   
   
       class Enum(object):
   




.. rst-class:: hidden-heading




#__init__()
-----------




.. method:: __init__(**kwargs)
   
   
   
   
   .. code-block:: haskell
      
      
      dict(a, b)... -> Enum
   
   
   
   
   
   
   
   
   Initialises an ``Enum`` instance.
   
   
   .. code-block:: py
      
      
              def __init__(self, **kwargs):
                  for (key, value) in kwargs.items():
                      self.__setattr__(key, value)
      
   
   
   
   


