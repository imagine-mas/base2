from talon import Module, actions, clip

''' 
    front tier means frontier
    front tier means frontier
    front tier

    class Node():
    self front tier is a list   
    self.front_tier = []
    self.front_tier = []


    def add(self, node):
    Self front tier calls append takes note

    Method contains state takes self and state
    Return any takes note calls the state equates the state for note in self frontier

    Method empty takes self
    Return length self frontier equates 0

    Method removed takes self
    If self empty takes
    Raise exception takes "empty frontier"
    Else
    note equals the cell front tier at -1
    Self a front tier equals self frontier at :-1
    Return node

'''

''' 
    Class node
    initial method takes self and state and parent and action
    Initialize state, parents, action  # have a command that says estate means state
    Self state is state
    self parent is parent
    self action is action

    Class stack frontier
    Initial method takes self
    self front tier is a list   # have a temporary place where front tier Means frontier, Note to means node

    Method add takes self and node
    Self front tier calls append takes note

    Method contains state takes self and state
    Return any takes note calls the state equates the state for note in self frontier

    Method empty takes self
    Return length self frontier equates 0

    Method removed takes self
    If self empty takes
    Raise exception takes "empty frontier"
    Else
    note equals the cell front tier at -1
    Self a front tier equals self frontier at :-1
    Return node
'''

''' 
words_to_skip_+=_num_words_converted
words_to_skip += num_words_converted
words_to_skip += num_words_converted

actions {} "
Actions string over


'''

mod = Module()
@mod.action_class
class Actions:
    # Has to do with application building
    def space_check() -> str:
        '''check for space'''
        actions.edit.line_start()
        actions.insert("\"") 
        actions.edit.line_end()
        
        actions.edit.extend_left()
        actions.edit.copy()
        actions.sleep("100ms")
        line = clip.text()
        actions.edit.line_end()
        actions.insert("\"") 

        if line == " ":
            actions.edit.line_end()
            actions.key("backspace")
    
    # ''' corrects spacing in code'''
    def clean_code():
        ''' corrects spacing in code'''
        
        values= ["+","=",",","+=","==","!="]
        for value in values:
            for options in range(3):
                actions.key("ctrl-f")
                actions.key("shift-tab")
                actions.key("enter")
                actions.key("tab")
                actions.edit.delete_line()

                if (value == "=="): actions.insert("=  =")
                elif (value == "+="): actions.insert("+ =")
                elif (value == "!=") and options == 0: actions.insert("! =")
                elif (value == "!=") and options == 1: actions.insert(" !=")
                elif options == 0: actions.insert(" "+value)  
                elif options == 1: actions.insert(value+" ")
                elif options == 2: actions.insert(value)

                actions.key("tab")
                actions.edit.delete_line()
                
                if options == 0: actions.insert(value)
                elif options == 1: actions.insert(value)
                elif (value == "!=") and options == 2: actions.insert(" "+value)
                elif (value == ",") and (options == 2): actions.insert(value+" ")
                elif options == 2: actions.insert(" "+value+" ")

                actions.key("ctrl-alt-enter")
                actions.sleep("500ms")
                actions.key("escape")
                actions.sleep("500ms")

                if (value == "+="): break
                if (value == "=="): break
    
    # ''' Duplicates a line '''
    def increase_lines() -> str:
        ''' Duplicates a line '''
        #select line
        actions.edit.line_start()
        actions.edit.extend_line_end()
        actions.edit.copy()
        actions.sleep("100ms")
        #save wording
        line = clip.text()
        #convert line
        output = line + "\n"
        for i in range(2):
            output += line + "\n"
        output += line 
        return output
    