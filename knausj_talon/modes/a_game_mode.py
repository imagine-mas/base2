from talon import Module, actions, clip

left, up, right, down = False,False,False,False
previous = ""


mod = Module()
@mod.action_class
class Actions:

    # method
    def hold_key(direction:str):
        ''' Holds down the key '''
        global previous

        if previous=="left":
            actions.key("left:up")
        if previous=="right":
            actions.key("right:up")
        if previous=="up":
            actions.key("up:up")
        if previous=="down":
            actions.key("down:up")

        previous = direction
        
        actions.key(direction+":down")
        
    def move_some(direction:str, time:int):
        ''' Stuff stuff '''
        actions.key(direction+":down")
        actions.sleep(time)
        actions.key(direction+":up")

    def stop_all():
        ''' Holds down the left key '''
        actions.key("left:up")
        actions.key("right:up")
        actions.key("up:up")
        actions.key("down:up")
