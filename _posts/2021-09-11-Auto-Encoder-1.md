---
layout: post
title: "1.오토인코더(AutoEncoder)"
subtitle : AutoEncoder-1
tags: [AutoEncoder]
categories: AutoEncoder
author: Kimin Park
comments : True
---

## 1. 오토인코더 란?

---

오토인코더(Auto Encoder)란 입력이 들어왔을 때, 해당 입력 데이터를 최대한 compression 시킨 후, compressed data를 다시 본래의 입력 형태로 복원 시키는 신경망입니다. 이때, 데이터를 압축하는 부분을 Encoder라고 하고, 복원하는 부분을 Decoder라고 부릅니다. 그리고 압축 과정에서 추출한 의미 있는 데이터 Z를 보통 'latent variable', 'latent vector', 'code', 'feature'등과 같은 용어로 부릅니다. 

<br>

<center><img src="/assets/img/2021-09-11/AutoEncoder-1/Untitled.png" width='700'></center>

<br>

## 2. 왜 이름이 오토인코더일까?

---

그렇다면, 왜 우리는 "Auto Encoder"라고 부르게 되었을까요? 그 이유는 다음의 Auto Encoder 출력을 예시로 설명 드리겠습니다. 

<br>

<center><img src="/assets/img/2021-09-11/AutoEncoder-1/Untitled%201.png" width='700'></center>

<br>

위의 그림을 자세히 보면 y축으로 두께 변하고, x축으로는 기울기가 변하는 것을 확인할 수 있습니다. 이를 통해 latent vector가 **두께,** **회전, Class**로 정의하고 있다는 것을 알 수 있습니다.  여기서 중요한 점은 Auto Encoder가 출력하는 latent vector를 미리 알 수 없다는 사실입니다. 우리는 단지 3차원으로 데이터를 압축하라는 명령을 내렸을 뿐, 이후에는 모델이 알아서 중요한 latent vector를 찾아 준 것입니다. 즉,  encoder 모델이 학습을 통해 자동적(automatically)으로 latent vector를 찾아준 것이죠. 그래서 우리는 고차원 데이터를 잘 표현해주는 latent vector를 자동으로 추출해주는 모델을 Auto-Encoder라 부릅니다.

Auto-Encoder에서 Decoder는 latent vector를 잘 찾기 위한 도우미 역할을 합니다. 다시 말해서 Auto-Encoder에서 Decoder는 거둘 뿐, Encoder에 초점이 맞춰져 있습니다. 우리의 목적은 의미 있는 latent vector를 찾는 것이니까요!

## 3. Auto Encoder의 다양한 관점

---

Auto Encoder는 다양한 관점에서 해석이 가능합니다. 다시 말해, 다양한 분야에서 사용될 수 있다는 뜻이죠. 일반적으로 4가지 관점이 있습니다. 이에 대해서 다음 글을 통해 하나씩 알아보도록 하겠습니다.

1. Unsupervised learning
2. Maximum Likelihood density estimation
3. Manifold learning
4. Generative model learning