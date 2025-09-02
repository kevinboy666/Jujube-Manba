[繁體中文](README_tw.md) | English

# Jujube-Manba
Enhancing Detection Transformer with Mamba and Multi-scale Features for
Panoptic Segmentation of the Maturity and Quality of Green Jujubes

## Introduction

Jujube-Manba, built upon the DEtection TRansformer architecture, integrates Mamba modules and Atrous Spatial Pyramid Pooling modules within its backbone to enhance the model's multi-scale feature extraction capabilities and effectively capture long-range dependencies in images.

Furthermore, it employs a Noisy Student semi-supervised learning strategy, which effectively leverages a large amount of unlabeled data, reducing the model's reliance on manually labeled data.

Experimental results show that the method achieves a PQ value of 54.59, a significant improvement of 5.62 compared to the baseline model, demonstrating a substantial enhancement in maturity detection performance. It can also adapt to the complex scenes of real-world farms, effectively addressing issues such as leaf occlusion and fruit overlap, and achieving more accurate maturity grading.

## Performance

###  Complex Scenarios
<div align="center">
  <img src="https://github.com/kevinboy666/Jujube-Manba/blob/main/assets/2-1-1_35.jpg" width=500 >
<!--   <img src="https://github.com/kevinboy666/Jujube-Manba/blob/main/assets/2-1-1_35_label.png" width=400 > -->
  <img src="https://github.com/kevinboy666/Jujube-Manba/blob/main/assets/2-1-1_35_f3.png" width=500 >
</div>

###  Difficult Conditions
<div align="center">
  <img src="https://github.com/kevinboy666/Jujube-Manba/blob/main/assets/11-1-1_34.jpg" width=500 >
  <img src="https://github.com/kevinboy666/Jujube-Manba/blob/main/assets/11-1-1_34_f3.png" width=500 >

</div>

### Install
conda env create -f environment.yml

### [Train](https://github.com/kevinboy666/Jujube-Manba/blob/main/jujube-mamba2.ipynb)

### [Inference](https://github.com/kevinboy666/Jujube-Manba/blob/main/infer.ipynb)

Paper,

@article{Jujube-DETR,
    title={Jujube-DETR: An Enhanced Detection Transformer for the Panoptic Segmentation of the Maturity and Quality of In-Field Taiwanese Jujubes Using Mamba and Multi-Scale Features},
    author={Yin, Tang-Kai and Wang, Kuan-Yan},
    journal={submitted for publication},
    year={2025}
}
