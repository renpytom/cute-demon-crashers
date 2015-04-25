.. This file is auto-generated from Dollphie.




Saving, Loading, and Rollback
*****************************

Ren'Py has a store (well, multiple stores now) where it logs how
values change over the course of a visual novel, such that it can
properly rollback to previous lines of dialogue while also showing the
correct images, as well as saving/loading the current user state,
which is quite neat.


However, the store only “saves” the new value of a particular object
in the store when one replaces the ol value with a new one. In other
words, modifying the fields of an object will not cause that object to
be saved in the store, which might cause quite some trouble when you
have many moving parts.


Compound data structures help you alleviate some of the problem of
keeping track of all the parts by giving you `data coherence`_,
but Python's built-in ones aren't compatible with the Ren'Py store
model, so we can't use them directly.


The objects in this file try to solve that by reconcilling the Ren'Py
store and compound data structures. It works very naïvely by having an
object *claim* an unique name (which must be provided by the user
since this affects future runs of the game as well) in the store, and
properly updating the store reference in response to changes in the
object.



.. _`data coherence`: https://www.youtube.com/watch?v=gVXt1RG_yN0





.. code-block:: py
   
   
   init -100 python:
   






Class: ``StoreBackedObject``
============================




.. class:: StoreBackedObject(slot_name)
   
   
   
   
   .. code-block:: haskell
      
      
      str -> StoreBackedObject
   
   
   
   
   
   
   



The ``StoreBackedObject`` is the core class that encompasses the
premise above. It does so by exposing two methods: ``store`` and
``load``, both manipulating the contents of the Ren'Py's store in
your behalf.


One should call ``store`` when they want to update the value in the
store to whatever new object. Whereas ``load`` is to be called when
one desires to read the value from the store.


Since ``StoreBackedObject`` is a low-level class, it's not meant to
be used directly, but rather mixed into higher-level classes to
give them the ability of storing and manipulating pieces of a
compound data as a shole in the Ren'Py's store.


.. code-block:: py
   
   
       class StoreBackedObject(object):
   




.. rst-class:: hidden-heading




#__init__()
-----------




.. method:: __init__(slot_name)
   
   
   
   
   .. code-block:: haskell
      
      
      str -> unit
   
   
   
   
   
   
   
   
   Initialises an instance of ``StoreBackedObject``.
   
   
   ``slot_name`` must be an unique name in the Ren'Py store.
   
   
   .. code-block:: py
      
      
              def __init__(self, slot_name):
                  self.slot_name = slot_name
      
      
   
   
   
   


.. rst-class:: hidden-heading




#store()
--------




.. method:: store(value)
   
   
   
   
   .. code-block:: haskell
      
      
      a -> unit
   
   
   
   
   
   
   
   
   Updates the contents of the Ren'Py store at the slot this
   object has claimed.
   
   
   This would be the equivalent of doing ``[slot_name] = value`` in
   Ren'Py, where ``slot_name`` is the name of the slot claimed by
   this object.
   
   
   .. code-block:: py
      
      
              def store(self, value):
                  renpy.store.__setattr__(self.slot_name, value)
      
      
   
   
   
   


.. rst-class:: hidden-heading




#load()
-------




.. method:: load([default=None])
   
   
   
   
   .. code-block:: haskell
      
      
      a? -> a | None
   
   
   
   
   
   
   
   
   Tries to retrieve the value stored in the Ren'Py store at the
   slot claimed by this object. If there is no value stored at
   that slot yet, returns the provided default value, if any.
   
   
   .. code-block:: py
      
      
              def load(self, default=None):
                  try:
                      return renpy.store.__getattribute__(self.slot_name)
                  except AttributeError:
                      return default
      
          
   
   
   
   




Class: ``StoreBackedSet``
=========================




.. class:: StoreBackedSet(slot_name)
   
   
   
   
   .. code-block:: haskell
      
      
      str -> StoreBackedSet(a)
   
   
   :Parents:
     StoreBackedObject
   
   
   
   
   



