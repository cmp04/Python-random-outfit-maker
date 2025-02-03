#main program script
import os
import random 
from PIL import Image
import cv2



def rand_top():
    path = 'Python-outfit-maker//Tops//'
    x = os.listdir(path)
    rand_item = random.choice(x)
    full_p_top = path + rand_item
    top = cv2.imread(full_p_top)
    return top
    

def rand_bottom():
    path = 'Python-outfit-maker//Bottoms//'  
    x = os.listdir(path)
    rand_item = random.choice(x)
    full_p_bottom = path + rand_item
    bottom = cv2.imread(full_p_bottom)
    return bottom
    
    

def rand_shoe():
    path = 'Python-outfit-maker//Shoe//'
    x = os.listdir(path)
    rand_item = random.choice(x)
    full_p_shoe = path + rand_item
    shoe = cv2.imread(full_p_shoe)
    return shoe
    


def main():
    ans = input("WELCOME! PRESS ANY LETTER KEY THEN HIT 'Return/Enter' TO GENERATE A RANDOM OUTFIT: ")


    cv2.imshow("Top", rand_top())

    cv2.imshow("Bottom", rand_bottom())

    cv2.imshow("Shoe", rand_shoe())

    cv2.moveWindow("Top", 1, 1) 
    cv2.moveWindow("Bottom", 500, 80) 
    cv2.moveWindow("Shoe", 950, 80) 

    cv2.waitKey(30000)

if __name__ == "__main__":
    main()
