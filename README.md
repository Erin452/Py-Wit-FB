# python

1. pip install virtualenv
2. virtualenv \(name)
3. \(name)\\Scripts\\activate   
   *everytime when you start
4. pip install flask requests pymessenger wit jieba


# fb for developers

1. 建立粉專
2. 設定Webhook \(ngrok)
3. 建立app.py
4. @app.route....['Get']
5. ngrop web 出現hello\(key word)
6. 輸入hub.verify_token設定
7. @app.route...['post']
8. 接收訊息json

#heroku 

1. pip install gunicorn
2. pip freeze > requirements.txt
3. echo > Procfile
4. open Procfile and enter \[web: gunicorn app:app]
5. git init
6. git status
7. echo > .gitignore
8. open .gitignore and enter \[mybot/]
9. git commit -m "\(name)"
10.git add .
11.git commit -m "\(name)"
12.heroku create
13.heroku git:remote -a \[網域名稱\(heroku create)]
14.git push heroku master

if you want to stop: heroku maintenance:on

# Wit.ai

1. get access_token in Wit.ai app
2. get res for entity and value

