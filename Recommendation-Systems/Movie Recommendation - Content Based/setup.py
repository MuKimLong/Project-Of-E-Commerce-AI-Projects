from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Muhammet Uzun'
SRC_REPO    = 'src'
LIST_OF_REQUIRMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version= '0.0.1',
    author= AUTHOR_NAME,
    author_email= 'muhammet.uzn@gmail.com',
    description= 'Comment Based Movies Recommendation System ',
    packages=[SRC_REPO],
)