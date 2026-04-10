import os
import numpy as np
import rasterio


class Preprocessing:
    def __init__(
        self,
        pre_image_path,
        pre_scl_path,
        post_image_path,
        post_scl_path,
        dem_path,
        slope_path,
        aspect_path,
        output_folder
    ):
        self.pre_image_path = pre_image_path
        self.pre_scl_path = pre_scl_path
        self.post_image_path = post_image_path
        self.post_scl_path = post_scl_path
        self.dem_path = dem_path
        self.slope_path = slope_path
        self.aspect_path = aspect_path
        self.output_folder = output_folder

    def run(self):
        print("Running preprocessing...")

        # placeholder for now
        return {}
