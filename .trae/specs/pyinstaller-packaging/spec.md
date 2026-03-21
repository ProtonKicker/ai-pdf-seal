# PyInstaller 打包功能规范

## 为什么需要此功能

当前程序需要安装 Python 环境才能运行，对非技术人员不友好。需要将程序打包成独立的 .exe 可执行文件，用户无需安装 Python，直接双击即可运行。

## 变更内容

- 使用 PyInstaller 打包项目为独立 .exe 文件
- 打包后的程序包含所有依赖，无需 Python 环境
- 用户可直接双击运行，或在命令行使用

## 影响范围

- 新增打包配置文件
- 可能需要调整代码以适应打包环境（如资源路径问题）

## 新增需求

### 需求：打包配置

| 项目 | 说明 |
|------|------|
| 打包工具 | PyInstaller |
| 输出格式 | 单文件 .exe |
| 程序名称 | ai-pdf-seal |
| 包含数据 | config.yaml（可选） |

### 需求：打包命令

```bash
pyinstaller --onefile --name ai-pdf-seal --add-data "config.yaml;." main.py
```

### 需求：打包后使用

- 直接双击 `ai-pdf-seal.exe` 运行
- 命令行运行：`ai-pdf-seal.exe -d .`
- 配置文件：自动读取同目录下的 `config.yaml`

## 注意事项

- 打包时需要包含 PyYAML 等依赖
- 某些系统可能需要 Visual C++ 运行库
- 建议在 Windows 环境打包 Windows 版本
