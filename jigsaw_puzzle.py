
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n2731061
#    Student name: Stephen Hannam
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]

# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [['Piece A', 'Top left'], ['Piece B', 'Top right'],
            ['Piece C', 'Bottom right'], ['Piece D', 'Bottom left']] 

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

### wish to create tabs randomly, that's right! ###
# can't import random module >:( ...but still want something akin to randomness
# a combination of 2 seeds, a selector and an PRNG algirthm
# based on George Marsaglia's Multiple With Carry is used

selector = 1 # select the int from the rand_int_list
k_seed = 0 # to be based on strings in attempt_
l_seed = 0 # to be based on strings in attempt_

# since the tabs are being randomized, lists for constructing the borders
# are made as global
borders = []
# anything above 786 looks no different to 786, lower num_colors do look different
num_colors = 786
# 3 is a good block_size, it gives almost as much detail as 2, in 1/4 to 1/3 the time of 2
block_size = 24 # pixels
colormode(255)
tracer(False)
piece_border_color = "white"
piece_border_thickness = 2 # for best results this should be an even number or 1

def hsl_to_rgb(hue, sat, lum):
    # hue: pivot value for the color balance
    # sat: saturation - adjusts the color balance relative to the hue
    # lum: luminosity - change intensity of all color channels equally

    # HSL values between 0.0 and 1.0: returns [r, g, b] values from 0 to 255
    # adapted from an algorithm found at http://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/
    
    hue_int = int(hue * 6) # six slices of the color wheel, which slice is hue in?
    factor = hue * 6 - hue_int # scale color position to between 0 and 1
    ## if sat = 0, then shade of grey, all channels are just lum values
    ## if lum = 0, all channels 0
    ## if sat = 1, no grey, solid color, one channel needs to be 0 (temp_red), the others add to lum      
    temp_red = (1 - sat) * lum # appears in every channel combination, analogous to the zero vector
    temp_green = (1 - factor * sat) * lum
    temp_blue = (1 + factor * sat - sat) * lum
    ## there are 3! color channel combinations, assign channel intensities from above to
    ## one of these combinations depending on which slice of the color wheel the hue is in
    [red, green, blue] = [lum, temp_red, temp_green] # pivot on red channel
    [red, green, blue] = [temp_blue, temp_red, lum] if hue_int == 4 else [red, green, blue] # pivot on blue channel
    [red, green, blue] = [temp_red, temp_green, lum] if hue_int == 3 else [red, green, blue] # pivot on blue channel
    [red, green, blue] = [temp_red, lum, temp_blue] if hue_int == 2 else [red, green, blue] # pivot on green channel
    [red, green, blue] = [temp_green, lum, temp_red] if hue_int == 1 else [red, green, blue] # pivot on green channel
    [red, green, blue] = [lum, temp_blue, temp_red] if hue_int == 0 else [red, green, blue] # pivot on red channel   
    return [int(red * 255), int(green * 255), int(blue * 255)]

