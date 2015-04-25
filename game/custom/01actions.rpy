#- Custom actions ------------------------------------------------------
#
# We define here classes that can be used as actions in buttons
# and other interactable elements in a screen, similar to the actions
# that you may find in Ren'Py's core distribution.

init -100 python:

    ### class: SetPersistent(name, value) < Action, FieldEquality
    # @type: str, a -> SetPersistent
    #
    # Ren'Py lacks an action that changes values from the persistent
    # storage in the core distribution, so this class provides that.
    #
    # Usage follows from the other `Set*` actions in Ren'Py's
    # core distribution:
    #
    # @example("py"){{{
    #   screen foo:
    #     textbutton _("Click Me!") action SetPersistent("clicked", True)
    # }}}
    @renpy.pure
    class SetPersistent(Action, FieldEquality):
        identity_fields = ['value']
        equality_fields = ['name']

        #### method: __init__(name, value)
        # @type: str, a -> unit
        #
        # Initialises a SetPersistent instance.
        def __init__(self, name, value):
            self.name = name
            self.value = value

        #### method: __call__()
        # @type: unit -> unit
        #
        # Invokes this action, causing the persistent value to be changed
        # and restarts the interaction so any element that might depend
        # on that value can update its representation on the screen.
        def __call__(self):
            setattr(persistent, self.name, self.value)
            renpy.save_persistent()
            renpy.restart_interaction()

        #### method: get_selected()
        # @type: unit -> unit
        #
        # Called internally by Ren'Py when used with buttons and similar
        # elements to automatically update the state of those elements
        # according to the value of the persistent field.
        def get_selected(self):
            return getattr(persistent, self.name) == self.value
    
