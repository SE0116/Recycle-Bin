## 가상 요소

```html
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

<div class="clearfix">
  <code block>
</div>
```

- 가장 보편적으로 쓰이는 방법

## CSS Flexible Box Layout

### 요소

- Flex Container (부모 요소)
  - Flexbox 레이아웃을 형성하는 가장 기본적인 모델
  - 생성하려면 display 속성을 flex 혹은 inline-flex로 지정
- Flex item (자식 요소)
  - 컨테이너의 컨텐츠

### 축

- main axis (메인 축) < = 무조건 x축이 메인은 아니다! (default 값은 x축)
- cross axis (교차 축)



## Flex에 적용하는 속성

- 배치 방향 설정
  - flex-direction < = 메인 축 방향만 변경
- 메인축 방향 정렬
  - justify-content
- 교차축 방향 정렬
  - align-items, align-self, align-content
- 기타
  - flex-wrap, flex-flow, flex-grow, order

### content & items & self

- `content`  여러 줄
- `items`  한 줄
- `self`  flex item 개별 요소

## Grid system

- flexbox로 제작
- `container`    `rows`    `column` 으로 컨텐츠를 배치하고 정렬
- 12개의 `column` , 6개의 `grid breakpoints`
  - 12의 약수가 많아 여러 개를 배치하기에 용이함

### Grid system class

- `row`
- `gutters`  grid 시스템에서 반응적으로 공간 확보와 컨텐츠 정렬에 사용되는 column 사이의 padding
- `col` ,  `col-*`
- breakpoint

- `offset`  지정한 만큼의 column 공간을 무시하고 다음 공간부터 컨텐츠를 적용