def getThumbprint_of_God(x, y, shift_right = 0.5, shift_up = 0, zoom = 250,
                         hue_adjust = 80, sharpness = 15, contrast = 10): # a Mandelbrot set block map
    ## all of this is my code. I know there is stuff out there written for Mandelbrot sets
    ## but this website: http://www.wikihow.com/Plot-the-Mandelbrot-Set-By-Hand for the general algorithm,
    ## is the only outside resource I used in the coding of this function

    # x, y: screen object coordinates at which to place a color
    # shift_right, shift_up: translation, but be mindful, these are not autoscaled to the zoom
    #                        the order of magnitude of values of shift_ must decrease as zoom increases
    # zoom: scale the actual x, y coords to values less than 2 from zero
    
    # hue_adjust: lower towards red/orange region, higher towards blue/violet region, green in the middle
    # sharpness: makes the logistic function that controls luminosity change more steeply
    # contrast: combined with sharpness determines the escape value at which a block has 50% luminosity

    # shrink the x, y position to bounds within which the Z will not immediately escape
    # to bounds (between about -2 and 2) where interesting things start to happen
    # the value of zoom is so chosen as to bring x, y to values somewhere between about -2 and 2
    # or, trickier, use shift_right and shift_up with zoom to zoom into interesting parts of the Mandeldbrot set
    [x_val, y_val] = [x/float(zoom) - shift_right,
                      y/float(zoom) + shift_up]
    Z = [0.0, 0.0] # initial complex value
    for it in range(num_colors): # it = iterator
        # iterate through Z, check if it 'escapes' else mark it SKIP (or black)
        Z = [Z[0]**2-Z[1]**2 + x_val, 2*Z[0]*Z[1] + y_val]
        if sqrt(Z[0]**2 + Z[1]**2) >= 2.0: 
            # create hue number from 'it', skew and smooth the values with arctan
            # lower hues are in arctans approximately linear region while higher
            # hue values are moved closer to each other, div by pi/2 keeps result between 0 and 1
            hue = atan(hue_adjust * (it/float(num_colors-1)))/(pi/2)
            # satuaration and luminosity are controlled by a logistic function of 'it'
            # the idea is that for a handful of low escape values lum should be very low
            # and then rise rapidly up to a plateau: y = 1/(1+Ae^(-kt)), inflection point: t = ln(A)/k                   
            contrast_factor = log(sharpness)/contrast # the 'it' value that takes 50% luminosity
            # contrast_factor is analogous to half the carrying capacity if a logistic function was
            # modelling a population, it is the result of setting the second derivative to 0 and solving
            lum = 1/(1+sharpness * exp(-contrast_factor * it))
            sat = 1.0
            return hsl_to_rgb(hue, sat, lum) # Z escapes, return rgb color
        elif it == num_colors - 1:
            return 0 # for no escape, set to 0 -> SKIP
            # for the purposes of this project, about half the image is black
            # so use the border fill functionality and avoid drawing the black parts of the image
                    
def numDigits(integer):
    # determine order of magnitude of an integer
    integer = int(integer)
    return len(str(integer))

def myRandInt(low, high, step):
    # low, high, step: between low to high in multiples of step
    
    # based on George Marsaglia's Multiple With Carry Algorithm
    # adapted from code written by John D. Cook, codeproject.com, 26 Jun 2014
    # seeding provided from k_seed and l_seed created from attempt_## strings
    # and use of a scattered selector iterator
    step = int(step) # robustify the code
    low = int(low) 
    high = int(high) 
    
    seed1 = k_seed
    seed2 = l_seed
    rand_int_list = []
    for _ in range(30):        
        seed1 = seed1 % seed2 # helps internally randomize shorter lists - not part of Cook's code
        ## Cook's code ##
        seed1 = 36969 * (seed1 & 65535) + (seed1 >> 16) # bit-shift, bitwise 'and'
        seed2 = 18000 * (seed2 & 65535) + (seed2 >> 16)
        seed1 = (seed1 << 16) + seed2
        ## /Cook's code ##
        OM = 10**numDigits(seed1) # order of magnitude, seed1 is typically a VERY big number
        # use OM to convert seed1 into something between 0 and 1
        # convert this number from 0 to 1, into a multiple of 'step' between 'low' and 'high'
        rand_int = int( step * (round(float((high - low) * seed1/(OM))/step))) + low
        rand_int_list.append(rand_int)
    # idx must not send rand_int_list out of range
    # use modulo, index 0 to n-1 rule, and selector, selector may be or become a very large number
    idx = (len(rand_int_list) - 1 + selector) % (len(rand_int_list) - 1) # <-- selector
    return rand_int_list[idx]


def makeDivisibleBy(target, divisor, further_from_zero = True):
    # increment or decrement target until it is DIVISIBLE by divisor
    if abs(divisor) > abs(target):
        print "divisor |", divisor, "| > target: |", target, "|"
        raise NameError("|TARGET| must be greater than |DIVISOR|")
        
    if further_from_zero:
        while target % divisor != 0:
            target = (abs(target) + 1) * target/abs(target) # increment, remove and return the sign +/-
        return target
    else:
        while target % divisor != 0:
            target = (abs(target) - 1) * target/abs(target) # decrement, remove and return the sign +/-
        return target
    
def makeFactorOf(target, higher_multiple, further_from_zero = True):
    # increment or decrement target until it is a FACTOR of higher_multiple
    if abs(target) > abs(higher_multiple):
        print "tagret |", target, "| > higher_multiple: |", higher_multiple, "|"
        raise NameError("|HIGHER_MULTIPLE| must be greater than |TARGET|") 
        
    if further_from_zero:
        while higher_multiple % target != 0:
            target = (abs(target) + 1)*target/abs(target) # increment, remove and return the sign +/-
        return target
    else:
        while higher_multiple % target != 0:
            target = (abs(target) - 1)*target/abs(target) # decrement, remove and return the sign +/-
        return target
    