The ``StoreBackedSet`` is similar to Python's built-in ``set`` data
structure, but provides only a subset of its functionality. It is,
however, completely compatible with Ren'Py's store model, by
automatically updating the underlying store whenever parts of it
are modified.


As explained in ``StoreBackedSet``, you must provide a unique name
in the store (i.e.: not being used by any other variable), which
will be the slot *claimed* by this ``set`` structure, and will be
used to save changes to the Ren'Py store behind the scenes.




.. code-block:: py
   :caption:
     Example
   :linenos:
   
   
   
     init python:
       cards_seen = StoreBackedSet("seen_cards")
   
     label cards:
       menu:
         "Select a card to see."
   
         "Ace" if "ace" not in cards_seen:
           cards_seen.add("ace")
   
         "Queen" if "queen" not in cards_seen:
           cards_seen.add("queen")
   
         "Joker" if "joker" not in cards_seen:
           cards_seen.add("joker")
   




.. code-block:: py
   
   
       class StoreBackedSet(StoreBackedObject):
   




.. rst-class:: hidden-heading




#__init__()
-----------




.. method:: __init__(slot_name)
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a), str -> unit
   
   
   
   
   
   
   
   
   Initialises an instance of ``StoreBackedSet``.
   
   
   ``slot_name`` must be an unique name in the Ren'Py store, at
   least amongst other ``StoreBackedSet`` objects.
   
   
   .. code-block:: py
      
      
              def __init__(self, slot_name):
                  super(StoreBackedSet, self).__init__("store_set__" + slot_name)
      
      
   
   
   
   


.. rst-class:: hidden-heading




#load()
-------




.. method:: load()
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a) -> set
   
   
   
   
   
   
   
   
   Tries to retrieve the set from the Ren'Py store. If it fails,
   returns an empty set.
   
   
   .. code-block:: py
      
      
              def load(self):
                  return super(StoreBackedSet, self).load(default=set())
      
      
   
   
   
   


.. rst-class:: hidden-heading




#__contains__()
---------------




.. method:: __contains__(value)
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a), a -> bool
   
   
   
   
   
   
   
   
   Allows one to check for set membership using Python's regular
   ``in`` operator:
   
   
   
   
   .. code-block:: py
      :caption:
        Example
      :linenos:
      
      
      
        s1 = StoreBackedSet("set1")
        "foo" in s1                 # => false
        s1.add("foo")
        "foo" in s1                 # => true
      
   
   
   
   
   .. code-block:: py
      
      
              def __contains__(self, value):
                  return value in self.load()
      
      
   
   
   
   


.. rst-class:: hidden-heading




#add()
------




.. method:: add(value)
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a), a -> StoreBackedSet(a)
   
   
   
   
   
   
   
   
   Adds a new value to the set.
   
   
   .. code-block:: py
      
      
              def add(self, value):
                  old = self.load()
                  old.add(value)
                  self.store(old)
                  return self
      
      
   
   
   
   


.. rst-class:: hidden-heading




#reset()
--------




.. method:: reset()
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a) -> StoreBackedSet(a)
   
   
   
   
   
   
   
   
   Removes all items from the set.
   
   
   .. code-block:: py
      
      
              def reset(self):
                  self.store(set())
                  return self
      
      
   
   
   
   


.. rst-class:: hidden-heading




#remove()
---------




.. method:: remove(value)
   
   
   
   
   .. code-block:: haskell
      
      
      self:StoreBackedSet(a) -> StoreBackedSet(a)
   
   
   
   
   
   
   
   
   Removes a particular item from the set.
   
   
   .. code-block:: py
      
      
              def remove(self, value):
                  old = self.load()
                  if value in old:
                      old.remove(value)
                      self.store(old)
                  return self
      
      
      
      
   
   
   
   


