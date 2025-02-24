#program starts here 
import numpy as np 
import argparse 
import cv2 
import imutils 

# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-p", "--puzzle", required = True, 
help = "Path to the puzzle image") 
ap.add_argument("-s", "--search", required = True, 
help = "Path to the search image") 
args = vars(ap.parse_args()) 

# load the puzzle and search images 
puzzle = cv2.imread(args["puzzle"]) 
search = cv2.imread(args["search"]) 
(searchHeight, searchWidth) = search.shape[:2] 

# find the waldo in the puzzle 
result = cv2.matchTemplate(puzzle, search, cv2.TM_CCOEFF) 
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result) 

# grab the bounding box of search and extract him from 
# the puzzle image 
topLeft = maxLoc 
botRight = (topLeft[0] + searchWidth, topLeft[1] + searchHeight) 
roi = puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] 

# construct a darkened transparent 'layer' to darken everything 
# in the puzzle except for search 
mask = np.zeros(puzzle.shape, dtype = "uint8") 
puzzle = cv2.addWeighted(puzzle, 0.25, mask, 0.75, 0) 

# put the original search back in the image so that he is 
# 'brighter' than the rest of the image 
puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi 

# display the images 
cv2.imshow("Puzzle", imutils.resize(puzzle, height = 650)) 
cv2.imshow("Search", search) 
cv2.waitKey(0)
