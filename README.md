# 学習記録

## 1. 基本構成

- 仮想環境：VirtualBox（Vagrant未使用）

- OS：CentOS Stream
- Webサーバー：nginx
- Frontend：next.js
- Backend：Dango Rest Framework
- DB：MySQL

## 2. 環境構築 VirtualBox

### 2-1. NATとホストオンリーアダプター接続

**参考資料**  
<https://blog.proglus.jp/3315/>
<https://uktia.hatenablog.jp/entry/20191102/1572698888>

### 2-2. SSH接続

**参考資料**  
<https://qiita.com/uhooi/items/137de4578534c8e7e7f2>
<https://qiita.com/CloudRemix/items/8b318c19e001d5a9b40d>

#### 2-2-1. ローカルマシンの↓でSSH接続の設定

/Users/XXXX/.ssh/config

##### 2-2-1-1. 以下のように2つ作成

- `ssh karte.root`（ホストマシンのroot設定用）
- `ssh karte.XXXX`（ホストマシンの個別設定用）

##### 2-2-1-2. sshのパスを毎回聞かれる場合

登録確認  
`ssh-add -l`

SSH鍵をssh-agentに登録  
`ssh-add -K`
（sshのファイル名が.ssh/id_rsaなので省略でOK）

### 2-3. 時間同期

再起動すると時間同期しているが、入りっぱなしだとダメ？
`VBoxManage guestproperty set karte "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold" 1000`  
`VBoxManage setextradata "karte" "VBoxInternal/Devices/VMMDev/0/Config/GetHostTimeDisabled" 0`  

## 3. 環境構築 CentOS Stream（root権限）

- **yumはdnfに置き換え**

### 3-1. SELinuxの無効化

#### 3-1-1. 確認

`getenforce`

#### 3-1-2. コマンドで無効化

`setenforce 0`

#### 3-1-3. 永続的に無効

`vi /etc/selinux/config`

```config
SELINUX=disabled
```

### 3-2. zsh設定

参考資料
<https://qiita.com/uchiko/items/253088bb0d7bbf574bff>

### 3-3. vim設定

参考資料
<https://qiita.com/Ping/items/e8702413b79d725c07d9>

### 3-4. ファイアウォール操作

#### (nginxインストール後にhttp接続するためにhttpを追加＆リロード)  

`firewall-cmd --permanent --zone=public --add-service=http`  
`firewall-cmd --reload`  

`systemctl start firewalld.service`  
`systemctl stop firewalld.service`  
`systemctl status firewalld.service`  
`sudo firewall-cmd --state`  

### 3-5. userをsudo可能にする

#### (可能にするだけでsudoは省略できない)

`visudo`

```sudoers.d
XXXX    ALL=(ALL)       ALL
```

### 3-6. タイムゾーン

- ロケール確認  
`localectl`

- 「ja_JP.UTF-8」ではないときにロケール変更  
`localectl set-locale LANG=ja_JP.UTF-8`

- タイムゾーン確認  
`timedatectl`

- 「Time zone: Asia/Tokyo (JST, +0900)」ではないときにタイムゾーン設定  
`timedatectl set-timezone Asia/Tokyo`

### 3-7. 時刻同期

#### いまいち同期していない

`dnf install chrony`  

`sudo systemctl start churned`  
`sudo systemctl enable chronyd`  

- 確認  
`chronyc sources -v`

### 3-8. 必要なツール類を入れる  

`dnf update`  
`dnf install vim mailx unzip bash-completion net-tools wget git yum-utils which telnet sudo bind-utils man rsyslog sysstat jq`  

- これはuwsgiインストールエラー解消のために追加  
`dnf group install 'Development Tools'`  
`dnf install python39-devel`

### 3-9. MySQL8

- 最新版を確認  
`dnf info mysql`

- インストール  
`dnf install @mysql:8.0`

- 確認  
`mysql --version`

- 自動起動  
`systemctl start mysqld.service`  
`systemctl enable mysqld.service`

#### 3-9-1. mysqlの初期設定

<https://vertys.net/centos8-mysql8-install/>

- mysql_secure_installation
PASS:XXXX1234

- db作成  
`mysql -u root -p`

`> create database karte;`

### 3-10. nginx

ダウンロード用の設定？  
`vim /etc/yum.repos.d/nginx.repo`

```nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
```

#### 3-10-1. インストール  

`dnf install nginx`  
`systemctl start nginx`  
`systemctl enable nginx`

`systemctl status nginx`

- **virtualboxからのアクセス**
ホストネットワークマネージャで設定したアドレス
<http://192.168.56.11>

#### 3-10-2. djangoとの連携用

`sudo mkdir /usr/share/nginx/html/media`  
`sudo mkdir /usr/share/nginx/html/static`  

