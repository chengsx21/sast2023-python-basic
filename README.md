# :100: SAST2023 - Cloze Test

> 程思翔 2021010761

## 🎮 基础版本

### 环境配置

使用第三方依赖项:

```python
pyperclip==1.8.2
```

使用 `pyperclip` 进行剪贴板操作, 用于复制文章到剪贴板.

### 使用设置

约定以下命令行参数:

```shell
--file    -f  <str>  文章路径  必选, 提供 'example.json' 供参考
--random  -r  <str>  游戏模式  必选, 为 'random' 或 'specific'
```

文章使用 `JSON` 存储, 的格式如下:

```json
[
    {
        "language": "语言",
        "articles": [
            {
                "title": "标题",
                "article": "空{{1}}, 空{{2}}...",
                "hints": ["提示1", "提示2", ...],
            }
        ]
    }
]
```

在 `CMD` 目录下, 运行

```shell
python main.py -f example.json -r random
```

以进行随机模式的游戏. 运行

```shell
python main.py -f example.json -r specific
```

以进行指定模式的游戏.

### 游戏功能

实现了基础功能, 包括:

+ 根据命令行参数启动, 包括: 题库数据文件路径、是否指定文章, 相关操作主要使用 `argparse` 库;

+ 读取相应题库并解析 `JSON` 文件; 解析 `JSON` 文件使用 `json` 库;

+ 在命令行中接收用户输入并将其填写到文章中, 使用 `re` 库进行替换;

+ 用户完成输入后, 将替换后的文章打印到命令行, 并支持复制到剪贴板.

程序基础版也实现了部分高级功能, 包括:

+ 鲁棒性: 使用 `try... except` 进行错误检查, 给出相应的提示;

+ 保存: 用户可以将自己得到的文章复制到剪贴板.

## 🎮 提高版本

### 环境配置

使用第三方依赖项:

```python
pyperclip==1.8.2
streamlit==1.24.1
```

使用 `pyperclip` 进行剪贴板操作, 用于复制文章到剪贴板;

使用 `streamlit` 进行图形界面开发与网页端交互.

### 使用设置

在 `GUI` 目录下运行

```shell
Streamlit run Cloze_Test.py
```

以启动网页端应用.

### 游戏功能

相比于基础版本, 提高版本增加实现的部分包括:

+ 出题: 用户可以在提供的图形窗口内出题.

+ 在提交答案后, 用户可以选择:
  
  + `Copy`: 用户可以将自己得到的文章复制到剪贴板.

  + `Restart`: 清空输入框, 重新开始当前游戏.

  + `Replay`: 开始一局新的游戏.
