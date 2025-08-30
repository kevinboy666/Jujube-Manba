import random
import os
import PIL
import PIL.ImageOps
import PIL.ImageEnhance
import PIL.ImageDraw
import PIL.ImageFilter
import numpy as np
import cv2
from PIL import Image

def gaussian_noise(img, _):
    
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    mean=0
    sigma=0.1
    
    # int -> float (標準化)
    img = img / 255.0
    # 隨機生成高斯 noise (float + float)
    noise = np.random.normal(mean, sigma, img.shape)
    # noise + 原圖
    gaussian_out = img + noise
    # 所有值必須介於 0~1 之間，超過1 = 1，小於0 = 0
    gaussian_out = np.clip(gaussian_out, 0, 1)
    
    # 原圖: float -> int (0~1 -> 0~255)
    gaussian_out = np.uint8(gaussian_out*255)
    
    img = Image.fromarray(cv2.cvtColor(gaussian_out, cv2.COLOR_BGR2RGB))
    return img
    


def Identity(img, v):
    return img


def AutoContrast(img, _):
    return PIL.ImageOps.autocontrast(img)


def Equalize(img, _):
    return PIL.ImageOps.equalize(img)


def Rotate(img, v):  # [-30, 30]
    assert -30 <= v <= 30
    if random.random() > 0.5:
        v = -v
    return img.rotate(v)


def Solarize(img, v):  # [0, 256]
    assert 0 <= v <= 256
    return PIL.ImageOps.solarize(img, v)


def Color(img, v):  # [0.1,1.9]
    assert 0.1 <= v <= 1.9
    return PIL.ImageEnhance.Color(img).enhance(v)


def Posterize(img, v):  # [4, 8]
    v = int(v)
    v = max(1, v)
    return PIL.ImageOps.posterize(img, v)


def Contrast(img, v):  # [0.1,1.9]
    assert 0.1 <= v <= 1.9
    return PIL.ImageEnhance.Contrast(img).enhance(v)


def Brightness(img, v):  # [0.1,1.9]
    assert 0.1 <= v <= 1.9
    return PIL.ImageEnhance.Brightness(img).enhance(v)


def Sharpness(img, v):  # [0.1,1.9]
    assert 0.1 <= v <= 1.9
    return PIL.ImageEnhance.Sharpness(img).enhance(v)


def ShearX(img, v):  # [-0.3, 0.3]
    assert -0.3 <= v <= 0.3
    if random.random() > 0.5:
        v = -v
    return img.transform(img.size, PIL.Image.AFFINE, (1, v, 0, 0, 1, 0))


def ShearY(img, v):  # [-0.3, 0.3]
    assert -0.3 <= v <= 0.3
    if random.random() > 0.5:
        v = -v
    return img.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, v, 1, 0))


def TranslateX(img, v):  # [-150, 150] => percentage: [-0.45, 0.45]
    assert -0.45 <= v <= 0.45
    if random.random() > 0.5:
        v = -v
    v = v * img.size[0]
    return img.transform(img.size, PIL.Image.AFFINE, (1, 0, v, 0, 1, 0))


def TranslateY(img, v):  # [-150, 150] => percentage: [-0.45, 0.45]
    assert -0.45 <= v <= 0.45
    if random.random() > 0.5:
        v = -v
    v = v * img.size[1]
    return img.transform(img.size, PIL.Image.AFFINE, (1, 0, 0, 0, 1, v))


def augment_list():
    aug_list = [
        (Identity, 0, 1),
        (AutoContrast, 0, 1),
        (gaussian_noise, 0, 1),
        #(Equalize, 0, 1),
        #(Rotate, 0, 30),
        #(Posterize, 0, 4),
        #(Solarize, 0, 256),
        #(Color, 0.1, 1.9),
        (Contrast, 0.1, 1.9),
        (Brightness, 0.1, 1.9),
        (Sharpness, 0.1, 1.9),
        # (ShearX, 0., 0.3),
        # (ShearY, 0., 0.3),
        # (TranslateX, 0., 0.33),
        # (TranslateY, 0., 0.33),
    ]

    return aug_list


def dirCheck(folderName):
    if not os.path.isdir(folderName ):
        os.mkdir(folderName)


class RandAugment:
    def __init__(self, n=2, m=30):
        self.n = n
        self.m = m      # [0, 30]
        self.augment_list = augment_list()

    def __call__(self, img):
        ops = random.choices(self.augment_list, k=self.n)
        for op, minval, maxval in ops:
            val = (float(self.m) / 30) * float(maxval - minval) + minval
            img = op(img, val)

        return img


if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # 獲取當前資料夾名稱然後存成dir_path
    all_file_name = os.listdir(dir_path)  # 列出所有檔案或資料夾名稱
    # 讀取資料夾內所有檔案名稱然後放進all_file_name

    for directory_name in all_file_name:
        full_dir_path = os.path.join(dir_path, directory_name)
        if os.path.isdir(full_dir_path):
            noise_dir = os.path.join(dir_path, directory_name + "_noise")
            dirCheck(noise_dir)
            for filename in os.listdir(full_dir_path):
                file_path = os.path.join(full_dir_path, filename)

                im = Image.open(file_path)
                randAug = RandAugment(m=10)
                im = randAug(im)
                save_path = os.path.join(noise_dir, filename)
                im.save(save_path)
            print("資料夾 " + directory_name + " 處理完成!")
    print("結束!")
