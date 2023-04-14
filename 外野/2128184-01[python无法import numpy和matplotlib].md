
*****

####  shamal0324  
##### 1#       楼主       发表于 2023-4-10 13:40

<img src="http://tva1.sinaimg.cn/large/779f3f1agy1hcujee1qf8j214d0pvai2.jpg" referrerpolicy="no-referrer">

在vscode和pycharm都是这样的情况，ModuleNotFoundError: No module named 'matplotlib'、ModuleNotFoundError: No module named 'numpy'.

到处搜索，也问过chatGPT了，首先，建议我pip install numpy/matplotlib，都装了，没用

然后，将python.exe所在的文件夹加入environmental variable 的 path，这个也加了，没用

之后，stackexchange有个答案，是建议先删了matplotlib，再针对python3重装一次 <blockquote>pip uninstall matplotlib

python3 -m pip install matplotlib</blockquote>我在win10的cmd里还没有python3这个指令，又找到个答案，把python.exe复制一份，改名python3.exe，命令行里python3就能跑了，但是，还是没用……

有些地方说可能是电脑上装了复数版本的python，用pycharm新建项目，选择base interpreter的时候看见有3个项可选，除了我刚手动安装的python3.10，还有个python3.9，在C:\Users\xxx\AppData\Local\Microsoft\WindowsApps下面，还有一个在C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64，看名字像是python3.7，用everything搜索"python"还会出来几百个结果，不知道哪些该删

没辙了，求助orz

*****

####  革萌  
##### 2#       发表于 2023-4-10 13:43

你这个python不是安装的python

你这么装

python -m pip install numpy

*****

####  Feena  
##### 3#       发表于 2023-4-10 13:45

额，这问题好眼熟，py最头疼的就是这种的环境乱了

*****

####  shamal0324  
##### 4#         楼主| 发表于 2023-4-10 13:45

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399707&amp;ptid=2128184" target="_blank">革萌 发表于 2023-4-10 13:43</a>

你这个python不是安装的python

你这么装

python -m pip install numpy</blockquote>
这个也试过了，显示Requirement already satisfied: numpy in c:\python\python310\lib\site-packages (1.24.2)，matplotlib那边也一样……

*****

####  华发夜眼[CN]  
##### 5#       发表于 2023-4-10 13:46

你的python和pip不是一个环境的呗，你用不到多个环境的话全删掉，然后就留一个加到环境变量里就行

*****

####  jchemphys  
##### 6#       发表于 2023-4-10 13:48

virtualenv

*****

####  onEgoOdmAn  
##### 7#       发表于 2023-4-10 13:49

楼主你又换新玩具了啊？！

直接装anaconda不行吗？
<img src="https://static.saraba1st.com/image/smiley/face2017/245.png" referrerpolicy="no-referrer">

*****

####  wangyi041228  
##### 8#       发表于 2023-4-10 13:49

你得确认IDE里项目用的解释器路径。如果项目用的虚拟环境，cmd敲pip给系统装一百个库都没用。pycharm里虚拟环境装库挺方便的。

*****

####  mero2001  
##### 9#       发表于 2023-4-10 13:50

anaconda+1

*****

####  蠢吐槽  
##### 10#       发表于 2023-4-10 13:50

装个anaconda就好了， 不要自己调环境

*****

####  shamal0324  
##### 11#         楼主| 发表于 2023-4-10 13:51

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399756&amp;ptid=2128184" target="_blank">华发夜眼[CN] 发表于 2023-4-10 13:46</a>

你的python和pip不是一个环境的呗，你用不到多个环境的话全删掉，然后就留一个加到环境变量里就行 ...</blockquote>
windows里面的也可以删吗？

*****

####  六尺之下  
##### 12#       发表于 2023-4-10 13:52

要么用指定python -m pip install，要么创建~/pip/pip.ini，里面指定pip对应的python路径
 [global]  target=C:\Program Files\Python310\Lib\site-packages复制代码

*****

####  忘归然  
##### 13#       发表于 2023-4-10 13:52

实测，别用conda的环境，装官方的Python，不会出现c库装失败的问题

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  华发夜眼[CN]  
##### 14#       发表于 2023-4-10 13:53

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399829&amp;ptid=2128184" target="_blank">shamal0324 发表于 2023-4-10 13:51</a>

windows里面的也可以删吗？</blockquote>
可以，不影响，等你到后面需要多版本环境的时候就回去学anaconda配置了

*****

####  忘归然  
##### 15#       发表于 2023-4-10 13:53

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399744&amp;ptid=2128184" target="_blank">Feena 发表于 2023-4-10 13:45</a>
额，这问题好眼熟，py最头疼的就是这种的环境乱了</blockquote>
我用官方的环境就没出过这类问题。。反而用了conda各种坑

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  oldttt  
##### 16#       发表于 2023-4-10 13:58

