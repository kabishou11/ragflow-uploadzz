## 上传文档到RagFlow知识库
[RagFlow](https://github.com/infiniflow/ragflow)是一个基于 LLM 的问答系统，能够快速构建智能问答平台。然而，RagFlow 默认的知识库上传界面存在一些局限性：每次只能上传有限数量的文件，并且上传后还需手动启动解析流程，当需要上传大量文件时，这样的操作便显得有些繁琐。

为了简化这一过程，我编写了一个脚本，该脚本可以遍历指定目录，自动逐个将文档上传至 RagFlow 知识库，并立即启动解析。当一个文档解析完成后，脚本将自动上传并解析下一个文档。特别是在需要上传大量文件时，这显著减少了人工干预，避免了手动分批上传和解析的等待时间。

（例如，我自己需要将mac中所有备忘录内容导入到知识库中查询）
 测试：注意Infinity模式下不支持 table解析方式

### 创建env环境
```shell
conda create -n ragflow-upload python=3.10.13 -y
```

### 安装依赖
```shell
pip install -r requirements.txt
pip install -e .  
```

## 复制并配置[ragflows/configs.py](ragflows/configs.py)
关于配置文件的说明可参考这个：[issues #2](https://github.com/Samge0/ragflow-upload/issues/2)
```shell
cp ragflows/configs.demo.py ragflows/configs.py
```

### 上传文档
```shell
python ragflows/main.py
```

### 相关截图
![image](https://github.com/user-attachments/assets/13c93d4a-66fd-4083-ab2c-75c93ef94ab0)
![image](https://github.com/user-attachments/assets/aad9dfb0-3231-4b33-8768-08a2d99cf47e)
