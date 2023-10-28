import os
import cv2
import csv
from PIL import ImageFont, ImageDraw, Image  
import numpy as np

list_of_names = []
list_of_dept = []
list_of_yr = []


def delete_old_data():
   for i in os.listdir("generated certificates/"):
      os.remove("generated certificates/{}".format(i))


def cleanup_data():
   with open("name data.csv", "r", newline="\n") as fil:
      line=csv.reader(fil)
      for i in line:
         list_of_names.append(i[0].strip())


def generate_certificates():
   counter=0
   for i in list_of_names:
      image = cv2.imread("certificate template.jpg")
      cv2_im_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
      pil_im = Image.fromarray(cv2_im_rgb)  
      draw = ImageDraw.Draw(pil_im)  
      font = ImageFont.truetype("C:\Windows\Fonts\BellB.ttf", 80)  
      isp=470      #image_start_in_px (depends on template)
      iep=1535     #image_end_in_px (depends on template)
      y_axis=705
      if len(i) >= 15:
         mf=27+len(i)-2    #27 is obtained by trial and error method
      else:
         mf=27+ len(i)     #27 is obtained by trial and error method
      draw.text((int((isp+iep-(len(i)*mf))/2),y_axis), i.strip(), font=font, fill="#ffffff", align="right")  
      cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)  
      cv2.imwrite("generated certificates/{}.jpg".format(i.strip()), cv2_im_processed)  
      print("Processing {} / {}".format(counter + 1,len(list_of_names)))
      counter+=1
      
def main():
   delete_old_data()
   cleanup_data()
   generate_certificates()



if __name__ == '__main__':
   main()

