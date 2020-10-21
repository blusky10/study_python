# Python

## data_visualization
python -m pip install --user plotly


## Web

### 전체 구조

```
root
│   db.sqlite3
│   manage.py    
│
└───venv
│
└───project
│   asgi.py
│   settings.py
│   urls.py
│   wsgi.py
│
└───app
│   └───migrations
│   admin.py
│   apps.py
│   model.py
│   test.py
│   views.py
└───
```

### 기본 환경 설정

1. 가상환경 만들기

        python -m venv [이름]
        ex) python -m venv my_venv

2. 가상환경 실행

        source my_venv/bin/activate
        my_venv/Scripts/activate (윈도우일 경우)

3. django 설치 
(3번 부터는 가상환경 안에서 모두 실행한다.)

        pip install django

4. 프로젝트 만들기

        django-admin startproject [이름] .

5. 데이터 베이스 만들기
    
    db.sqlite3 파일이 생성된다.

        python manage.py migrate
    
    데이터베이스가 수정 될 때마다 마이그레이션 작업을 해야한다.

6. 프로젝트 실행

        python manage.py runserver



### 앱 추가

프로젝트 내에서 앱을 추가하여 구성할 수 있다. 

    python manage.py startapp [앱이름]

python manage.py makemigrations [앱이름]

python manage.py migrate


### Web 에 Page 추가

- urls.py 에 path 추가
- views.py 에 추가
- html 파일 작성
