from skimage.metrics import structural_similarity as ssim
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

def getargs():
    file1 = 'file1.jpg'
    file2 = 'file2.jpg'
    if(len(sys.argv) >= 3):
        _,  file1, file2, *_ = sys.argv
    print(f'file1: {file1}')
    print(f'file2: {file2}')
    return file1, file2

def main():
    file1, file2 = getargs()
    imgdiff(file1, file2)

if __name__ == '__main__':
    main()
