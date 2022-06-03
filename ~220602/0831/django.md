### 가상환경 폴더 설정

```
python -m venv venv
```



### 가상환경 활성화

```
source venv/Scripts/activate # 가상환경 활성화
# pip list로 가상환경 체크 / (venv)가 떠 있는지 확인
```

### Django 설치

```
pip install django
```



### 프로젝트 생성

```
django-admin startproject projectA		# projectA/projectA/*.py
django-admin startproject projectB .	# projectB/*.py <= 주로 이걸로 사용
```



### 어플리케이션 생성

```
python manage.py startapp articles
# settings.py - 'INSTALLED_APPS'에 <'articles',> 작성 
```



### 서버 실행

```
python manage.py runserver
```

