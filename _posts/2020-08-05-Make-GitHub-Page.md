# GitHub 블로그 시작하기 (GitHub Page, Jekyll)

.github.io라는 독특한 주소를 가지고 있는 GiHub 블로그를 만들어보았습니다. 

</br>

GitHub 블로그는 특히 개발 블로그 용으로 인기가 높다고 합니다.

## 1. 새 저장소 (repository) 만들기

---

GitHub에서 새 저장소(repository)를 만듭니다.

 이 때 저장소의 이름을 자신의 username 뒤에 .github.io가 붙은 이름으로 짓습니다. 

이렇게 해야 `본인이름.github.io`의 도메인으로 접속할 수 있는 블로그가 됩니다.

![GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/git1.png](GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/git1.png)

## 2. jekyll과 bundler 설치

---

```bash
sudo gem install jekyll bundler
```

위의 명령어를 통해 jekyll와 bundler를 설치합니다.

저는  jekyll은 4.1.1, Bundler은 2.1.4 버전이 설치되었습니다.

![GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/git2.png](GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/git2.png)

## 3. GitHub page와 연동

---

자신의 Repository를 원하는 폴더로 가져옵니다.

```bash
git clone https://github.com/PEBmin/pebmin.github.io.git
```

그리고 clone 한 폴더에 들어갑니다.

```bash
cd pebmin.github.io.git
```

## 4. 마음에 드는 테마를 고릅시다.

---

Jekyll은 고맙게도 사용자들이 다양한 테마를 미리 만들고 공유하고 있습니다.

아래의 주소로 가시면 다양한 디자인을 다운받을 수 있습니다.

[http://jekyllthemes.org/](http://jekyllthemes.org/)

[http://themes.jekyllrc.org/](http://themes.jekyllrc.org/)

[https://jekyllthemes.io/](https://jekyllthemes.io/)

원하시는 테마를 zip파일로 다운받으시면 됩니다.

이번 포스팅에서는 minimal mistakes 테마를 다운받고 설치했습니다.

[https://github.com/mmistakes/minimal-mistakes/releases](https://github.com/mmistakes/minimal-mistakes/releases)

다운받은 폴더의 내용을 프로젝트 폴더에 옮깁니다.

이 과정에서 아래를 참조해 불필요한 파일을 삭제하도록 합니.

## 5. **불필요한 파일 삭제**

---

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

## 7. **_posts, _draft 폴더 생성**

---

그리고 _posts와 _draft 폴더가 없다면 생성하도록 한다. (최상위 경로)

- _drafts : 포스트 초안이 담기는 곳이다. 배포되지 않고 테스트 환경에서 보기가 가능하다.
- _posts : 배포될 포스트들이 담기는 곳.

## 6. 설치 명령어

---

- Gemfile 수정

```
source "https://rubygems.org"

gem "jekyll", "~> 3.5"
gem "minimal-mistakes-jekyll"
```

- bundle을 수행합니다.

```bash
bundle
```

### 아래와 같이 새로운 파일이 생겼습니다.

![GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/Untitled.png](GitHub%20%E1%84%87%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%20%E1%84%89%E1%85%B5%E1%84%8C%E1%85%A1%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20(GitHub%20Page,%20Jekyll)%20bd80d272a7bd4a59912bc903b7dd5f15/Untitled.png)

### 테스트, 배포

```bash
bundle exec jekyll serve
```

### 다음으로 git comit, push 를 통해 자신의 github page에 올린다.

```bash
git add .
git commit -m 'Apply theme'
git push origin master
```

### 자신의 주소를 검색해본다.

https://본인아이디.github.io/