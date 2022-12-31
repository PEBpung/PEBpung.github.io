---
layout: post
title: "Deep Anomaly Detection with Outlier Exposure"
subtitle : Anomaly Detection 파헤치기
tags: [AI]
categories: Anomaly Detection
author: Kimin Park
comments : True
typora-root-url: ../
use_math: true
---

> Deep Anomaly Detection with Outlier Exposure 논문을 읽고 정리한 포스트입니다. 

<br>

## Introduction

목적 : Auxiliary dataset(보조 데이터셋)을 활용하여 **OOD Detection 성능**을 높이자.

- Outlier Exposure을 기존의 OOD detection 방법들(MSP, BPP, GAN 등)에 독립적으로 추가
- 한 분야의 데이터만 이용하지 않고 이미지/ 텍스트 데이터 두 분야에 적용하여 두 분야 중에 어떤 데이터에 더 잘 적용하는지 알 수 있음.
- hyper-parameter에 민감하지 않다
- 모델 output의 calibration이 좋아진다. 
  - Calibration : 모델의 결과를 확률 값으로 보는 관점

**Heuristic?**

- 최고의 해답을 찾는 것이 아닌, 해결하기 어려운 문제에 대한 적당한 답을 찾는다는 컨셉.
-  Goal에 얼마나 가까워 질 수 있는지에 '대략적으로 추정할 수 있는' 정보 혹은 함수
- 이 논문에서는 Auxiliary dataset 사용해서 OOD를 대략적으로 추정하는 방법을 일컫는 것 같다.



## Related Work

**Out-of-Distribution Detection with Deep Networks.**

1. A baseline for detecting misclassified and out-of-distribution examples in neural networks, 2017.

   - **Maximum Softmax Probability (MSP)**

   - OOD detection이라는 task를 처음으로 정의하고 단순 soft-max 값을 OOD score로 사용하는 방식을 향후 연구의 baseline 모델로 제시함

   

2. Learning confidence for out-of-distribution detection in neural networks, 2018.

   - **Confidence Branch**.

   - 아래 그림과 같이 네트워크 구조와 loss function을 변형하여 모델이 confidence score(OOD score의 반대 개념)을 산출할 수 있도록 함

     ![image-20211204014147799](/assets/img/2021-10-10/image-20211204014147799.png)

3. Enhancing the reliability of out-of-distribution image detection in neural networks, 2018.

   - **Enhancing out-of-distribution detector.**

   - in-distribution examples에는 out-of-distribution examples 보다 더 높은 softmax score를 줘서 정확하게 분류 방법을 제안함

   

4. Training confidence-calibrated classifiers for detecting out-of-distribution samples, 2018

   - **Synthetic Outliers.**

   - GAN을 이용하여 out of distribution 데이터를 인공적으로 생성한 후 이를 활용하여 모델 을 재학습하여 OOD를 탐지하는 방식을 제안함







## Outlier Exposure

- 해당 sample이 "in-distribution"인 D_in인지 아니면, "out-distribution"인 D_out인지 분류하는 task이다.

- 실제 환경에서는 outliers의 distribution을 아는 것은 어렵다.

- 그러므로 우리는 unknown인 D_out의 현실적인 setting을 해줄 필요가 있다. 

  - OOD detector와 Outlier Exposure (OE) dataset 
    $$
    D_{out}^{OE}
    $$

  - OE dataset과 disjoint된 dataset 준비
    $$
    D_{out}^{test}
    $$

- 모델을 학습 시키고  sample이 D_in인지 D_out_OE 인지 검출하는 heuristics을 배운다.

- 이러한 heuristics이 unseen distribution인 D_out으로 일반화된다는 것을 발견했다.



- Deep parametrized anomaly detectors는 일반적으로 auxiliary task로 부터 representation을 학습한다. 
- 다음 수식에서 원래 learning objective L이 주어지면, Outlier Exposure objective를 최소화하는 것으로 식을 세울 수 있다. 

<img src="/assets/img/2021-10-10/image-20211203234656371.png" alt="image-20211203234656371" style="zoom: 50%;" />



- Outlier Exposure은 다양한 type의 data와 task에 적용될 수 있다. 

