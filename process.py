import numpy as np
from pathlib import Path
from PIL import Image
from numpy.typing import ArrayLike


class Converter:
    def __init__(self, image: ArrayLike, col_size: int = 64):

        self.col_size = col_size
        self.row_col_ratio = 3.8
        self.characters_set = (
            "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
        )
        self.set_len = len(self.characters_set)
        self.image_ds = self.downsample(image)
        self.image_grey = self.grey_magnatude(self.image_ds)

    @classmethod
    def from_Path(path: Path):

        img_path = "data/f9_rocket.jpg"  #  'data/cat.webp'
        img = Image.open(img_path)
        img_np = np.array(img)
        c = Converter(img_np)
        pass

    @staticmethod
    def grey_magnatude(img: ArrayLike):
        return 1.0 - (np.mean(img, axis=-1) / 255.0)

    def downsample(self, img: ArrayLike):
        rows, cols, _ = img.shape
        row_factor = round((rows / self.col_size) * self.row_col_ratio)
        col_factor = round((cols / self.col_size))
        img_ds = img[::row_factor, ::col_factor]
        return img_ds

    def value_to_character(self, value: float):
        ix = round(value * (self.set_len - 1))
        return self.characters_set[-(ix + 1)]

    @staticmethod
    def colored(r: int, g: int, b: int, text: str):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

    def ascii_print(self, color: bool = True) -> None:
        rows_, cols_ = self.image_grey.shape
        for i, row in enumerate(range(rows_)):
            for col in range(cols_):
                value = self.image_grey[row, col]
                text = self.value_to_character(value)
                if color:
                    r, g, b = self.image_ds[row, col]
                    text = self.colored(r, g, b, text)
                print(text, end="")
            print(i)
