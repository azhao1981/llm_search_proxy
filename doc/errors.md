## install pycld2 

答案：不能用3.11.9
实测 3.10 可用
uv venv ~/.py/venvs/llm310
uv pip install -r requirements.txt
source /home/weiz/.py/venvs/llm310/bin/activate

uv 不能安装，好像 conda 就可以
要安装 clang


解决：
 CPPFLAGS="-std=c++98" pip install pycld2
 CPPFLAGS="-std=c++03" pip install pycld2

`CPPFLAGS="-std=c++98"` 和 `CPPFLAGS="-std=c++03"` 的区别在于它们指定的 C++ 标准版本不同：

1. **`CPPFLAGS="-std=c++98"`**：
   - 指定使用 C++98 标准。
   - C++98 是第一个国际标准化的 C++ 版本，于 1998 年发布。
   - 它定义了许多基础的 C++ 特性，但缺乏一些现代特性和改进。

2. **`CPPFLAGS="-std=c++03"`**：
   - 指定使用 C++03 标准。
   - C++03 是对 C++98 的一个小修订版，于 2003 年发布。
   - 它主要是对 C++98 的一些错误修正和细微改进，没有引入新的语言特性。

总结：
- 两者基本上是相同的，C++03 是对 C++98 的一个小幅修订。
- 在大多数情况下，使用这两个选项编译代码不会有明显的区别。
- 
ref:

https://github.com/CLD2Owners/cld2/issues/47

https://github.com/emk/rust-cld2/issues/2

原因：

CLD2 is not compatible with GCC 6 because it assigns negative values to varibales typed unsigned. (see internal/cld_generated_cjk_uni_prop_80.cc) The support ...

Error installing cld2 gem with gcc 6+ #2804
https://github.com/mastodon/mastodon/issues/2804
这个是 ruby的项目，也有 cld2的问题

这里建议使用 cld3 ,而且有详细出问题的原因
https://git.chinwag.org/chinwag/chinwagsocial/commit/d5cabfe5c65ac29d2f9c151b46c01a9fd885a9e0

这个是google的C库
https://github.com/CLD2Owners/cld2

这个是python
https://github.com/aboSamoor/pycld2/

有出3了

https://github.com/google/cld3

https://pypi.org/project/gcld3/

```bash
pip install gcld3
```

Python Extension for CLD2

https://bofeng.github.io/post/python-extension-for-cld2/

CFLAGS=-stdlib=libc++ pip install pycld2
x86_64-linux-gnu-gcc: error: unrecognized command-line option ‘-stdlib=libc++’
error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
[end of output]

https://github.com/aboSamoor/pycld2

https://www.cnblogs.com/leimu/p/14810464.html
polyglot 安装和使用

特征
语言检测 Language Detection (支持196种语言)
分句、分词 Tokenization (支持165种语言)
实体识别 Named Entity Recognition (支持40种语言)
词性标注 Part of Speech Tagging(支持16种语言)
情感分析 Sentiment(支持136种语言)
词嵌入 Word Embeddings(支持137种语言)
翻译 Transliteration(支持69种语言)
管道 Pipelines

https://www.cnblogs.com/leimu 木叶流云 NLP

```python
text_en = u"Japan's last pager provider has announced it will end its service in September 2019 - bringing a national end to telecommunication beepers, 50 years after their introduction.Around 1,500 users remain subscribed to Tokyo Telemessage, which has not made the devices in 20 years."
text_cn = u" 日本最后一家寻呼机服务营业商宣布，将于2019年9月结束服务，标志着日本寻呼业长达50年的历史正式落幕。目前大约还有1500名用户使用东京电信通信公司提供的寻呼服务，该公司在20年前就已停止生产寻呼机。"
text_mixed = text_cn + text_en
```

python -u "/home/weiz/projects/github.com/llm_search_proxy/tests/test_polyglot.py"
Segmentation fault
这个好像就是3.11.9 的问题了
conda的3.10.12没有问题

polyglot：Pipeline 多语言NLP工具
https://cloud.tencent.com/developer/article/1519291

这篇很好，但是pycld2装不上

这里已经打不开了
https://www.lfd.uci.edu/~gohlke/pythonlibs/

这个也是这个大学的网站的库，现在没有了
Links to Christoph Gohlke's GDAL and Numpy packages are dead on GDAL wiki page #863

https://github.com/domlysz/BlenderGIS/issues/863

GDAL Python Binding:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal

new link seems to be here - https://github.com/cgohlke/geospatial-wheels/releases

Numpy wheel package:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

new link seems to be here - https://github.com/cgohlke/numpy-mkl-wheels/releases

这个应该是说这个事，但怎么解决，不知道
https://pypi.org/project/gohlkegrabber/

这个也是讨论而以
https://www.reddit.com/r/Python/comments/vcaibq/christoph_gohlkes_windows_wheels_site_is_shutting/

这个好像可以了
 pip install pycld2

但 uv pip install pycld2 不行
uv pip install pip 然后再安装
python -m pip install pycld2
python -m pip install LTpycld2
也是失败的

这个也装不上，这个是0.42 比上面高一个版本
https://pypi.org/project/LTpycld2/

这个好像也没有
https://pypi.org/project/dzbee/


https://github.com/aboSamoor/pycld2/issues/34
这个是windows的
https://github.com/aboSamoor/pycld2/files/15179096/gohlke-pycld2-0.41-wheels.zip


不解决问题：
spacy-cld 无法安装的问题

https://blog.csdn.net/m0_55419239/article/details/137194249

How to determine the language of a piece of text?
https://stackoverflow.com/questions/39142778/how-to-determine-the-language-of-a-piece-of-text


因为我的版本不够 libicui18n.so.70 只有
libicui18n.so.73: cannot open shared object file: No such file or directory

https://github.com/unicode-org/icu/releases/tag/release-73-2
data用来干什么，要下载吗？
icu4c-73_2-src.zip

unzip  icu4c-73_2-src.zip
这个好像是windows的
cd icu/source
./configure
make
sudo make install

icu4c-73_2-src.tgz
tar -xzf icu4c-73_2-src.tgz
cd icu/source
./configure
make
sudo make install
安装完后在这里： 不是在 /usr/lib/x86_64-linux-gnu/ 下
ll /usr/local/lib | rg libic
export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

sudo apt-get install libicu-dev
dpkg -l | grep libicu
ll /usr/lib/x86_64-linux-gnu/ | rg libicui18n

sudo ln -s /usr/lib/x86_64-linux-gnu/libicui18n.so.72 /usr/lib/x86_64-linux-gnu/libicui18n.so.73
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH


ModuleNotFoundError: No module named 'morfessor'
pip install morfessor