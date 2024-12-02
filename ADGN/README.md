### Augmented Data Generation Network(ADGN)
 
See [INSTALL.md](INSTALL.md) for the installation of dependencies required.

## Demo

To test the pre-trained Restormer models of [Deraining](https://drive.google.com/drive/folders/1ZEDDEVW0UgkpWi-N4Lj_JUoVChGXCu_u), [Motion Deblurring](https://drive.google.com/drive/folders/1czMyfRTQDX3j3ErByYeZ1PM4GVLbJeGK), [Defocus Deblurring](https://drive.google.com/drive/folders/1bRBG8DG_72AGA6-eRePvChlT5ZO4cwJ4?usp=sharing), and [Denoising](https://drive.google.com/drive/folders/1Qwsjyny54RZWa7zC4Apg7exixLBo4uF0) on your own images, you can either use Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1C2818h7KnjNv4R1sabe14_AYL7lWhmu6?usp=sharing), or command line as following
```
python demo.py --task Task_Name --input_dir path_to_images --result_dir save_images_here
```
Example usage to perform Defocus Deblurring on a directory of images:
```
python demo.py --task Single_Image_Defocus_Deblurring --input_dir './demo/degraded/' --result_dir './demo/restored/'
```
Example usage to perform Defocus Deblurring on an image directly:
```
python demo.py --task Single_Image_Defocus_Deblurring --input_dir './demo/degraded/portrait.jpg' --result_dir './demo/restored/'
```

## Training and Evaluation

Training and Testing instructions for Deraining, Motion Deblurring, Defocus Deblurring, and Denoising are provided in their respective directories. Here is a summary table containing hyperlinks for easy navigation:

<table>
  <tr>
    <th align="left">Task</th>
    <th align="center">Training Instructions</th>
    <th align="center">Testing Instructions</th>
    <th align="center">Restormer's Visual Results</th>
  </tr>
  <tr>
    <td align="left">Deraining</td>
    <td align="center"><a href="Deraining/README.md#training">Link</a></td>
    <td align="center"><a href="Deraining/README.md#evaluation">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1HcLc6v03q_sP_lRPcl7_NJmlB9f48TWU?usp=sharing">Download</a></td>
  </tr>
  <tr>
    <td>Motion Deblurring</td>
    <td align="center"><a href="Motion_Deblurring/README.md#training">Link</a></td>
    <td align="center"><a href="Motion_Deblurring/README.md#evaluation">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1qla3HEOuGapv1hqBwXEMi2USFPB2qmx_?usp=sharing">Download</a></td>
  </tr>
  <tr>
    <td>Defocus Deblurring</td>
    <td align="center"><a href="Defocus_Deblurring/README.md#training">Link</a></td>
    <td align="center"><a href="Defocus_Deblurring/README.md#evaluation">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1V_pLc9CZFe4vN7c4SxtXsXKi2FnLUt98?usp=sharing">Download</a></td>
  </tr>
  <tr>
    <td>Gaussian Denoising</td>
    <td align="center"><a href="Denoising/README.md#training">Link</a></td>
    <td align="center"><a href="Denoising/README.md#evaluation">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1rEAHUBkA9uCe9Q0AzI5zkYxePSgxYDEG?usp=sharing">Download</a></td>
  </tr>
  <tr>
    <td>Real Denoising</td>
    <td align="center"><a href="Denoising/README.md#training-1">Link</a></td>
    <td align="center"><a href="Denoising/README.md#evaluation-1">Link</a></td>
    <td align="center"><a href="https://drive.google.com/file/d/1CsEiN6R0hlmEoSTyy48nnhfF06P5aRR7/view?usp=sharing">Download</a></td>
  </tr>
</table>

## Results
Experiments are performed for different image processing tasks including, image deraining, single-image motion deblurring, defocus deblurring (both on single image and dual pixel data), and image denoising (both on Gaussian and real data). 
