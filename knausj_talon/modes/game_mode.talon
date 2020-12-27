mode: user.game_mode
-
jump$:key(space)
sprint$:key(left-shift)
swim down$:key(left-ctrl)
(extract|get|interact)$:key(E)
drop$:key(Q)
rotate$:key(R)
tab$:key(tab)
escape$:key(escape)

dog <word>$:user.hold_key("{word}")
left$:user.hold_key("left")
right$:user.hold_key("right")
go$:user.hold_key("up")
back$:user.hold_key("down")
down some$:user.move_some("down","2000ms")
(stop|cat)$:user.stop_all()


(touch|click)$:
	mouse_click(0)
	# close the mouse grid if open
	user.grid_close()

righty$: 
	mouse_click(1)
	# close the mouse grid if open
	user.grid_close()



help active$: user.help_context_enabled()