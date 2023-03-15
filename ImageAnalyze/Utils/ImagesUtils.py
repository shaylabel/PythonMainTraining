import os
import shutil
import time

from matplotlib import image
from selenium import webdriver
from PIL import Image, ImageChops


class ImagesUtils():

    def __init__(self,driver):
        path_captured_image = "..//Images//image2.png"
        path_cropped_image = "..//Images//imageCrop.png"
        path_result_image = "..//Images//imageCrop.png"

        self.path_capture_image=path_captured_image
        self.path_cropped_image=path_cropped_image
        self.path_result_image=path_result_image
        self.driver = driver


    def get_screen_capture(self,path):
        print ('get screen capture at ',path)
        self.driver.save_screenshot(path)


        # rectangle parameters :left, upper, right, lower

    def crop_image(self,rectangle,path_save,path_under_test):
        im = Image.open(path_under_test)
        cropped = im.crop(rectangle)
        cropped.save(path_save)

    #     basic method to compare between 2 images

    def compare_images(self ,path_file_under_test,path_ref,path_res):
        res_image = Image.open(path_file_under_test)

        under_test_binary = Image.open(path_file_under_test).convert('1')  # binary image for pixel evaluation
        p1 = under_test_binary.load()

        ref_binary = Image.open(path_ref).convert('1')  # binary image for pixel evaluation
        p2 = ref_binary.load()

        width = under_test_binary.size[0]
        height = under_test_binary.size[1]
        for x in range(0, width):
            for y in range(0, height):

                if (p1[x, y] != p2[x,y]):
                    print('mismatch found x=', x, ',y=', y)
                    res_image.putpixel((x,y), (185, 185, 185))

        res_image.show()
        res_image.save(path_res)

    def compare_image_rectangle (self, path_file_ref, box, name):

        properties = self.prapare(name,path_file_ref)
        res_image = Image.open(properties.get('path_res'))

        self.get_screen_capture(properties.get('path_screenshot'))
        shutil.copyfile(properties.get('path_screenshot'),properties.get('path_res'))
        self.crop_image(box, properties.get('path_crop'), properties.get('path_screenshot'))

        under_test_binary = Image.open(properties.get('path_screenshot')).convert('1')  # binary image for pixel evaluation
        p1 = under_test_binary.load()

        ref_binary = Image.open(properties.get('path_res')).convert('1')  # binary image for pixel evaluation
        p2 = ref_binary.load()

        width = ref_binary.size[0]
        height = ref_binary.size[1]
        for x in range(box[0], box[2]):
            for y in range(box [1], box[3]):

                if (p1[x, y] != p2[x, y]):
                    print('mismatch found x=', x, ',y=', y)
                    res_image.putpixel((x, y), (185, 185, 185))

        res_image.show()
        res_image.save(properties.get('path_res'))


    def prapare(self,prefix,path_file_ref):
        ms = str(round(time.time() * 1000.0))
        ms = ms[6:]
        path_dir = "..//Images//results//" + prefix + ms
        os.makedirs(path_dir, exist_ok=True)
        assert os.path.exists(path_file_ref), 'Ref. file not found as expected at '+path_file_ref


        properties = {
            'path_root' :  "..//Images//results//" + prefix + ms,
            'path_res' : path_dir+"//result_image.png",
            'path_crop' : path_dir+"//Error.png",
            'path_screenshot' : path_dir+"//screenshot_image.png"
        }
        self.get_screen_capture(properties.get('path_res'))
        shutil.copyfile(path_file_ref, path_dir+"//ref_image.png")

        return properties

