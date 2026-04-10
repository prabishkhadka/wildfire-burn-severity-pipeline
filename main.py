from src.pre_processing import Preprocessing


def main():
    print("Wildfire Burn Severity Pipeline\n")

    print("Step 1: Run input notebook first:")
    print("notebooks/01_get_input.ipynb\n")

    print("Step 2: Running preprocessing...\n")

    # ----------------------------------------
    # Define input paths
    # ----------------------------------------
    preprocessing = Preprocessing(
        pre_image_path="data/raw/pre_fire_B8_B12.tif",
        pre_scl_path="data/raw/pre_fire_SCL.tif",
        post_image_path="data/raw/post_fire_B8_B12.tif",
        post_scl_path="data/raw/post_fire_SCL.tif",
        dem_path="data/raw/dem_srtm.tif",
        slope_path="data/raw/slope_srtm.tif",
        aspect_path="data/raw/aspect_srtm.tif",
        output_folder="data/preprocessed"
    )

    # ----------------------------------------
    # Run preprocessing
    # ----------------------------------------
    results = preprocessing.run()

    print("\nPreprocessing complete.")
    print("Outputs saved to: data/preprocessed\n")


if __name__ == "__main__":
    main()
