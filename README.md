# mqtt-python 学习记录
1，在linux中安装mqtt server：mosquitto的方法

2，配置 mosquitto 为同时支持 raw tcp协议 和 websocket 的方法

  2.1， 修改 /etc/mosquitto/mosquitto.conf文件
  
  2.2，在default listener中，改 port 1883   和   protocol mqtt
  
  2.3，在extra listener中，改 listener 9001 、 protocol websockets、 http_dir /home/tomcat/http_dir(随便一个目录)

3，在linux中安装mqtt client : python的方法 和 代码例程

  3.1 先装好 python： sudo get install python
  
  3.2 再装mqtt client包： sudo pip install paho-mqtt
  
  3.3 试运行一下： client_sub_pub_demo.py    demo详见 《python例程说明》

4，在linux中安装mqtt client : c for embedded的方法 和 代码例程（还没搞定）

5, 浏览器可通过 webservice方式访问MQTT服务器，常见 mqtt-test.html 例程
