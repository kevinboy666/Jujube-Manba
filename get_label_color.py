import json
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np
from PIL import Image

def dirCheck(folderName):
    if not os.path.isdir(folderName ):
        os.mkdir(folderName)



if __name__ == '__main__':

    dir_path = os.path.dirname(os.path.realpath(__file__))
    # 獲取當前資料夾名稱然後存成dir_path
    all_file_name = os.listdir(dir_path)  # 列出所有檔案或資料夾名稱
    # 讀取資料夾內所有檔案名稱然後放進all_file_name

    print(all_file_name[:-2])
    

    json_path = '/media/tkyin/新增磁碟區/DETR/DETR/cityscapes_panoptic_all.json'
    with open(json_path, 'r') as f:
        data = json.load(f)

    # panoptic_mask_path = '/media/tkyin/新增磁碟區/DETR/DETR/jujube/fold1/gtFine/cityscapes_panoptic_train/6-2-1_39_panoptic.png'

    category_colors = {
        # 1: (255, 182, 193),    # 粉紅
        2: (0, 0, 255),    # 背景 blue
        3: (255, 255, 0),    # X yellow
        4: (0, 0, 0),  # bad 
        5: (0, 255, 0),  # normal green
        6: (255, 0, 0),  # good red
        # ...
    }

    # 選擇顏色
    color_map = {
        (255, 0, 193):   [255, 0, 193],         # IG 粉紅
        (0, 0, 255):   [0, 0, 255],              # 背景 blue
        (255, 255, 0):   [255, 255, 0],       #X yellow
        (0, 0, 0):   [0, 0, 0],    # bad
        (0, 255, 0):   [0, 255, 0],  # normal green
        (255, 0, 0):   [255, 0, 0],  # good red
    }

    for directory_name in all_file_name[:-2]:
        full_dir_path = os.path.join(dir_path, directory_name)
        if os.path.isdir(full_dir_path):
            color_dir = os.path.join(dir_path, directory_name + "_colored")
            label_dir = os.path.join(dir_path, directory_name + "_labeled")
            dirCheck(color_dir)
            dirCheck(label_dir)

            for filename in os.listdir(full_dir_path):
                file_path = os.path.join(full_dir_path, filename)
                # print(file_path)
                # break
                # im = Image.open(file_path)
                folder =  file_path.split('/')[-2]
                img_name = file_path.split('/')[-1].replace('.jpg', '')
                panoptic_mask_path = f'/media/tkyin/新增磁碟區/DETR/DETR/get_pic/gt/{img_name}_panoptic.png'
                # print(panoptic_mask_path)
# /media/tkyin/新增磁碟區/DETR/DETR/get_pic/gt/1-1-1_0_panoptic.png


                # # 載入 panoptic mask（通常為 RGB 或單通道對應 id）
                mask_image = Image.open(panoptic_mask_path)
                mask_np = np.array(mask_image)

                # # 如果是 RGB，要轉成單一整數 id，例如：id = R * 256^2 + G * 256 + B
                if mask_np.ndim == 3:
                    mask_id = mask_np[:, :, 2] * 256 * 256 + mask_np[:, :, 1] * 256 + mask_np[:, :, 0]
                else:
                    mask_id = mask_np  # 如果已經是單通道（即每個 pixel 的值是 segment id）

                # 建立彩色圖
                default_color = (255, 0, 193)
                height, width = mask_id.shape
                colored_mask = np.full((height, width, 3), default_color, dtype=np.uint8)

                # 找出這張圖對應的 annotation
                image_id = img_name
                annotation = next(a for a in data['annotations'] if a['image_id'] == image_id)

                # 遍歷 segments
                for segment in annotation['segments_info']:
                    seg_id = segment['id']
                    cat_id = segment['category_id']
                    color = category_colors.get(cat_id, (0,0,0))  # 若未定義顏色則用黑色
                    # print(seg_id,cat_id,color)

                    # 將 mask 中對應 seg_id 的像素塗上對應 category 顏色
                    colored_mask[mask_id == seg_id] = color

                # 儲存上色後的結果
                output_image = Image.fromarray(colored_mask)
                save_path = os.path.join(color_dir, filename.replace('jpg', 'png'))
                output_image.save(save_path)



                # 設定分割遮罩的路徑
                segmentation_path =  f'/media/tkyin/新增磁碟區/DETR/DETR/get_pic/{folder}_colored/{img_name}.png'
                # print(segmentation_path)
# /media/tkyin/新增磁碟區/DETR/DETR/get_pic/1-1-1_colored/1-1-1_0.jpg
                # 載入圖片
                img = io.imread(file_path)

                # 獲取當前 axes 對象
                ax = plt.gca()

                # 載入分割遮罩 
                segmentation_mask = Image.open(segmentation_path)
                segmentation_mask = np.array(segmentation_mask)


                #    先建立一個和原始圖片一樣大小的全黑畫布
                color_mask_display = np.zeros_like(img)

                #    遍歷你的顏色映射表
                for mask_rgb_tuple, display_color_list in color_map.items():
                    # 找到原始遮罩中所有像素值等於 mask_rgb_tuple 的位置
                    locations = np.all(segmentation_mask == mask_rgb_tuple, axis=-1)
                    
                    # 將這些位置在新的彩色遮罩上著色
                    color_mask_display[locations] = display_color_list


                # 3. 將彩色遮罩疊加到原始圖片上
                alpha = 0.4  # 設定透明度 (0.0 完全透明, 1.0 完全不透明)

                # 建立一個布林遮罩，標記所有不是背景色的地方 (即我們想要疊加顏色的地方)
                # 這裡我們假設背景在 color_map 中被映射為 [0,0,0]
                non_background_mask = np.any(color_mask_display > 0, axis=-1)

                # 複製一份原始影像，以避免修改原始影像
                blended_img = img.copy()

                # 只在非背景區域進行 alpha 混合
                # 公式: blended = img * (1 - alpha) + overlay * alpha
                blended_img[non_background_mask] = (
                    (img[non_background_mask] * (1 - alpha)) + 
                    (color_mask_display[non_background_mask] * alpha)
                ).astype(np.uint8)


                # blended_img 是 numpy array，shape = (H, W, 3)
                output_img = Image.fromarray(blended_img)
                target_size=(640, 360)
                output_img = output_img.resize(target_size, resample=Image.BILINEAR)

                save_path = os.path.join(label_dir, filename.replace('jpg', 'png'))
                output_img.save(save_path)

            print("資料夾 " + directory_name + " 處理完成!")
    print("結束!")
