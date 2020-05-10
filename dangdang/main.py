from scrapy import cmdline
#导入cmdline模块,可以实现控制终端命令行。
import os  # 用来设置路径
import sys  # 调用系统环境，就如同cmd中执行命令一样
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
cmdline.execute(['scrapy', 'crawl', 'dangdang'])
# #用execute（）方法，输入运行scrapy的命令。