import numpy as np
import numpy.typing as npt


###################################################
# implement the BILINEAR INTERPOLATION scaling here
#############################################
def bilinear_interpolation_scaling(scaling: float, img_array: npt.ArrayLike) -> npt.NDArray:
    orig_h, orig_w = img_array.shape[0:2]
    new_h, new_w = int(orig_h * scaling), int(orig_w * scaling)

    if img_array.ndim == 3:
        scaled_img = np.zeros((new_h, new_w, img_array.shape[2]), dtype=np.float32)
    else:
        scaled_img = np.zeros((new_h, new_w), dtype=np.float32)

    for i in range(new_h):
        for j in range(new_w):
            # Map coordinate back to original
            x = i / scaling
            y = j / scaling

            x0 = int(np.floor(x))
            x1 = min(x0 + 1, orig_h - 1)
            y0 = int(np.floor(y))
            y1 = min(y0 + 1, orig_w - 1)

            dx = x - x0
            dy = y - y0

            if img_array.ndim == 3:
                top = (1 - dy) * img_array[x0, y0] + dy * img_array[x0, y1]
                bottom = (1 - dy) * img_array[x1, y0] + dy * img_array[x1, y1]
                value = (1 - dx) * top + dx * bottom
            else:
                top = (1 - dy) * img_array[x0, y0] + dy * img_array[x0, y1]
                bottom = (1 - dy) * img_array[x1, y0] + dy * img_array[x1, y1]
                value = (1 - dx) * top + dx * bottom

            scaled_img[i, j] = value

    # Convert back to original dtype
    return np.clip(scaled_img, 0, 255).astype(img_array.dtype)
