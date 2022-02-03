---
layout: post
title: "VoxelMorph: A Learning Framework for Deformable Medical Image Registration 논문 리뷰"
subtitle : VoxelMorph
tags: [Registration, Paper Review]
categories: Registration
author: Pebpung
comments : True
typora-root-url: ../
use_math: true

---

> VoxelMorph: A Learning Framework for Deformable Medical Image Registration 논문을 읽고 정리한 글입니다.  

<br>



앞선 글에서 Medical 분야에서 주로 사용되는 [Image Registration 방법론](https://pebpung.github.io/registration/2022/01/30/Registration-1.html) 들에 대해서 살펴보았습니다. 이번 글에서는 Registration 방법중  Deformable Registration에 대해서 알아보고 CNN based Deformable Registration의 대표적인 논문인 VoxelMorph를 정리해볼 예정입니다. 



## Deformable Registration 이란?

<img src="/assets/img/2022/3-Figure1-1.png" alt="3-Figure1-1" style="zoom: 67%;" />

 Deformable Registration이란 뒤틀려져 있는 정보를 정합할 수 있는 매우 유연한 Registration 기법입니다. Medical 이미지는  연속체에서 어떤 힘이나 시간 흐름에 따라 기하학적인 변화가 생기게 됩니다. 그렇기 때문에 rigid, affine 변화처럼 linear한 공간만 다루는 registration 기법은 정확한 정합을 기대하기 힘듭니다. Deformable Registration은 공간 자체를 warping 시기 위한 Nonlinear registration map을 얻어서 위의 사진과 같이 기하학적인 변화를 일으킵니다. 

대부분의 사진 정합에서 높은 정확도로 Registration이 될 수 있다는 장점에도 불구하고 Deformable Registration은 실제로 사용하기 어렵다는 단점이 있습니다. 그 이유는 Deformable field를 계산하기 위한 computational resource가 많이 든다는 점입니다. 특히 3D 영상의 경우 각 pair에 대해서 dense하고 non-linear한 correpondance가 이루어지기 때문에 계산량이 많아지게 됩니다. 이러한 문제를 해결하기 위해서 최근에는 CNN을 도입한 Deformable registration 기법이 등장하게 됩니다. 

<br>

## **VoxelMorph**

### 접근 방식

VoxelMorph는 기존 방법론에서 2가지의 문제를 해결하는데 초점을 맞췄습니다. 이 논문에서 제기한 문제는 다음과 같습니다. 

- Deep learning 없이 Nonlinear registration mapping을 구하는 계산량이 엄청나게 높음.

- 기존의 Nonlinear registration은 ground truth를 이용하여 Supervised learning으로 학습을 진행했음.

앞서 설명드렸던 것 처럼, Nonlinear registration(Deformable registration)을 구하는 것은 굉장히 계산량이 많이 드는 작업입니다. 이를 CNN을 도입하여 계산량을 줄이는 데 성공하였지만, 논문의 저자는 Supervised learning에 대한 문제점을 제기하고 있습니다. 

Supervised learning의 특성상 ground truth 정보가 필요합니다. 하지만 3차원 상에서 전체 이미지의 Nonlinear registration map을 얻는 작업 또한 계산량이 많이 들게 됩니다. 그렇기 때문에 이 논문에서는 Nonlinear registration map이 필요 없는 Unsupervised learning 방식을 제안하고 있습니다. 



### 방법론

<img src="/assets/img/2022/voxelmorph.png" alt="voxelmorph" style="zoom: 67%;" />

입력으로 들어가기 전에 Moving 3D image와 Fixed 3D image는 affine alignment를 수행한다. 그 후에 두개의 input을 Unet에 misalignment가 nonlinear하다고 가정하고 들어간다. 
