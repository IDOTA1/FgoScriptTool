2019.3.3更新：

已确认2.0.22版本mumu可以正常接收消息。自动吃苹果已更新，BUG待检验。

祝贺作者泳装玉藻前满绊！

## fgo小工具使用教程

本软件完全开源，使用本软件造成后果由使用者本人承担。

以下默认使用者使用的平台为windows。

### 关于安全

本工具点击的时候有随机延时和随机落点偏差。

这个工具不带加速，不带注入代码，不带直接收发包，刷本效率和实际手刷没有区别，即使要查封也不应该首当其冲。而且这就是一个大学生自己写的小东西也不收费，要封去封那些工作室嘛！

如果还是担心本工具的安全性，建议去寻求其他脚本（比如从驱动层面模拟的，或者机器人操作的物理脚本）。

### 第一步：下载mumu模拟器和fgo

下载mumu模拟器，需要下载2.0.22版本（而不是最新版本）。

2.0.22版本的下载地址：http://a11.gdl.netease.com/nemu-2.0.22-1023110937.exe

> 华为服需要先下载华为应用市场的apk，再在应用市场里下载fgo。
>
> 小米服貌似没法在模拟器上玩……

### 第二步：在mumu模拟器上设置

因为mumu不支持滚轮操作，所以需要设置一个键位用来滑动助战。

点击mumu下方的键位设置，在助战界面画一条从一个好友框的底端线到顶端线的线，设置其对应的键位为Q。

然后点击mumu右上角的设置中心，在界面设置里把隐藏下方工具栏勾上，分辨率调成1600×900，然后重启mumu。

### 第三步：安装Python 3.7.x

没装python的话，在官网上下载安装即可。

python 3.7.2的下载地址：https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe

### 第四步：安装依赖的Python包

在本项目的文件夹里按住shift+鼠标右键，点“打开PowerShell窗口”进入命令行。

依次输入以下命令（可以复制粘贴）：

```powershell
pip install .\python\pyHook-1.5.1-cp37-cp37m-win_amd64.whl
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple aircv
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pywin32
```

其中第一行是针对Python 3.7.x的64位版本的，32位版本可以用./python文件夹里的另一个文件，其他Python版本的PyHook包可以在https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook 下载。

### 第五步：修改配置文件

我们的小工具里要改的只有config.py（配置文件）和play.py。

config.py里面，宝具时间没什么用，写在那里备用的。

其他那些时间是我测定的大概时间，给了一定的容错误差，正常情况下不需要改可以直接跑（误差很大的进出本和换面时间可以自动判断），换人时间个别机器可能比较长，可以自己加个几秒。

#### 修改显示倍率

在桌面右键进显示设置，在“缩放与布局”里有一个“更改文本、应用等项目的大小”。这个数值写在“缩放倍率”里，默认的缩放倍率为2.0，因为作者的这一项是“200%”。

#### 修改吃苹果设定

用户可以修改“允许食用圣晶石/金/银/铜苹果”这一项，来设计自己的吃苹果策略。在开启多个选项的情况下，优先吃价值低的AP回复道具。比如同时开启金、银、铜苹果的情况下，优先吃铜苹果，铜苹果没了吃银的，银苹果没了吃金的，金苹果没了则脚本卡在那里。

#### 修改期望助战

平时要改的内容只有“期望的助战”，默认的期望助战为午餐孔明，修改方法如下：

##### 第5.1步：截取助战界面

在mumu上进入助战选择界面，然后在本项目的文件夹里打开PowerShell（方法前面说了），输入：

```powershell
python .\cuter.py
```

##### 第5.2步：裁剪期望助战

在画图（或者美图秀秀等图片编辑软件）里把需要的助战头像裁下来，只需要裁头像框（包括礼装），就像例子里的午餐孔明那样。裁剪下来的头像自己命个名保存在同一目录下，注意保存为png格式，比如“merlin_wc.png”。

##### 第5.3步：修改config.py

把config.py中的“期望的助战”改掉，比如改成：

```python
期望的助战 = 'merlin_wc'
```

在选择助战的时候就会寻找刚才保存的“merlin_wc.png”。

### 第六步：写脚本

play.py里写的是脚本，我已经让脚本非常接近自然语言。

目前脚本只支持三回合宝具速刷，接下来会陆续更新暴击队、平A一面、补刀等策略。下面是一个例子。

```python
def 公会堂羽毛():
    设置阵容([
        '大英雄',
        '船长',
        '孔明',
        '骑凛',
        '枪玉',
        '占位从者1'
    ], 面数=3)
    使用技能('大英雄', 3)
    宝具('大英雄')
    使用技能('孔明', 3)
    使用技能('孔明', 2)
    使用技能('孔明', 1, 目标='船长')
    使用技能('骑凛', 1)
    宝具('骑凛')
    使用技能('船长', 1)
    使用技能('船长', 3)
    使用技能('咕哒', 1, 目标='船长')
    使用技能('咕哒', 3)
    换人('孔明', '枪玉')
    使用技能('枪玉', 2, 敌对目标=2)
    使用技能('枪玉', 1)
    宝具('船长')
```

我们写的脚本是函数“脚本”里的内容。

上面这个例子是一个船长带黑杯+御主换人服的公会堂打法。

> 我知道实际上不用这么打，伤害大量溢出了，但我只是想展示一下脚本的写法啊QAQ

脚本的第一步操作是**设置阵容**，这里注意设置的从者名不能相同，如果有两个孔明，可以写成“孔明1”和“孔明2”。除此之外怎么取名随意，比如214写成“两仪式”、“杀式”、“Shiki”或者“83b15149589639d0”什么的都是可以的。

设置阵容同时给出面数，面数为3的时候（绝大多数情况），"面数=3"可以省略。

接下来写一步一步的操作，这个工具支持3种操作：

* 使用技能，第一个参数为使用者（要在阵容里，或者为“咕哒”表示御主技能），第二参数为这是几技能（1~3），后面可以跟两种补充参数，格式见上。
  * 目标=xxx，需要选择目标的技能（如狐嫁女）选择的目标（写名字）
  * 敌方目标=x，需要选择敌方目标的技能（如咒术）选择的目标（1~3，从左到右）
* 宝具，只有一个参数，使用者。可以跟一种补充参数，格式见上。
  * 敌方目标=x，需要切换目标时指定（1~3，从左到右）。

* 换人：使用换人技能时，因为换人有两个目标，所以要特别写一句，格式见上。

### 第七步：运行脚本

进本（在助战选择界面），然后在本项目的文件夹里打开PowerShell（方法前面说了），输入：

```powershell
python .\enter.py
```

接下来你可以把PowerShell窗口和mumu都扔到另一个桌面去（win+Tab开启桌面控制，新建桌面，然后拖动窗口到新建的桌面即可），在刷本的同时还可以做别的事，毫不耽误。

脚本会自动吃苹果和碎石。

