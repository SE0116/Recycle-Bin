### bash에서 파일 생성 방법

```python
touch <filename.extension>
```



### URL 불러오기

```python
pip install requests
```



```python
import requests

<variable> = requests.get(<URL>) # requests.get(<URL>)의 값이 200일 때 성공

```



### Crawling

```python
pip install beautifulsoup4
from bs4 import BeautifulSoup4
BeautifulSoup(requests.txt, 'html.parser') # python이 사용하기 쉽게 번역

select_one('#<keyword>') # 셀럭터에 맞는 데이터 검색, 키워드 뒤에 .text 입력시 키워드에 맞는 값만 제공
```



### API

- 응용 프로그램에서 사용할 수 있도록 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스

  => 응용 프로그램을 위한 접점