def setPieceBorders():
    # randomly define the tabs
    ## side, conj_side proforma
    # side : come in constant, left or right, out/in some depth, opposite turn, along some width, left or right, out/in some depth, opposite turn, along some width, same
    #        turn, back the needed depth to reach the depth at the beginning, opposite turn, go along until all width-wise travel adds to size_of_pieces ( = 300)
    # side : leg1 -> +/- 1 -> deep1 10-50 -> -/+ 1 -> wide1 10-50 -> +/- 2 -> step1 = deep2 10-50 + (deep1/2 (+/- 2)*(-/+ 1) deep1/2) -> -/+ 2 -> wide2 10-50 -> -/+ 2 ->
    #        step2 = deep2 10-50 + (deep1/2 (+/- 2)*(+/- 1) deep1/2)  -> +/- 2 -> leg2 = 300-(leg1 + wide1 + wide2) -> + fixed (right turn always)
    # conj_side: reverse order of elements from side, and reverse left/right choices
    # conj_side: leg2 -> -/+ 2 -> step2 -> +/- 2 -> wide2 -> +/- 2 -> step1 -> -/+ 2 -> wide1 -> +/-1 -> deep1 -> -/+ 1 -> leg1
    
    global borders
    global selector # for use in myRandInt
    borders = [] # reset borders to nothing, regen new puzzle borders
    conj_sides = []
    sides = []
    lower = block_size # lowest random value of tab side dimension
    upper = makeDivisibleBy(max_tab_size/2, block_size, False) # highest random value of tab side dimension
    # gen edges for four pieces
    # all lengths used randomly or plann-edly must be divisible by block_size
    # all differences between lengths used must be divisible by block_size
    for _ in range(4):       
        pm = [] # plus-minus - left/right
        deep = []
        wide = []
        for _ in range(2): # random turn left or right
            selector = selector + 1             
            pm.append(myRandInt(-1, 1, 2)) # -1 or 1
            
        npm = [-pm[0], -pm[1]]
        
        for _ in range(2): # random length into or out of tab
            selector = selector + 1 
            deep.append(myRandInt(lower, upper, block_size))
            
        for _ in range(2): # random width of tab parallel to border
            selector = selector + 1 
            wide.append(myRandInt(lower, upper, block_size)) 

        in_leg = makeDivisibleBy(size_of_pieces/3, block_size, False) # length before tab
        out_leg = size_of_pieces - (in_leg + wide[0] + wide[1]) # length after tab
        leg = [in_leg, out_leg]
        
        step = [deep[1] + int(0.5 * (deep[0] + npm[0] * pm[1] * deep[0])),
                deep[1] + int(0.5 * (deep[0] + pm[0] * pm[1] * deep[0]))]
        # since step is a linear combination of deeps[] it's possible for it to be indivisible by block_size
        step = [makeDivisibleBy(step[0], block_size, False), makeDivisibleBy(step[1], block_size, False)]
        
        side = [[leg[0], pm[0] * 90], [deep[0], npm[0] * 90], [wide[0], pm[1] * 90], [step[0], npm[1] * 90],
                [wide[1], npm[1] * 90], [step[1], pm[1] * 90], [leg[1], 90]]

        conj_side = [[leg[1], npm[1] * 90], [step[1], pm[1] * 90], [wide[1], pm[1] * 90],
                     [step[0], npm[1] * 90], [wide[0], pm[0] * 90], [deep[0], npm[0] * 90], [leg[0], 90]]
     
        # assemble side instructions for pieces: A,B,C,D -> 0,1,2,3 first list indices of borders list of lists of lists
        sides.append(side) # assemble the non-conjugate sides for all 4 pieces
        conj_sides.append(conj_side) # assemble the conjugate sides for all 4 pieces       
    for it in range(4):  
        borders.append([[size_of_pieces, 90]] + sides[it] + conj_sides[it - 1] + [[size_of_pieces, 90]])

