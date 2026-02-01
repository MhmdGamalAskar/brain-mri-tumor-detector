FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    ninja-build \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 1) Install CPU PyTorch (compatible with detectron2 wheels)
RUN pip install --no-cache-dir \
    torch==1.10.2+cpu torchvision==0.11.3+cpu \
    -f https://download.pytorch.org/whl/cpu/torch_stable.html

# 2) Install detectron2 from official wheels (CPU + torch1.10)
RUN pip install --no-cache-dir \
    detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.10/index.html

# 3) Install app deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy everything
COPY . .

EXPOSE 7860
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]