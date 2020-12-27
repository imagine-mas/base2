
from talon import Module, actions, clip
from typing import List


# if you say any of these words they will be converted into their corresponding letter
default_alphabet = "air bat catch drum each fine gust harp ice jury kite look made near odd plug quench red sun trap urge vest whale flex yank zip".split(" ")
letters_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = dict(zip(default_alphabet, letters_string))

# if you say the word version or number version of a number, it will be converted into a number/digit
default_digits = "zero one two three four five six seven eight nine".split(" ")
digits = [str(i) for i in range(10)]
numbers = dict(dict(zip(default_digits, digits)), **dict(zip(digits, digits)))


first_variable_name = None
capitalize = None
phrases = {
    "string over": "GIUSDG1673",
    "is a list": "kwKTUH6nS",
    "ends with":".endswith",
    "starts with":".startswith",
}

phrase_file = "C:\\Users\\Thandiwe Brown\\Documents\\talon_storage_docs\\phrase_dictionary.txt"
# retrieves And saves a keyword from a file
f = open(phrase_file, "r")
for line in f:
    phrase,value = line.split(",")
    phrases[phrase] = value.replace("\n","")
f.close()

symbols = {
    "=":" = ", 
    "+=":" += ", 
    "==":" == ", 
    "+":" + ", 
    "(":" ( ", 
    ")":" ) ", 
    "()":" () ", 
    "[":" [ ", 
    "]":" [ ", 
    "[]":" [] ", 
    "{":" { ", 
    "}":" } ", 
    "{}":" {} ", 
    ".":".", 
    ":":":", 
    ",":", ", 
}

words_to_symbols = {
    "takes":"(", 
    "calls":"(",        
    "parentheses":"(", 
    "parameters":"(", 
    "close":")", 

    "plus":" + ", 
    "is":" = ", 
    "equals":" = ", 
    "equates":" == ", 

    "dot":".", 
    "and":" , ", 
    "with":", ", 
    "then":", ",
}

keyword_map = {

    "for":"for ", 
    "in":" in ", 
    "if":"if ",
    "not":"not ",
    "return":"return ", 
    "import":"import ", 
    "def":"def ",

    "true":"True", 
    "false":"False", 
    "none":"None",
    "kwKTUH6nS":" = []", 

    "self":"self.",
    ".endswith":".endswith(",
    ".startswith":".startswith(",


}

keyword_map.update(symbols)
keyword_map.update(words_to_symbols)

mod = Module()
@mod.action_class
class Actions:
    
    # starts the conversion
    def start_conversion() -> str:
        ''' Returns converted line'''
        return line_distribution(copy_to_code())

    # replaces the wrong word with the right word
    def fix_it(wrong_word:str,right_word:str) -> str:
        ''' Placeholder '''
        return copy_to_code().replace(wrong_word,right_word)
    
    # in progress
    def save_phrase():
        ''' saves a phrase '''
        global phrases
        global phrase_file

        # finds out what phrase is supposed to mean what phrase
        line = copy_to_code().lower()
        phrase,value = line.split(" means ")
        phrases[phrase] = value
        

        f = open(phrase_file, "a")
        f.write(phrase+","+value+"\n")
        f.close()
        


#----------------------------------------Line Types----------------------------------------            
    
# sends the line text where it needs to go
def line_distribution(current_line):
    ''' Finds out which method to send the line to '''
    global keyword_map
    
    current_line = current_line.strip()
    lower_line = current_line.lower()

    # method header
    if lower_line.startswith("method") or lower_line.startswith("define") or lower_line.startswith("initial method") or lower_line.startswith("class method"):
        if lower_line.startswith("initial method"): current_line = lower_line.replace("initial method","method initial")
        if lower_line.startswith("class method"): current_line = lower_line.replace("class method","method class")
        return method_header(current_line.partition(" ")[2])
    # class
    elif lower_line.startswith("class"):
        return class_header(current_line.partition(" ")[2])
    # one line if statement
    elif "if" and "else" in lower_line:
        return one_line_if(current_line)
    elif "is a list of" in lower_line or "is a list:" in lower_line or "is a string list of" in lower_line or "is a string list:" in lower_line:
        return list_handling(current_line)
    # normal line
    else:
        return convert_line(keyword_map, current_line)
    
    return new_code_line

# properly formats the class name
def class_header(current_line):
    return "class "+actions.user.formatted_text(current_line, "PUBLIC_CAMEL_CASE")+"():"