def draw_block(col, x_p, y_p, def_center_x, def_center_y, center_x = None, center_y = None, length = 1, width = 1):
    # col: color to fill block
    # x_p, y_p: coords relative to piece center where block is to be drawn, from top left corner
    # def_center_x-y: non-origin piece default center relative to which all predraw mapping is done
    # center_x-y: actual center of the piece where it is finally drawn
    # length: length of 1st and 3rd line drawn, width for 2nd and 4th
    #         not used for Mandelbrot set draw, but available for other draws    
    penup() # no outline, just fill
    
    offset_x = center_x - def_center_x 
    offset_y = center_y - def_center_y     
    x = x_p + offset_x # shift from def_center to actual center
    y = y_p + offset_y 
   
    goto(x, y)  
    setheading(0)   
    ## draw the block
    width = float(width)/2 # halve for use in odd/even width/length selection
    length = float(length)/2
    fillcolor(col)
    begin_fill()
    
    for it in range(4):
        # even n -> draw length, odd n -> draw width, length and width are multiples of block_size
        forward( block_size*(width + length + ((-1)**(it+1)) * width + ((-1)**it) * length) )
        right(90)
    end_fill()  
                
def draw_border(which_piece, piece_center_x = None, piece_center_y = None, fill_col = None,
                shown = False, returnInterior = False):
    # which_piece: Piece A, B, C or D
    # center_x-y: actual center of piece
    # fill_col: color to fill inside borders if so desired
    # shown: boolean, actually draw the borders or simply map them out and return the interior
    # returnInterior: return a list of points for subsequent draws 
    
    # top left corner going east is considered the "zero" starting vector
    # pieces dict: [turn used at start of draw, index for piece in list of borders]
    pieces = {"Piece A" : [0.0, 0], "Piece B" : [-90.0, 1], "Piece C" : [-180.0, 2], "Piece D" : [-270.0, 3]} 
    # piece borders are drawn by starting at a corner and moving forward and right turns by 90deg, left by -90deg
    # set the top left piece borders as the template and create all other piece borders by turning the top left
    # starting point by multiples of 90 degrees
    turn = pieces[which_piece][0]
    x_O = -float(size_of_pieces) # top left corner of whole image
    y_O = float(size_of_pieces)
    # turn starting vector to location needed for given piece A,B,C or D
    x_start = x_O*cos(radians(turn)) - y_O*sin(radians(turn))
    y_start = x_O*sin(radians(turn)) + y_O*cos(radians(turn))
    # x-y_start/2 -> pieces default center
    def_center_x = x_start/2
    def_center_y = y_start/2
    # and account for x, y offsets from default center
    if piece_center_x != None and piece_center_y != None:
        offset = [piece_center_x - def_center_x, piece_center_y - def_center_y]
    else:
        offset = [0, 0]
        
    x_start = x_start + offset[0]
    y_start = y_start + offset[1]
        
    ## draw the piece borders virtually    
    penup()
    goto(x_start, y_start)
    # face starting vector in the correct direction  
    setheading(turn)
    directions = borders[pieces[which_piece][1]] # access draw directions from list of borders
    if shown:
        skirting_board = [] # to record points for drawing a border, needed for border thickness > 1
    if returnInterior:
        # Interior records all coords visited for later use in drawing the piece
        Interior = [[int(round(def_center_x)), int(round(def_center_y))]] # first element is the default piece center    
    if fill_col != None:
        fillcolor(fill_col)
        begin_fill()
    for idx, direction in enumerate(directions):
        # record coords visited after removing the offset, return to virtual default piece space
        # all draw decisions are made from the virtual default draw space, and offsets applied afterwards
        [x, y] = [xcor() - offset[0], ycor() - offset[1]]
        # build a list of inner corners to draw a border along
        if shown:
            skirting_board.append([int(round(x)), int(round(y)), int(round(heading()))])
        if returnInterior:          
            Interior.append([int(round(x)), int(round(y))])       
        # virtual draw
        forward(direction[0])
        right(direction[1]) # the very last turtle turn does not change the resulting border map
    
    if shown:
        if piece_border_thickness > 1:
            # if thickness == 1, no need for corner insetting: find and store insetting points below
            for idx, cnr in enumerate(skirting_board):
                last_heading = int(skirting_board[idx - 1][2])
                this_heading = int(cnr[2])
                # inset_factor: translate cnr x, y by 0.5 * border thickness left/right and up/down
                # this works based on unique heading combinations possible for drawing corners in steps and tabs
                inset_factor = [0.5, 0.5]
                inset_factor = [-0.5, -0.5] if abs(last_heading - this_heading) == 270 else inset_factor
                inset_factor = [0.5, -0.5] if last_heading + this_heading == 90 else inset_factor
                inset_factor = [-0.5, 0.5] if last_heading + this_heading == 450 else inset_factor

                skirting_board[idx][0] = skirting_board[idx][0] + piece_border_thickness * inset_factor[0]
                skirting_board[idx][1] = skirting_board[idx][1] + piece_border_thickness * inset_factor[1]
                
        skirting_board.append(skirting_board[0]) # make sure turtle draws back to where it started
        ## draw the borders
        penup()
        start = [skirting_board[0][0] + offset[0],
                 skirting_board[0][1] + offset[1]] # restore the offset
        goto(start[0], start[1])
        setheading(turn)
        pensize(piece_border_thickness)
        pencolor(piece_border_color)
        pendown()
        tracer(True)
        for skirt in skirting_board[1:]:
            goto(skirt[0] + offset[0], skirt[1] + offset[1])
        penup()
        tracer(False)
    if fill_col != None:
        end_fill()
    if returnInterior:
        # return list for finding correct elements in complete map of blocks to draw inside the borders
        return Interior
    
