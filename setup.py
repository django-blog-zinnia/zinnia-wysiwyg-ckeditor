"""Setup script of zinnia-wysiwyg-ckeditor"""
from setuptools import setup
from setuptools import find_packages

import zinnia_ckeditor

setup(
    name='zinnia-wysiwyg-ckeditor',
    version=zinnia_ckeditor.__version__,

    description='CKEditor for editing entries in django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, zinnia, wysiwyg, ckeditor',

    author=zinnia_ckeditor.__author__,
    author_email=zinnia_ckeditor.__email__,
    url=zinnia_ckeditor.__url__,

    packages=find_packages(exclude=['demo_zinnia_ckeditor']),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_ckeditor.__license__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-ckeditor-updated']
)
