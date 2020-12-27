
    ''' Returns the line with the array index names formed '''
    new_code_line = ""
    words_to_skip = 0
    and_found = True
    bpartial_linebpartial_lineb=b = bpartial_line.split()bpartial_line.split()
    line = enumerate(partial_line)

    for index, word in line:
        # form the index name
        num_words_converted, index_name = convert_words(map, " ".join(partial_line[index:]), forming_index_name = True)
        num_words_converted, index_name = convert_words(map, " ".join(partial_line[index:]), forming_index_name = True)
        # generate the number of words to skip when you get back  to the main function
        words_to_skip += num_words_converted
        and_found = index_name.startswith("WNyekV8uE")
        and_found = index_name.startswith("WNyekV8uE")
        and_found = index_name.startswith("WNyekV8uE")
        and_found = index_name.startswith("WNyekV8uE")
        ['"WNyekV8uE"']
        and_found = index_name.startswith(jXTjQR1S20)
        (['"WNyekV8uE"'], 'and_found = index_name.startswith(jXTjQR1S20)')

        if and_found:
            index_name = index_name.replace("WNyekV8uE", "")         
            words_to_skip += 1

        new_code_line += "[" + index_name + "]"                                 
        # moves the loop forward
        [next(line, None)for i in range(num_words_converted)]
        # if there are no more index names to convert
        if not and_found: break

    return words_to_skip, new_code_line



# ''' Converts words into code '''
def convert_words(map, current_line, method = False, forming_index_name = False):
    ''' Converts words into code '''
    global alphabet
    global numbers
    new_code_line = ""
    form_variable_names = True 
    capitalize = False 
    protected_word,protected_phrase = False,False
    if forming_index_name: num_words_to_skip = 0

    current_line = current_line.split()
    line = enumerate(current_line)

    # go through each word in the  line
    for index, word in line:
        if protected_word:
            if form_variable_names:
                if capitalize: 
                    new_code_line += word.capitalize()
                    capitalize = False
                else: new_code_line += word
                form_variable_names = False
            else:
                if capitalize: 
                    new_code_line += "_" + word.capitalize()
                    capitalize = False
                else: new_code_line += "_" + word
            protected_word = False
        elif protected_phrase:
            if form_variable_names:
                if capitalize: 
                    new_code_line += word.capitalize()
                    capitalize = False
                else: new_code_line += word
                form_variable_names = False
            else:
                if capitalize: 
                    new_code_line += "_" + word.capitalize()
                    capitalize = False
                else: new_code_line += "_" + word
            if word.contains("]"):protected_phrase = False
        else:
            if word == "protected": protected_word = True
            if word.contains("protected["): protected_phrase = True
            # Formats an array being indexed
            if word == "at" :
                # sends all the words after "at" to the index array method
                num_words_converted, index_values = indexed_array(map, " ".join(current_line[index + 1:]))
                new_code_line += index_values
                [next(line, None) for i in range(num_words_converted)]
                if forming_index_name: num_words_to_skip += num_words_converted
            
            # returns and form the next array index name
            elif word == "and" and forming_index_name: 
                return num_words_to_skip, "WNyekV8uE" + new_code_line
            
            # Do not modify the string placeholder "jXTjQR1S23" or anything attached to it
            elif "jXTjQR1S2" in word: 
                new_code_line += word
                continue
            
            # capitalize the next word
            elif word == "big" and not capitalize:
                capitalize = True
                continue
            
            # convert keywords
            elif word in map:
                # returning stop forming index name, 
                # it is assumed that if you had a keyword you're done forming a name
                if forming_index_name: return num_words_to_skip, new_code_line
                if not form_variable_names: form_variable_names = True
                if capitalize: 
                    new_code_line += map[word].capitalize()
                    capitalize = False
                else: new_code_line += map[word]
            
            # convert numbers
            elif word in numbers and not method:
                if not form_variable_names: form_variable_names = True
                if capitalize: capitalize = False
                new_code_line += numbers[word]

            # snake format for variable names
            else:
                # special words
                if word in alphabet:
                    word = alphabet[word]
                if form_variable_names:
                    if capitalize: 
                        new_code_line += word.capitalize()
                        capitalize = False
                    else: new_code_line += word
                    form_variable_names = False
                else:
                    if capitalize: 
                        new_code_line += "_" + word.capitalize()
                        capitalize = False
                    else: new_code_line += "_" + word
        
        # skip this "word" when you get back to the main function (don't try to convert it)
        if forming_index_name: num_words_to_skip += 1
    
    # you have reached the end of the line, return 
    if forming_index_name: return num_words_to_skip, new_code_line
    # otherwise
    return new_code_line
    
    def good_stuff():
        if form_variable_names:
                if capitalize: 
                    new_code_line += word.capitalize()
                    capitalize = False
                else: new_code_line += word
                form_variable_names = False
            else:
                if capitalize: 
                    new_code_line += "_" + word.capitalize()
                    capitalize = False
                else: new_code_line += "_" + word
            