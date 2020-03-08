## 伪静态博客框架

![运行流程]( https://ae01.alicdn.com/kf/H485cf804ba92481ba9456e9fc454563aZ.png )

点击查看: [demo1](https://czaorz.github.io/ioco/blog/blogV1.html)

> 该框架采用前后端分离思想，由于`纯静态`页面基本不能满足需求。  
> 故将整体分为两大部分，即伪静态后端 和 前端。前端是独立模块，
> 可以根据指定不同"后端"来实现不同内容的对接，
> 故需要保证"后端"接口一致性。

#### 执行指令
1、创建模板  
需要先安装模块minitools，pip install minitools  
该模块所需其他模块较多，详情见minitools的requirements.txt
> python command.py create

该指令根据当前时间创建标准模板。 eg: ./2020/3/7/pv_blog_1.md  
md文件顶部为该篇博客信息，分别表示：图片、标签、标题、摘要、文本大致内容  
```html
<!--
https://ae01.alicdn.com/kf/Haf4d3b0529ba47669bf69c7bfc71a5f1Y.png
未定义
default title
default abstract
default blog content, please don't use some markdown grammar in first paragraph.
-->
```

2、收集模板并编译json  
> python command.py gather  
> python command.py gather --html=True --author=CzaOrz

不加 --html 参数，则默认为False，表示编译过程不会创建对应的html文件，
因为github.io服务器会帮我们渲染md文件，故此方法是可行的，对于非github类的静态服务器，
则需要编译为html文件以保证页面的正常渲染。

而 --author 参数，表示需要在编译的时候指定作者....不然就默认是我...

该方法会在目录上生成对应的settings.json文件，该文件为数据接口，数据格式如下：
```json
{
  "blog_url": "./json/blog1.json",
  "blog_total": 1,
  "blog_total_page": 1,
  "blog_last_url": "./json/blog1.json",
  "labels": [
    {
      "name": "未定义", 
      "url": "./label/未定义/label1.json", 
      "total": 1, 
      "total_page": 1
    }
  ]
}
```

通过该份数据，我们可以看到，具体的博客数据在"blog_url"里面，故发起该连接的请求，
可获取数据格式如下：
```json
{
  "blogs": [
    {
      "blog_id": 1, 
      "blog_img": "https://ae01.alicdn.com/kf/He75017a01c204550ace3b3d5293d4075y.png", 
      "blog_title": "default title", 
      "blog_abstract": "default abstract", 
      "blog_author": "CzaOrz", 
      "blog_created": "2020-02-20 11:24:49", 
      "blog_amend": "2020-02-23 22:06:54", 
      "blog_content": "default blog content, please don't use some markdown grammar in first paragraph.", 
      "blog_url": "./2020/3/7/pv_blog_1", 
      "labels": ["未定义"]
    }
  ],
  "next_url": ""
}
```
至此，我们即可拿到博客的所有相关信息。在开发前端页面时，需要遵循此接口规范。
