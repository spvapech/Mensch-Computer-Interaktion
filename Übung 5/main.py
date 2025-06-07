import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class GreenScreenRemover:
    def __init__(self, person_image_path, background_image_path):
        self.original_npa = plt.imread(person_image_path)
        self.og_shape = self.original_npa.shape

        self.background_npa = plt.imread(background_image_path)
        self.background_npa = self.background_npa[:self.og_shape[0], :self.og_shape[1], :self.og_shape[2]]

        self.selected_pixels_image = np.zeros_like(self.original_npa)
        self.combined_image = np.zeros_like(self.original_npa)

    def remove_green_background(self):
        red = self.original_npa[:, :, 0]
        green = self.original_npa[:, :, 1]
        blue = self.original_npa[:, :, 2]

        # Mask for non-green pixels
        mask = ~((green > 100/255.0) & (green > red + 0.1) & (green > blue + 0.1))

        # Apply mask to keep only the person
        self.selected_pixels_image[mask] = self.original_npa[mask]

    def combine_with_background(self):
        # Use the same mask as above to overlay the background where green was removed
        mask = (self.selected_pixels_image.sum(axis=2) > 0)
        self.combined_image = self.background_npa.copy()
        self.combined_image[mask] = self.selected_pixels_image[mask]

    def show_and_save_result(self, output_file='person_in_forest.png'):
        plt.subplot(1, 3, 1)
        plt.title("Original Image")
        plt.imshow(self.original_npa)
        plt.xticks([])
        plt.yticks([])

        plt.subplot(1, 3, 2)
        plt.title("Selected Pixels")
        plt.imshow(self.selected_pixels_image)
        plt.xticks([])
        plt.yticks([])

        plt.subplot(1, 3, 3)
        plt.title("Combined Image")
        plt.imshow(self.combined_image)
        plt.xticks([])
        plt.yticks([])

        plt.savefig(output_file)
        plt.show()


if __name__ == '__main__':
    remover = GreenScreenRemover('person_on_greenscreen.jpg', 'forest.jpg')
    remover.remove_green_background()
    remover.combine_with_background()
    remover.show_and_save_result()
