from distutils.core import setup


setup(
    name="django-jinja2",
    version='0.1',
    description="A django form widget for CLEditor (a super clean, MIT licensed WYSIWYG HTML editor",
    long_description='',
    author="Yuji Tomita",
    author_email="yuji@yujitomita.com",
    url="https://github.com/yuchant/django-cleditor",
    packages=[
        "cleditor",
        "cleditor.static",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
