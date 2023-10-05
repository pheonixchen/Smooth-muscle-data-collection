# Smooth-muscle-data-collection
This Python script can help you collect smooth muscle contraction data under BL420N.
通过手动计算一个标准峰可以实现对其他峰的快速测算。
首先你需要在CLI键入标准峰大小
其次，你需要将光标放在标准峰的最高点按下空格再按下回车。
然后再在标准峰的谷底最低点按下空格再按下回车
这样实现了标准峰的数据采集。
之后用同样的方式（先放到待测峰最高点空格加回车，再放到最低点空格加回车）
在采集完足够数据以后脚本会在CLI中直接把待测峰的Max-Min数值print出来
一次脚本可以采集一个标准峰和无限的待测峰，这可以大大加速你信息采集的速度
基本原理如下
![b63f6db17072f3ca66eaa0cc46c4fa5](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/b4d1f90b-1542-4d32-8d08-5476e18f6d21)
流程如下
![10b94ae87f3b3432aec5a8fbf840143](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/ca32b1e8-69f2-4d82-bde2-495253d3bf17)
公式如下
![70eabd743e2ec2501234277dbeb76ac](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/26c49c2e-654b-4af1-bdf7-6c2ae27df8fc)
运行效果如下
![51baaf635abfe8481f21146bddbd254](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/4f3e907c-2d93-48bd-a577-e95d328c4766)