def myRandPenDown():
    global selector
    # randomize the draw color before putting the pendown
    selector = selector + 7
    hue = myRandInt(0, num_colors, num_colors/10)/float(num_colors)
    hue = atan(hue)/(pi/2)
    sat = 1.0
    lum = 1.0
    pencolor(hsl_to_rgb(hue, sat, lum))
    ### 
    pendown()
    
def draw_broken(where):
    speed("fastest")
    tracer(True)
    radius = max_tab_size/2
    pensize(3)
    penup()
    goto(where[0], where[1] - radius) # move to draw start position
    setheading(0)
    myRandPenDown()
    circle(radius) 
    for it in range(2): # draw the two crossed eyes
        penup()
        goto(where[0], where[1]) # return to center
        setheading(45 + 90 * it) # it = 0 draw right eye, it = 1 draw left eye
        forward(makeDivisibleBy(radius, 3, False)/3) # move to draw start position
        myRandPenDown()
        for cousin_it in range(2):
            right(90 * cousin_it) 
            forward( ((-1) ** (cousin_it)) * (makeDivisibleBy(radius, 3 + 3 * cousin_it, False)/(3 + 3 * cousin_it)) )
            forward( ((-1) ** (cousin_it + 1)) * (makeDivisibleBy(radius, 6 - 3 * cousin_it, False)/(6 - 3 * cousin_it)) )
    penup()
    # get in position for next draw: the mouth
    goto(where[0], where[1])
    setheading(225)
    forward(3*radius/4)
    right(180)
    for it in range(6): # draw zig-zag mouth
        myRandPenDown()
        forward(radius/4)
        right(((-1) ** (it)) * 90)
        penup()
    hideturtle()
    tracer(False)
    
