## install pycld2 

答案：不能用3.11.9
实测 3.10 可用
uv venv ~/.py/venvs/llm310
uv pip install -r requirements.txt
source /home/weiz/.py/venvs/llm310/bin/activate

这个是google的C库
https://github.com/CLD2Owners/cld2
这个是python
https://github.com/aboSamoor/pycld2/

有出3了
https://github.com/google/cld3
https://pypi.org/project/gcld3/
pip install gcld3

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

