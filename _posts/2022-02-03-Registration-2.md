---
layout: post
title: "VoxelMorph: A Learning Framework for Deformable Medical Image Registration 논문 리뷰"
subtitle : VoxelMorph
tags: [Medical, AI]
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

VoxelMorph에 대한 내용을 하나씩 살펴보도록 하겠습니다. 우선 입력으로는 Moving 3D image와 Fixed 3D image가 있어야 합니다. 이 두개의 이미지는 미리 affine alignment를 수행해야 합니다. 그 후에 두개의 input을 Unet으로 넣어주게 됩니다. 

### VoxelMorph를 사용하는 이유

VoxelMorph 이전에도 ANTs모듈의 SyN을 사용해서 Non-rigid Registration을 수행했습니다. 하지만 기존의 Non-rigid Registration 방식은 뒤틀려져 있는 기하학적인 변화를 계산하기에 굉장히 많은 시간이 걸립니다.

![img](/assets/img/2022/https%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252F39b698ee-6aad-478b-b23f-85a0f77f9b33%252FUntitled.png)

위의 표를 보게 되면 ANTs모듈의 SyN의 경우 CPU에서 9059s 즉, 2시간 반 정도의 시간이 소모됩니다. 이에 반해서 VoxelMorph는 성능은 비슷하지만 57초로 매우 빠른 성능을 보여주고 있습니다.

### VoxelMorph를 사용해서 Parcellation 수행

Registration를 사용해서 Parcellation을 하는 방식은 기존 Segmentation 방법론과는 전혀 다른 방식입니다. Segmentation을 사용할 때는 [위에서 드린 설명](https://www.notion.so/VoxelMorph-09e80ca725d04249bebd787f1998a8f2)과 같이 입력을 넣으면 픽셀 단위로 인식하는 단계가 필요합니다. 하지만 Registration은 픽셀 단위로 인식 하는 단계 없이, 기존 Segmentation Mask정보를 변형해서 원하는 작업을 수행하겠다는 것입니다.

![img](/assets/img/2022/https%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252Fc5c3ca20-ad28-40d9-9fb6-5fe2b76f0e04%252FUntitled.png)

위의 예시로 설명 드리겠습니다.  Moving image인 *y*1과 Segmentation mask  *z*1이 입력 되었다고 가정하면, *y*1을 Fixed image인 *x*와 registration(정합)될 수 있는 하는 registration field *T*를 계산합니다.

여기서 Moving image란 Fixed image와 비슷한 형태로 변형이 되는 대상입니다.

그리고 *y*1의 Segmentation mask *z*1에 *T*를 적용해서 *x*의 Segmentation mask *T*(*z*1)을 얻게됩니다. 이렇게 되면 기존 *y*1의 정보 만으로 x의 마스크 정보를 얻을 수 있는 것입니다.


![img](/assets/img/2022/https%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252Ffcfc6a45-f6e1-472b-90b2-b58cf07a8256%252FUntitled.png)

VoxelMorph 방식도 이와 유사합니다. Moving 3D image인 m, Segmentation mask 정보인 Sm, Fixed 3D image인 f가 주어져 있습니다. 여기서 M**oving 3D image인 m을 Fixed 3D image인 f로 정합하는 Registration field 찾는 것**이 VoxelMorph를 이용한 Parcellation 방식의 핵심입니다. 이렇게 찾은 Registration field를 사용해서 m의 Segmentation mask 정보인 Sm을 Fixed 3D image f의 Segmentation mask로 변형시켜야 되기 때문입니다.

![img](/assets/img/2022/https%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252F320f9136-e8fd-42d6-a304-96dc2fc97e9e%252FUntitled.png)

즉, 위와 같이 파란색 박스의 정보를 얻게 되면 Moved Segmentation 정보를 Fixed 3D image f의 Segmentation Mask로 활용할 수 있게 됩니다.
