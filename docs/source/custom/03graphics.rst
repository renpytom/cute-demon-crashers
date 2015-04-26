.. This file is auto-generated from Dollphie.




Custom Displayables & Graphics
******************************

Ren'Py ships with a handful of displayable objects, which fits quite a
lot of use cases. As for **Cute Demon Crashers!**, we wanted to have
the equivalent of the built-in ``ConditionSwitch``, but which could use
transitions between each state.


The side image is actually the only place where using something like
``ConditionSwitch`` would be absolutely required, but in all other
places it would cut down the amount of work (and image tags!) by quite
a lot, since we've got a plethora of variants for eyes, mouths, and
all sorts of parts that compose a character's sprite.


In light of this, the ideal solution was to write a new displayable
that works in a way very similar to ``ConditionSwitch``, but that allows
transitions to be defined when moving from one state to another. The
custom ``StateMachineDisplayable`` does this by encoding a kind of
`Finite State Machine`_, where one may provide an additional
transition when moving between states. Unlike ``ConditionSwitch``,
however, moving between states in the ``StateMachineDisplayable`` is
explicit, and this comes with the nice side-effect of being able to
provide different transitions at different points in time.


Furthermore, while the ``StateMachineDisplayable`` can only handle one
state at a given time (so, for example, it could only be used for a
single layer in a image), the ``ComposedSprite`` object makes up for
that by providing the analogous of ``LiveComposite`` for
``StateMachineDisplayable``s.



.. _`Finite State Machine`: http://en.wikipedia.org/wiki/Finite-state_machine


.. code-block:: py
   
   
   init -100 python:
   






Class: ``StateMachineDisplayable``
==================================




.. class:: StateMachineDisplayable()
   
   
   :Parents:
     renpy.Displayable, StoreBackedObject
   
   
   
   
   


The ``StateMachineDisplayable`` allows one to have a displayable
that changes throughout the time. It operates as a
`Finite State Machine`_, in which there are several possible
states that it might be, but only one of those can be active at
any given time. 


Each state has an associated Ren'Py displayable, which will be
shown when that this object reaches that state, and transitions
may be provided for moving from one state to another.




Creating StateMachineDisplayables
---------------------------------

To create a ``StateMachineDisplayable``, one needs to pass in an
unique name for the displayable, the initial state of the
displayable, and a mapping of states to other Ren'Py displayables,
which will constitute the possible states that the displayable
might ever be in its lifetime.


The unique name is used to store the current state of the
displayable in a way that's compatible with Ren'Py's
save/load/rollback mechanism. See ``02store.rpy`` for more
information.




.. code-block:: py
   :caption:
     Creating a StateMachineDisplayable
   :linenos:
   
   
   
     claire_base = StateMachineDisplayable(
       "claire_base",        # An unique name for this displayable
       "default",            # The initial state for this displayable
       # A mapping of "state": displayable
       {
         "default": "assets/sprites/claire/cl_base_clothed.png",
         "lazy": "assets/sprites/claire/cl_base/lazy.png",
         "chemise": "assets/sprites/claire/cl_base_chemise.png"
       }
     )
   






Showing and moving between states
---------------------------------

You can change the current state of a ``StateMachineDisplayable`` by
calling the ``set_state`` method and passing in the new state (and
optionally a transition to be used when showing the new
displayable).




.. code-block:: py
   :caption:
     Showing and switching states
   :linenos:
   
   
   
     $ claire_base.set_state("lazy")
     show claire_base with dissolve
     "I feel so lazy today..."
     $ claire_base.set_state("default", transition=Dissolve(1.0, alpha=True))
     "Why must I change? I just want to stay in bed all day..."
   




Another method in the ``StateMachineDisplayable`` class is
``snapshot``, which gives you the displayable associated with a
particular state. This was introduced here primarily so we could
show the CGs that are constructed with this class in the gallery
in a simpler way.




.. code-block:: py
   :caption:
     StateMachineDisplayable snapshots
   :linenos:
   
   
   
     image claire lazy = claire_base.snapshot("lazy")
     $ claire_base.set_state("default")
     show claire lazy at left        # Still the correct `lazy` displayable
     show claire_base at right
   