def draw_piece(which_piece, where, fill_col = None, broken = False):
    # see draw_border argument summary
    # x-y_offset: additional control over where to place the piece
    # where: key in locations dictionary below, where to place piece center    
    # dictionary of IFB104-assignment1-specific piece locations    
    locations = {"Bottom left" : template_centres[0],
                 "Bottom right": template_centres[1],
                 "Top left": template_centres[2],
                 "Top right": template_centres[3],
                 "In box": box_centre}
    piece_center = [locations[where][0], locations[where][1]]
    if broken:
        draw_broken(piece_center)
        return
    ## draw piece border, obtain boundaries returned by draw_border: Interior
    # draw_border(which_piece, center_x = None, center_y = None, fill_col = None,
    #             shown = False, returnInterior = False)
    bounds = draw_border(which_piece, piece_center[0], piece_center[1], fill_col, False, True)
    # first element of bounds is the default piece center - as returned from draw_border
    def_piece_center = [bounds[0][0], bounds[0][1]]
    limits = bounds[1:] # exclude def_piece_center, assign by value, not by reference
    
    ### scan and fill across, cross a limit line then flip on/off for draw
    ## create the set of vertical line limits, if scan hits limit, set draw on or off
    # B and D are 1 element out-of-sync for the interior points, thus put them in sync 
    if which_piece == "Piece B" or which_piece == "Piece D": # make horizontal lines vertical, put in sync
        limits.append(limits[0]) 
        del limits[0] # swap first and last element
    
    lines = []
    for it in range(-1, len(limits) - 1, 2): 
        lines.append([limits[it], limits[it + 1]]) # [[[x1, y1], [x2, y2]], ...]
        
    x_lims = [x_vals[0][0] for x_vals in lines] # these trigger 'crossed a line' during scan

    start = [def_piece_center[0] - (size_of_pieces + 2 * max_tab_size)/2,
             def_piece_center[1] + (size_of_pieces + 2 * max_tab_size)/2] # start position
    
    # enable "any" block_size to be used, obviously really big ones (>max_tab_size/2) shouldn't be used
    # make start location divisible by block_size, slightly increase the start position values
    start = [makeDivisibleBy(start[0], block_size), makeDivisibleBy(start[1], block_size)]
    
    # alter the range of plot-space slightly to make it divisible by the block_size
    scan_length = makeDivisibleBy(size_of_pieces + 2 * max_tab_size, block_size)
    scan_range = scan_length/block_size
    
    draw = False
    for vert in range(scan_range):              
        y = start[1] - vert * block_size              
        for horz in range(scan_range):          
            crossed_a_line = False # by default at every new point
            x = start[0] + horz * block_size
            # check to see if a line has been crossed
            if x in x_lims:
                for line in lines:
                    if x in line[0] and x in line[1]:
                        y_s = [line[0][1], line[1][1]]
                        y_s.sort()
                        if y > y_s[0] and y <= y_s[1]:
                            # check that the current location is in between two points vertically
                            crossed_a_line = True
            
            if crossed_a_line:
                draw = not draw

            if draw:
                color = getThumbprint_of_God(x, y)
                # draw_block(col, x_O, y_O, def_center_x, def_center_y,
                #            center_x = None, center_y = None, length = 1, width = 1)
                if color != 0: # SKIP black blocks, since borders filled black at beginning
                    draw_block(color, x, y, def_piece_center[0], def_piece_center[1], piece_center[0], piece_center[1])

    # drawing the inside image would have covered the borders if they'd been drawn first
    # set shown = True now in draw_border argument, returnInterior = False
    # draw_border(which_piece, center_x = None, center_y = None, fill_col = None,
    #             shown = False, returnInterior = False)
    draw_border(which_piece, piece_center[0], piece_center[1], None, True, False)    
        
def adjustBlockSize():
    # adjust block_size to fit evenly inside preset puzzle piece dimensions
    # keep in own separate function since "globalizing" block_size in other functions where it
    # is used heavily could potentially lead to problems, especially in subsequent code revisions
    global block_size
    block_size = makeFactorOf(block_size, size_of_pieces)
    if block_size > max_tab_size/2: # block_size too big breaks the limits within which borders are generated
        block_size = max_tab_size/2

def draw_attempt(attempt):
    ### for the pseudo-random int generator ###
    global k_seed
    global l_seed
    words = [items for item in attempt for items in item] # flatten the attempt list of lists of strings
    # convert each string to an integer
    nums = [sum([ord(character) for character in words[0]]), sum([ord(character) for character in words[1]]),
            sum([ord(character) for character in words[-1]]), sum([ord(character) for character in words[-2]])]
    k_seed = nums[0] + nums[1] 
    l_seed = abs(nums[2] - nums[3])        
    ### for the pseudo-random int generator ###
    # ensure that border thickness is an even number so that there is no overlap of pieces
    global piece_border_thickness
    if piece_border_thickness > 1: # if 1 then makeDivisibleBy will raise an error        
        piece_border_thickness = makeDivisibleBy(piece_border_thickness, 2, False)
    adjustBlockSize() # basic dimensions of pieces must be divisible by block_size
    # since it is stipulated not to change the basic dimensions, the blocks must be factors of the preset dimensions
    setPieceBorders()
    
    for piece in attempt:
        # draw_piece(which_piece, where, fill_col = None, broken = False)
        # set fill to BLACK, since a great deal of the Mandelbrot set is black; save time
        if len(piece) == 3: # check if a third string exists
            if piece[2] == 'X':
                draw_piece(piece[0], piece[1], "black", True) # broken
        else:
            draw_piece(piece[0], piece[1], "black") # not broken
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Thumbprint of God')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_attempt(solution)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