- 그렇기 때문에 L_OE는 특정한 공식으로 선택될 수 있고, task와 OOD detector에 종속적이다. 

  - 예를 들어, maximum softmax probability(MSP) baseline detector는 L_OE를 uniform distribution과 f(x')의 cross-entropy로 구성한다. 

    <img src="/assets/img/2021-10-10/image-20211204005819974.png" alt="image-20211204005819974" style="zoom: 80%;" />

  - original objective L이 density estimation 이고 labels을 사용할 수 없다면, L_OE는 margin ranking loss를 사용한다. 






## Experimental 



### Dataset

[Din]: SVHN, CIFAR-10&100, Tiny ImageNet, Places365, 20Newsgroups, TREC, SST 

- in-distribution에서 만들어진 sample들

[Dout−oe]: 80 Million Tiny Images, ImageNet-22K, WikiText-2 

- out-distribution, 즉 OOD에서 나오는 sample들 중에서 **Din과 같이 training에 사용되는 sample들**

[Dout−test]: SVHN, CIFAR-10&100, Tiny ImageNet, Places365, 20Newsgroups, TREC, SST

- out-distribution, 즉 OOD에서 나오는 sample들 중에서 **test에서만 사용되는 sample들**

Dout−oe, Dout−test 이 두개의 데이터 셋은 **겹치면 안되므로(disjoint) 겹치는 데이터의 경우 다 제거**해주었다고 한다.

![image-20211204023405443](/assets/img/2021-10-10/image-20211204023405443.png)

### 성능지표

**1. FPRN(False Positive Rate at N% True Positive Rate)**

- Maximum softmax probability threshold가 특정 값으로 정해져 있을 때의 OOD detector 성능
- N%의 OOD sample이 감지 되어야 한다고 가정하고 Threshold를 지정한다. 그 threshold로 FPR을 계산

**2. AUROC**

- Threshold 값을 다르게 할 때 각각의 OOD detector의 성능을 표현

**3. AUPR**

- OOD와 in-distribution 간의 imbalance가 있을 때 유용



### **Maximum Softmax Probability (MSP)**

- MSP의 경우 Dout−oe데이터의 정답 label을 uniform 분포로 하여 classifier를 학습한 후 진행함.

<img src="/assets/img/2021-10-10/image-20211203234656371.png" alt="image-20211203234656371" style="zoom: 50%;" />

![image-20211204022542242](/assets/img/2021-10-10/image-20211204022542242.png)

**실험결과**

![image-20211204022806086](/assets/img/2021-10-10/image-20211204022806086.png)

- 기존의 MSP 보다 모든 데이터셋의 3가지 지표에 대해 성능이 높게 나옴

### **Confidence Branch**

- Confidence branch 방법론의 경우 Dout−oe 데이터에 대해서 p는 학습하지 않고 c만 다음과 같은 loss를 추가하 여 학습함



**실험결과**

![image-20211204022829898](/assets/img/2021-10-10/image-20211204022829898.png)

- MSP에 Branch를 추가 한 것 보다 모든 데이터셋의 3가지 지표에 대한 성능이 높게 나옴.



### **Synthetic Outliers**

- 이 경우는 MSP의 GAN 이미지를 추가한 경우이므로 단순하게 Dout−oe를 또 새롭게 추가하여 학습을 진행함



**실험결과**

![image-20211204022900553](/assets/img/2021-10-10/image-20211204022900553.png)

- MSP에 GAN을 추가한 것 보다 모든 데이터셋의 3가지 지표에 대한 성능이 높게 나옴.





## Discussion

**Choosing Dout_oe**



![image-20211204024532243](/assets/img/2021-10-10/image-20211204024532243.png)

## Conclusion

- . 본 논문에서는 다양한 setting을 통해 OOD detector를 향상시키는 간단한 기술인 Outlier Exposure을 소개했다.
- out-of-distribution sample을 사용하여 new, unmodeled, OOD example의 network heuristics을 학습한다. 
- 이 방법은 large scale image task나 자연어 처리에 광범위하게 적용 가능하다.
- OE는 몇가지 이전의 anomaly detection techniques 또한 개선할 수 있다.
- 마지막으로,  Outlier Exposure은 계산적으로 effective하고 out-of-distribution detection systems을 개선하기 위한 효과적인 방법이다.