import cv2 as cv
import numpy as np
from math import exp
""" Parameters for the Non-Local Mean algorithm. """
IMG_PATH = './input.png'
PATCH_SIZE = 1      # 3 for a 3x3 patch
WINDOW_SIZE = 5     # 5 for a 5x5 window
H = 100


class NLM:
    """ A class that implements non-local mean algorithm described in A. Buades et al., CVPR 2005.
    """
    def __init__(self, patch_size, window_size, h):
        self.patch_size = patch_size
        self.window_size = window_size
        self.padding = max(self.patch_size, self.window_size)
        self.h = h

    def filter(self, img_in):
        img_in = img_in / 255.0
        np.pad(img_in, self.padding, mode="edge")
        shape = img_in.shape
        img_out = np.zeros(shape, dtype=np.float)

        for x in range(self.padding, shape[0] - self.padding):
            for y in range(self.padding, shape[1] - self.padding):
                print(x, y)
                sum = 0
                for i in range(x - self.window_size // 2, x + self.window_size // 2 + 1):
                    for j in range(y - self.window_size // 2, y + self.window_size // 2 + 1):
                        sum += self.calc_weight(img_in, x, y, i, j) * img_in[i, j]
                img_out[x, y] = sum
        # Truncate to initial image size without padding
        return img_out[self.padding: shape[0] - self.padding, self.padding: shape[1] - self.padding, :]

    def calc_weight(self, img, x_1, y_1, x_2, y_2):
        normalize_const = self.calc_normalize_const(img, x_1, y_1)
        gauss_weighted_dist = self.calc_gauss_weighted_euclid_dist(img, x_1, y_1, x_2, y_2)
        return 1 / normalize_const * gauss_weighted_dist

    def calc_normalize_const(self, img, x, y):
        sum = 0
        for i in range(x - self.window_size // 2, x + self.window_size // 2 + 1):
            for j in range(y - self.window_size // 2, y + self.window_size // 2 + 1):
                sum += self.calc_gauss_weighted_euclid_dist(img, x, y, i, j)
        return sum

    def calc_gauss_weighted_euclid_dist(self, img, x_1, y_1, x_2, y_2):
        radius = self.patch_size // 2
        patch_i = img[x_1-radius: x_1+radius+1, y_1-radius: y_1+radius+1]
        patch_j = img[x_2-radius: x_2+radius+1, y_2-radius: y_2+radius+1]
        # Euclidean distance
        dist = np.linalg.norm(patch_i - patch_j) ** 2
        gauss_weighted_dist = exp(-dist / self.h ** 2)
        return gauss_weighted_dist


def wheel():
    nlm = NLM(PATCH_SIZE, WINDOW_SIZE, H)
    img_in = cv.imread(IMG_PATH)
    img_out = nlm.filter(img_in)
    cv.imshow("Initial Image", img_in)
    cv.imshow("Filtered Image", img_out)
    cv.waitKey(0)


if __name__ == '__main__':
    wheel()

