from skimage.metrics import structural_similarity as ssim
from pathlib import Path

import sys
import cv2

def measure_similarity(image1_path, image2_path):
    # Load images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    # Ensure the images are the same size
    image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
    # Compute SSIM between the two images
    similarity, _ = ssim(image1, image2, full=True)
    return similarity

# Example usage
def imgdiff(file1, file2):
    similarity = measure_similarity(file1, file2)
    print(f"Image similarity (SSIM): {similarity}")
    return 1.0 - similarity

def diff_filter(imgpath, dmin):
    """
    Given a path containing images in sequential order,  only return the paths of the files
    are less that the minimum similarity from the preceeding file. 
    - For each comparison there will be a "file1" and "file2" .
    - if imgdiff(file1, file2) < dmin, output the path of file1, and then set 
        file2 to be the next file1.  
    - continue the process until all files processed.

    """
    # get list of files
    paths = [filepath for filepath in sorted(Path(imgpath).iterdir())]
    curdiff = None
    lastimg = None
    for path in paths:
        if lastimg is None:
            print('lastimg is null')
            lastimg = path
            next
        curimg = path
        d = imgdiff(lastimg, curimg)
        if d > dmin:
            print(f'{curimg} has d-value of {d}, minimum is {dmin}')
            lastimg = curimg
        print(path)

def getargs():
    file1 = 'file1.jpg'
    file2 = 'file2.jpg'
    if(len(sys.argv) >= 3):
        _,  file1, file2, *_ = sys.argv
    # print(f'file1: {file1}')
    # print(f'file2: {file2}')
    return file1, file2

def main():
    file1, file2 = getargs()
    imgdiff(file1, file2)

def main2(): 
    print('you called main2')

    print(f'arg length is {len(sys.argv)}')
    if len(sys.argv) < 2:
        print('not enough args')
        exit(1)
    filepath = sys.argv[1]
    diff_filter(filepath, 0.001)


if __name__ == '__main__':
    main2()