.. code-block:: py
   
   
       class StateMachineDisplayable(renpy.Displayable, StoreBackedObject):
   




.. rst-class:: hidden-heading




#__init__()
-----------




.. method:: __init__(slot, initial_state, states, **kwargs)
   
   
   
   
   .. code-block:: haskell
      
      
      str, α, { α: Displayable } -> unit
   
   
   
   
   
   
   
   
   Initialises a ``StateMachineDisplayable`` instance.
   
   
   .. code-block:: py
      
      
              def __init__(self, slot, initial_state, states, **properties):
   
   
   
   
   Ren'Py's core displayable classes must be called with the
   additional displayable properties (like style things and
   what not).
   
   
   .. code-block:: py
      
      
                  super(StateMachineDisplayable, self).__init__(**properties)
      
   
   
   
   
   Since this class also uses ``StoreBackedObject`` to properly
   handle Ren'Py's save/loading/rollback system, we need to
   initialise that with an unique slot. We prepend
   ``smd_state__`` to the provided slot so it won't collide
   with other variables/StoreBackedObject classes.
   
   
   .. code-block:: py
      
      
                  StoreBackedObject.__init__(self, "smd_state__" + slot)
      
   
   
   
   
   A ``Transition`` object needs to be provided with two
   displayables, *old* and *new*, it then transitions from
   the old displayable to the new one.
   
   
   We keep track of the old state of this object in the
   ``old_state`` field, then dynamically compute which
   displayable was that from the state mapping. This assumes
   that ``states`` never changes.
   
   
   .. code-block:: py
      
      
                  self.old_state = None
      
   
   
   
   
   Since Ren'Py can rollback, and we only keep track of the
   current state in the store, we need to make sure we don't
   show incorrect transitions when rolling back/forward. Just
   keeping track of the ``current_state`` is sufficient for
   that, but the core of this is done in the ``per_interact``
   method.
   
   
   .. code-block:: py
      
      
                  self.current_state = None
      
   
   
   
   
   The mappings of *state* to *displayable* are stored in the
   ``states`` field. We assume this field never changes.
   
   
   .. code-block:: py
      
      
                  self.states = states
      
   
   
   
   
   At any point in time we'll be showing a displayable to the
   user. This may be a transition, if we've just changed the
   state in this interaction, or a regular displayable.
   
   
   The ``transition`` field stores the transition we're showing
   the user in this interaction, in response to a ``set_state``
   call.
   
   
   .. code-block:: py
      
      
                  self.transition = None
      
   
   
   
   
   The ``displayable`` field stores the displayable associated
   with the current state of the displayable, and we fallback
   to showing just this when no transition is being shown.
   
   
   .. code-block:: py
      
      
                  self.displayable = None
      
   
   
   
   
   Furthermore we need to keep track of the transition's
   shown/animation times, so we pass the correct values when
   rendering it.
   
   
   .. code-block:: py
      
      
                  self.shown_time = 0
                  self.anim_time = 0
      
   
   
   
   
   We use the ``reset`` field to keep track of when we've
   changed states, so we can update the ``shown_time`` and
   ``anim_time`` values accordingly and get the transition
   animation to play correctly.
   
   
   .. code-block:: py
      
      
                  self.reset = False
      
   
   
   
   
   Finally, we move this displayable to the provided initial
   state, so it's ready to be shown on the screen.
   
   
   .. code-block:: py
      
      
                  self.set_state(initial_state)
      
      
   
   
   
   


.. rst-class:: hidden-heading




#snapshot()
-----------




.. method:: snapshot([state=None])
   
   
   
   
   .. code-block:: haskell
      
      
      a -> Displayable
   
   
   
   
   
   
   
   
   Returns the displayable associated with the provided state in
   this object. Fallsback to the current state if no state is
   provided, and finally to the ``Null`` displayable if we can't
   find any displayable in the state mapping.
   
   
   .. code-block:: py
      
      
              def snapshot(self, state=None):
                  return self.states.get(state or self.current_state) or Null()
      
      
   
   
   
   


