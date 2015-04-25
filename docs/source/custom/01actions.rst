.. This file is auto-generated from Dollphie.




Custom actions
**************

We define here classes that can be used as actions in buttons
and other interactable elements in a screen, similar to the actions
that you may find in Ren'Py's core distribution.




.. code-block:: py
   
   
   init -100 python:
   






Class: ``SetPersistent``
========================




.. class:: SetPersistent(name, value)
   
   
   
   
   .. code-block:: haskell
      
      
      str, a -> SetPersistent
   
   
   :Parents:
     Action, FieldEquality
   
   
   
   
   



Ren'Py lacks an action that changes values from the persistent
storage in the core distribution, so this class provides that.


Usage follows from the other ``Set*`` actions in Ren'Py's
core distribution:




.. code-block:: py
   :caption:
     Example
   :linenos:
   
   
   
     screen foo:
       textbutton _("Click Me!") action SetPersistent("clicked", True)
   




.. code-block:: py
   
   
       @renpy.pure
       class SetPersistent(Action, FieldEquality):
           identity_fields = ['value']
           equality_fields = ['name']
   




.. rst-class:: hidden-heading




#__init__()
-----------




.. method:: __init__(name, value)
   
   
   
   
   .. code-block:: haskell
      
      
      str, a -> unit
   
   
   
   
   
   
   
   
   Initialises a SetPersistent instance.
   
   
   .. code-block:: py
      
      
              def __init__(self, name, value):
                  self.name = name
                  self.value = value
      
   
   
   
   


.. rst-class:: hidden-heading




#__call__()
-----------




.. method:: __call__()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> unit
   
   
   
   
   
   
   
   
   Invokes this action, causing the persistent value to be changed
   and restarts the interaction so any element that might depend
   on that value can update its representation on the screen.
   
   
   .. code-block:: py
      
      
              def __call__(self):
                  setattr(persistent, self.name, self.value)
                  renpy.save_persistent()
                  renpy.restart_interaction()
      
   
   
   
   


.. rst-class:: hidden-heading




#get_selected()
---------------




.. method:: get_selected()
   
   
   
   
   .. code-block:: haskell
      
      
      unit -> unit
   
   
   
   
   
   
   
   
   Called internally by Ren'Py when used with buttons and similar
   elements to automatically update the state of those elements
   according to the value of the persistent field.
   
   
   .. code-block:: py
      
      
              def get_selected(self):
                  return getattr(persistent, self.name) == self.value
          
      
   
   
   
   


