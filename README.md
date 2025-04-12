pip install -r requirements.txt

# 这个包因为需要c++编译环境，所以直接用编译好的
pip install ./lib/libsass-0.23.0-cp38-abi3-win_amd64.whl


# postgreSQL
create user odoo with password 'bst123456';
alter role  odoo with superuser;


# 生产
更新代码
git pull origin 18.0


# 项目信息
项目地址：https://github.com/lu401809469/odoo.git
分支：18.0（唯一）