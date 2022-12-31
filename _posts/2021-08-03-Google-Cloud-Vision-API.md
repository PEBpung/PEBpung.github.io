---
layout: post
title: "Google Cloud Vision API 사용하기"
subtitle : Cloud Vision API
tags: [AI]
categories: API
author: Kimin Park
comments : True
---

<br>

[https://console.cloud.google.com/](https://console.cloud.google.com/) 에 접속합니다.

<br>

## 1. Cloud Vision API 실행시키기

<br>

<center><img src="/assets/img/2021-08-03/Untitled.png" width='700'></center>

<br>

"cloud vision" 으로 검색을 하여 "Cloud Vision API"를 클릭합니다.

<br>

<center><img src="/assets/img/2021-08-03/Untitled 1.png" width='700'></center>

<br>

위와 같은 그림에서 파란색 박스인 사용 버튼을 클릭합니다. 

<br>

## 2. 사용자 인증 정보 만들기

<br>

<center><img src="/assets/img/2021-08-03/Untitled 2.png" width='700'></center>

<br>

상단에 **사용자 인증 정보 만들기**를 클릭합니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled_(21).png" width='700'></center>

<br>

그럼 사용자 인증 정보 유형을 입력하는 칸이 나옵니다. 

여기서 저희는 Vision API를 사용할 예정이기 때문에 Cloud Vision API를 선택합니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled 3.png" width='700'></center>

<br>

추가로 어떤 데이터를 사용할 지 선택하는 칸이 나옵니다. 

다음과 같은 순서로 진행합니다. 

<br>

1. 애플리케이션 데이터를 선택합니다.
2. "아니요, 사용하지 않습니다."를 선택합니다.

<br>

<center><img src="/assets/img/2021-08-03/Untitled 4.png" width='700'></center>

<br>

서비스 계정 이름은 자신이 사용하고 싶은 이름으로 지정하시면 됩니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled 5.png" width='700'></center>

<br>

(선택사항)은 따로 설정을 하지 않아도 돼서 완료 버튼을 눌러줍니다. 

<br>

## 3. Json 파일 만들기

저희는 Application에서 API를 사용해야 되기 때문에 json 파일을 만들어야 합니다. 

그래서 사용자 인증 정보에 있는 서비스 계정의 Keys를 만드는 과정을 진행해야 됩니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled_(20).png" width='700'></center>

<br>

서비스 계정에서 서비스 계정 관리를 클릭합니다.

<br>

<center><img src="/assets/img/2021-08-03/Untitled 6.png" width='700'></center>

<br>

점 세 개를 눌러서 **키 관리**를 선택합니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled 7.png" width='700'></center>

<br>

키 추가를 누르면 **새 키 만들기**라는 선택지가 나오게 됩니다.

<br>

<center><img src="/assets/img/2021-08-03/Untitled 8.png" width='700'></center>

<br>

여기서 Json 파일을 만들면 xxxx.json 파일이 생성 됩니다!!

<br>

## 4. 사용하기

<br>

<center><img src="/assets/img/2021-08-03/Untitled 9.png" width='700'></center>

<br>

다음과 같은 에러가 발생합니다. 

PermissionDenied: 403 This API method requires billing to be enabled.

오류 로그를 자세히 보시면 링크가 있습니다. 

해당 링크로 들어갑니다. 

<br>

<center><img src="/assets/img/2021-08-03/Untitled 10.png" width='700'></center>

<br>

그럼 위와 같이 프로젝트의 결제 사용 설정 팝업이 뜨게 됩니다. 

API를 사용하기 위해 결제 계정을 만들면 됩니다. 

이름, 주소, 카드 번호까지 적으면 90일 동안 무료 크래딧을 받으실 수 있습니다.

이렇게 모두 완료되었으면 API를 사용할 수 있습니다.