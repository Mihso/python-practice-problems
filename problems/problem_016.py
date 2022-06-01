# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    if x <= 10 or x >= 0 or y <= 10 or y= > 0:
        return True
    else:
        return False
