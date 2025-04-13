# Odoo Windows 开发/生产部署手册

---

## 一、安装 PostgreSQL

### 版本要求
- 指定版本: **PostgreSQL 15**

### 配置修改

#### 1. 配置 pg_hba.conf

路径：`/data/pg_hba.conf`

文件最后添加：
```ini
host    all             all             all            md5
```

#### 2. 配置 postgresql.conf

路径：`/data/postgresql.conf`

找到第一条 `listen_addresses`，如果被注释，将注释去掉：
```ini
listen_addresses = '*'
```

#### 3. 重启 PostgreSQL 服务

#### 4. 创建 Odoo 用户：
```sql
create user odoo with password 'bst123456';
alter role odoo with superuser;
```

---

## 二、安装 Python

- 指定版本：**Python 3.10.x**
- 建议不要切换小版本

---

## 三、拉取 Odoo 项目

```bash
git clone https://github.com/lu401809469/odoo.git
```

> 如果 GitHub 拉取慢，可考虑使用 VPN ，或上传自己 Fork 到个人仓库

---

## 四、安装 Python 虚拟环境

在项目目录下：
```bash
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
```

### 特殊包处理

为了避免大型 C++ 编译环境，直接使用编译好的 .whl 包：
```bash
pip install ./lib/libsass-0.23.0-cp38-abi3-win_amd64.whl
```

---

## 五、配置 odoo.conf 文件

当前生产环境配置：
```ini
[options]
addons_path = addons,custom_addons
db_host = 127.0.0.1
db_port = 5433
db_name = odoo18
db_filter = odoo18
db_user = odoo
db_password = bst123456
# 线上密码统一用这个
# db_password = z)7D!rPq%L$8tBJ@fM4yXZ*R9#vcuEna
load_language = zh_CN
log_level = info
# 线上可考虑降低级别 
#log_level = error
admin_passwd = $pbkdf2-sha512$600000$/p.T8p5TSqk1BsB4D0EoZQ$oLfCRiQD08gE/ckLKk.upndSMYxxc/RmEMPvcbYXuuyozcPj2B36LrA0cLbgqHovdm/QKIJJTFb0ta54m4peig
http_port = 8069
# 附件存储目录（使用了这个目前无法分布式部署，如不使用注释就行）
data_dir = D:\odoodata\data
```

---

## 六、运行 Odoo

### 测试/开发模式
```bash
venv\Scripts\activate
python odoo-bin -c odoo.conf --dev=all
```

### 生产环境测试运行，无问题则利用nssm注册为服务
```bash
venv\Scripts\activate
python odoo-bin -c odoo.conf
```

---

## 七、注册 NSSM 服务 (Windows 生产环境)

### 1. 创建启动脚本 start_odoo.bat
```bat
@echo off
cd /d C:\odoo
call venv\Scripts\activate
python odoo-bin -c odoo.conf
```

### 2. NSSM 配置
| 项目 | 值 |
|--------|------|
| Application | `C:\odoo\start_odoo.bat` |
| Arguments | （空着） |
| Startup dir | `C:\odoo` |

### 3. 设置日志
保证 `C:\odoo\log\` 目录存在：
```text
stdout: C:\odoo\log\odoo_out.log
stderr: C:\odoo\log\odoo_err.log
```

---

## 八、代码更新 (生产环境)

```bash
cd C:\odoo
git pull origin 18.0

:: 如需更新依赖
pip install -r requirements.txt
```

如更新了模型或视图，运行升级：
```bash
python odoo-bin -c odoo.conf -u your_module
```

---

## 九、项目信息

- 项目地址：https://github.com/lu401809469/odoo.git
- 分支：18.0 (唯一分支)

---

## 十、总结部署流程

1. 安装 Python 3.10
2. 安装 PostgreSQL 15
3. 修改 pg 配置，创建 odoo 账号
4. 拉取 Odoo 项目，配置 odoo.conf
5. 创建虚拟环境，安装依赖
6. 启动 Odoo (cmd/脚本或 NSSM)

---
