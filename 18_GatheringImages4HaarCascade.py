## Changed the code to use python2
## Use code in the above link for python3
## https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/

import urllib
import cv2
import numpy as np 
import os

def store_raw_images():
    #http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513
    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513' 
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode('utf8')

    if not os.path.exists('neg'):
        os.makedirs('neg')

    pic_num = 1418

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i,"neg/"+str(pic_num)+'.jpg')
            img = cv2.imread("neg/"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+'.jpg',resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()