.. rst-class:: hidden-heading




#redraw()
---------




.. method:: redraw()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> unit
   
   
   
   
   
   
   
   
   Forces this displayable to redraw itself with the new state
   information. Usually called after moving states, or new
   interactions.
   
   
   .. code-block:: py
      
      
              def redraw(self):
                  self.reset = True
                  renpy.redraw(self, 0)
      
      
   
   
   
   


.. rst-class:: hidden-heading




#set_state()
------------




.. method:: set_state(new_state[, transition=None])
   
   
   
   
   .. code-block:: haskell
      
      
      a, Transition -> unit
   
   
   
   
   
   
   
   
   Transitions to the provided new state, optionally with a nice
   transition animation.
   
   
   We'll construct a transition by changing from the current
   state (which is loaded from the Ren'Py store) to the new
   one. If we can't get a displayable for either, we use the
   ``Null`` displayable, which means we don't get any transition
   for things like Dissolve.
   
   
   This also updates the store with the new state, so state
   changes works properly with rollbacks and loading.
   
   
   .. code-block:: py
      
      
              def set_state(self, new_state, transition=None):
                  self.current_state = new_state
                  self.old_state = self.load()
                  self.store(new_state)
          
                  old_d = self.states.get(self.old_state) or Null()
                  cur_d = renpy.easy.displayable(self.states.get(new_state) or Null())
                  self.displayable = cur_d
                  self.transition = anim.TransitionAnimation(old_d, 0.0, transition, cur_d)
                  self.redraw()
      
      
   
   
   
   


.. rst-class:: hidden-heading




#per_interact()
---------------




.. method:: per_interact()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> unit
   
   
   
   
   
   
   
   
   Ren'Py calls ``per_interact`` internally every time a new
   interaction begins. This gives us a chance of showing the
   proper state to the user in case of rollbacks.
   
   
   .. code-block:: py
      
      
              def per_interact(self):
                  new_state = self.load()
      
   
   
   
   
   To avoid creating displayables unecessarily, we only call
   ``set_state`` when the new state is really a **new** state.
   
   
   .. code-block:: py
      
      
                  if self.current_state != new_state:
                      self.set_state(new_state)
      
   
   
   
   
   Also, in order to avoid showing the wrong transition to
   people, we get rid of it in new interactions.
   
   
   .. code-block:: py
      
      
                  if not self.reset:
                      self.transition = None
                      self.redraw()
      
      
   
   
   
   


.. rst-class:: hidden-heading




#current_displayable()
----------------------




.. method:: current_displayable()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> Displayable
   
   
   
   
   
   
   
   
   Returns the displayable that should be shown to the user in
   this interaction.
   
   
   .. code-block:: py
      
      
              def current_displayable(self):
                  return self.transition or self.displayable
      
      
   
   
   
   


.. rst-class:: hidden-heading




#render()
---------




.. method:: render(width, height, st, at)
   
   
   
   
   .. code-block:: haskell
      
      
      int, int, int, int -> renpy.Render
   
   
   
   
   
   
   
   
   Renders the current displayable so Ren'Py can show it on the
   screen.
   
   
   .. code-block:: py
      
      
              def render(self, width, height, st, at):
   
   
   
   
   We need to reset the times if this is the first time we're
   showing this state, so transitions/animations work
   correctly.
   
   
   .. code-block:: py
      
      
                  if self.reset:
                      self.reset = False
                      self.shown_time = st
                      self.anim_time = at
      
                  d = self.current_displayable()
                  if d:
                      return renpy.render(d,
                                          width,
                                          height,
                                          st - self.shown_time,
                                          at - self.anim_time)
                  else:
                      return renpy.Render(0, 0)
      
   
   
   
   


.. rst-class:: hidden-heading




#visit()
--------




.. method:: visit()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> list(Displayable)
   
   
   
   
   
   
   
   
   Ren'Py uses this list to predict images and stuff.
   
   
   .. code-block:: py
      
      
              def visit(self):
                  return [self.transition, self.displayable]
          
      
   
   
   
   


