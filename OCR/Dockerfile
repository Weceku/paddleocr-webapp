# 使用官方 Python 基础镜像
FROM python:3.11-slim-buster

# 设置工作目录
WORKDIR /OCR

# 复制 requirements.txt 到工作目录
COPY requirements.txt .

# 安装依赖
RUN pip install -r requirements.txt --no-cache-dir

# 复制应用程序代码到工作目录
COPY . .

# 设置环境变量（如果需要）
# ENV PADDLE_WITH_GPU=0

# 暴露 Flask 应用的端口
EXPOSE 5000

# 定义启动命令
CMD ["python", "app.py", "--host=0.0.0.0"]