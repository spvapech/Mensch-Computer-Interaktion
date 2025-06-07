import numpy as np
import numpy.typing as npt


#############################################
# implement the NEAREST NEIGHBOR scaling here
#############################################
def nearest_neighbor_scaling(scaling: float, img_array: npt.ArrayLike) -> npt.NDArray:
    orig_h, orig_w = img_array.shape[0:2]
    new_h, new_w = int(orig_h * scaling), int(orig_w * scaling)

    # Prepare output array
    if img_array.ndim == 3:
        scaled_img = np.zeros((new_h, new_w, img_array.shape[2]), dtype=img_array.dtype)
    else:
        scaled_img = np.zeros((new_h, new_w), dtype=img_array.dtype)

    for i in range(new_h):
        for j in range(new_w):
            orig_i = min(int(i / scaling), orig_h - 1)
            orig_j = min(int(j / scaling), orig_w - 1)
            scaled_img[i, j] = img_array[orig_i, orig_j]

    return scaled_img
