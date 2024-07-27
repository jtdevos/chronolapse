from skimage.metrics import structural_similarity as ssim
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
def imgdiff():
    image1_path = '/Users/jim/temp/img1a.jpg'
    image2_path = '/Users/jim/temp/img3.jpg'
    similarity = measure_similarity(image1_path, image2_path)
    print(f"Image similarity (SSIM): {similarity}")

def main():
    print(f'in main: ${__name__}')
    print()
    imgdiff();

if __name__ == '__main__':
    print('i am myself')

main()
