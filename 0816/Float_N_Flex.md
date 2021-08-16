## Float

- 이미지의 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입
- 기본값은 none - > left, right로 원하는 위치에 띄울 수 있음
- 이미지 내의 글씨의 경우 화면에 표출되는 공간을 기준으로 정렬됨



## Flex

- `container`    `item` 으로 구성

### d-flex

- class명에 선언함으로 flex를 사용



### flex-direction

- 배치 방향 설정 (메인축이 무조건 x축은 아님)
- row, column, reverse



### justify (메인 축 정렬)

- justify-content (여러 줄)



### align (교차 축 정렬)

- align-items(한 줄), align-self(선택 요소 하나), align-content



### etc

- flex-wrap(각 요소들을 한 줄에 배치), flex-flow, ...



### order

- 기본적으로 item들의 order값은 0이므로 원하는 item을 앞으로 배치하려면 -1을 줘야 함