import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, activation_function=None): #默认activation_function为None
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size])) #矩阵，随机变量，形状是[in_size,out_size]
        biases = tf.Variable(tf.zeros([1,out_size]) + 0.1) #列表，biases尽量不要为0
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]  #加一个维度，300行，都在-1和1之间，linspace是一个等差数列
noise = np.random.normal(0,0.05,x_data.shape)   #方差0.05，跟x_data一样的格式
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs=tf.placeholder(tf.float32,[None, 1],name='x_input')
    ys=tf.placeholder(tf.float32,[None, 1],name='y_input')

l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)  #输入层有一个，隐藏层有10个
prediction = add_layer(l1,10,1,activation_function=None) #隐藏层有10个，输出层有1个

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices = [1]))
#对每个例子进行求和再求平均值

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
#学习率要小于1，对误差进行更正

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

'''
Matplotlib对象简介

   FigureCanvas  画布

   Figure        图

   Axes          坐标轴(实际画图的地方)

'''

fig = plt.figure()  #图片框
ax = fig.add_subplot(1,1,1) #子图：就是在一张figure里面生成多张子图。
ax.scatter(x_data, y_data) #以x_data和y_data作为散点
plt.ion()   #打开交互模式，可以不断的显示
#plt.show()


for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    #run1000次train_step
    if i %50 ==0:
        #print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        #打印loss值
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        
        prediction_value = sess.run(prediction,feed_dict={xs:x_data})
        lines = ax.plot(x_data, prediction_value,'r-',lw=5)
        #x轴x_data,y轴prediction_value,r-表示红线,lw=5表示粗度为5
        plt.pause(0.1)


