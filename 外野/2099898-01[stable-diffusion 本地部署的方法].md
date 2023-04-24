
*****

####  yanchi  
##### 1#       楼主       发表于 2022-10-15 22:25

 本帖最后由 yanchi 于 2022-11-14 18:48 编辑 

之所以发这个贴子是因为 

[https://bbs.saraba1st.com/2b/thread-2098295-1-1.html](https://bbs.saraba1st.com/2b/thread-2098295-1-1.html)

 这个贴子的教程看得我实在头大

虽然原贴楼主贴心地提供了整合包，但我这个人不喜欢使用整合包这类方

式，大概是因为玩老滚、辐射玩的吧，用别人打包好的就要有耐心，等上

游更新后你还要等大佬再为你打包一遍，像我这种急急国王大概是等不了

的，所以趁今天周六摸索了一天，成功在本地跑了起来，特地发出来供有

心想要自己部署在本地的人参考

---

目录

─────────────────

1. 硬性要求

2. Windows

.. 1. 基础

..... 1. python

..... 2. git

..... 3. 其他

.. 2. 项目搭建

..... 1. 将项目克隆到本地

..... 2. 搭建 python 环境

.. 3. 运行

.. 4. 后续更新

.. 5. 卸载

..... 1. python

..... 2. git

..... 3. 删除 stable-diffusion-webui 文件夹

1 硬性要求

══════════

  • 电脑

  • 手

2 Windows

═════════

2.1 基础

────────

2.1.1 python

╌╌╌╌╌╌╌╌╌╌╌╌

  `stable diffusion' 的运行环境为 python，所以我们首先需要先在自己的电脑

  上搭建一个 python 环境。为了避免影响系统的正常工作，推荐使用 conda 来

  进行管理本机的 python 环境（熟悉 pyenv 等其他管理 python 版本的软件可

  使用自己熟悉的方式）。

  *注意*​，使用 python 自带的 `python -m venv' 需要自行安装 cuda 等相关组

   件，可参考下[这一楼]，有问题请询问成功了的人，我没用这种方法，恐怕提

   供不了多大帮助。

  • 下载地址：[Anaconda]

  • 国内清华镜像：[TUNA]，点击网站右侧 `获取下载链接' 的按钮，随后 `应用

    软件' -&gt; `Conda'

    选择 Miniconda3-xxx 或者 Anaconda3 xxx 均可，两者区别在于 Miniconda

    提供了一个最小管理环境，会为你节省下一部分硬盘空间。

  安装设置一路默认即可。

  安装完成后，将 `Anaconda Powershell Prompt' 固定到桌面（总之能随时找到

  的地方），之后运行 `stable diffusion' 的主要操作都需要在这里面完成。

[这一楼]

&lt;[https://bbs.saraba1st.com/2b/for ... mp;pid=58257390&gt;](https://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;ptid=2099898&amp;pid=58257390&gt;)

[Anaconda] &lt;[https://www.anaconda.com/&gt;](https://www.anaconda.com/&gt;)

[TUNA] &lt;[https://mirrors.tuna.tsinghua.edu.cn/#&gt;](https://mirrors.tuna.tsinghua.edu.cn/#&gt;)

2.1.2 git

╌╌╌╌╌╌╌╌╌

  首先打开 Windows Terminal，在打开的终端窗口中输入下面的指令并回车

  ┌────

  │ winget install git.git

  └────

2.1.3 其他

╌╌╌╌╌╌╌╌╌╌

  具体训练模型需要自己在网上下载

2.2 项目搭建

────────────

2.2.1 将项目克隆到本地

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  选择项目文件存放的位置，在本文中以 D 盘为例，并选择使用人数最多的

  stable-diffusion-webui。

  在之前打开的 Windows Terminal 中，输入下列指令

  ┌────

  │ cd d:/

  │ git clone [https://github.com/AUTOMATIC1111/stable-diffusion-webui.git](https://github.com/AUTOMATIC1111/stable-diffusion-webui.git)

  └────

  克隆完成后，将自己的模型放入 stable-diffusion-webui 中的 models 文件夹。

  克隆过程中如果出现相关网络问题，可以在终端中输入下列文本来解决

  ┌────

  │ git config --global url."https://ghproxy.com/https://github.com/".insteadof [https://github.com/](https://github.com/)

  └────

  如果 ghproxy 连接不畅，可以用 gitclone 或者 hub.fastgit.xyz 提供的代理，

  具体操作跟 ghproxy 类似，可百度一下怎么使用。

  *注意*​，ghproxy 这些网站均不能保证个人账号安全性，如果你有 github 账号

   请不要在这些网站上登录！

  如果你知道 git 的配置文件在哪，可以直接将下列文本附加到配置文件的最后

  ┌────

  │ [url "https://ghproxy.com/https://github.com/"]

  │       insteadof = [https://github.com/](https://github.com/)

  └────

  如果不知道文件在哪，但熟悉终端下编辑文本，可以通过下述方式完成

  ┌────

  │ git config --global --edit

  └────

2.2.2 搭建 python 环境

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  打开我们之前提到的 `Anaconda Powershell Prompt'​，如果正常的话，我们会

  发现与普通终端不同的地方在于它前面多了 `(base)' 字符，说明我们进入到了

  conda 管理的 python 环境。

  之后具体操作步骤如下

  ┌────

  │ cd d:/stable-diffusion-webui

  │ conda env create -f environment-wsl2.yaml

  └────

  如果在创建 python 环境时再次遇到相关网络问题，可以通过 TUNA 提供的[方

  式]解决，在此不再赘述。

  安装完成后，输入 `conda activate automatic'​，如果 `(base)' 改为

  `(automatic)'​，即代表环境搭建成功。

[方式] &lt;[https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/&gt;](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/&gt;)

◊ 2.2.2.1 xformers（可选）

  xformers 纯粹为提高出图速度，跳过此部分对出图质量无影响。

  对于 Pascal, Turing 或者 Amphere 架构的显卡，可以使用[C43H66N12O12S2]

  提供的包，选择本机对应的 `wheel' 文件并下载，将其放置在项目目录下，在

  终端中输入（*注意*，此时你应在刚刚安装的 automatic 环境中）

  ┌────

  │ pip install xformers-&lt;这里是你下载的对应版本&gt;.whl

  └────

  即可安装。遇到问题可以参照下[这一楼]。

  非以上架构的显卡，可以自己手动编译一份

  ┌────

  │ # 相信懂怎么自己编译的这里也不需要教了

  │ git clone [https://github.com/facebookresearch/xformers.git](https://github.com/facebookresearch/xformers.git)

  │ cd xformers

  │ git submodule update --init --recursive

  │ pip install -r requirements.txt

  │ pip install -e .

  └────

  [C43H66N12O12S2]

  &lt;[https://github.com/C43H66N12O12S ... -webui/releases&gt;](https://github.com/C43H66N12O12S2/stable-diffusion-webui/releases&gt;)

  [这一楼]

  &lt;[https://bbs.saraba1st.com/2b/for ... mp;pid=58283104&gt;](https://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;ptid=2099898&amp;pid=58283104&gt;)

2.3 运行

────────

  *第一次运行时*，在项目目录中并已经激活相对应的 python 环境的条件下，在

   Windows Terminal 中输入

  ┌────

  │ python launch.py [--xxx]

  └────

  第一次运行时项目会下载一类诸如 gfpgan 啥的第三方库，如果遇到网络问题可

  以参见之前对 git 的相关设置。

  运行 `python launch.py' 安装的第三方库都安装完成后，之后启动后就可以单

  纯使用下面的命令来加快启动速度，避免启动时再联网检查一次相关三方库有没

  有下载成功。

  ┌────

  │ python webui.py [--xxx]

  └────

  *注意*，​`[]'​中的内容非必填，此处代表启动 stable diffusion 时所附带的参

   数，相当于使用 bat 文件启动时设置的 `COMMANDLINE_ARGS' 的值，常用的参

   数有

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   可用参数                      相关解释                                 

  ────────────────────────────────────────────────────────────────────────

   –xformers                     使用 xformers 库                         

   –force-enable-xformers        强行使用 xformers 库，不会报错           

   –opt-split-attention          性能优化，torch 能加载 cuda 库时默认开启 

   –disable-opt-split-attention  关闭上面那条                             

   –opt-split-attention-v1       旧版优化，占用显存更少，但会影响产出     

   –ckpt                         要载入的 ckpt 文件                       

   –use-cpu                      使用 cpu 进行计算                        

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  全部的参数可以自己在本地运行下述指令查看

  ┌────

  │ python webui.py --help

  └────

  或者参照 stable diffusion 所提供的[wiki]（可能过时，以 `python

  webui.py --help' 输出的为准）。

  示例：如果你此前安装了 xformers 包，此处可以加上参数 `--xformers'​，也

  就是运行时输入 `python launch.py --xformers'​。

  运行后如果没有报错，并且出现诸如下面所示的信息，则代表运行成功；在浏览

  器中打开信息中展示的 `Running on local URL:' 后面所跟的网址即可看到相

  关操作界面。

  ┌────

|  │ Python 3.10.6 | packaged by conda-forge | (main, Oct  7 2022, 20:14:50) [MSC v.1916 64 bit (AMD64)]|

  │ Commit hash: 606519813dd998140a741096f9029c732ee52d2a

  │ xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  │ xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  │ xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  │ xxxxxxxxxx

  │ xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  │ Running on local URL:  [http://127.0.0.1:7860](http://127.0.0.1:7860)  &lt;--- 这是你运行成功后需要打开的网址

  │ 

  │ To create a public link, set `share=True` in `launch()`.

  └────

[wiki]

&lt;[https://github.com/AUTOMATIC1111 ... stom-Parameters&gt;](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Run-with-Custom-Parameters&gt;)

2.4 后续更新

────────────

  打开 Windows Terminal，执行下述操作

  ┌────

  │ cd d:/stable-diffusion-webui

  │ git pull -r

  └────

  之后照旧运行 `python launch.py [--xformers --xxx]'

  *注意*，是要在 conda 构造的虚拟环境中运行，也就是要先运行 `conda

  activate automatic'​。（如果提示找不到 conda 啥的，记得要用 Anaconda

  Powershell Prompt 打开）

2.5 卸载

────────

  如果不想玩了，想让电脑恢复到安装之前的状态，可以遵循下述操作：

2.5.1 python

╌╌╌╌╌╌╌╌╌╌╌╌

  首先打开 Anaconda Powershell Prompt，输入下列指令：

  ┌────

  │ conda env remove -n automatic

  └────

  即可。当然，如果不想保留 Anaconda，直接全部卸载掉也可以。

2.5.2 git

╌╌╌╌╌╌╌╌╌

  ┌────

  │ git config --global --unset url."https://ghproxy.com/https://github.com/".insteadof

  └────

  *注意*，这种做法实际上在你的 gitconfig 文件中实际上还残留了一行 `[url

   "https://ghproxy.com/https://github.com"]'​，但实际上对 git 来说无任何

   影响，有洁癖的话可以找到自己的 `~/.gitconfig' 文件删除对应行。

  然后卸载 git

  ┌────

  │ winget uninstall git.git

  └────

2.5.3 删除 stable-diffusion-webui 文件夹

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  打开 D 盘，右键删除。

﹍﹍﹍

评分

 参与人数 8战斗力 +10

|昵称|战斗力|理由|
|----|---|---|
| yolu| + 2|好评加鹅|
| N-Time| + 1||
| Ollie| + 2|好评加鹅|
| 路西恩| + 1|好评加鹅|
| eulereld| + 1||
| Alicest| + 1|好评加鹅|
| 相参降解社畜| + 1|整挺好，条理清晰|
| Retr0_Wusami| + 1|好评加鹅|

查看全部评分

*****

####  nordicvan  
##### 2#       发表于 2022-10-15 22:36

楼主这个文档风格乍一看像markdown但其实不是，很有互联网刚兴起时各种readme文档的古早味。这种文档风格有特定名称吗？

*****

####  处男鉴黄师  
##### 3#       发表于 2022-10-15 22:42

如果网络科学哪用那么麻烦，原版就有一键部署脚本<img src="https://static.saraba1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

*****

####  yanchi  
##### 4#         楼主| 发表于 2022-10-15 22:52

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57928012&amp;ptid=2099898" target="_blank">nordicvan 发表于 2022-10-15 22:36</a>

楼主这个文档风格乍一看像markdown但其实不是，很有互联网刚兴起时各种readme文档的古早味。这种文档风格有 ...</blockquote>
说来惭愧，我这是用 org 写好后直接导出成这种纯文本形式

你这么一说让我也有种很复古的感觉，我还特意去看了下文档，遗憾的是文档里并没有提及这是什么风格，只是说
 <blockquote>This is the simplest and most direct text output.</blockquote>

<img src="https://static.saraba1st.com/image/smiley/face2017/026.png" referrerpolicy="no-referrer">

*****

####  实在是不会起名  
##### 5#       发表于 2022-10-15 22:59

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  yanchi  
##### 6#         楼主| 发表于 2022-10-15 23:21

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57928495&amp;ptid=2099898" target="_blank">实在是不会起名 发表于 2022-10-15 22:59</a>

考虑到不管是naifu还是webui用的都是venv虚拟环境，我觉得没有必要装Anaconda，直接装原版python就行 ...</blockquote>
第一次装的时候的确看到 webui 使用的 venv，但是我没有用过，并且我也不懂 windows 下面这些 bat 啥的逻辑

所以最后还是用了自己最熟悉的方式，这样安装卸载啥的我也都清楚，对我这样的小白最友好了

*****

####  实在是不会起名  
##### 7#       发表于 2022-10-15 23:26

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  碧琟  
##### 8#       发表于 2022-10-15 23:48

最喜欢那种烹饪手册般的教程了，从头照着一步一步做就行了。

楼主有空能不能讲一下如何训练风格

*****

####  桐江  
##### 9#       发表于 2022-10-15 23:55

<img src="https://static.saraba1st.com/image/smiley/face2017/045.png" referrerpolicy="no-referrer">蹲

*****

####  Lisylfn  
##### 10#       发表于 2022-10-15 23:55

 本帖最后由 Lisylfn 于 2022-10-15 23:56 编辑 

怎么还用anaconda自带的shell<img src="https://static.saraba1st.com/image/smiley/face2017/037.png" referrerpolicy="no-referrer">

Windows终端开powershell, conda init powershell, 视情况set-executionpolicy remotesigned

另外强烈建议安装miniconda而不是anaconda

*****

####  meltykiss  
##### 11#       发表于 2022-10-16 00:01

这叫强行折腾

*****

####  774252330  
##### 12#       发表于 2022-10-16 00:17

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57929450&amp;ptid=2099898" target="_blank">碧琟 发表于 2022-10-15 23:48</a>

最喜欢那种烹饪手册般的教程了，从头照着一步一步做就行了。

楼主有空能不能讲一下如何训练风格 ...</blockquote>
这两天尝试训练了一个同人本作者的画风，得到的结果还行

大致流程参考坛友的[Textual Inversion](https://www.bilibili.com/video/BV1ae4y1S7v9)

总结了几点要注意的地方：

1.数据一定要进行预处理，包括裁减大小，消除多余部分，以及校对deepdanbooru生成的标识（这部分工作量很大，但是对效果的提升很显着）

2.数据可以数量少，但一定要质量高，可以用CG图就不要用漫画，彩图和黑白图比例适中，人物的空间位置（头像、半身、全身）比例也要合适

3.训练过程也很玄学，有时越训练结果越糟，注意到训练结果越来越离谱时就要从之前的自动保存的结果里面选一个效果比较好的来重新训练

*****

####  相参降解社畜  
##### 13#       发表于 2022-10-16 00:35

楼主的逻辑很清晰了，赞一个，linux系统上进行部署思路基本也是类似的

不过要严谨一点说的话，部署硬件需求还是要GPU的，软件方面需要安装好GPU的驱动、CUDA以及cudnn

*****

####  eulereld  
##### 14#       发表于 2022-10-16 00:50

 本帖最后由 eulereld 于 2022-10-16 00:51 编辑 

<img src="https://static.saraba1st.com/image/smiley/face2017/018.png" referrerpolicy="no-referrer">原帖少了uninstall步骤，这帖有教到安心多了，我一纯文系小白没教科书啥都不懂，又不欈用整合包
是说能不能再手把手指教一下，没有设xformers的情况要怎么开启运行？

*****

####  天下有狗狗  
##### 15#       发表于 2022-10-16 00:53

感谢楼主
写教程什么的一直是我的弱点
<img src="https://static.saraba1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer"> 自己顺手就能弄好的东西就是写不出来

—— 来自 Xiaomi M2007J1SC, Android 12上的 [S1Next-鹅版](https://github.com/ykrank/S1-Next/releases) v2.5.4

*****

####  eulereld  
##### 16#       发表于 2022-10-16 00:53

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57929573&amp;ptid=2099898" target="_blank">Lisylfn 发表于 2022-10-15 23:55</a>
怎么还用anaconda自带的shell

Windows终端开powershell, conda init powershell, 视情况set-executi ...</blockquote>
我也觉得anaconda太大了，但用miniconda其他要输入全是一样的吗？

*****

####  宵神乐  
##### 17#       发表于 2022-10-16 00:55

原贴确实乱看得头大

*****

####  Lisylfn  
##### 18#       发表于 2022-10-16 01:01

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57930277&amp;ptid=2099898" target="_blank">eulereld 发表于 2022-10-16 00:53</a>
我也觉得anaconda太大了，但用miniconda其他要输入全是一样的吗？</blockquote>
一模一样

—— 来自 [S1Fun](https://s1fun.koalcat.com)

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| eulereld| + 1|好的謝!|

查看全部评分

*****

####  该用户不存在  
##### 19#       发表于 2022-10-16 01:22

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  yanchi  
##### 20#         楼主| 发表于 2022-10-16 09:13

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57929450&amp;ptid=2099898" target="_blank">碧琟 发表于 2022-10-15 23:48</a>
最喜欢那种烹饪手册般的教程了，从头照着一步一步做就行了。

楼主有空能不能讲一下如何训练风格 ...</blockquote>
抱歉，我还没有用过这个功能，可以看一下别人的教程。

我看下面回你的坛友说得就挺好的，具体咨询一下他吧。

*****

####  綠茶椰菜花  
##### 21#       发表于 2022-10-16 09:18

好家伙，喂饭到嘴里，思路步骤好清晰，感谢楼主

*****

####  yanchi  
##### 22#         楼主| 发表于 2022-10-16 09:18

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57929573&amp;ptid=2099898" target="_blank">Lisylfn 发表于 2022-10-15 23:55</a>
怎么还用anaconda自带的shell

Windows终端开powershell, conda init powershell, 视情况set-executi ...</blockquote>
看不懂啊大佬<img src="https://static.saraba1st.com/image/smiley/face2017/026.png" referrerpolicy="no-referrer">

我想过把 anaconda 提供的 prompt 添加到 Windows terminal 里，但看了一眼快捷方式的详细信息就放弃了

*****

####  yanchi  
##### 23#         楼主| 发表于 2022-10-16 09:22

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57930256&amp;ptid=2099898" target="_blank">eulereld 发表于 2022-10-16 00:50</a>
原帖少了uninstall步骤，这帖有教到安心多了，我一纯文系小白没教科书啥都不懂，又不欈用整合包
是 ...</blockquote>
抱歉，之前写的不太清晰，主楼更新了一下，可以重新看一下。

简单来说，如果你没装的话，就直接运行 `python webui.py' 就行了，后面的参数是可选的。

---

miniconda 的操作也是完全一致的，我们只需要用到里面的 Anaconda Powershell Prompt

﹍﹍﹍

评分

 参与人数 1战斗力 +1

|昵称|战斗力|理由|
|----|---|---|
| eulereld| + 1|了解!|

查看全部评分

*****

####  すぴぱら  
##### 24#       发表于 2022-10-16 09:30

为啥还要上wsl，按照webui的说明弄个便携版python放到父目录然后改一下webui user.bat里的环境变量就行了…纯绿色甚至不需要安装卸载之类的

*****

####  Lisylfn  
##### 25#       发表于 2022-10-16 09:32

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57932549&amp;ptid=2099898" target="_blank">yanchi 发表于 2022-10-16 09:18</a>

看不懂啊大佬

我想过把 anaconda 提供的 prompt 添加到 Windows terminal 里，但看了一眼快捷方 ...</blockquote>
用windows终端打开powershell的标签(或者你直接开powershell, 不用Windows终端也是一样的), 然后输入 conda init powershell复制代码
重启一下终端

因为系统默认设置, 可能会出现"在此系统中禁止运行脚本"的警告, 管理员打开powershell, 运行 set-executionpolicy remotesigned复制代码改策略

同样是出现(base)就算成功了, 然后你的powershell就设置好conda环境, 可以执行conda activate相关的命令了, 不再需要anaconda powershell prompt

*****

####  Antonidas  
##### 26#       发表于 2022-10-16 09:35

提示: 作者被禁止或删除 内容自动屏蔽

*****

####  yanchi  
##### 27#         楼主| 发表于 2022-10-16 10:18

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57932661&amp;ptid=2099898" target="_blank">Lisylfn 发表于 2022-10-16 09:32</a>

用windows终端打开powershell的标签(或者你直接开powershell, 不用Windows终端也是一样的), 然后输入

重 ...</blockquote>
我懂了，不过前提是还需要把 anaconda 添加到环境变量里吧。如果是一路默认安装下来，anaconda 默认是不添加到环境变量里的，感觉比我更小白的不一定知道怎么添加，还是尽量减少可能遇到的问题吧

*****

####  yanchi  
##### 28#         楼主| 发表于 2022-10-16 10:20

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57932699&amp;ptid=2099898" target="_blank">Antonidas 发表于 2022-10-16 09:35</a>

有cpu和内存版本教程来一个么？

显卡实在太弱了，不想换</blockquote>
在运行 `python webui.py' 时后面添加参数 --with-cpu

python webui.py --with-cpu

但这样出图据说很慢，并且还有别的问题，你可以自己试一下

*****

####  violettor  
##### 29#       发表于 2022-10-16 11:11

感谢楼主，有没有针对整合包版sd webui的xformers安装教程呀...

*****

####  yanchi  
##### 30#         楼主| 发表于 2022-10-16 11:19

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57933859&amp;ptid=2099898" target="_blank">violettor 发表于 2022-10-16 11:11</a>

感谢楼主，有没有针对整合包版sd webui的xformers安装教程呀...</blockquote>
整合包版操作过程也跟我说的一样

如果你用的整合包版，你也会有一个对应的 python 环境，打开那个 python 环境，把自己电脑对应的 whl 文件放到项目里，在项目目录下运行 pip install xformers-&lt;替换成相对应的&gt;.whl 就可以了


*****

####  碧琟  
##### 31#       发表于 2022-10-16 16:07

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57932501&amp;ptid=2099898" target="_blank">yanchi 发表于 2022-10-16 09:13</a>

抱歉，我还没有用过这个功能，可以看一下别人的教程。

我看下面回你的坛友说得就挺好的，具体咨询一下他 ...</blockquote>
好的，谢谢

*****

####  碧琟  
##### 32#       发表于 2022-10-16 16:07

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57929896&amp;ptid=2099898" target="_blank">774252330 发表于 2022-10-16 00:17</a>

这两天尝试训练了一个同人本作者的画风，得到的结果还行

大致流程参考坛友的Textual Inversion

总结了几 ...</blockquote>
非常感谢

*****

####  k1no  
##### 33#       发表于 2022-10-16 17:06

感谢楼主让我这个小白也玩得上

*****

####  mimighost  
##### 34#       发表于 2022-10-16 17:09

为啥不直接上docker

*****

####  nekomimimode  
##### 35#       发表于 2022-10-17 04:16

 本帖最后由 nekomimimode 于 2022-10-17 04:17 编辑 

虽然但是, s1的整合包也可以自己git pull的....无非是环境路径全部指向了包里面, 这个带来的好处是明面上不支持win7的py310在win7下也跑得好好的<img src="https://static.saraba1st.com/image/smiley/face2017/067.png" referrerpolicy="no-referrer">

*****

####  violettor  
##### 36#       发表于 2022-10-17 18:21

ValueError: When running in Google Colab or when localhost is not accessible, a shareable link must be created. Please set share=True.

请问下这个报错怎么解决呀

*****

####  yanchi  
##### 37#         楼主| 发表于 2022-10-18 19:14

 本帖最后由 yanchi 于 2022-10-18 22:33 编辑 
<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57959081&amp;ptid=2099898" target="_blank">violettor 发表于 2022-10-17 18:21</a>

ValueError: When running in Google Colab or when localhost is not accessible, a shareable link must  ...</blockquote>
看描述是你没开启本地端口映射或者是在 google colab 里跑的，所以需要有个可供分享出来的链接

你先运行下 `python webui.py --help' 看下有没有 share 相关的参数吧，有的话就在运行 `python webui.py' 后面加上；没有的话你可能得改一下 webui.py 里的代码，不知道你有没有这个基础

我现在电脑不在身边，没法帮你查明是啥问题

---

看了一下，有个参数是 `--share'，这样运行 `python webui.py --share' 就行了，但是需要有个公网 ip，没有的话需要用 ngrok 一类的做转发；感觉你的问题是不是在 colab 里跑的，本地的话应该不会访问不了本地端口

*****

####  藤田有静  
##### 38#       发表于 2022-10-18 19:44

1 硬性要求

══════════

  • 电脑

  • 手

<img src="https://static.saraba1st.com/image/smiley/face2017/001.png" referrerpolicy="no-referrer">本地部署还是要附带一下硬件最低要求

*****

####  yanchi  
##### 39#         楼主| 发表于 2022-10-18 22:35

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57977423&amp;ptid=2099898" target="_blank">藤田有静 发表于 2022-10-18 19:44</a>

1 硬性要求

══════════</blockquote>
但这个的确没啥苛刻的硬件要求吧，cpu 也能跑，只是速度巨慢

*****

####  violettor  
##### 40#       发表于 2022-10-18 23:01

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57976970&amp;ptid=2099898" target="_blank">yanchi 发表于 2022-10-18 19:14</a>

看描述是你没开启本地端口映射或者是在 google colab 里跑的，所以需要有个可供分享出来的链接

你先运行 ...</blockquote>
谢谢，排查了一下，应该是关了梯子的原因

*****

####  タマネギ  
##### 41#       发表于 2022-11-3 13:02

运行webui user后出现troch not use gpu。查了下是cude版本和gpu版本不匹配。怎么破。电脑小白真不懂。

*****

####  yanchi  
##### 42#         楼主| 发表于 2022-11-3 14:07

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=58255060&amp;ptid=2099898" target="_blank">タマネギ 发表于 2022-11-3 13:02</a>

运行webui user后出现troch not use gpu。查了下是cude版本和gpu版本不匹配。怎么破。电脑小白真不懂。 ...</blockquote>
额，下载对应的版本？

我没遇到过这个问题，可以到 github 上的 issue 里搜搜有没有遇到过类似问题的。不好意思啦

*****

####  タマネギ  
##### 43#       发表于 2022-11-3 15:12

<blockquote>yanchi 发表于 2022-11-3 14:07
额，下载对应的版本？

我没遇到过这个问题，可以到 github 上的 issue 里搜搜有没有遇到过类似问题的。 ...</blockquote>
试了下Cpu可行。但那速度。。。还是得用gpu啊

*****

####  タマネギ  
##### 44#       发表于 2022-11-3 15:18

用skip torch cude test可以人跳过去进入画面，但没吊用，每次出图就报错

*****

####  dakupola  
##### 45#       发表于 2022-11-3 15:22

等一个docker一键

*****

####  dakupola  
##### 46#       发表于 2022-11-3 15:22

等一个docker一键

*****

####  phorcys02  
##### 47#       发表于 2022-11-3 15:27

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=57928012&amp;ptid=2099898" target="_blank">nordicvan 发表于 2022-10-15 22:36</a>

楼主这个文档风格乍一看像markdown但其实不是，很有互联网刚兴起时各种readme文档的古早味。这种文档风格有 ...</blockquote>
ASCII art 

新闻组 时代的产物

那个年代大部分计算机没有图形界面

*****

####  yanchi  
##### 48#         楼主| 发表于 2022-11-3 15:41

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=58256675&amp;ptid=2099898" target="_blank">タマネギ 发表于 2022-11-3 15:12</a>

试了下Cpu可行。但那速度。。。还是得用gpu啊</blockquote>
盲猜一下啊，你是不是没用 conda，而是自己用的 python -m venv 这种方式？

这种方式我最开始试过，但是发现还需要自己安装 cuda 环境。貌似是这个原因：如果你从清华源下载 torch 的话没有 cuda 的相关东西，需要自己从 pytorch 官网上装。

我实在太懒，不想在电脑上装乱七八糟的环境，看了下 environment-wsl2.yaml 里用的 conda，会额外下载相关的 cudatoolkit，就不需要在本机装 cuda 环境了。所以就用的那个 yaml 文件，就什么都不用操心了，日后卸载也方便

*****

####  タマネギ  
##### 49#       发表于 2022-11-3 15:42

<blockquote>yanchi 发表于 2022-11-3 14:07
额，下载对应的版本？

我没遇到过这个问题，可以到 github 上的 issue 里搜搜有没有遇到过类似问题的。 ...</blockquote>
看了下github上的解法基本就是跑cpu。服了

*****

####  タマネギ  
##### 50#       发表于 2022-11-3 15:46

<blockquote>yanchi 发表于 2022-11-3 15:41
盲猜一下啊，你是不是没用 conda，而是自己用的 python -m venv 这种方式？

这种方式我最开始试过，但是 ...</blockquote>
的确是的。去pytroch官网看了下，看不懂，请教下要下些什么，怎样装，要怎么调教的厶？

*****

####  yanchi  
##### 51#         楼主| 发表于 2022-11-3 15:57

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=58257218&amp;ptid=2099898" target="_blank">タマネギ 发表于 2022-11-3 15:46</a>

的确是的。去pytroch官网看了下，看不懂，请教下要下些什么，怎样装，要怎么调教的厶？ ...</blockquote>
首先我得说下，我自己是没用 python -m venv 这个方法跑通的（我看到又要下 cuda，又要自己下 pytorch 就换用 conda 了），所以说仅供参考

1. 去英伟达网站上下载 cuda 套装

[https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)

安装到电脑上后，确定 nvcc -V 有输出

ps：我看到 torch 只支持 11.7 版本，不知道 11.8 是否兼容，自己考虑装哪个版本，我推荐是装 11.7

2. 进 pytorch 官网，选择自己对应的环境，以 pip 安装为例

pip3 install --force-reinstall torch torchvision torchaudio --extra-index-url [https://download.pytorch.org/whl/cu117](https://download.pytorch.org/whl/cu117)

如果你之前用 pip 安装了 torch，那就得加上 --force-reinstall 这个参数

---

之后再测试下是否正常吧，再次说下仅供参考，我也不确定这种方法能不能跑通

*****

####  タマネギ  
##### 52#       发表于 2022-11-4 12:12

<blockquote>yanchi 发表于 2022-11-3 15:57
首先我得说下，我自己是没用 python -m venv 这个方法跑通的（我看到又要下 cuda，又要自己下 pytorch 就 ...</blockquote>
ok了，谢了老铁。

我个八经验，cuda在版本11.0以下的话，是跑不起来的。大概这样

*****

####  狂鸟渡渡  
##### 53#       发表于 2022-11-5 11:50

 本帖最后由 狂鸟渡渡 于 2022-11-5 11:51 编辑 

很好的教程 把另一个帖子的ckpt拿过来就能用

用主楼的方法装xformers在我的平台上会报torch相关的依赖错误 折腾半天最后用wiki里的办法解决 成功跑起来了
 <blockquote>If you use a Pascal, Turing, Ampere, Lovelace or Hopper card with Python 3.10, you shouldn't need to build manually anymore. Uninstall your existing xformers and launch the repo with --xformers. A compatible wheel will be installed.   [https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Xformers)</blockquote>

*****

####  处男鉴黄师  
##### 54#       发表于 2022-11-14 15:54

[https://ghproxy.com](https://ghproxy.com) 已被墙，求其他的git clone代理方法<img src="https://static.saraba1st.com/image/smiley/face2017/004.gif" referrerpolicy="no-referrer">

*****

####  秒速三千转  
##### 55#       发表于 2022-11-14 16:18

 本帖最后由 秒速三千转 于 2022-11-14 16:22 编辑 

我推荐B站大佬的整合包，下载，解压，打开启动助手就可以玩了，启动助手支持纯CPU硬算和笔记本核显、独显切换
[https://www.bilibili.com/video/BV1MK411S7Uh](https://www.bilibili.com/video/BV1MK411S7Uh)

还跟新了新的中文模型包，支持中文输入，下载，覆盖就可以用了
[https://www.bilibili.com/video/BV1Qd4y1F7ai](https://www.bilibili.com/video/BV1Qd4y1F7ai)

迫真把饭喂嘴里，顺带帮你按几下下巴咀嚼<img src="https://static.saraba1st.com/image/smiley/face2017/220.png" referrerpolicy="no-referrer">

*****

####  yanchi  
##### 56#         楼主| 发表于 2022-11-14 17:49

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=58431703&amp;ptid=2099898" target="_blank">处男鉴黄师 发表于 2022-11-14 15:54</a>

https://ghproxy.com 已被墙，求其他的git clone代理方法</blockquote>
没有吧，我这里还能用；ghproxy 提供的是 git 一类流量的代理（我不懂这是啥，但是跟用浏览器访问是不一样的），不能用 ghproxy.com/https://github.com/xxxx 这样的方式在浏览器里访问

如果 ghproxy 在你那边不能用的话，可以试试用 gitclone 或者 hub.fastgit.xyz 这些网站

*****

####  kk霖洞九  
##### 57#       发表于 2022-11-14 17:53

Mark

*****

####  套路设计师  
##### 58#       发表于 2023-4-17 01:32

装了整合包，启动不了是什么情况？启动器依赖装了。

<img src="https://img.saraba1st.com/forum/202304/17/013202wbhkoe5lr3e34a44.png" referrerpolicy="no-referrer">

<strong>sd.png</strong> (246.78 KB, 下载次数: 0)

下载附件

2023-4-17 01:32 上传

*****

####  itsmyrailgun  
##### 59#       发表于 2023-4-17 02:13

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60485664&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 01:32</a>

装了整合包，启动不了是什么情况？启动器依赖装了。</blockquote>
搭个梯子试试

*****

####  Kym1908  
##### 60#       发表于 2023-4-17 08:55

而你，我的朋友，你才是真正的英雄


*****

####  すぴぱら  
##### 61#       发表于 2023-4-17 09:00

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60485664&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 01:32</a>

装了整合包，启动不了是什么情况？启动器依赖装了。</blockquote>

字体损坏了吧，提示了fonts无法加载


*****

####  yanchi  
##### 62#         楼主| 发表于 2023-4-17 13:42

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60485664&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 01:32</a>

装了整合包，启动不了是什么情况？启动器依赖装了。</blockquote>
不知道整合包是啥情况，建议去看你用的整合包的说明

但是看报错信息，是说缺少 Roboto 字体，可能是这个字体没下下来吧


*****

####  套路设计师  
##### 63#       发表于 2023-4-17 18:31

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60490773&amp;ptid=2099898" target="_blank">yanchi 发表于 2023-4-17 13:42</a>

不知道整合包是啥情况，建议去看你用的整合包的说明

但是看报错信息，是说缺少 Roboto 字体，可能是这个 ...</blockquote>
我看过字体文件夹，这个字体是下下来的。

我重新下一遍整合包试试


*****

####  宵神乐  
##### 64#       发表于 2023-4-17 18:34

直接上github给出安装也就4 5步？前提是你科技上网


*****

####  某浩  
##### 65#       发表于 2023-4-17 19:04

其实最难的部分，你都没有讲啊。

1、网络问题（如果有条件能翻墙到官方pip下载python 包，会减少无数错误。墙内的镜像经常缺包，或者下载错误，失败），建议几个大包: pytorch，xformers，transformers等，先下载对应的版本在本地，然后修改requirements.txt文件，让他在本地安装

2、cuda显卡的版本要和 pytorch 一致。举例子来讲，” pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117  “ ，这个 cu117 就是你 cuda 的安装版本，经常有人 cuda 安装了 118 或者更高，但是torch版本缺对不上。特别是傻瓜包，基本问题都是出自这里


*****

####  套路设计师  
##### 66#       发表于 2023-4-17 19:20

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60490773&amp;ptid=2099898" target="_blank">yanchi 发表于 2023-4-17 13:42</a>

不知道整合包是啥情况，建议去看你用的整合包的说明

但是看报错信息，是说缺少 Roboto 字体，可能是这个 ...</blockquote>
外网搜了一圈，才发现原来是路径里竟然不能出现 [] 符号。总算解决了。

中文圈有很多疑难解答，但竟然没什么人提这个问题，

难道是因为中国人不用 [] 或者普遍用 【】？

*****

####  shangshicc  
##### 67#       发表于 2023-4-17 19:21

感谢大佬


*****

####  套路设计师  
##### 68#       发表于 2023-4-17 21:03

sd有办法只对图片高清化吗？

就像那些ai高清修复软件那样

*****

####  yanchi  
##### 69#         楼主| 发表于 2023-4-17 21:06

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60495244&amp;ptid=2099898" target="_blank">某浩 发表于 2023-4-17 19:04</a>

其实最难的部分，你都没有讲啊。

1、网络问题（如果有条件能翻墙到官方pip下载python 包，会减少无数错误 ...</blockquote>
1. 这个文中讲 git 的时候说过可以替换成国内源。并且 51 楼实际上有讲，后续更新忘了加上了，这是我的问题。不过照最近几人的经验，都没有遇到缺包的情况。

2. 这个实际上我感觉不是什么问题，webui 指定用的 torch 版本是 11.7，我自己装的是 12.1，其他人装的是 11.8，都没遇到过版本不一致导致出错的问题。版本不一致出错，可能是启动器啥其他原因导致的吧

*****

####  yanchi  
##### 70#         楼主| 发表于 2023-4-17 21:08

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60495472&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 19:20</a>

外网搜了一圈，才发现原来是路径里竟然不能出现 [] 符号。总算解决了。

中文圈有很多疑难解答，但竟然没 ...</blockquote>
可能是之前没人在文件名里加上 [] 这种符号吧，如果整合包就是这样起的名，估计也有说明吧


*****

####  yanchi  
##### 71#         楼主| 发表于 2023-4-17 21:29

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60496928&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 21:03</a>

sd有办法只对图片高清化吗？

就像那些ai高清修复软件那样</blockquote>
不行吧，我只知道能文生图、图生图，对图片高清化一般都是用 waifu2x 吧，用 sd 难免会对原图做些修改


*****

####  套路设计师  
##### 72#       发表于 2023-4-17 22:04

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60497300&amp;ptid=2099898" target="_blank">yanchi 发表于 2023-4-17 21:29</a>

不行吧，我只知道能文生图、图生图，对图片高清化一般都是用 waifu2x 吧，用 sd 难免会对原图做些修改 ...</blockquote>
waifu2x主要还是放大吧，而且还是专门针对卡通图的，

我是画背景图，用下来效果不太行。

其实对原图有一点修改也没问题，只要能变清晰，我用SD图生图，始终没法生出清晰的图


*****

####  yanchi  
##### 73#         楼主| 发表于 2023-4-17 22:59

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60497696&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 22:04</a>

waifu2x主要还是放大吧，而且还是专门针对卡通图的，

我是画背景图，用下来效果不太行。</blockquote>
好吧，不过我也没啥解决办法，只是搭建起来自己用了一会儿，没仔细研究过这东西，估计得找专门玩这个的大佬问问咋解决


*****

####  桧川直巳  
##### 74#       发表于 2023-4-17 23:09

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60497696&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-17 22:04</a>

waifu2x主要还是放大吧，而且还是专门针对卡通图的，

我是画背景图，用下来效果不太行。</blockquote>
git上找multidiffusion插件，可以把图分块放进网络放大，避免显存溢出


*****

####  191634  
##### 75#       发表于 2023-4-17 23:39

版本管理不妨试试PDM


*****

####  asergh0630rx  
##### 76#       发表于 2023-4-18 00:48

对小白来说用github官方软件应该比git方便点


*****

####  冬眠的龙凰  
##### 77#       发表于 2023-4-18 01:27

每次更新都会爆炸，折腾了一晚上都没折腾好，以后不追新版本了……


*****

####  yanchi  
##### 78#         楼主| 发表于 2023-4-18 02:40

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60499433&amp;ptid=2099898" target="_blank">asergh0630rx 发表于 2023-4-18 00:48</a>

对小白来说用github官方软件应该比git方便点</blockquote>
主要是考虑这个教程里绝大多数步骤都是在命令行下完成的，所以选择 git 也在命令行中进行，并且教程中用到的 git 命令也很简单，复制粘贴就好了；如果用 GitHub 的官方软件操作上可能会简单点，但对小白来说还要去学习怎么使用，可能会出其它问题

*****

####  yanchi  
##### 79#         楼主| 发表于 2023-4-18 02:43

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60499647&amp;ptid=2099898" target="_blank">冬眠的龙凰 发表于 2023-4-18 01:27</a>

每次更新都会爆炸，折腾了一晚上都没折腾好，以后不追新版本了……</blockquote>
就我所知，webui 轻易不怎么更新依赖库，唯一一次印象深的就是升级了 gradio 的版本，如果不升级项目会跑不起来。并且就这种大项目，如果改个依赖库的版本，就真的是牵一发而动全身吧，还是跟着官方指定的版本走最好了


*****

####  套路设计师  
##### 80#       发表于 2023-4-18 22:54

画背景图的时候经常出现多层图怎么办？有什么反向提示词可以设置吗？

我是垂直布局

*****

####  harukiiii  
##### 81#       发表于 2023-4-18 23:00

逻辑清晰，给力

[论坛助手,iPhone](https://bbs.saraba1st.com/2b/forum.php?mod=viewthread&amp;tid=2029836)

*****

####  yanchi  
##### 82#         楼主| 发表于 2023-4-22 00:37

<blockquote><a href="httphttps://bbs.saraba1st.com/2b/forum.php?mod=redirect&amp;goto=findpost&amp;pid=60512128&amp;ptid=2099898" target="_blank">套路设计师 发表于 2023-4-18 22:54</a>

画背景图的时候经常出现多层图怎么办？有什么反向提示词可以设置吗？

我是垂直布局 ...</blockquote>
不懂这个，建议找大佬问一下吧

