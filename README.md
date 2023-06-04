# Unet-semantic-segmentation-
Project Description:
This project aims to address the task of artery-vein classification and center-line extraction in retinal images. The initial step involves preprocessing the dataset to enhance luminosity using Contrast Limited Adaptive Histogram Equalization (CLAHE) and reduce noise using a Median filter. Since retinal images contain intricate details, a cropping technique called patch extraction is applied to simplify the training process. This involves dividing the original image into smaller regions known as patches.

The training process begins with the original U-Net architecture, a popular choice for image segmentation tasks. However, modifications are made to the architecture based on evaluation results. To improve performance, each block of the U-Net architecture is augmented by adding a convolutional layer. Additionally, the number of filters is reduced to 32 instead of the original 64, aiming to strike a balance between efficiency and accuracy.

By employing these preprocessing techniques and refining the U-Net architecture, the project aims to achieve accurate classification of arteries and veins in retinal images while extracting the center-lines. This work is essential for various medical applications, such as diagnosing vascular diseases and monitoring retinal health.
