# URL传参

1. 参数的作用：可以在相同的URL，指定不同的参数，来加载不同的数据。

2. 在flask当中，如何使用参数

   ```	
   @app.route('/article/<id>')
   def article(id):
   	return u'您请求的参数是：%s' % id
   #参数需要放在两个尖括号中。
   ```
## 反转URL
反转url:从视图函数到url的转换叫做反转url

用处：

* 在页面重定向的时候，会使用url反转

* 在模板中，也会使用url反转

  

使用url_for反转URL

```python
@app.route('/')
def index():
	print(url_for('my_list'))
	print(url_for('article'))
	return 'Hello World'
	
@app.route('/list/')
def my_list():
	return 'list'
	
@app.route('/')
def article(id):
	return u'您请求的id是： %s'  % id
```