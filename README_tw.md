繁體中文 | [English](README.md)

# Jujube-Manba

"基於曼巴及多尺度特徵強化之偵測變換器應用於棗子成熟度和品質的全景分割" 的實現

## 簡介

Jujube-Manba 以 DEtection TRansformer 為基礎架構，並於 Backbone 中整合 Mamba 模塊與 Atrous Spatial Pyramid Pooling模塊，以強化模型對多尺度特徵的提取能力，並有效捕捉影像中長距離依賴關係。
同時採用 Noisy Student 半監督學習策略，可有效利用大量未標記資料，降低模型對人工標記數據的依賴性。
實驗結果顯示，該方法的PQ值達54.59，相較於基準模型提升5.62，顯著提升了成熟度檢測的效果，並且能夠適應真實農場的複雜場景，有效應對葉片遮擋、果實重疊等情況，實現更精準的成熟度分級。

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
