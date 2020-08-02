---
layout: post
title: Ubuntu 18.04 테마 변경하기
subtitle : How Ubuntu theme is changed as Adapta
tags: [Ubuntu, Theme]
author: Kimin Park
comments : True
---


이번 글은 `우분투의 테마`를 변경하는 방법입니다!

우분투 18.04의 기본테마는 다음과 같습니다.

![smile](/assets/img/2020-08-01/pic1.png)

빨간 테마도 이쁘지만 뭘가 좀 부담스럽다는 생각이 들었습니다.

그래서 테마를 바꿔보기로 했습니다 😀

글에서 나와있는 대로 차근차근 하시면 다음과 같은 테마를 만들 수 있습니다.

![smile](/assets/img/2020-08-01/pic2.png)

맥 OS 처럼 깔끔한 디자인이 마음에 듭니다.

화면 크기도 왠지 더 넓어 보이는 효과가 있습니다.

## 1. 그놈 기능 개선(gnome-tweak-tool) 설치하기

---

우분투의 데스크탑 환경은 기본적으로 `그놈(GNOME)`이 사용되고 있다고 합니다.

터미널 창을 열어 다음과 같은 명령어를 작성합니다.

```bash
sudo apt-get install gnome-tweak-tool
```

어플리케이션에 `Tweaks`가 설치된 모습을 볼 수 있습니다.

![smile](/assets/img/2020-08-01/pic3.png)

눌러보시면 다양한 설정이 가능한 것을 알 수 있습니다.

## 2. Adapta 테마 설치하기

---

다음은 `Adapta`  테마를 설치 할 것입니다.

Adapta 테마는 기존 테마 중 가장 `Material`한 디자인이라고 합니다.

Material한 디자인이란?  픽셀을 종이 질감 처럼!

![smile](/assets/img/2020-08-01/pic4.png)

(출처: [adapta-gtk-theme Github](https://github.com/adapta-project/adapta-gtk-theme))

```bash
# 1. 저장소 추가
sudo add-apt-repository ppa:tista/adapta
# 2. 저장소 업데이트
sudo apt-get update
# 3. Adapta 테마 설치
sudo apt-get install adapta-gtk-theme
```

설치는 금방 되실 겁니다.

아까 설치했던 `Tweaks` 를 다시 실행시켜 주세요.

(이미 켜져있던 분들은 다시 창을 닫았다 켜주시길 바랍니다.)

![smile](/assets/img/2020-08-01/pic5.png)

테마를 적용하기 전에는 위와 같은 화면입니다.

![smile](/assets/img/2020-08-01/pic6.png)

`Adapta` 테마를 적용하니 더욱 깔끔해 보입니다.

![smile](/assets/img/2020-08-01/pic7.png)

하지만 위의 화살표가 가리키는 **상단바**는 적용한 테마와 달라서 이질감이 듭니다.

## 3. User Themes 설치하기

---

그래서 우리는 쉘(상단바) 또한 `Adapta` 테마로 바꿔줄 것입니다.

우선 어플리케이션에서 **Ubuntu Software**에 들어갑니다.

![smile](/assets/img/2020-08-01/pic8.png)

**User themes**라고 검색하면 설치할 수 있는 아이콘이 뜹니다.

~~오전에는 서버가 먹통인지 설치가 안되는 경우가 있어라고요.~~

![smile](/assets/img/2020-08-01/pic9.png)

설치가 완료되면 **그놈 개선 도구 (Tweaks)**를 실행시켜 주세요!

![smile](/assets/img/2020-08-01/pic10.png)

이번에도 창을 껐다가 다시 켜야됩니다.

(아니면 아래처럼 ❗가 뜹니다.)

![smile](/assets/img/2020-08-01/pic11.png)

이제 쉘에서 ❗가 사라지고 테마를 고를 수 있습니다.

![smile](/assets/img/2020-08-01/pic12.png)

추가적으로 상태바와 아이콘을 설정해주겠습니다.

이제 거의 완성입니다!

## 4. Dash to Dock 설치하기

---

아까와 똑같이 어플리케이션에서 **Ubuntu Software**에 ****들어갑니다.

그리고 Dash to Dock을 검색해서 설치해 줍니다.

![smile](/assets/img/2020-08-01/pic13.png)

그리고 Dash to Dock의 확장자를 활성화 시켜줍니다.

![smile](/assets/img/2020-08-01/pic14.png)

## 5. 사용자 맞춤 설정하기

---


설치된 확장자는 직접 들어가서 설정을 바꿀 수 있습니다.

우선 `톱니바퀴 모양`을 눌러줍니다.

![smile](/assets/img/2020-08-01/pic15.png)

빨간 동그라미에서 **상태바의 위치와 아이콘의 크기**를 변경해줍니다.

<img src="/assets/img/2020-08-01/pic16.png" width="400"></center>

- Position and size 설정 방법
    1. **상태바 위치 변경**
    2. **상태바 숨기기**
    3. **아이콘 사이즈 조절**

설정하시면 됩니다.

다음은 상태바를 설정할 것입니다.

상단에서 Appearance로 들어가 주세요.

<img src="/assets/img/2020-08-01/pic17.png" width="400"></center>


- Appearance 설정 방법
    1. **맨 위에 체크되어 있는 것을 해제 하세요.**
    2. **사용중인 창의 갯수를 나타내는 모양입니다. 저는 Dots를 사용합니다.**
    3. **Default를 Fixed로 바꿔주시고, 원하시는 만큼 불투명도를 낮춰줍니다.**

## 이렇게 하면 우분투 테마 설정이 완료됩니다!!
