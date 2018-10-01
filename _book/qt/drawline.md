# 如何使用qt来draw line(qt的使用方法和第一个程序)

安装好qt之后，file->new file or project->qt c++ project->qt gui application，在detials中选择Qwidget
就自动创建好了widget.h,main.cpp,widget.cpp等文件

此时widget.h中有四个函数：
```cpp
protected:
    void paintEvent(QPaintEvent *);             //画布事件
    void mousePressEvent(QMouseEvent *);        //鼠标点击事件
    void mouseMoveEvent(QMouseEvent *);         //鼠标移动事件
    void mouseReleaseEvent(QMouseEvent *);      //鼠标释放事件
};
```


