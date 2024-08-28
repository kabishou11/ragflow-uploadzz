#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-08-23 16:49
# describe：

API_URL = 'http://localhost:80/v1'  # ragflow的api地址，请替换为实际的服务器地址
AUTHORIZATION = 'your authorization'  # ragflow的api鉴权token
DIFY_DOC_KB_ID = 'your kb_id'  # ragflow的知识库id
KB_NAME = "your kb_name"  # ragflow的知识库名称
PARSER_ID = "naive"  # ragflow的知识库文档解析方式

DOC_DIR = ''    # 文档目录
DOC_SUFFIX = 'md,txt,pdf,docx'    # 指定文档后缀

MYSQL_HOST = 'localhost'
MYSQL_PORT = 5455
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'infini_rag_flow'
MYSQL_DATABASE = 'rag_flow'

# 文档最少行数，低于该值的文档则被忽略，该参数仅作用于 txt,md,html 后缀文件
DOC_MIN_LINES = 1


def get_header():
    return {'authorization': AUTHORIZATION}