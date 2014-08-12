zabo
====

자보갤러리 세팅법

# 0. Initialize Development Environments 
Django version 1.6을 사용하기 위해 `python-virtualenv`를 이용합니다

```
$ virtualenv FOLDER_NAME
$ source FOLDER_NAME/bin/activate
```

을 실행 시

`(FOLDER_NAME) $`
으로 command line이 나타나 현재 virtualenv에서 작업중이라는 정보를 알 수 있습니다.

이후 

`$ pip install -r requirements.txt`

를 실행해 설치한 뒤 작업하면 됩니다.

`virtualenv`에서 빠져나오려면 다음 명령어를 사용하면 됩니다.

`(FOLDER_NAME) $ deactivate`

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


