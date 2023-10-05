# Smooth-muscle-data-collection
This Python script can help you collect smooth muscle contraction data under BL420N.

通过手动计算一个标准峰可以实现对其他峰的快速测算。

首先你需要在CLI键入标准峰大小。

其次，你需要将光标放在标准峰的最高点按下空格再按下回车。

然后再在标准峰的谷底最低点按下空格再按下回车。

这样实现了标准峰的数据采集。

之后用同样的方式（先放到待测峰最高点空格加回车，再放到最低点空格加回车）。

在采集完足够数据以后脚本会在CLI中直接把待测峰的Max-Min数值print出来。

一次脚本可以采集一个标准峰和无限的待测峰，这可以大大加速你信息采集的速度。

基本原理如下
![b63f6db17072f3ca66eaa0cc46c4fa5](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/b4d1f90b-1542-4d32-8d08-5476e18f6d21)
流程如下
![10b94ae87f3b3432aec5a8fbf840143](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/ca32b1e8-69f2-4d82-bde2-495253d3bf17)
公式如下
![70eabd743e2ec2501234277dbeb76ac](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/26c49c2e-654b-4af1-bdf7-6c2ae27df8fc)
运行效果如下
![51baaf635abfe8481f21146bddbd254](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/4f3e907c-2d93-48bd-a577-e95d328c4766)
后续数据在excel中进行β加权平滑
![2946134c4183c72040757380a293978](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/ea416c16-fd4d-4966-a118-030b3e2e6561)
![867ba1c6e74f11990edf8b5dea0ad5b](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/292869c4-2c30-4c93-86af-69b33c115236)

最终的乙酰胆碱和兔小肠的量效曲线如下，可以看到有明显的平台期，为标准的逻辑斯蒂曲线

![64714f4053036f54994e2cfcabe90d7](https://github.com/pheonixchen/Smooth-muscle-data-collection/assets/115352360/fc2f744e-ea45-45c8-b559-fe7376f7d676)
