import tensorflow as tf

state = tf.Variable(0,name = 'counter') #定义counter = 0
#print(state.name)
one = tf.constant(1)    #定义常量1

new_value = tf.add(state, one)
update = tf.assign(state, new_value) #把new_value赋给state

init = tf.initialize_all_variables()    #非常重要，初始化变量

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))