# overfitting(过拟合)

机器学习模型过于自信已经到自负的阶段了。

```
自负
在自己的小圈子里表现非凡
在现实的大圈子里却处处碰壁
```

解决方法：
dropout

每一次都忽略一些神经元和神经来训练
也就可以不那么依赖于某些神经元和神经了。

Wx_plus_b = tf.nn.dropout(Wx_plus_b,keep_prob)
keep_prob = tf.placeholder(tf.float32)


sess.run
- keep_prob参数=1 
    没有dropout
- keep_prob参数=0.5
    dropout 50%



