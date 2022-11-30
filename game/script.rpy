
define e = Character("Eileen") 
default romance_points = 0

init python:
    def love(how_much=1):
        global romance_points

        romance_points = romance_points + how_much

    def hate(how_much=1):
        global romance_points

        romance_points = romance_points - how_much

# The game starts here.

label start:

    "Eileen is looking at you, with hope in her eyes"

menu:
    "What will you gift [e.name]"
    "A PS5":
        e "Ohhh, thank you."
        $ love(10)

    "An XBox Series S":
        e "I... see.... "
        $ hate(10)
    
label after_initial_gifts:

if romance_points > 0:
    "Eileen likes you some. (Romance points: [romance_points])"
else:
    "You failed pretty hard."

    return
