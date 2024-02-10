import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".svg") and "-dark.svg" in filename:
            new_filename = filename.replace("-dark.svg", "-light.svg")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    img_directory = "img-light/img"
    rename_files(img_directory)