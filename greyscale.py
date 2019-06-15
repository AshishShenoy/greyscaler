from os import path
from subprocess import Popen
from PIL import Image
from progressbar import progressbar
from platform import system


OSname = system()
DEFAULT_DICT = {"Windows":"start", "Linux":"see", "Darwin":"open"}
DEFAULT_APP = DEFAULT_DICT[OSname]


def greyscale(img):
    width, height = img.size
    newImg = Image.new("RGB", (width, height))

    for j in progressbar(range(height)):
        for i in range(width):
            r, g, b = img.getpixel((i, j))
            avg = relativeLuminanace(r, g, b)
            newImg.putpixel((i, j), (avg, avg, avg))

    return newImg


def relativeLuminanace(r, g, b):
    """
    Returns an integer denoting the relative luminance of the RGB values.

    Relative luminance is an attempt to estimate the brightness of a color as
    perceived by our eyes. A rough approximation of the algorithm is used here
    to calculate the luminance of a color (r, g, b) as:

                    0.2 ∗ r + 0.7 ∗ g + 0.1 ∗ b
    """
    return int(r*0.2 + g*0.7 + b*0.1)


def main():
    imgName = input("Enter the image filename with its extension: ")
    while not path.exists(imgName):
        imgName = input("The image does not exist. Please enter a valid image filename: ")
    
    image = Image.open(imgName)
    newImage = greyscale(image)
    newImageName = imgName[:imgName.index(".")] + "_gs.jpg"
    newImage.save(newImageName)

    Popen([DEFAULT_APP, newImageName])


if __name__ == "__main__":
    main()