# fast-llm-template

## env

uv + poetry

### 安装 uv

下载 https://github.com/astral-sh/uv/releases

```bash
which uv
```

### 安装 poetry

https://python-poetry.org/docs/ 官方的要求是建在虚拟环境中，以防止异常升级造成环境破坏。

```bash
# 修改 .env
cp .env.example .env
# 修改 .env 中的 变量

# 初始化环境和安装 poetry
build.sh
# 载入环境
. .env
# 验证
which poetry

# 添加依赖:
poetry lock
poetry install --no-root

# 运行
poetry run python main.py
```

### 项目环境:
```bash
. .envrc
uv pip install -r uv.poetry.txt
uv pip install -r requirements.txt
```


## QA

1 变量 VENV_ROOT VENV_PATH 用来干什么

```bash
VENV_ROOT=~/.py/venvs/
VENV_PATH=~/.py/venvs/llm
```
VENV_ROOT 为了把所有的虚拟环境放在一个公共目录下，方便管理。不设置默认为项目目录

VENV_PATH 为了指定当前项目的虚拟环境的位置。默认为 VENV_ROOT/.项目名

开发环境建议设置在公共目录下，生产环境建议设置在项目目录下。


## error 
