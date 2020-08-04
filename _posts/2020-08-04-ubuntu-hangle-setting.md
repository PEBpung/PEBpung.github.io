---
layout: post
title: "Ubuntu에서 한/영 키 사용하는 방법!"
subtitle : How to change the Hangle key in Ubuntu
tags: [Ubuntu, Hangle, Setting]
author: Kimin Park
comments : True
---

안녕하세요!

<br>

이번 포스트는 우분투에서 한글키 사용하는 방법에 대한 내용입니다!

<br>

우분투에서의 기본  Input 변경 키는 Shift+Space 인데요.

<br>

두 가지 키를 동시에 사용하는 건 꽤 귀찮은 일입니다.

<br>

기존 사용자들은 괜찮지만, 한글에 익숙한 저는 매번 번거로웠습니다. ㅠㅠ

<br>


그래서 우분투에서 한글키를 사용하는 방법을 찾아서 설정했습니다.

<br>

## 1. 그놈 기능 개선(gnome-tweak-tool) 설치하기

---

우분투의 데스크탑 환경은 기본적으로 `그놈(GNOME)`이 사용되고 있다고 합니다.

<br>

터미널 창을 열어 다음과 같은 명령어를 작성합니다.

<br>

```bash
sudo apt-get install gnome-tweak-tool
```
<br>

어플리케이션에 `Tweaks`가 설치된 모습을 볼 수 있습니다.

<br>

![flow](/assets/img/2020-08-04/hangle0.png)

## 2. 기능 개선에서 Layout Options 설정하기

---

설치한 `Tweaks` 를  실행시켜 주세요.

<br>

**Keboad & Mouse**를 들어가면 **Additional Layout Options**을 설정하는 버튼이 보이실 것 입니다.

<br>

![flow](/assets/img/2020-08-04/hangle1.png)

<br>

옵션에 들어간 뒤, **Switching to another layout**에서 **Right Alt** 를 체크하면 됩니다.

<br>

우분투가 한글로 설정되어 있다면 tweaks가 **기능 개선** 으로 번역되고
Additional layout options는 **다른키 배치로 전환** 으로 번역되어있습니다!

<br>

![flow](/assets/img/2020-08-04/hangle2.png)

<br>

Tweaks의 설정은 여기까지 입니다.

<br>

그리고 이젠 Tweaks(기능 개선)이 아닌
 **Setting(설정)** 에서 영문을 추가하셔야 됩니다.

<br>

## 3. Setting에서 Input Sources 추가하기

---
<br>

Setting에서 **Region & Languge**를 선택합니다.

<br>

그리고 **+** 버튼을 눌러서 언어를 추가하는 창을 열어줍시다.

<br>

![flow](/assets/img/2020-08-04/hangle3.png)

그런 다음 **English(US)** 를 선택하시면 됩니다.

<br>

(한국어 버전에서는 "영어(미국)" 으로 되어 있을 것 입니다.)

<br>

![flow](/assets/img/2020-08-04/hangle4.png)

<br>

그리고 아래와 같이 **Start in Hangul mode**를 설정해줍신다.

<br>

혹시 Toggle키에 **Art+R** 또는 **Hangle** 버튼이 설정되어 있으면
 **Remove**를 눌러서 없애줍니다!

<br>

![flow](/assets/img/2020-08-04/hangle5.png)

<br>

## 4. 완성

---

<br>

우측 상단에 한글 혹은 en을 클릭하시고, **한/영** 버튼을 누르시면 바뀌는 모습을 볼 수 있습니다. 😃

<br>

![flow](/assets/img/2020-08-04/hangle6.png)   ![flow](/assets/img/2020-08-04/hangle7.png)
