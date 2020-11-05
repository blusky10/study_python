# WEB

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
   ```
   python -m venv [이름]
   ex) python -m venv my_venv
   ```
2. 가상환경 실행
   ```
   source my_venv/bin/activate
   my_venv/Scripts/activate (윈도우일 경우)
   ```
3. django 설치 
(3번 부터는 가상환경 안에서 모두 실행한다.)
   ```
   pip install django
   ```

### 프로젝트 만들기
```
django-admin startproject [이름] .
```

### 데이터 베이스 만들기
```    
python manage.py migrate
```    

- db.sqlite3 파일이 생성된다.
- 데이터베이스가 수정 될 때마다 마이그레이션 작업을 해야한다.

### 프로젝트 실행
   ```
   python manage.py runserver
   ```

### 앱 추가

프로젝트 내에서 앱을 추가하여 구성할 수 있다. 
   ```
   python manage.py startapp [앱이름]
   python manage.py makemigrations [앱이름]
   python manage.py migrate
   ```
- 프로젝트 내에 [앱이름] 으로 폴더가 생성된다.
- 생성된 앱은 settings.py 에 추가를 해준다.
  ```
  INSTALLED_APPS = [
    '앱이름',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',]
  ```
- urls.py 에 앱 url 추가
  ```
  urlpatterns = [
        path('admin/', admin.site.urls),
        path('users/', include('users.urls'))
  ]
  ```
### admin 사이트

- superuser 만들기
  ```
  python manage.py createsuperuser
  ```

- 접속 URL : 접속URL/admin

### Web 에 Page 추가

- urls.py 에 path 추가
  ```
  urlpatterns = [path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),]       
  ```
- views.py 에 추가
  ```
  def new_entry():
  ```        
- html 파일 작성


### 페이지에 권한 추가

from django.contrib.auth.decorators import login_required

@login_required 사용

### 배포

- bootstrap 추가
  pip install django-bootstrap4

- setting.py 에 bootstrap4 추가  
  ```
  INSTALLED_APPS = [
    'bootstrap4',
    ..
  ```