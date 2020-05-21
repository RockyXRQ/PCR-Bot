# PCR_Ro_BOT

![License](https://img.shields.io/badge/license-MIT-green.svg) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

PCR_Ro_Bot概览

PCR_Ro_Bot 是一个基于，酷Q，Nonebot，CQHTTP，和OpenPyXL制作的QQ机器人，用来解决公主连结行会QQ群内在工会战期间的自主出刀，出刀数据上传（伤害，分数，队伍阵容），击杀状况，挂树申请与救树申请等请求与信息的处理，并且可以将全部数据自动导出为Excel文件，便于信息的查阅和分析。

本仓库包括以下内容：

1. 一份完整的PCR_Ro_BOT代码。
2. PCR_Ro_Bot的安装及使用教程。
3. PCR_Ro_Bot指令的使用介绍。

## 内容列表

- [背景](#背景)

- [安装](#安装)
  - [酷Q](#酷Q)
  - [NoneBot](#NoneBot)
  - [CQHTTP](#CQHTTP)
  - [OpenPyxl](#OpenPyxl)

- [配置](#配置)
- [运行](#运行)
- [指令](#指令)
  - [指令流程图](#指令流程图)
  - [各指令介绍](#各指令介绍)
- [查看数据](#查看数据)
  - [Excel表格](#Excel表格)
  - [日志](#日志)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 背景

**PCR_Ro_Bot** 是为了让只有基础的编程经验的人，也可以轻松搭建出一个具有高功能性的PCR工会战排刀机器人而产生的。只需要简单几步操作，就可以获得一个操作便捷，且可以自主完成数据导出与信息分析的QQ机器人。该项目的本意，是为了编写出一个可以记录尽量多的工会战信息，又可以替代人力对信息进行汇总和处理的QQ机器人。这个项目因此开始。

> 该项目目前不具有很高的自定义程度，如果您对于机器人有更多自己的想法，请联系作者或在贴吧留言，并等待项目更新。该项目将会持续更新。

## 安装

该项目使用Python，并依赖酷Q，NoneBot，CQHTTP插件，和OpenPyXL。在使用PCR_Ro_Bot之前，请先保证你在本地安装了他们。

- [Python官网](https://www.python.org/)

作者使用的Python版本为3.8，在运行过程中并无问题。

> 注意：在使用NoneBot机器人之前，请不要忘记将机器人账号添加到您要管理的QQ群中。

### 酷Q

- [酷Q官网](https://cqp.cc/)

出于某种原因，目前酷Q无法在官网上下载，请自行搜索酷Q下载安装。

作者使用的为酷Q轻量版，在使用过程中并无问题。

### NoneBot

NoneBot是一个基于酷Q的Python异步机器人框架，是本仓库机器人的主体框架。

- [NoneBot官网](https://nonebot.cqp.moe/)

在安装好Python之后，请打开CMD窗口并直接输入:

```sh
pip install nonebot
```

### CQHTTP

CQHTTP是一个酷Q的插件，构成了链接酷Q和NoneBot的桥梁，使得NoneBot可以接收到QQ的信息，并进行处理。

- [CQHTTP官网](https://cqhttp.cc/docs/4.15/#/)

进入到CQHTPP的仓库Release栏下，下载最新的 cpk 文件放到 酷Q 的 app 文件夹，然后启用即可。

- [CQHTTP仓库Release页](https://github.com/richardchien/coolq-http-api/releases)

### OpenPyXL

OpenPyXL是一个解决Python读写Excel文件的开源库。

- [OpenPyXL官网](https://openpyxl.readthedocs.io/en/stable/)

打开CMD窗口并直接输入:

```sh
pip install openpyxl
```

## 配置

进入到酷Q程序内该目录下 \data\app\io.github.richardchien.coolqhttpapi\config，如果您之前已经运行过一次机器人，则该目录下会已经存在一个以您的QQ机器人的QQ号命名的json文件，如果没有，您也可以新建一个。请打开它，并写入以下配置：

```json
{
    "$schema": "https://cqhttp.cc/config-schema.json",
    "host": "0.0.0.0",
    "port": 5700,
    "use_http": true,
    "ws_host": "0.0.0.0",
    "ws_port": 6700,
    "use_ws": false,
    "ws_reverse_url": "ws://127.0.0.1:8080/ws/",
    "ws_reverse_api_url": "",
    "ws_reverse_event_url": "",
    "ws_reverse_reconnect_interval": 3000,
    "ws_reverse_reconnect_on_code_1000": true,
    "use_ws_reverse": true,
    "post_url": "",
    "access_token": "",
    "secret": "",
    "post_message_format": "string",
    "serve_data_files": false,
    "update_source": "global",
    "update_channel": "stable",
    "auto_check_update": false,
    "auto_perform_update": false,
    "show_log_console": true,
    "log_level": "info",
    "enable_heartbeat": true
}
```

这是作者使用的配置，该配置与本仓库机器人代码的配置相同。保存之后即可正常运行PCR_Ro_Bot。

## 运行

首先请完整下载本仓库内容，然后用VSCode或任意编辑器打开项目文件夹并运行Bot.py文件，或者直接在项目根目录下执行:

```sh
python bot.py
```

正常情况下，您将观察到以下信息：

![VSC](https://raw.githubusercontent.com/RockyXRQ/PCR_Ro_Bot/master/assets/py_info.png?token=AIKEPB5653SDHN5PXKLPYOS6YZEA4)

![CQHTTP](https://raw.githubusercontent.com/RockyXRQ/PCR_Ro_Bot/master/assets/cqhttp_info.png?token=AIKEPB6VLHQ44OUTB4VXN2S6YZD7Q)

则PCR_Ro_Bot至此已经成功运行。

## 指令

### 指令流程图

![Flow_Chart](https://raw.githubusercontent.com/RockyXRQ/PCR_Ro_Bot/master/assets/PCR_Bot_Command_Flow.png?token=AIKEPB3UNCUVFPS6TMLN4YK6YZD4G)

### 各指令介绍

1. atk_apply

   - 别名：出刀，申请出刀，出刀申请

   - 输入格式：atk_apply(或别名) [出刀阵容] 

     		PS:出刀阵容要求不存在名称重复且各角色名字以空格隔开角色名。

2. atk_finish

   - 别名：完成，出刀完成，完成出刀，出刀完毕
   - 输入格式：atk_finish(或别名) [出刀总伤害]

3. on_tree

   - 别名：挂树，已挂树，申请挂树，会长！我挂树了！
   - 输入格式：on_tree(或别名)

4. save_tree

   - 别名：救树，申请救树，别慌！我来也！
   - 输入格式：save_tree(或别名) [出刀总伤害]
   
5. get_list

   - 别名：查看，查看情况，获取情况
   - 输入格式：get_list(或别名)

> 指令使用注意事项：
>
> 1. 使用指令前请艾特机器人，PS：复制别人对机器人的艾特是无效的。
> 2. 任何带有参数的指令，在使用时，参数和指令之间须有一空格
> 3. 若使用了某一需要参数的指令，却没有给出参数，此时Bot会自行向你索取参数，此时用户无需艾特机器人，直接发送参数即可。
> 4. 任何指令不可以中途结束，如果机器人在向你索取参数，请先上传好参数，再执行下一指令。

## 查看数据

PCR_Ro_Bot自带数据记录，整理，与导出的功能，机器人运行之后，您可以在程序根目录下找到记录信息的文件。

### Excel表格

程序默认调用项目根目录下的PCR_Bot_Template.xlsx文件，并将信息记录在其中。

> 注意：程序目前只支持处理 PCR_Bot_Template.xlsx 文件中的表格格式，请不要擅自修改本文件，在本项目的 /assets目录下存有一份额外的 PCR_Bot_Template.xlsx文件，请在需要时复制至根目录。

您可以通过查看这份文件，来实时查看数据的记录情况。

> 注意：请尽量不要在有人使用指令时打开该文件，这会导致机器人运行错误。推荐的做法是复制一份主目录下的 PCR_Bot_Template.xlsx 文件，并查看该副本。

### 日志

该机器人拥有日志系统，机器人运行之后，您可以在程序根目录下 pcr_log.txt 文件，并通过其查看日志，监控机器人的运行情况。

![log](https://raw.githubusercontent.com/RockyXRQ/PCR_Ro_Bot/master/assets/log.png?token=AIKEPB6ESEJ2DPI5VYWEMEK6YZDSK)

## 维护者

[@Rocky_](https://github.com/RockyXRQ)

## 如何贡献

非常期待您的任何建议，如果您有任何想法，或者发现了程序中的问题，请务必发起 Issue 或者直接与我联系。

## 使用许可

[MIT](LICENSE) © Rocky Xu
