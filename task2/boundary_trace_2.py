import cv2
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

#--------------------------create image-------------------
#set back ground
black_background = np.zeros((600,600,3),dtype =  "uint8")
blue_background= cv2.rectangle(black_background, (0, 0), (600, 600),(0, 183, 235), -1) 
#set shape
p1 = (220, 220)
p2 = (220, 380)
p3 = (380, 300)
cv2.line(blue_background, p1, p2, (255, 255, 255), 100)
cv2.line(blue_background, p2, p3, (255, 255, 255), 100)
cv2.line(blue_background, p1, p3, (255, 255, 255), 100)

cv2.rectangle(blue_background, (450, 50), (550, 500),(0,150, 150), -1) #blue
cv2.rectangle(blue_background, (150, 50), (420, 150),(255,150, 255), -1) #red

cv2.imwrite('trace_4.png', blue_background)


# ---------------------------boundry tracing---------------------------
def boundary_tracing(image,R_COMPONENT,G_COMPONENT,B_COMPONENT,edge_color):

    row_size = image.shape[0]
    col_size = image.shape[1]
    points =[0,0]   ## array to put x,y boundary founded
    dir =7  ## as use 8neighbours
    stop_condition =1  ##use as condition to detect all boundary
    enditerate =0  ## use to stop search about first white pixel
    edge_row=0
    edge_col=0
    new_edge_row=0
    new_edge_col=0
    #function to change color
    def change_color(row ,col):
        if(edge_color == "RED"):
            image_detected[row][col][0] = 0
            image_detected[row][col][1] = 0
            image_detected[row][col][2] = 0
        elif(edge_color == "YELLOW"):
            image_detected[row][col][0] = 235
            image_detected[row][col][1] = 183
            image_detected[row][col][2] = 0
        elif(edge_color == "BLUE"):
            image_detected[row][col][0] = 0
            image_detected[row][col][1] = 0
            image_detected[row][col][2] = 255

    #function to set direction after found any white pixel
    def update_dir(dir):
        if(dir % 2 == 0): ##direction is even
            dir = (dir+7) % 8
        else :## direction is odd
            dir =(dir+6)%8
        return dir
    #search about first white pixel in image
    for i in range(0, row_size ):
        for j in range(0, col_size ):
            if ( (image[i][j][0]==R_COMPONENT) and (image[i][j][1]==G_COMPONENT) and (image[i][j][2]==B_COMPONENT)):
                dir = update_dir(dir)
                change_color(i,j)
                points[0]=i
                points[1]=j
                edge_row=i
                edge_col=j
                enditerate =1

                if(enditerate ):
                    break
    ##loop to detect all boundary for shape
    while( stop_condition ):

        #depend on direction set row and col number to check if it related to boundary
        if (dir == 0):
            new_edge_row = edge_row
            new_edge_col = edge_col+ 1
        elif (dir == 1):
            new_edge_row = edge_row-1
            new_edge_col =edge_col+ 1
        elif (dir == 2):
            new_edge_row =edge_row- 1
            new_edge_col = edge_col
        elif (dir == 3):
            new_edge_row = edge_row-1
            new_edge_col = edge_col-1
        elif (dir == 4):
            new_edge_row = edge_row
            new_edge_col = edge_col-1
        elif (dir == 5):
            new_edge_row = edge_row+1
            new_edge_col = edge_col- 1
        elif (dir == 6):
            new_edge_row = edge_row+1
            new_edge_col = edge_col
        elif (dir == 7):
            new_edge_row = edge_row+1
            new_edge_col = edge_col+1

        if ((image[new_edge_row][new_edge_col][0]==R_COMPONENT) and (image[new_edge_row][new_edge_col][1]==G_COMPONENT) and image[new_edge_row][new_edge_col][2]==B_COMPONENT):
            dir = update_dir(dir)
            change_color(new_edge_row, new_edge_col)
            points.append(new_edge_row)
            points.append(new_edge_col)
            edge_row = new_edge_row
            edge_col = new_edge_col
            if ((points[0] == points[-2]) and (points[1] == points[-1])):
                stop_condition = 0

        else:
            dir += 1
            dir %= 8


image = cv2.imread("trace_4.png")
image_detected = np.copy(image)
boundary_tracing(image ,255,255,255, "RED") #for white region
boundary_tracing(image ,0,150,150 ,"YELLOW") #for green region
boundary_tracing(image ,255,150, 255, "BLUE")
fig, axs = plt.subplots(1,2)
axs[0].imshow(image)#axs[0,0] yields an error
axs[0].set_title("original image")
axs[1].imshow(image_detected)
axs[1].set_title("detected regions")
plt.show()