오늘은 `주피터 노트북 테마`를 변경하고 `확장 기능`까지 사용할 수 있는 방법을 다뤄보겠습니다.

<br>

주피터 노트북의 기본 구성은 다음과 같습니다.

<br>

![flow](/assets/img/2020-08-06/pic0.png)

<br>

흰색 바탕에 가지런히 정리된 모습이 깔끔해 보이지만, 장시간 사용하면 눈에 피로가 오게 됩니다.

<br>

그리고 코드가 길어지면 스크롤 위아래로 움직이기도 번거로워집니다. 😢

<br>

그래서 저는 아래와 같이 `테마`와 `확장 기능`을 사용했습니다.

<br>

![flow](/assets/img/2020-08-06/pic4.png)

<br>

이번 포스팅에서 설명하는 방식대로 하시면, 금방 설정하실 수 있으실 것입니다.

<br>

## 테마 변경

---

<br>

먼저 `jupyterthemes`를 설치해주세요.

<br>

```bash
pip install jupyterthemes
```

<br>

`Jupyter Themes 모듈`은 다양한 테마를 지원하고 있습니다.

<br>

사용 가능한 테마 리스트를 간단히 설명해보았습니다.

<br>

- ***`chesterish**`
전체적으로 어두운 테마*
- ***`grade3`**
밝은 분위기의 테마*
- ***`gruvboxd`**
어두운 테마와 갈색 계열의 조합*
- ***`gruvboxl`**
노란 느낌의 테마*
- ***`monokai`**
개발자용 테마*
- ***`oceans16`**
파란 계열의 테마*
- ***`onedork`**
이것도 ****파란 계열의 테마*
- ***`solarizedd`**
초록 계열의 테마*
- ***`solarizedl`***

<br>

아래 코드와 같이 명령어를 입력할 경우 간편하게 테마를 변경할 수 있습니다.

<br>

📌 테마 이름 뒤에 `-T`를 붙이지 않으면 툴바가 없어집니다.

<br>

```bash
jt -l # 가능한 테마 리스트 출력

jt -t (테마 이름) -T

```

<br>

`테마가 변경이 안된다면` 주피터 노트북을 새로 실행시키면 됩니다!!

<br>

그리고 나중에 테마를 `기본`으로 설정하고 싶다면  아래 명령어를 실행하면 됩니다.

<br>

```bash
jt- r #default theme으로 복귀
```

<br>

## Tip. 추천 테마 4가지.

---

<br>


![flow](/assets/img/2020-08-06/pic1.png)
***oceans16 테마***

<br>

![flow](/assets/img/2020-08-06/pic2.png)
***grade3 테마***

<br>

![flow](/assets/img/2020-08-06/pic3.png)
***monokai 테마***

<br>

![flow](/assets/img/2020-08-06/pic4.png)
***onedork 테마***

<br>

## 주피터 확장 기능

---

<br>

우선 `확장 프로그램`을 설치해주세요.

<br>

### pip

`pip` 으로 설치를 하실 경우에는 아래 명령어를 실행합니다.

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

<br>

### conda

`conda`로 설치를 하는 경우에는 아래 명령어를 실행합니다.

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
```

<br>

## 확장 프로그램 설치하기

---

<br>

확장 프로그램을 설치하셨다면, 주피터 노트북을 실행시킵니다.

```bash
jupyter notebook
```

<br>

확장 기능 탭에 들어가는 방법은 `두 가지`입니다.

1. **링크로 들어가기.**

[http://localhost:8888/nbextensions](http://localhost:8888/nbextensions)

<br>

❗ local host의 주소에 따라 `링크의 주소`(8888)가 변경될 수 있습니다.

<br>

2. **파일의 Edit에서 들어가기**

![flow](/assets/img/2020-08-06/pic5.png)

<br>

위에서 `Edit`을 클릭해 줍니다.

<br>

![flow](/assets/img/2020-08-06/pic6.png)

<br>

그리고 `nbextensions config`를 누르시면 설정하는 곳으로 들어가게 됩니다.

<br>

확장 기능 탭에 들어가면 아래와 같은 화면을 보게 됩니다.

<br>

![flow](/assets/img/2020-08-06/pic7.png)

<br>

제가 활성화한 기능은 다음과 같습니다. 😃

<br>

- **`Table of Contents` (목차)**
- **`hinterland` (자동완성)**
- **`Variable Inspector` (변수 탐색기)**
- **`Codefolding` (코드 접기)**
- **`Collapsible Headings` (섹션 접기)**
- **`ExececuteTime` (코드 실행 시간)**

<br>

- `Table of Contents` (목차)

<br>

  ![flow](/assets/img/2020-08-06/pic8.png)

  <br>

    마크다운의 `Heading` 크기에 맞춰서 자동으로 `목차`가 생깁니다.

    목차를 클릭하면 해당 위치로 가주기 때문에 매우 편리한 기능입니다.

    <br>

- `hinterland` (자동완성)

<br>

![flow](/assets/img/2020-08-06/pic9.png)

<br>

    주피터 노트북은 다른 IDE와 다르게 `자동완성` 기능이 없습니다.

    하지만 이 확장 기능을 활성화 하면 탭을 누르지 않아도 코드를 `자동완성` 시켜줍니다.

    <br>

- **`Variable Inspector`** (변수 탐색기)

    ![flow](/assets/img/2020-08-06/pic10.png)

    <br>

`변수의 값`을 볼 수 있기 때문에 중간 중간 `디버깅 용도`로 좋을 것 같습니다.

<br>

- `Collapsible Headings` (섹션 접기)

<br>

    ![flow](/assets/img/2020-08-06/pic11.png)

    화살표 모양을 눌러서 `섹션`을 접으면 좀 더 깔끔하게 만들 수 있습니다.

    <br>

- `ExececuteTime` (코드 실행 시간)

  <br>


    ![flow](/assets/img/2020-08-06/pic12.png)

    <br>

    코드의 `실행시간`을 알려주는 기능입니다.

    <br>

    모델 학습할 때 시간 측정하기에 참 좋아보입니다.

    <br>

    이외에도 다양한 기능이 많습니다.

    <br>

    만약 더 유용한 기능을 찾게 된다면 이 포스트에 추가하겠습니다!
