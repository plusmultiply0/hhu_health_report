# 河海大学2020健康填报--自动化脚本

此脚本可配合 windows 系统程序实现自动化[健康填报](http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list)。免除每日打开 app/网页/微信扫码 点击的麻烦。

完成下面的描述的要求，可以实现每日定时完成健康填报提交,并根据生成提交成功截图。

## 前置准备

**安装必要程序**

- [Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjw8pH3BRAXEiwA1pvMsX0LaGtiAauQozaMwIx7QvDJPlK1SDK45oIoCLowZxP_pbLlj4vu8xoC3nQQAvD_BwE&gclsrc=aw.ds) 下载Chrome
- [Chrome deriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) 根据Chrome版本，下载对应的Chrome driver
- [python](https://www.python.org/downloads/) 下载python

以上程序下载安装后，请配置好环境路径

安装selenium，打开命令行输入

```bash
pip install selenium
```

**修改脚本**

打开auto.py, 

1. 修改 PATH of chromedriver 为你的Chrome driver 安装路径，并修改路径中 \ 为 \\\

2. 修改 your login id 为你的登陆ID（学号）

3. 修改 your password 为你的登陆密码

**设置定时启动**

1. 在 windows 上搜索 **任务计划程序** ，点击创建基本任务。

2. 填写名称和描述，下一步
3. 设置为每天
4. 选择启动程序
5. 程序和脚本处填写 python.exe 的文件路径，添加参数处填写 auto.py 的文件路径，起始于填写一个文件路径（用来存放成功填报的截图）。
6. 完成，之后 windows 会根据设定的时间执行程序

<a id="result"></a>**查看结果**

1. 根据上文的文件路径，查看截图
2. 自行登陆健康填报系统，查看历史填报
3. ~~等班干部发布未填报人名单~~

## 注意事项
1. 根据上述设置完毕后，到达脚本执行时间后，windows会在后台执行脚本（执行结果的查看可根据[**查看结果**](#result)）
2. 整个脚本执行过程约为14-20s
3. 请在脚本的启动时间之前，打开电脑并保持网络连接（若设置了脚本执行时电脑自启动，可忽略）
