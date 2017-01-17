# 恶俗古风自动生成器

本程序用于自动生成古风诗句，重写自[此文](http://www.jianshu.com/p/f893291674ca)中的Ruby代码。

Have a good day.

-----
已为nginx增加配置文件，可用gunicorn或uwsgi运行本程序。为方便服务器运行去掉sleep函数并将循环改为100次。

请先注释掉poem.conf中相应行，并将其放入指定位置。

## gunicorn
后台启动：
```
gunicorn run:application -b 127.0.0.1:8080 -p server.pid -D
```

结束：
```
kill `cat server.pid`
```

## uwsgi
后台启动：
```
./start.sh
```

结束：
```
./stop.sh
```
