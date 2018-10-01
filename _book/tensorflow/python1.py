#导入包
import tensorflow as tf
import numpy as np

#创建数据
x_data = np.random.rand(100).astype(np.float32) #生成100个随机数列，tensorflow的数据大部分是float32
y_data =x_data*0.1 + 0.3 # W(Weights) = 0.1 , b(biases) =0.3

###创建tensorflow结构开始###
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) #Weights初始化为-1到1的一个随机数
biases = tf.Variable(tf.zeros([1])) #biases初始化为0

y = Weights*x_data +biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables() #初始化
###创建tensorflow结构结束###

sess = tf.Session()
sess.run(init)  #非常重要

for step in range(401):
    sess.run(train)
    if step % 40 == 0:
        print(step,sess.run(Weights),sess.run(biases))



