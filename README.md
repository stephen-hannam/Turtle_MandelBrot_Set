## Mandelbrot Set Jigsaw Puzzle Drawn by Turtle

This was part of a 1st year uni assignment. It will draw a 'blocky' Mandelbrot Set given some specified block size.

Other parameters that affect the MSet visualization control for fade of intensity as pixels get further from the skeletal center of the MSets features, and that control for the colorspace used to draw it.

HSL to RGB color conversions are performed. Some randomization done without using the random library, and the arrangement of jigsaw pieces is controlled by specifying sets of strings (names) in lists, these lists are named by the convention 'attempt_xx' where 'xx' is a number.

The borders between jigsaw pieces are randomized given a particular seed based on which arrangement of pieces is chosen.
