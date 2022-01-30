---
layout: post
title: "Medical Image Registration 알아보기"
subtitle : Medical Image
tags: [Registration]
categories: Registration
author: Pebpung
comments : True
typora-root-url: ../
use_math: true

---

> 이번 글에서는 Registration한 정의와 종류에 대해서 알아보도록 하겠습니다. 

이번 글은 박상현 교수님의 [딥러닝을 이용한 의료영상분석](https://www.edwith.org/medical-20200327/home) 강의를 참고하여 정리하였습니다. 



## 1. Registration 이란?

<img src="/assets/img/2022/jmrs417-fig-0001-m.jpg" alt="image1" style="zoom: 33%;" />

Registration은 다른 각도나 크기, 위치에 있는 두 영상을 매칭 시켜주는 영상 정합을 말합니다. 우선 두 영상 간의 매칭점을 찾아 주고, 매칭점을 바탕으로 Transformation Matrix를 예측해줍니다. 이렇게 예측된 Matrix는 영상을 변환시켜줄 때 사용됩니다. 

Registration은 Medical 분야에서 많이 사용이 됩니다. 전통적으로 Transformation matrix가 있습니다. Registration을 위한 matrix를 찾아서 변환을 시켜줍니다. 매칭점을 찾기 위해서 사용되는 방법은 iteration closest point(ICP)가 있습니다. 이 알고리즘은 자율주행을 위한 SLAM의 핵심 기술이기도 합니다. 여기서 Rigid , Affine  혹은 Non-Rigid 변환 중에서 상황에 따라 사용할 수 있습니다. 

보통 두 영상에서 움직이는 영상을 Moving, Source image라고 부르고, 고정된 영상은 Fixed, Target, Reference image라고 부릅니다. 또한 Registration이 완료된 이미지는 Moved, Result, Transformed image로 쓰여집니다. 

<br>

## 2. Registration을 사용하는 이유

Medical 분야에서 Registration을 사용하는 이유는 크게 세가지로 나눌 수 있습니다. 

1. 동일한 환자, 동일한 모달
2. 동일한 환자, 다른 모달
3. 다른 환자, 동일한 모달

동일한 환자, 동일한 모달의 경우 과거와 현재 영상을 비교하기 위해서 registration을 사용합니다. 시간의 흐름에 따라서 환자의 뇌 영상에 어떤 변화가 있는지 파악하고 싶지만, 위치와 크기가 다른 이미지는 비교가 힘들게 됩니다. 그렇기 때문에 registration을 사용해서 비교의 용이성을 가져오게 됩니다. 

![Axial view of T1, T1ce, T2 and Flair.](/assets/img/2022/Axial-view-of-T1-T1ce-T2-and-Flair.png)

동일한 환자, 다른 모달의 경우 좀 더 풍부한 정보를 얻기 위해서 registration을 사용합니다. 예를 들어 딥러닝으로 뇌의 병변을 파악하기 위해서는 동일한 타입의 영상이 아니라 다양한 타입의 영상을 같이 사용하는 것이 좋습니다. 위에서는 4개의 모달이 주어져있습니다. 하지만, 서로 다른 모달의 모양은 조금씩 다를 수 있습니다. 그렇기 때문에 모델의 입력으로 들어가기 전에 registration을 통해서 정합하는 과정이 필요합니다. 



<img src="/assets/img/2022/2020-11-09-segmentation-for-medical-image-6-atlas-based-methods-01.png" alt="Segmentation for MEDIA" style="zoom:48%;" />



다른 환자, 동일한 모달의 경우 label fusion을 위해서 registration을 사용합니다. Label fusion이란 기존에 존재하는 label(segmentation mask) 정보를 활용해서 label이 없는 새로운 영상에 label을 해주는 기법입니다. medical 이미지 처럼 큰 변화가 없는 영상에서 주로 사용 됩니다. Medical 이미지의 경우 annotation을 수행하려면 많은 비용이 들게 됩니다. 여기서 registration을 사용해서 자동으로 annotion을 수행하면 비용 절감 효과가 있습니다.  

<br>

## 3. Registration 종류

위에서 registration을 사용하는 이유에 대해서 알아봤습니다. registration의 종류는 생각보다 다양합니다. 이번 글에서는 대표적으로 사용되는 Rigid, Similarity, Affine, Non-rigid 방법에 대해서 알아보겠습니다. 

![Geometric transformation](/assets/img/2022/Geometric-transformation-functions-for-image-registration-Note-that-affine.png)

Rigid, Similarity, Affine Registration은 여러 Matrix의 조합으로 이루어져 있습니다. 위의 그림에서 보면 대표적으로 Translation, Rotation, Scaling, Shear가 보이게 됩니다. 이제 각 Matrix의 수식을 알아보고 조합을 통해서 registration을 설명드리겠습니다. 

<img src="/assets/img/2022/image-20220130172126420.png" alt="image-20220130172126420" style="zoom:33%;" />



x, y는 변경 전 이미지가 되고 x', y'은 변경 후 이미지가 됩니다. 각 수식을 그림과 매칭해서 보면 이해하기 편할 것입니다. 그리고 registration은 아래와 같이 구성이 되어 있습니다. 

- Rigid Registration: 이동 + 회전
- Similarity: 이동 + 회전 + 크기
- Affine: 이동 + 회전 + 크기 + 전단 

Affine이 가장 계산량이 많지만, 다양한 이미지에 대해서 유연하게 대응할 수 있습니다. 하지만 Affine Registration도 변환에 한계가 존재합니다. Rigid, Similarity, Affine 모두 linear transformation이므로 실제 환경의 왜곡된 정보를 표현할 수 없습니다. 그렇기 때문에 뒤틀려져 있는 정보를 정합할 수 있는 Non-Rigid Registration 혹은 Deformable Registration이라는 알고리즘을 사용해야됩니다. 다음 글에서는 Deformable Registration에 대해서 알아보고 CNN based Deformable Registration의 대표적인 논문인 **VoxelMorph: A Learning Framework for Deformable Medical Image Registration**에 대해서 알아보겠습니다. 





