#-------------------- Helpers --------------------
slack: key(shift-enter)
#testing: insert(user.starter())
dip: key(backspace)
(shock|next): key(enter)
dub (shock|enter):key(enter enter)
equal weights: " equates "
print that: key(ctrl-p)
speak line:user.space_check()

full remove:
    edit.delete_line()
    edit.delete_line()
    key(delete)
cup: 
    insert("()")
    key(left)
speak$: 
    insert("\"\"")
    key(left)
(speak left|left speak)$: 
    key(space)
    insert("\"\"")
    key(left)
(speak right|right speak)$: 
    insert("\"\"")
    key(space)
    key(left left)
speak <phrase>:
    insert("\"\"")
    key(left)   
    insert("{phrase}")

subset:
    edit.line_end()
    key(enter)
    insert("-")
    key(space)

continue <phrase>$:
    " "
    insert(user.formatted_text(phrase, "ALL_LOWERCASE"))
    " "


#-------------------- Coding --------------------
back tab$:key(shift-tab)
pick$:
    "<>"
    key(left)
control$:"ctrl"
special command clean code$: user.clean_code()
duplicate$: insert(user.increase_lines())


tip$: " = "

plus equals$: " += "
new terminal$: key(ctrl-shift-`)

open panel$: key(ctrl-shift-P)
get hub$:"github"
get reset$: "git reset --hard HEAD~1"
undo reset part one$: "git reflog"
get reset part two$: "git reset --hard xxx"

#new-line$:"new_line"
fold$:key(ctrl-shift-[)
unfold$:key(ctrl-shift-])
fold all other$: 
    key(ctrl-shift-P)
    "fold all"
    key(down enter)
fold all$: 
    key(ctrl-shift-P)
    "fold all"
    key(enter)
unfold all$: 
    key(ctrl-shift-P)
    "unfold all"
    key(enter)

<phrase> tip$:
    insert(user.formatted_text(phrase, "PRIVATE_CAMEL_CASE"))
    insert(" = ")
box$: 
    insert("[]")
    key(left)
(our|are) box:"]"
L box:"["
key$:
    insert("key()")
    key(left)
key <word>:
    insert("key()")
    key(left)    
    "{word}"
key he tab:
    "key(tab)"
get commit:
    key(ctrl-shift-`)
    "git add ."
    key(enter)
    "git commit -m \"\""
    key(left)
get$: "git "
get push:
    key(enter)
    "git push"
    key(enter)
get status:
    "git status"
    key(enter)
#-------------------- Phrases --------------------
good morning$: 
    insert("Good morning ")
    sleep(500ms)
    key(tab)
    insert(",")
    key(enter enter)
good afternoon$: 
    "Good afternoon "
    sleep(500ms)
    key(tab)
    insert(",")
    key(enter enter)
hi format$: 
    "Hi "
    sleep(500ms)
    key(tab)
    insert(",")
    key(enter enter)
hey format$: 
    "Hey "
    sleep(500ms)
    key(tab)
    insert(",")
    key(enter enter)
hello format$: 
    "Hello "
    sleep(500ms)
    key(tab)
    insert(",")
    key(enter enter)
say ^: "carrot"
LOL$: "lol"
tandy$:"Thandiwe"
tandy short$:"Thandi"
full name$:"Thandiwe Brown"
my e-mail address$: "tabrown3@aggies.ncat.edu"
(junkman|junk mail)$: "junkmailgotyoface@gmail.com"
my (school|school name)$: "North Carolina Agricultural and Technical State University"
school abbreviation$: "NCAT"
okey-dokey$:"Okie dokie "
