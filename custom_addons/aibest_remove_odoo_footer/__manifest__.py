{
    'name': '替换网站页脚copyright',
    'version': '1.0',
    'summary': '去除网页构建器构建出来的网页，footer底部copyright行中的“由 Odoo - 创建 免费的网站 提供支持”字样',
    'category': 'Website',
    'author': 'lulu',
    'depends': ['website'],
    'data': [
        'views/website_footer.xml',
    ],
    'installable': True,
    'application': False,
}
