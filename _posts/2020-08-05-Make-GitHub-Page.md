---
layout: post
title: "GitHub 블로그 시작하기 (GitHub Page, Jekyll)"
subtitle : How to start the blog in GitHub
tags: [Ubuntu, GitHub, Theme, blog]
author: Kimin Park
comments : True
---

깃헙에는 .github.io라는 독특한 주소를 가지고 있는 블로그가 있습니다.

<br>

저장 공간도 무료로 제공되고, 도메인 연결도 편리하게 할 수 있지만, 가장 마음에 드는 점은 깃헙의 생태계입니다.

<br>

GitHub은 개발자들이 많이 애용하는 플랫폼이므로 GitHub 블로그는 특히 개발 블로그 용으로 인기가 높다고 합니다.

<br>

하지만 이런 매력적인 특징에도 불구하고 `설치과정이 번거롭다`는 단점이 있습니다.

<br>

그래서 이번에는 `GitHub 블로그를 만드는 방법` 을 공유하고자 합니다.

<br>

## 1. 새 저장소 (repository) 만들기

---

우선 먼저 해야될 작업은 GitHub에서 ``새 저장소(repository)``를 만드는 것입니다.

<br>

 이 때 저장소의 이름을 자신의 username 뒤에 `.github.io`가 붙은 이름으로 짓습니다.

 <br>

이렇게 해야 `본인이름.github.io`의 도메인으로 접속할 수 있는 블로그가 만들어지게 됩니다.

<br>

![flow](/assets/img/2020-08-05/git1.png)

<br>

## 2. jekyll과 bundler 설치

---

```bash
sudo gem install jekyll bundler
```

<br>

위의 명령어를 통해 `jekyll와 bundler` 를 설치합니다.

<br>

저는  jekyll은 4.1.1, Bundler은 2.1.4 버전이 설치되었습니다.

<br>

![flow](/assets/img/2020-08-05/git2.png)

<br>

## 3. GitHub page와 연동

---

<br>

`본인의 Repository`를 원하는 폴더로 가져옵니다.

<br>

여기서는 git clone을 사용해서 복제하겠습니다.

<br>

```bash
git clone https://github.com/PEBmin/pebmin.github.io.git
```

<br>

그리고 clone 한 폴더에 들어갑니다.

<br>

```bash
cd pebmin.github.io.git
```

<br>

## 4. 마음에 드는 테마를 고릅시다.

---

<br>

Jekyll은 고맙게도 사용자들이 다양한 테마를 미리 만들고 공유하고 있습니다.

<br>

아래의 주소로 가시면 다양한 디자인을 다운받을 수 있습니다.

<br>

[http://jekyllthemes.org/](http://jekyllthemes.org/)

[http://themes.jekyllrc.org/](http://themes.jekyllrc.org/)

[https://jekyllthemes.io/](https://jekyllthemes.io/)

<br>

원하시는 테마를 zip파일로 다운받으시면 됩니다.

<br>

이번 포스팅에서는 `minimal mistakes` 테마를 다운받고 설치했습니다.

<br>

아래 주소로 가시면 release 된 버전을 다운받으실 수 있습니다.
<br>

[https://github.com/mmistakes/minimal-mistakes/releases](https://github.com/mmistakes/minimal-mistakes/releases)



## 5. **불필요한 파일 삭제**

---

<br>

다운받은 폴더의 내용을 프로젝트 폴더에 옮깁니다.

<br>

이 과정에서  ``불필요한 파일을 삭제``하도록 합니다.

<br>

**삭제할 파일 리스트**

<br>

- .editorconfig
- .gitattributes
- .github
- /docs
- /test
- CHANGELOG.md
- minimal-mistakes-jekyll.gemspec
- README.md
- screenshot-layouts.png
- screenshot.png

<br>

#### **_posts, _draft 폴더 생성**

<br>

그리고 _posts와 _draft 폴더가 없다면 생성하도록 합니다. (최상위 경로)
<br>
- _drafts : 포스트 초안이 담기는 곳입니다. 배포되지 않고 테스트 환경에서 보기가 가능합니다.
- _posts : 배포될 포스트들이 담기는 곳입니다.

<br>

## 6. 설치 명령어

---

<br>

우선 폴더 안에 있는 Gemfile을 수정해줍니다.

```
source "https://rubygems.org"

gem "jekyll", "~> 3.5"
gem "minimal-mistakes-jekyll"
```

<br>

수정이 완료되었으면 bundle을 수행합니다.

```bash
bundle
```

<br>

아래와 같이 새로운 파일이 생긴 모습을 볼 수 있습니다.

<br>

![flow](/assets/img/2020-08-05/git3.png)

<br>

## 7. 배포 및 PUSH

---

아래 명령어를  이용해서 만든 사이트가 잘 동작이 되는 지 봅시다.
```bash
bundle exec jekyll serve
```

<br>

명령어를 실행시키면  실행 로그가 보일 것입니다.

<br>

그중에서 http://127.0.0.1:4000를 클릭하거나 주소창에 검색해서 들어갑니다.

<br>

![flow](/assets/img/2020-08-05/git4.png)

<br>

이제 마지막으로 git comit, push 를 통해 자신의 github page에 올립니다.


<br>

```bash
git add .
git commit -m 'Apply theme'
git push origin master
```

<br>

조금 기다린 뒤 테마가 제대로 적용 됐는지 확인하기 위해 자신의 주소를 검색해봅니다.

https://본인아이디.github.io/
