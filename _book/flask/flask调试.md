# Flask调试

调试在源代码的app.run()的括号中加上debug=True

```python
app.run(debug=True)
```

### 注意

但是在pycharm中加上也没用。

查阅发现，原来得开启pycharm的flask_debug功能。

右上角项目->edit Configurations->勾选flask debug

### 调试模式的作用

* 网页上可以看到调试错误信息而不会直接报错
* 只要修改了项目中的`python`文件，程序会自动加载不需要手动重新启动服务器

### 调试模式可以放在配置文件中

主文件中加入

```python
import config
app.config.from_object(config)
```

配置文件*config.py*

```python
DEBUG = True		#DUBUG大写
```





