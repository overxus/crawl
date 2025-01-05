# crawl: 网页爬虫包

## 如何打包
运行以下命令打包：
```bash
python setup.py sdist bdist_wheel
```
在目录`dist`下会生成一个whl文件。

安装时运行：
```bash
pip install crawl-X.Y.Z-py3-none-any.whl
```