认准你要用的那个版本 找到python全路径 确认你pycharm工程里也是这个
/abs_path/python -m pip install xxx

pycharm里注意右下角是不是选的你这个python interpreter

ps：其实pycharm里就能pip

*****

####  bad_alloc  
##### 17#       发表于 2023-4-10 13:59

你之前用windows的命令行装的包，然后新建项目的时候建了个新的virtualenv，新建的env里面没有装这两个包吧？用pycharm项目的命令行再跑一次pip试试

*****

####  nexus1  
##### 18#       发表于 2023-4-10 14:00

<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">感觉只要你整明白环境,其他py具体代码都是小问题了

*****

####  shamal0324  
##### 19#         楼主| 发表于 2023-4-10 14:01

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399791&amp;ptid=2128184" target="_blank">onEgoOdmAn 发表于 2023-4-10 13:49</a>

楼主你又换新玩具了啊？！

直接装anaconda不行吗？</blockquote>
我是脑抽了才会想用C去写计算几何的作业，想plot个图都要调用gnuplot_i.h，然后这个东西死活装不上，chatGPT也只会说车轱辘话，对了有没有大神懂的怎么装这个？

后来怒了索性全部推翻用python重新写，就遇到上面的问题了

*****

####  坑狗madao  
##### 20#       发表于 2023-4-10 14:04

只用python库的话conda

有python以外其他奇怪的库搞不定的话，试试docker

—— 来自 HUAWEI AQM-AL10, Android 10上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

*****

####  日日夜夜  
##### 21#       发表于 2023-4-10 14:04

切换环境对了conda也不会出问题啊，conda环境和virtualenv环境可以一个系统里装着不冲突，甚至不需要用python相关的环境也可以，只要你分得清怎么进入和切换虚拟环境就行

*****

####  hugosol  
##### 22#       发表于 2023-4-10 14:06

其实也没那么复杂，就是网上教程很多没说清楚ide编译和运行的环境不一定和你系统的环境一致的，你要去setting之类的地方看一眼

搞清楚你在用的python在哪个路径下就行了

*****

####  yueyue2002  
##### 23#       发表于 2023-4-10 14:09

在你程序开头加上这两句代码，首先确定是用哪个 python 跑的, 安装包之前先执行一下 pip --version，确认 pip 和 python 是同一个环境

import sys

print(sys.executable)

*****

####  lvcha  
##### 24#       发表于 2023-4-10 14:09

anaconda在create env的时候就把依赖加进来

*****

####  iriyano  
##### 25#       发表于 2023-4-10 14:09

不如装个ubuntu虚拟机
从0开始，不要在windows上搞了

*****

####  lvcha  
##### 26#       发表于 2023-4-10 14:10

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399948&amp;ptid=2128184" target="_blank">shamal0324 发表于 2023-4-10 14:01</a>

我是脑抽了才会想用C去写计算几何的作业，想plot个图都要调用gnuplot_i.h，然后这个东西死活装不上，chat ...</blockquote>
你还真问chatgpt啊。。我觉得这玩意在解答技术问题方面不是很靠谱，凭空写code人再去修改还可以

*****

####  vuder  
##### 27#       发表于 2023-4-10 14:10

直接装Anaconda

*****

####  遇事不决掷骰子  
##### 28#       发表于 2023-4-10 14:10

环境变量里面，有没有pythonhome/pythonpath这两个变量？有的话改成你现在安装的python3.10的路径，然后是PATH这个环境变量，找找里面有没有其他python的路径，删除，添加你现在用的python路径，大部分情况下就可以了。

*****

####  xburke  
##### 29#       发表于 2023-4-10 14:11

conda create -n env_name，请

—— 来自 [S1Fun](https://s1fun.koalcat.com)

*****

####  忘归然  
##### 30#       发表于 2023-4-10 14:15

你试试这样做：

1、在命令行里输入 python &gt; 检查当前python的版本

2、在命令行输入 where python &gt; 检查当前python的路径

3、输入pip list 检查安装的包 

4、在idea里打开命令行输入 python 和 where python （如果是power shell 输入 where.exe python) 

5、检查系统和idea的环境是不是一样的


*****

####  马桶3  
##### 31#       发表于 2023-4-10 14:18

无脑解决方案：卸载所有python，只装一个

无脑方案2：系统重装，再装一个官方python安装包，一个

*****

####  忘归然  
##### 32#       发表于 2023-4-10 14:19

然后重新装一下numpy和matplotlib，检查pip的输出内容有没有失败的

*****

