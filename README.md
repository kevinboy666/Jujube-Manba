[繁體中文](README_tw.md) | English

# Jujube-Manba
Enhancing Detection Transformer with Mamba and Multi-scale Features for
Panoptic Segmentation of the Maturity and Quality of Green Jujubes

## Introduction

Jujube-Manba, built upon the DEtection TRansformer architecture, integrates Mamba modules and Atrous Spatial Pyramid Pooling modules within its backbone to enhance the model's multi-scale feature extraction capabilities and effectively capture long-range dependencies in images.
Furthermore, it employs a Noisy Student semi-supervised learning strategy, which effectively leverages a large amount of unlabeled data, reducing the model's reliance on manually labeled data.
Experimental results show that the method achieves a PQ value of 54.59, a significant improvement of 5.62 compared to the baseline model, demonstrating a substantial enhancement in maturity detection performance. It can also adapt to the complex scenes of real-world farms, effectively addressing issues such as leaf occlusion and fruit overlap, and achieving more accurate maturity grading.
