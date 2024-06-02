from PIL import Image
import os
SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR_PATH = os.path.dirname(SCRIPT_DIR_PATH) # new_game
DATA_PATH = os.path.join(PROJECT_DIR_PATH, "resources", "worlds", "maps")

# """OPTION
resize_w = 256
resize_h = 192
image_path = os.path.join(DATA_PATH, "white_240_180.png")
save_path = os.path.join(DATA_PATH, f"white_{resize_w}_{resize_h}.png")
# """


def resize():
    # サイズが指定サイズと一致しない場合のみリサイズ
    background_img = Image.open(image_path)
    if background_img.size != (resize_w, resize_h):
        resized_img = background_img.resize((resize_w, resize_h))
        resized_img.save(save_path)
        print(f"before size is {background_img.size}")
        print(f"after size is {resize_w, resize_h}")
    else:
        print("サイズが一致しています。")

if __name__ == "__main__":
    resize()