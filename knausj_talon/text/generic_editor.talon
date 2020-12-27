find it:
	key(ctrl-f)

next one:
	edit.find_next()

word left: 
	edit.word_left()
	
word right: 
	edit.word_right()

go left: 
	edit.left()

go right: 
	edit.right()

go up: 
	edit.up()

go down: 
	edit.down()

line start: 
	edit.line_start()
	
(line end | slip): 
	edit.line_end()

(way left|front): 
	edit.line_start()
	edit.line_start()
	
(way right|back): 
	edit.line_end()

(way down|bottom): 
	edit.file_end()
	
(way up): 
	edit.file_start()

page down:
	edit.page_down()

page up:
	edit.page_up()

# selecting
select line: 
	edit.line_start()
	edit.extend_line_end()

select left: 
	edit.extend_left()
	
select right: 
	edit.extend_right()

select up: 
	edit.extend_line_up()
	edit.extend_line_start()
	
select down: 
	edit.extend_line_down()
	edit.extend_line_end()

select word left:
	edit.extend_word_left()
	
select word right: 
	edit.extend_word_right()

select (way left|front):
	edit.extend_line_start()
	
select (way right|back): 
	edit.extend_line_end()
	
select (way up|top): 
	edit.extend_file_start()
	
select (way down|bottom): 
	edit.extend_file_end()

# editing
indent [more]:
	edit.indent_more()

(indent less | out dent):
	edit.indent_less()

# deleting
clear line: 
	edit.delete_line()
    
clear left: 
	edit.extend_line_start()
	edit.delete()
	
clear right: 
	edit.extend_line_end()
	edit.delete()
	
clear up: 
	edit.extend_line_up()
	edit.delete()

clear down: 
	edit.extend_line_down()
	edit.delete()

clear word left: 
	edit.extend_word_left()
	edit.delete()
	
clear word right: 
	edit.extend_word_right()
	edit.delete()

(clear way left | clear front): 
	edit.extend_line_start()
	edit.delete()

(clear way right | clear back): 
	edit.extend_line_end()
	edit.delete()

clear (way up | top): 
	edit.extend_file_start()
	edit.delete()
	
clear (way down | bottom): 
	edit.extend_file_end()
	edit.delete()
	
