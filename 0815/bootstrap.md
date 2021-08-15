# 시작 전 붙여넣어야 하는 코드

## CSS

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
```

### JavaScript

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
```



## Customize

### Color

- `primary`    `dark`    `light`    `danger`    `warning`    `success`



## Layout

### Breakpoints

- `X-Small`  ( `xs` )  < 576px
- `Small`  ( `sm` )  >= 576px
- `Medium`  ( `md` )  >= 768px
- `Large`  ( `lg` )  >= 992px
- `Extra Large`  ( `xl` )  >= 1200px
- `Extra Extra Large`  ( `xxl` )  >= 1400px



### Container

- `.container`  뒤에 화면 크기에 따라 `-<breakpoint>`  추가



### Grid

- `container`  - >  `row`  - >  `col`
- 너비를 12칸으로 잘라 분할배분 가능
  - `col-6`    `col-lg-2`    `col-md-auto`



### Gutters

- `gx-5`
- `column`  사이의 간격 설정



## Content

### Typography

- `<h1>~<h6>`    `display-1 ~ display-6`

- 기존 h1~h6보다 더 큰 글씨를 원할 때 display 사용



### Images

```html
src="..." class="<img>"
```



### Tables



## Forms

### Overview

- `mb-3`    로그인 화면



## Components

### Alerts

```html
<div class="alert alert-..." role="alert">
```

- 주로 notice 용으로 사용



### Buttons

```html
<button type="button" class="btn btn-..."></button>
```





### Card

```html
<div class="card">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text">.</p>
    <a href="#" class="btn btn-..."></a>
  </div>
</div>
```

- 그림과 그에 대한 설명을 같이 표현



### Carousel

```html
<div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
```

- 여러 장의 그림 파일을 슬라이드 형식으로 출력

### Dropdowns

- 버튼 클릭 시 그에 맞는 하위 목록들이 나오게 설정 가능



### Modal

- 추가적인 팝업창을 띄우지 않고 기존 창에 레이어의 형태로 표현



### Navbar



### Pagination

- 보통 각 페이지 하단에 나오는 페이지 수 출력



## Helpers

### Position

- `fixed-top`    `fixed-bottom`    `sticky-top`    sticky-bottom은 없음