# Properly formats the method name
def method_header(current_line):
    ''' Returns converted method header '''
    
    method_map = {
        "initial":"__init__", 
        "takes":"(", 
        "calls":"(", 
        "parentheses":"(", 
        "parameters":"(", 
        ":":":", 
        "type":":", 
        "and":", ", 
        "with":", ", 
        "then":", ", 
        "string":"str", 
        "bool":"bool", 
        "boolean":"bool", 
        "return":") -> ", 
        "returns":") -> ", 
        "dot":".", 
        ".":".", }
    
    new_code_line = "def "
    if "class" in current_line:
        new_code_line += convert_words(method_map, current_line.replace("class ",""), method = True)
    else:
        new_code_line += convert_words(method_map, current_line, method = True)
    if "initial" in current_line or "class" in current_line: 
        if "takes" not in current_line:
            new_code_line = new_code_line+"(self"
        else:
            new_code_line = new_code_line.replace("(","(self, ")
    new_code_line += ":" if '->' in new_code_line else "):"

    return new_code_line

# Formats a one line if statement
def one_line_if(current_line):
    ''' Returns converted one line if statement '''
    global keyword_map
    map = keyword_map.copy()
    map["if"] = " if "
    map["else"] = " else "
    return convert_line(map, current_line) 

# formats array/list calls
def indexed_array(map, partial_line,form_list = True):
    ''' Returns the line with the array index names formed '''
    new_code_line = ""
    words_to_skip = 0
    and_found = True
    partial_line = partial_line.split()
    line = enumerate(partial_line)

    for index, word in line:
        # form the index name
        num_words_converted, index_name = convert_words(map, " ".join(partial_line[index:]), forming_index_name = True)
        # generate the number of words to skip when you get back  to the main function
        words_to_skip += num_words_converted
        and_found = index_name.startswith("WNyekV8uE")

        if and_found:
            index_name = index_name.replace("WNyekV8uE", "")         
            words_to_skip += 1

        new_code_line += "[" + index_name + "]"                                 
        # moves the loop forward
        [next(line, None) for i in range(num_words_converted)]
        # if there are no more index names to convert
        if not and_found: break

    return words_to_skip, new_code_line

# Formats the creation of a list/a new list
def list_handling(current_line):
    ''' Placeholder '''
    is_a_string = False
    if "is a list of" in current_line: current_line = current_line.split("is a list of")
    elif "is a list:" in current_line: current_line = current_line.split("is a list:")
    elif "is a string list of" in current_line: 
        current_line = current_line.split("is a string list of")
        is_a_string = True
    elif "is a string list:" in current_line: 
        current_line = current_line.split("is a string list:")
        is_a_string = True

    new_code_line = "["
    the_list = current_line[1].split(",")

    for i in range(len(the_list)-1):
        if is_a_string: new_code_line  += "\""+the_list[i].strip()+"\", "
        else:new_code_line += convert_words(keyword_map,the_list[i].strip()) + ", "

    if is_a_string: return convert_words(keyword_map, current_line[0].lower()) + " = " + new_code_line + "\""+the_list[len(the_list)-1].strip()+"\"" + "]"
    return convert_words(keyword_map, current_line[0].lower()) + " = " + new_code_line + convert_words(keyword_map, the_list[len(the_list)-1].strip()) + "]"    

#----------------------------------------Helper Methods----------------------------------------

# grabs the text off the screen and saves it into  the program
def copy_to_code():
    ''' Saves text into code '''
    #select line
    actions.edit.line_start()
    actions.edit.extend_line_end()
    actions.edit.copy()
    actions.sleep("100ms")
    #save wording
    line = clip.text()
    #convert line
    return line

# ''' Replaces a string with a string identifier '''
def string_handling(line):
    ''' Replaces a string with a string identifier '''
    # Holds the string word values present in the line
    string_values = []
    # finds all the strings in the line 
    string_indices = find_string(line)
    if len(string_indices)%2!=0: return "the string quotes are not even"
    # Save the string value
    if len(string_indices) != 0: 
        for i in range(0,len(string_indices),2):
            string_values.append(line[string_indices[i]:string_indices[i+1] + 1])
    line = line.lower()
    # place the string identifier
    if len(string_indices) != 0: 
        for i in range(0,len(string_values)):
            line = line.replace(string_values[i].lower(), "jXTjQR1S2"+str(i), 1)
    return string_values, line

# finds all the strings in the line
def find_string(line):
    ''' Returns the starting and ending indices of a string in a line'''
    # used to identify " in a line
    quote = "\""
    # used to identify \" in a line
    backslash_and_quote = "\\\""

    quote_indices = []
    backslash_and_quote_indices = []

    # finds all indices of " and \" and saves them in their respective lists
    for i in range(len(line)):                                  
        if line.startswith(quote, i):
            quote_indices.append(i)
        if line.startswith(backslash_and_quote, i):
            backslash_and_quote_indices.append(i + 1)

    # removes all indices of \"    
    final_list = [x for x in quote_indices if x not in backslash_and_quote_indices]    
    
    return final_list

# ''' Replaces a phrase with an identifier '''
def phrase_handling(line):
    ''' Replaces a phrase with an identifier '''
    
    global phrases
    
    for key, value in phrases.items():
        line = line.replace(key,value)
    
    return line

