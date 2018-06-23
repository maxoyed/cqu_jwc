from setuptools import setup, find_packages

setup(
    name = 'cqu_jwc',
    version = '0.0.2',
    keywords='spider cqu jwc',
    description = '重庆大学教务处登录模块',
    license = 'MIT License',
    url = 'https://github.com/maxoyed-MS/cqu_jwc',
    author = 'maxoyed',
    author_email = 'maxoyed@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['lxml', 'requests']
)
