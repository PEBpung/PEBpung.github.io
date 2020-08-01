이번 글은 `우분투의 테마`를 변경하는 방법입니다!

우분투 18.04의 기본테마는 다음과 같습니다.

![smile](/assets/img/2020-08-01/pic1.png)
![smile](/assets/smile.png)

빨간 테마도 이쁘지만 뭘가 좀 부담스럽다는 생각이 들었습니다.

그래서 테마를 바꿔보기로 했습니다 😀

글에서 나와있는 대로 차근차근 하시면 다음과 같은 테마를 만들 수 있습니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0f707f4e-dffb-4196-a79f-c72ea41a2170/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0f707f4e-dffb-4196-a79f-c72ea41a2170/Untitled.png)

맥 OS 처럼 깔끔한 디자인이 마음에 듭니다.

그리고 화면도 왠지 더 넓어 보입니다.

## 1. 그놈 기능 개선(gnome-tweak-tool) 설치하기

---

우분투의 데스크탑 환경은 기본적으로 `그놈(GNOME)`이 사용되고 있다고 합니다.

터미널 창을 열어 다음과 같은 명령어를 작성합니다.

```bash
sudo apt-get install gnome-tweak-tool
```

어플리케이션에 `Tweaks`가 설치된 모습을 볼 수 있습니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97027b90-c67d-438f-b96a-a683687f5238/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97027b90-c67d-438f-b96a-a683687f5238/Untitled.png)

눌러보시면 다양한 설정이 가능한 것을 알 수 있습니다.

## 2. Adapta 테마 설치하기

---

다음은 `Adapta`  테마를 설치 할 것입니다.

Adapta 테마는 기존 테마 중 가장 `Material`한 디자인이라고 합니다.

Material한 디자인이란?  픽셀을 종이 질감 처럼!

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/755fa6c8-8ce3-49f4-8c30-60f2d4540acb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/755fa6c8-8ce3-49f4-8c30-60f2d4540acb/Untitled.png)

(출처: [https://github.com/adapta-project/adapta-gtk-theme](https://github.com/adapta-project/adapta-gtk-theme))

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

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1bbc8c9-7e5d-4d4f-a8e0-e22645c589e9/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1bbc8c9-7e5d-4d4f-a8e0-e22645c589e9/Untitled.png)

테마를 적용하기 전에는 위와 같은 화면입니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28531c43-3c8e-46fb-88a4-8c9374e6b282/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28531c43-3c8e-46fb-88a4-8c9374e6b282/Untitled.png)

`Adapta` 테마를 적용하니 더욱 깔끔해 보입니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf9148ed-3fd2-48bd-b8a9-80539a94f2ac/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf9148ed-3fd2-48bd-b8a9-80539a94f2ac/Untitled.png)

하지만 위의 화살표가 가리키는 **상단바**는 적용한 테마와 달라서 이질감이 듭니다.

## 3. User Themes 설치하기

---

그래서 우리는 쉘(상단바) 또한 `Adapta` 테마로 바꿔줄 것입니다.

우선 어플리케이션에서 **Ubuntu Software**에 ****들어갑니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d07901f2-ab48-46ff-86b6-65c1be8e6e73/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d07901f2-ab48-46ff-86b6-65c1be8e6e73/Untitled.png)

**User themes**라고 검색하면 설치할 수 있는 아이콘이 뜹니다.

~~오전에는 서버가 먹통인지 설치가 안되는 경우가 있어라고요.~~

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/359bb84f-f4b8-4d8c-92c2-c84d4ac0dc00/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/359bb84f-f4b8-4d8c-92c2-c84d4ac0dc00/Untitled.png)

설치가 완료되면 **그놈 개선 도구 (Tweaks)**를 실행시켜 주세요!

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/819b73d5-bf4d-46fe-8889-711d0ebc60d1/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/819b73d5-bf4d-46fe-8889-711d0ebc60d1/Untitled.png)

이번에도 창을 껐다가 다시 켜야됩니다.

(아니면 아래처럼 ❗가 뜹니다.)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8aac16cf-6506-4da4-a83c-bc7619db5bcc/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8aac16cf-6506-4da4-a83c-bc7619db5bcc/Untitled.png)

이제 쉘에서 ❗가 사라지고 테마를 고를 수 있습니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f11e5cb9-5046-4a67-8b69-565ea24fcd16/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f11e5cb9-5046-4a67-8b69-565ea24fcd16/Untitled.png)

추가적으로 상태바와 아이콘을 설정해주겠습니다.

이제 거의 완성입니다!

## 4. Dash to Dock 설치하기

---

아까와 똑같이 어플리케이션에서 **Ubuntu Software**에 ****들어갑니다.

그리고 Dash to Dock을 검색해서 설치해 줍니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9094075f-7593-4821-9968-8771f0eb3e72/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9094075f-7593-4821-9968-8771f0eb3e72/Untitled.png)

그리고 Dash to Dock의 확장자를 활성화 시켜줍니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fe01111-fc20-40ce-868a-17f061ae7c23/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fe01111-fc20-40ce-868a-17f061ae7c23/Untitled.png)

## 5. 사용자 맞춤 설정하기

---

설치된 확장자는 직접 들어가서 설정을 바꿀 수 있습니다.

우선 `톱니바퀴 모양`을 눌러줍니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db88e2a4-5dc6-42ae-bce4-885c14ac9bcf/picture1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db88e2a4-5dc6-42ae-bce4-885c14ac9bcf/picture1.png)

빨간 동그라미에서 **상태바의 위치와 아이콘의 크기**를 변경해줍니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc84301a-0b7e-4c25-ac47-54b4abb2bf1a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc84301a-0b7e-4c25-ac47-54b4abb2bf1a/Untitled.png)

- Position and size 설정 방법
    1. **상태바 위치 변경**
    2. **상태바 숨기기**
    3. **아이콘 사이즈 조절**

설정하시면 됩니다.

다음은 상태바를 설정할 것입니다.

상단에서 Appearance로 들어가 주세요.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edd57b0c-297f-4d69-93ff-74511922a310/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/edd57b0c-297f-4d69-93ff-74511922a310/Untitled.png)

- Appearance 설정 방법
    1. **맨 위에 체크되어 있는 것을 해제 하세요.**
    2. **사용중인 창의 갯수를 나타내는 모양입니다. 저는 Dots를 사용합니다.**
    3. **Default를 Fixed로 바꿔주시고, 원하시는 만큼 불투명도를 낮춰줍니다.**

## 이렇게 하면 우분투 테마 설정이 완료됩니다!!
