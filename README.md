zabo
====

자보갤러리 세팅법

Django version 1.6을 사용하기 위해 `python-virtualenv`를 이용합니다

`$ virtualenv FOLDER_NAME`

`$ source FOLDER_NAME/bin/activate`

을 실행 시

`(FOLDER_NAME) $`
으로 command line이 나타나 현재 virtualenv에서 작업중이라는 정보를 알 수 있습니다.

이후 `pip install django`, `pip install pillow-PIL`를 실행해 설치한 뒤 작업하면 됩니다.

(단 .py 파일들은 전부 python을 붙여서 실행해야만 합니다.)

`virtualenv`에서 빠져나오려면 다음 명령어를 사용하면 됩니다.

`(FOLDER_NAME) $ deactivate`

`virtualenv` setting을 완료했다면 이후부터는 `$ source FOLDER_NAME/bin/activate`만 실행시켜 사용 할 수 있습니다.


자보갤러리에서는 jshint, pylint를 사용합니다.

**Commit하기 전에 반드시 jshint, pylint를 반드시 실행한 후 Commit하도록 합니다!**

우측 메뉴에서 찾을 수 있는 위키 페이지에서 jshint, pylint, git 사용법과 convention에 대한 자세한 정보를 얻을 수 있습니다.
