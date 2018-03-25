# 필요 파일들 설치

```Shell
#up-to-date
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
```

# port 열기

/etc/apache2/ports.conf 에 들어가서 사용하고 싶은 포트를 추가하여 줍니다. 저는 8080 포트를 사용하도록하겠습니다.

```shell
Listen 8080
```

# 해당 port 연결

기존 apache 의 기본 포트인 80을 사용해도 되나 다른 포트를 사용하겠습니다.

```shell
<VirtualHost *:8080>
        ServerAdmin merryman

        #You can check error    /var/log/apache2/error.log
        ErrorLog ${APACHE_LOG_DIR}/error.log
        #You can check access   /var/log/apache2/access.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        WSGIScriptAlias / /home/merryman/merrybot/bot/wsgi.py

        #Address of django-project
        <Directory /home/merryman/merrybot/bot>
        <Files wsgi.py>
                #Apache version 2.4.*
                Require all granted

                #Apache version 2.2.*
                #order deny, allow
                #deny from all
        </Files>
        </Directory>
</VirtualHost>
```

# 마무리

아파치에서 변화가 생겼으면 새로 재부팅을 해줘야 합니다.

```shell
sudo apachectl -k restart
```

# Error 해결

```
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
```

위와 같은 에러가 나오면 /etc/apache2/apache2.conf 마지막에 해당 줄을 추가해주면 됩니다.

```shell
ServerName localhost
```

다음과 같은 명령으로도 해결할수 있습니다.

```shell
sudo "ServerName localhost" >> /etc/apache2/apache2.conf
```
