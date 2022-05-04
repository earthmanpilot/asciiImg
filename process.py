import numpy as np
from pathlib import Path
from PIL import Image



class Converter:
    def __init__(self, image):

        self.col_size = 200
        self.row_col_ratio = 3.8
        self.characters_set = "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
        self.set_len = len(self.characters_set)
        self.image_ds = self.downsample(image)

        print(self.image_ds.shape)
        self.image_grey = self.grey_magnatude(self.image_ds)
        print(self.image_grey.shape)


    @classmethod
    def from_Path(path: Path):
        pass

    @staticmethod
    def grey_magnatude(img):
        return 1.0 - (np.mean(img, axis=-1) / 255.)

    def downsample(self, img):
        rows, cols, _ = img.shape
        row_factor = round((rows/self.col_size)*self.row_col_ratio)
        col_factor = round((cols/self.col_size))
        img_ds = img[::row_factor, ::col_factor]
        return img_ds

    def value_to_character(self, value):
        ix = round(value*(self.set_len-1) )
        return self.characters_set[-(ix+1)]

    @staticmethod
    def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

    def __repr__(self):
        rows_, cols_ = self.image_grey.shape
        for i, row in enumerate(range(rows_)):
            for col in range(cols_):
                value = self.image_grey[row, col]
                r,g,b = self.image_ds[row, col]
                text = self.value_to_character(value)
                colored_text = self.colored(r,g,b,text)
                print(colored_text, end='')
            print(i)
        return ''
