from setuptools import setup, find_packages

setup(
    name="seo-auditor",
    version="1.0.0",
    description="A CLI tool to audit websites for SEO issues and generate HTML/CSV reports.",
    author="Robert Mitchell",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "beautifulsoup4",
        "lxml",
        "tldextract",
        "pandas",
        "jinja2"
    ],
    entry_points={
        "console_scripts": [
            "seo-auditor=seo_auditor.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
