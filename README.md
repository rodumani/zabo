zabo
====

자보갤러리 세팅법

# 0. Initialize Development Environments 

## Global Dependent Packages 

`libjpeg`


## Python Dependent Packages 

```
Django==1.6.5
Pillow==2.5.1
django-imagefit==0.4
django-endless-pagination==2.0
pil==1.1.7
```

### 빠른 설정 (Quick Initialization)

Python 의존성 패키지 관리를 위해 [`python-virtualenv`](https://pypi.python.org/pypi/virtualenv)를 이용합니다

다음 명령은 virtualenv 를 생성, 활성화, 의존성패키지 설치까지 수행합니다.

```
# Virtualenv 생성 
$ virtualenv FOLDER_NAME

# Virtualenv 활성화 
$ source FOLDER_NAME/bin/activate
(FOLDER_NAME) $ 

# 의존성패키지 설치
(FOLDER_NAME) $ pip install -r requirements.txt
```

Virtualenv 에서 전역환경으로 다시 돌아가기
```
(FOLDER_NAME) $ deactivate
```

`virtualenv` setting을 완료했다면 이후부터는 `$ source FOLDER_NAME/bin/activate`만 실행시켜 사용 할 수 있습니다.

우측 메뉴에서 찾을 수 있는 위키 페이지에서 git 사용법과 convention에 대한 자세한 정보를 얻을 수 있습니다.

# 1. Sync DB

자보갤러리를 실행하기 위해 Database를 초기화 해야 합니다. 

개발환경에서는 SQLite3를 사용합니다. 

```
$ python manage.py syncdb
```

# 2. Load Fixtures 

자보갤러리 개발을 위한 예시가 준비되어 있습니다. 
불러오기 위해서는 다음의 코드를 이용합니다. 

```
$ python manage.py loaddata test
```

# 3. Run

자보갤러리를 실행할 준비가 되었습니다. 

```
$ python manage.py runserver 0:[PORT]
```


