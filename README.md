# raspi_line_following
this is just recognizing where the black line is on the screen(left or right) determined by the coordinate x1
Description of Logic behind the code
-finds mask is used to find the pixle with balue 0 - 60 using cv2.inRange
-find the contour(largest enclosed area of pixle)
-find the largest contour
-draw rectangle around the contour[ you could just use moments to find the midpoint but i couldn't figure out how to do it]
-find the center of the rectangle 
now you have the cooridinates for the line midpoint, just use that value to map it to the speed of your motor on your car or something
