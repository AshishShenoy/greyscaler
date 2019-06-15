greyscaler
===

greyscaler is a small python script that converts an image to a greyscale or 'black and white' format.

It does this by calculating the greyscale 'luminanace' for each pixel using the relative luminance algorithm and converting the image to greyscale pixel-by-pixel.

To run this module, the following dependencies in the form of Python 3
libraries are needed:

- Pillow
- progressbar

Install these with the command:

    $ sudo pip3 install Pillow progressbar2


Download:

    $ git clone https://github.com/AshishShenoy/greyscaler.git

## **Usage**:

Consider the following image:

<img src="https://github.com/AshishShenoy/greyscaler/blob/master/test.jpg" width = "720">

Processing:

    $ python3 greyscaler.py
    Enter the image filename with its extension: test.jpg

Output:

<img src="https://github.com/AshishShenoy/greyscaler/blob/master/test_gs.jpg" width = "720">
