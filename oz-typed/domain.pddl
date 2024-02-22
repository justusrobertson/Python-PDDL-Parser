;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; OZ World
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define 
	(domain OZ-EXAMPLE)
	(:requirements :typing :adl :universal-preconditions)
	(:types character location holdable - object
			thing wand - holdable)
	(:constants )
	(:predicates 
		(player ?character - character)
		(at-char ?character - character ?location - location)
		(at-thing ?thing - thing ?location - location)
	    (has ?character - character ?holdable - holdable)
		(connected ?to - location ?from - location)
		(enchanted ?thing - thing)
	)
		
	(:action take-character-thing-location
	    :parameters (?taker - character ?thing - thing ?location - location)
	    :precondition 
			(and 
				(at-thing ?thing ?location)
				(at-char ?taker ?location)
			)
	    :effect
			(and 
				(not (at-thing ?thing ?location))
				(has ?taker ?thing)
			)
	)
	
	(:action move-character-location-location
	    :parameters (?mover - character ?from - location ?to - location)
	    :precondition 
			(and 
				(at-char ?mover ?from)
				(connected ?to ?from)
			)
	    :effect
			(and 
				(not (at-char ?mover ?from))
				(at-char ?mover ?to)
			)
	)
	
	(:action give-character-thing-character-location
	    :parameters (?giver - character ?thing - thing ?receiver - character ?location - location)
	    :precondition 
			(and 
				(has ?giver ?thing)
				(not (= ?giver ?receiver))
				(at-char ?giver ?location)
				(at-char ?receiver ?location)
			)
	    :effect
			(and 
				(has ?receiver ?thing)
				(not (has ?giver ?thing))
			)
	)
	
	(:action disenchant-character-thing-wand-location
	    :parameters (?witch - character ?thing - thing ?wand - wand ?location - location)
	    :precondition 
			(and 
				(enchanted ?thing)
				(has ?witch ?wand)
				(at-char ?witch ?location)
				(at-thing ?thing ?location)
			)
	    :effect
			(not (enchanted ?thing))
	)
)
