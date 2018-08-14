# Arduino学习

* LED灯，把灯插在13号和GND引脚上

  使用arduino ide拷入代码：

  ```c
  #define LED 13
  void setup() {
    // put your setup code here, to run once:
    pinMode(LED, OUTPUT);
  }
  
  void loop() {
    // put your main code here, to run repeatedly:
    digitalWrite(LED,HIGH);
    delay(8000);
    digitalWrite(LED,LOW);
    delay(1000);
  }
  ```

可以观察到灯泡亮8s，熄灭1s；