`chmod -R 775 /usr/share/nginx/html/static/`  
`chown -R root:nginx /usr/share/nginx/html/static/`  
`chmod -R 775 /usr/share/nginx/html/media/`  
`chown -R root:nginx /usr/share/nginx/html/media/`

### 3-11. python3

#### 3-11-1. 現状確認

**もう3が入っているためpython3コマンドが必要**
`python3 -V`
`pip3 -V`

#### 3-11-2. 最新の3.9をインストール

`dnf module -y install python39`  
**OSの依存関係はデフォルトの3.6を使用して、開発用にはインストールした3.9を使用する。**

- 確認（まだ3.9にはならない）  
`python3 -V`

- python3で使用するバージョンを切り替える  
`alternatives --config python3`

- 確認（3.9になるはず）  
`python3 -V`

#### 3-11-3. pipenv導入と紐付け

**3.6に紐づけてしまってWarningが出る場合はvi Pipfileで3.6⇨3.9に修正**  
`pip3 install pipenv`

### 3-12. next.js

- 準備  
`dnf module -y install nodejs:14`  
`npm install -g yarn`

- よくわからないけど、言われたままに実施  
`npx browserslist@latest --update-db`

### 3-13. NginxとuWSGIの連携

#### 3-13-1. ソケットファイルはrunディレクトリに配置が通例

##### runディレクトリに配置しないと権限エラーになる

- ただ権限絡みで動かないので、自由なディレクトリを作成。  
`mkdir /run/uwsgi`  
`chmod 775 uwsgi`  
`chown nginx:nginx uwsgi`

#### 3-13-2. /run配下は再起動で削除されるので対象外設定

**参考資料**  
<https://qiita.com/suemoc/items/e29285e8e67263298f35>

- 削除対象外の設定  
`vim /etc/tmpfiles.d/hoge.conf`

```hoge.conf
d /var/run/uwsgi 0775 nginx nginx
```

#### 3-13-3. nginxの接続ファイルを修正

`vim /etc/nginx/conf.d/project.conf`

```project.conf
# djangoに割り当てるポート
upstream django {
        server unix:///run/uwsgi/uwsgi_karte.sock;
        #server 127.0.0.1:8888;
    }

server {
    listen  80;
    server_name localhost;

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    location /static {
        alias /usr/share/nginx/html/static;
    }

    location /media {
        alias /usr/share/nginx/html/media;
    }

    location /django {
        include /home/XXXX/backend/uwsgi_params;
        uwsgi_pass django;
    }

    location / {
         proxy_pass http://localhost:3000;
    }
}
```

### 3-13-4. uwsgi_params の準備

`cd /etc/nginx/`  
`cp uwsgi_params ~/backend/karte`

**グループの設定（exit後に反映される）**

- 確認  
`id XXXX`  
`groups XXXX`

- 設定  
`usermod -aG nginx XXXX`

- 確認  
`id XXXX`  
`groups XXXX`

#### 3-13-5. uwsgiのINIファイル自動起動用のサービス作成

/etc/systemd/systemにsystemctlの自動起動用ファイル(ここではuwsgi.service)を作成  
仮想環境(pipenv)でプロジェクトを作成したため、uwsgi.serviceのExecStartには仮想環境内でpipenv --venvで確認した実行ファイルの場所を指定

`cd /etc/systemd/system`  
`vim uwsgi.service`

```uwsgi.service
[Unit]
Description = uWSGI
After = syslog.target

[Service]
ExecStart = /home/XXXX/.local/share/virtualenvs/backend-rLzvHKzg/bin/uwsgi --ini /home/XXXX/backend/karte/uwsgi/uwsgi.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=main

[Install]
WantedBy=multi-user.target
```

- **サービスファイルを変更したらデーモンリロード**  
`systemctl daemon-reload`

- **サービスファイルの確認と自動化設定**  
`systemctl status uwsgi`  
`systemctl start uwsgi`  
`systemctl enable uwsgi`

## 4. 環境構築 DangoRestFramework（user権限）

**backendディレクトリ配下で展開**
Djangoまでのアクセスは以下のようになる。

- **ブラウザ→nginx→uWSGI→Django**

## 5. 環境構築 next.js（user権限）

**frontendディレクトリ配下で展開**
Next.jsまでのアクセスは以下のようになる。

- **ブラウザ→nginx→nextjs開発サーバー**

### 5-1. next.js

**プロジェクトの作成（typescriptを使用）**  
`cd frontend`  
`npx create-next-app karte --ts`

**プロジェクト運用**  
`cd karte`  
`yarn dev`

### 5-2. Nginxの設定にnextjsの開発サーバーアクセスを追加

#### （これはroot権限の作業で実施済み）

**以下は抜粋**  
`vim /etc/nginx/conf.d/project.conf`

```project.conf
location / {
         proxy_pass http://localhost:3000;
    }
```