####  shamal0324  
##### 33#         楼主| 发表于 2023-4-10 14:26

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60400105&amp;ptid=2128184" target="_blank">遇事不决掷骰子 发表于 2023-4-10 14:10</a>

环境变量里面，有没有pythonhome/pythonpath这两个变量？有的话改成你现在安装的python3.10的路径，然后是P ...</blockquote>
看了看，并没有这些变量啊，path里面也只有python3.10的

一下子那么多建议，s1温暖人心<img src="https://static.saraba1st.com/image/smiley/face2017/051.png" referrerpolicy="no-referrer">，我先把anaconda装上……

*****

####  shamal0324  
##### 34#         楼主| 发表于 2023-4-10 14:34

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60399921&amp;ptid=2128184" target="_blank">bad_alloc 发表于 2023-4-10 13:59</a>

你之前用windows的命令行装的包，然后新建项目的时候建了个新的virtualenv，新建的env里面没有装这两个包吧 ...</blockquote>
啊啊搞定了<img src="https://static.saraba1st.com/image/smiley/face2017/056.gif" referrerpolicy="no-referrer">，学这个视频BV1V44y1o7E9在pycharm装上这两个库，能跑了，鬼使神差地，连vscode下面都能跑了，这些编译器共用一个virtualenv的吗？

我过几天再慢慢研究了，赶作业先

*****

####  bad_alloc  
##### 35#       发表于 2023-4-10 15:10

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60400521&amp;ptid=2128184" target="_blank">shamal0324 发表于 2023-4-10 14:34</a>
啊啊搞定了，学这个视频BV1V44y1o7E9在pycharm装上这两个库，能跑了，鬼使神差地，连vscode下面都 ...</blockquote>
vscode在底栏可以选择使用的是哪个解释器

*****

####  カドモン  
##### 36#       发表于 2023-4-10 15:12

你直接  pycharm settings 里面安装就行了，图形化界面店的

*****

####  矢吹奈子  
##### 37#       发表于 2023-4-10 15:15

电脑-属性-高级系统设置-环境变量-pach-把最新版python的安装目录贴进去。

*****

####  migros  
##### 38#       发表于 2023-4-10 15:25

一般是启动的python和pip用的python不是同一个python

—— 来自 samsung SM-N9860, Android 13上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.2-play

*****

####  thq  
##### 39#       发表于 2023-4-10 15:25

我前两天刚解决了类似问题, 命令行下一运行python就给我弹应用商店.

解决方法说来也简单:

用pyenv安装特定版本的python, 然后用pyenv global设置全局python版本之后就ok了.

*****

####  冰寒之月  
##### 40#       发表于 2023-4-10 15:28

你开pycharm的时候输入命令查查它用的是哪个python

然后用绝对路径\python.exe -m pip 的方式安装包就不会错

*****

####  NavierStokes  
##### 41#       发表于 2023-4-10 15:29

装错环境了吧<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  TonyKnight  
##### 42#       发表于 2023-4-10 15:31

额，这是怎么把问题搞这么复杂的。。anaconda完善很多了，现在Python环境配置真无脑很多了，去官网下好anaconda一路下一步，最后去cmd或PowerShell一个conda init就完事了，根本不需要管环境变量。

*****

####  chachi  
##### 43#       发表于 2023-4-10 15:46

妈耶。。。

你确定你学了很多年CS吗

*****

####  GETTER2  
##### 44#       发表于 2023-4-10 16:14

你的文件名不能和import的模块冲突

*****

####  幻想风靡_  
##### 45#       发表于 2023-4-10 16:16

如果使用pycharm的话，可以用它的版本管理

或者自己折腾venv

实在不行把电脑里python全删了再装你想要的版本

*****

####  Viteeee  
##### 46#       发表于 2023-4-10 16:42

请初学者不要没事自己配环境折磨自己，老老实实上anaconda<img src="https://static.saraba1st.com/image/smiley/face2017/066.png" referrerpolicy="no-referrer">

*****

####  于干  
##### 47#       发表于 2023-4-10 16:58

每个项目一个venv不好么，或者都删掉上anaconda吧

*****

####  libratest  
##### 48#       发表于 2023-4-10 17:09

anaconda 请

*****

####  shamal0324  
##### 49#         楼主| 发表于 2023-4-11 02:58

再问一下，python有没有一种sort function是支持自定义comparator的？像C的qsort那样。python的sorted()里的key好像不能这样用

