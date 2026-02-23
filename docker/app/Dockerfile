
FROM python:3.10

# MariaDB用のパッケージ追加
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential && rm -rf /var/lib/apt/lists/*

# 開発ユーザーを作成
# UID/GIDは開発ホストに合わせて必要に応じて変更。WSL2初期ユーザーは1000:1000で作成される。
# ユーザー名/グループ名は一致させる必要なし。
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID appgroup \
    && useradd -m -u $UID -g $GID appuser

# Pythonパッケージインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY ./msmtprc /etc/msmtprc

# 作業ディレクトリ設定
# WORKDIR /my-app

# 一般ユーザーへ切替
USER appuser

# デフォルトのコマンド指定
# 何も指定しないなら即終了する

# シェルを起動する:composeでttyとstdin_openをtrueにしないと即終了
#CMD ["/usr/bin/bash"]
# 待機するだけの状態にするテクニック
CMD ["/usr/bin/tail","-f","/dev/null"]

# シンプルなHTTPサーバー
# /my-workディレクトリ配下を公開する
#CMD ["/usr/local/bin/python3", "-m","http.server", "8000", "--directory","/my-work"]

# DjangoのHTTPサーバー
# ※ プロジェクト作成後でないとダメ
#CMD ["/usr/local/bin/python3", "manage.py", "0.0.0.0:8000"]
