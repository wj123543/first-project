问题 1：读取 txt 文件出现中文乱码（编码问题）
现象:初次运行`week02_text_stats.py`读取`data/week02_sentences.txt`时，控制台输出一堆问号、乱码，无法正常识别中文句子。
原因:Python 打开文件默认采用系统编码（Windows 为 gbk），而文本文件保存为 UTF-8 编码，编码不匹配导致中文解析失败。
文件路径:./data/week02_sentences.txt`