[https://zhuanlan.zhihu.com/p/108949863](https://zhuanlan.zhihu.com/p/108949863)

找到了一些教程说可以用functool里面的cmp_to_key，本来以为来了救星，但是，安装functool失败，就像我上面装numpy一样装，失败了，在pycharm命令行装也不行

有什么类似的自定义排序的方式吗？作业要求必须自定义排序。没有的话我又要滚回C去写了……

*****

####  peacearlo  
##### 50#       发表于 2023-4-11 04:53

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60408696&amp;ptid=2128184" target="_blank">shamal0324 发表于 2023-4-11 02:58</a>

再问一下，python有没有一种sort function是支持自定义comparator的？像C的qsort那样。python的sorted()里 ...</blockquote>
安装失败的原因是啥？如果是下载失败就换一个节点

*****

####  blueshift  
##### 51#       发表于 2023-4-11 05:17

自定义comparator写在你的自定义类里面，那不是sort管的事情，看看https://docs.python.org/3/library/functools.html#functools.total_ordering

*****

####  blueshift  
##### 52#       发表于 2023-4-11 05:22

还有functools是自带的标准库啊兄弟，你在这装什么呢？

*****

####  shamal0324  
##### 53#         楼主| 发表于 2023-4-11 06:01

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60408801&amp;ptid=2128184" target="_blank">peacearlo 发表于 2023-4-11 04:53</a>

安装失败的原因是啥？如果是下载失败就换一个节点</blockquote><blockquote>  note: This error originates from a subprocess, and is likely not a problem with pip.

error: legacy-install-failure

Encountered error while trying to install package.

functools

note: This is an issue with the package mentioned above, not pip.

hint: See above for output from the failure.</blockquote>

提示我升级pip，但又说失败与pip无关，不知怎么办了，类似名字的functoolplus什么的装了，没有这个cmp_to_key

*****

####  shamal0324  
##### 54#         楼主| 发表于 2023-4-11 06:03

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60408817&amp;ptid=2128184" target="_blank">blueshift 发表于 2023-4-11 05:17</a>

自定义comparator写在你的自定义类里面，那不是sort管的事情，看看https://docs.python.org/3/library/func ...</blockquote>
好像明白了，自己造轮子是吧，应该也不难，但是晚了，已经滚回去C写了，一堆point排好序之后输出到txt，再用python读取，plot出来检查有没有排好序<img src="https://static.saraba1st.com/image/smiley/face2017/068.png" referrerpolicy="no-referrer">

真没想到伪代码5分钟的东西写了我5天，还没写完

*****

####  shamal0324  
##### 55#         楼主| 发表于 2023-4-11 06:04

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60408820&amp;ptid=2128184" target="_blank">blueshift 发表于 2023-4-11 05:22</a>

还有functools是自带的标准库啊兄弟，你在这装什么呢？</blockquote>
诶？？但是from functools import cmp_to_key不成功啊？

*****

####  blueshift  
##### 56#       发表于 2023-4-11 06:29

有错搜错误信息吧，这东西不论是py2还是py3都是标准库，如果连这个都没，我也不知道你那python是什么玩意了，建议把全部python删光了好好重装

*****

####  GYSS_  
##### 57#       发表于 2023-4-11 06:36

合理猜测是没选对interpreter，选到其他没装包的虚拟环境了<img src="https://static.saraba1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  blueshift  
##### 58#       发表于 2023-4-11 06:40

还有是不是可能venv没有继承base的库啊？我记得有这种选项，但是我从没有用过这种venv

*****

####  peacearlo  
##### 59#       发表于 2023-4-11 08:36

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60408850&amp;ptid=2128184" target="_blank">shamal0324 发表于 2023-4-11 06:01</a>

提示我升级pip，但又说失败与pip无关，不知怎么办了，类似名字的functoolplus什么的装了，没有这个cmp_ ...</blockquote>
<img src="https://static.saraba1st.com/image/smiley/face2017/044.png" referrerpolicy="no-referrer">感觉还是几个版本混在了一起的样子，其实应该是个很容易的事情

一个小建议，都学cs了，顺便装个干净的 linux系统吧，会方便不少的（虽然区别也不是很大）

*****

####  kamarus  
##### 60#       发表于 2023-4-11 08:39

多半pip安错位置了，或者直接重新下anaconda。


*****

####  zkjqw139  
##### 61#       发表于 2023-4-11 08:53

&gt;&gt; python

&gt;&gt; import pip

&gt;&gt; pip.main(['install','numpy'])


*****

####  すぴぱら  
##### 62#       发表于 2023-4-11 09:17

只装一个py，其他用venv


*****

####  绕指流光  
##### 63#       发表于 2023-4-11 10:24

2023都过了3个多月了，有开发需求就直接anaconda，不要那么多包就miniconda吧，所有项目都搞venv

这几个月AI绘画大爆炸，各种py问题真是层出不穷，环境问题对于新手来说根本没法解，网上教程大量过期

