"""A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:

    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater than 0 and less than 1
    Float parameter "window" must be less than half.

If all three conditions above are fulfilled, return a positive integer, otherwise return -1."""


def bouncing_ball(h, bounce, window):
    count = -1
    while h > window:
        if h > 0 and 1 > bounce > 0 and window < h:
            h *= bounce
            count += 2
    return count


print(str(bouncing_ball(h=59, bounce=0.52, window=1.5)) + ' раз мяч пролетит мимо мамы')
print(str(bouncing_ball(h=21, bounce=0.7, window=1.5)) + ' раз мяч пролетит мимо мамы')
print(str(bouncing_ball(h=39, bounce=0.66, window=1.5)) + ' раз мяч пролетит мимо мамы')
print(str(bouncing_ball(h=35, bounce=0.62, window=1.5)) + ' раз мяч пролетит мимо мамы')
print(str(bouncing_ball(h=30, bounce=0.79, window=1.5)) + ' раз мяч пролетит мимо мамы')

