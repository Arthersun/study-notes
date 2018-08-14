运行pycharm，创建一个flask工程，然后run

```python
from flask import Flask

app = Flask(__name__)

# @开头并且在函数的上面的说明是一个装饰器
# 这个装饰器的作用是做一个url与视图函数的映射
@app.route('/')
def hello_world():
    a = 1
    b = 0
    c = a/b
    return '第一个flask程序'


if __name__ == '__main__':
    app.run()
```

result:

```python
FLASK_APP = app.py

FLASK_ENV = development

FLASK_DEBUG = 0

In folder /home/sun/PycharmProjects/first_flask

/home/sun/PycharmProjects/first_flask/venv/bin/python -m flask run

- Serving Flask app "app.py"
- Environment: development
- Debug mode: off
- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

我们打开http://127.0.0.1:5000/

出现一串文字：

```test
第一个flask程序
```



