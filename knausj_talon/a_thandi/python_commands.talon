
return$:"return "
comment$: 
    #key(enter)
    "# "
default multiline$: 
    insert("\'\'\'  \'\'\'")
    key(left left left left)
multiline$: 
    insert("\'\'\' Placeholder \'\'\'")
convert$: insert(user.start_conversion())
special <word> means <word>$: 
    insert(user.fix_it("{word_1}","{word_2}"))

new (vocab|vocabulary)$: insert(user.save_phrase())
    