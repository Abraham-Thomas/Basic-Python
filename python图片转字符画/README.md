## 1.项目介绍

本项目用 50 行 Python 代码完成图片转字符画小工具。

#### 1.1 知识点

1. Python 基础
2. pillow 库的使用
3. argparse 库的使用（[参考教程](http://blog.ixxoo.me/argparse.html)）

#### 1.2 环境

- Python 3.6.9
- pillow 6.2.1

PIL 是一个 Python 图像处理库，是本课程使用的重要工具，使用下面的命令来安装 pillow（PIL）库：

```sh
$ pip install pillow
```



## 2.原理

字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（为了简化可以这么理解），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。

问题来了，我们是要转换一张彩色的图片，这么多的颜色，要怎么对应到单色的字符画上去？这里就要介绍灰度值的概念了。

> 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。

另外一个概念是 RGB 色彩：

> RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。- 来自百度百科介绍

我们可以使用灰度值公式将像素的 RGB 值映射到灰度值（注意这个公式并不是一个真实的算法，而是简化的 sRGB IEC61966-2.1 公式，真实的公式更复杂一些，不过在我们的这个应用场景下并没有必要）：

```python
gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
```

这样就好办了，我们可以创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。



## 3.步骤

在目录中创建文件ascii.py

#### 3.1导库

导入必要的库，argparse 库是用来管理命令行参数输入的

```python
from PIL import Image
import argparse
```



#### 3.2处理命令行参数

我们首先使用 argparse 处理命令行参数，目标是获取输入的图片路径、输出字符画的宽和高以及输出文件的路径：

```python
# 首先，构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 60) #输出字符画高

# 解析并获取参数
args = parser.parse_args()

# 输入的图片文件路径
IMG = args.file

# 输出字符画的宽度
WIDTH = args.width

# 输出字符画的高度
HEIGHT = args.height

# 输出字符画的路径
OUTPUT = args.output
```



#### 3.3实现 RGB 值转字符的函数

首先将 RGB 值转为灰度值，然后使用灰度值映射到字符列表中的某个字符。

下面是我们的字符画所使用的字符集，一共有 70 个字符。字符的种类与数量可以自己根据字符画的效果反复调试：

```python
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
```

下面是 RGB 值转字符的函数，注意 alpha 值为 0 的时候表示图片中该位置为空白：

```python
def get_char(r,g,b,alpha = 256):

    # 判断 alpha 值
    if alpha == 0:
        return ' '

    # 获取字符集的长度，这里为 70
    length = len(ascii_char)

    # 将 RGB 值转为灰度值 gray，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 灰度值范围为 0-255，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1)/length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]
```



#### 3.4处理图片

完成上面的代码之后，我们进入到最后一个步骤，对图片进行处理。

这一个步骤我们放入到 `if __name__ == '__main__':` 代码块中（表示如果 ascii.py 被当作 python 模块 import 的时候，这部分代码不会被执行）。图片的处理步骤如下：

1. 首先使用 PIL 的 Image.open 打开图片文件，获得对象 im
2. 使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。
3. 遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
4. 将所有的像素对应的字符拼接在一起成为一个字符串 txt
5. 打印输出字符串 txt
6. 如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，则默认输出到 `output.txt` 文件

这个过程中需要注意的是调用 getchar 时候的参数是通过 PIL 库的 getpixel 获取的，见如下代码：

```python
char = get_char(*im.getpixel((j,i)))
```

其中 `im.getpixel((j,i))` 获取得到坐标 `(j,i)` 位置的 RGB 像素值（有的时候会包含 alpha 值），返回的结果是一个元组，例如 `(1,2,3)` 或者 `(1,2,3,0)`。我们使用 `*` 可以将元组作为参数传递给 get_char，同时元组中的每个元素都对应到 get_char 函数的每个参数。

该部分的代码实现如下（注意 name 和 main 前后都是两个下划线）：

```python
if __name__ == '__main__':

    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    # 初始化输出的字符串
    txt = ""

    # 遍历图片中的每一行
    for i in range(HEIGHT):
        # 遍历该行中的每一列
        for j in range(WIDTH):
            # 将 (j,i) 坐标的 RGB 像素转为字符后添加到 txt 字符串
            txt += get_char(*im.getpixel((j,i)))
        # 遍历完一行后需要增加换行符
        txt += '\n'
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
```



## 4.测试

![卡卡西](./kkx.jpg)



在命令行执行：

```sh
$ python ascii.py kkx.jpg
```

控制台会显示：

![](./output.png)

打开 `output.txt` 文件，也能看到同样的效果。

