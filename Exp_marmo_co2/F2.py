# #!/usr/bin/env python3.7  
#### Checked on 16th August 2024, Field2_fixPos.html is also correct
# import os 
# import RPi.GPIO as GPIO

# #设置GPIO输出模式，此处使用33号端子作为输出正极
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(33,GPIO.OUT)
# #设置PWM信号
# p = GPIO.PWM(33,801) #2s，0.1mL
# p.start(0)

from bottle import route,run,request,template,static_file

experiment = "Field2_fixPos" #此处填写实验网页的文件名
#平板电脑端输入“树莓派ip：端子”进入实验网页
@route("/",method="GET") 
def index():
    return template(experiment)
#载入图片文件
@route('/img/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./img/')
#接收到平板电脑端控制信号时启动或停止PWM输出
@route("/cmd",method="POST") 
def cmd():
    press = request.body.read().decode()
    if press == "correct":
       print("correct")
        #p.ChangeFrequency(801)
        #p.ChangeDutyCycle(50)
    elif press == "bonus":
        print("bonus")
        #p.ChangeFrequency(1601)
        #p.ChangeDutyCycle(50)
    elif press == "finish":
         print("finish")
         #p.ChangeDutyCycle(0)
#启动监听
run(host="0.0.0.0",port="8010",debug=True,reloader=False) 