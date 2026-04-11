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

    def load_bands(self):
        print("Loading raster data...")

        with rasterio.open(self.pre_image_path) as src:
            self.pre_nir = src.read(1).astype(np.float32)
            self.pre_swir = src.read(2).astype(np.float32)
            self.meta = src.meta.copy()

        with rasterio.open(self.post_image_path) as src:
            self.post_nir = src.read(1).astype(np.float32)
            self.post_swir = src.read(2).astype(np.float32)

        with rasterio.open(self.pre_scl_path) as src:
            self.pre_scl = src.read(1)

        with rasterio.open(self.post_scl_path) as src:
            self.post_scl = src.read(1)

        print("Bands loaded successfully.")

    def run(self):
        print("Running preprocessing...")
        self.load_bands()

        return {
            "pre_nir": self.pre_nir,
            "pre_swir": self.pre_swir,
            "post_nir": self.post_nir,
            "post_swir": self.post_swir
        }