# 河海大学2020健康填报--自动化脚本

此脚本可配合 windows 系统程序实现自动化[健康填报](http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list)。免除每日打开 app/网页 点击的麻烦。

根据下面的描述，可以实现每日定时完成健康填报提交,并根据生成提交成功截图。

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

**设置定时启动**

1. 在 windows 上搜索 **任务计划程序** ，点击创建基本任务。

2. 填写名称和描述，下一步
3. 设置为每天
4. 选择启动程序
5. 程序和脚本处填写 python.exe 的文件路径，添加参数处填写 auto.py 的文件路径，起始于填写一个文件路径。
6. 完成

**修改程序**

打开auto.py, 

1. 修改 PATH of chromedriver 为你的Chrome driver 安装路径，并修改路径中 \ 为 \\\

2. 修改 your login id 为你的登陆ID（学号）

3. 修改 your password 为你的登陆密码

**查看结果**

1. 根据上文的文件路径，查看截图
2. 自行登陆健康填报系统，查看历史填报
3. ~~等班干部发布未填报人名单~~

