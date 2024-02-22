(define (problem 01)
	(:domain OZ-EXAMPLE)
	(:objects 
		dorothy glinda - character
		woods castle town - location
		magic-wand - wand
		ring axe slippers - thing
	)
	(:init    
		(player dorothy)
		(at-char dorothy woods)
		(at-char glinda castle)
		(at-thing axe woods)
		(at-thing ring castle)
		(at-thing slippers town)
		(has glinda magic-wand)
		(enchanted slippers)
		
		(connected castle town)
		(connected town castle)
		(connected castle woods)
		(connected woods castle)
		(connected town woods)
		(connected woods town)
	)
	(:goal 
		(and 
			(has dorothy slippers) 
			(has glinda ring)
		)
	)
)