# Does any last-minute final formatting for the line
def final_formatting(line, string_values):
    ''' Performs any final changes needed before returning the line '''
    #return string_values
    # Do string replacement if needed
    string_keyword = "jXTjQR1S2"
    i = 0
    while(string_keyword in line):
        line = line.replace(string_keyword+str(i), string_values[i], 1)
        i += 1
    # format appropriately or if and for statements
    
    if not line.endswith(":") and (line.startswith("if ") or line.startswith("for ")): line += ":"
    ''' 
    if line.startswith("if ") or line.startswith("for "): line += ":"
    bifbif blineblinebdoesn'tb_doesn'tbendb_endbwith:b, :
    if not_line_ends, ":":
    If not line ends with ":"
    if not line.endswith(":"):
    if not line.endswith":"):
    if not line_ends, ":":
    not line ends with ":"
    bifbif bnotbnot blineblinebendsb_endsbwithb, b:b:
    If not line
    '''
    return line

#----------------------------------------Conversion Base----------------------------------------

# ''' Formats and converts line into code '''
def convert_line(map, current_line):
    ''' Formats and converts line into code '''
    
    # holds the value of a string if it's in a line
    string_values = ""

    # handles strings
    if "\"" in current_line: string_values, new_code_line = string_handling(current_line)
    else: new_code_line = current_line.lower()
    
    # handles phrases
    new_code_line = phrase_handling(new_code_line)
    
    # converts words
    new_code_line = convert_words(map, new_code_line)   
    
    # final formatting
    new_code_line = final_formatting(new_code_line, string_values)

    # return line
    return new_code_line

# ''' Converts words into code '''
def convert_words(map, current_line, method = False, forming_index_name = False):
    ''' Converts words into code '''
    global alphabet,numbers
    global first_variable_name,capitalize
    new_code_line = ""
    first_variable_name = True 
    capitalize = False 
    protected_word = False
    protected_phrase = False
    keyword_attached = False
    method_capture = False
    keyword_list = []
    if forming_index_name: num_words_to_skip = 0

    current_line = current_line.split()
    line = enumerate(current_line)

    # go through each word in the  line
    for index, word in line:
        #new_code_line += "b"+word+"b"
        while word.endswith(",") or word.endswith(":") or word.endswith(")"):
            keyword_attached = True
            keyword_list.append(word[-1])
            word = word[:-1]
        if protected_word or protected_phrase:
            new_code_line = form_variable_name(word,new_code_line)
            if protected_word: protected_word = False
            elif "]" in word and protected_phrase:
                new_code_line = new_code_line[:-1]
                protected_phrase = False
        else:
            # protected words
            if word == "protected" : 
                protected_word = True
            elif word == "protected[" : 
                protected_phrase = True
            
            # Save string for later
            elif "jXTjQR1S2" in word: 
                new_code_line += word
                if method_capture: 
                    new_code_line += ")"
                    method_capture = False

            
            # capitalize the next word
            elif word == "big" and not capitalize: 
                capitalize = True
            
            # Next index array name
            elif word == "and" and forming_index_name: 
                return num_words_to_skip, "WNyekV8uE" + new_code_line
            
            # Index array name
            elif word == "at" :
                # sends all the words after "at" to the index array method
                num_words_converted, index_values = indexed_array(map, " ".join(current_line[index + 1:]))
                new_code_line += index_values
                [next(line, None) for i in range(num_words_converted)]
                if forming_index_name: num_words_to_skip += num_words_converted
            
            # convert keywords
            elif word in map:
                if forming_index_name: return num_words_to_skip, new_code_line
                if not first_variable_name: first_variable_name = True
                if word == ".endswith" or word == ".startswith": method_capture = True
                word = map[word]
                if capitalize: 
                    word = word.capitalize()
                    capitalize = False
                new_code_line += word
            
            # convert numbers
            elif word in numbers and not method:
                if not first_variable_name: first_variable_name = True
                if capitalize: capitalize = False
                new_code_line += numbers[word]

            # snake format for variable names
            else:
                if word in alphabet: word = alphabet[word]
                new_code_line = form_variable_name(word,new_code_line)
            
        # skip (don't try to reconvert) this word when you get back to the main function
        if forming_index_name: num_words_to_skip += 1
        if keyword_attached: 
            if not first_variable_name: first_variable_name = True
            for keyword in keyword_list[::-1]:
                new_code_line += keyword
            if new_code_line[-1] == ",": new_code_line += " "
            keyword_attached = False
            keyword_list = []

        
        
    # if you returning from forming an array index name
    if forming_index_name: return num_words_to_skip, new_code_line
    if "," in new_code_line:# and ", " not in new_code_line:
        new_code_line = new_code_line.replace(", ",",")
        new_code_line = new_code_line.replace(",",", ")

    # otherwise
    return new_code_line

def form_variable_name(word,new_code_line):
    global first_variable_name,capitalize
    # special words
    if capitalize: 
        word = word.capitalize()
        capitalize = False
    if first_variable_name:
        new_code_line += word
        first_variable_name = False
    else:
        new_code_line += "_" + word 

    return new_code_line