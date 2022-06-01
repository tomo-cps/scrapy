This repository is for scraping using scrapy

<!-- toc -->

- [Objective](#objective)
- [Components](#components)
  * [Spiderfile](#Spiderfile)
  * [Itemsfile](#Itemsfile)
  * [Pipelinefile](#Pipelinefile)
- [Requirements](#Requirements)
- [Install](#Install)
- [Starter Repo](#Starter Repo)

<!-- tocstop -->

## Objective

Scrapy is a fast high-level web crawling and web scraping framework, used to
crawl websites and extract structured data from their pages. It can be used for
a wide range of purposes, from data mining to monitoring and automated testing.

Check the Scrapy homepage at <https://scrapy.org> for more information,
including a list of features.

## Components

The components of scrapy is a bit complicated and will explain below.

### Spiderfile

This file describes the parsing process of requests and responses to the site to be crawled.
So, It describes the logic of how to navigate the site and how to parse the page content.

### Itemsfile

This file describes the data structure to be extracted from the data to be crawled.
You can define any structure you want for your purposes.
The Itemsfile is generated in the Spiderfile and passed to the Pipelinefile.

### Pipelinefile

This file describes the process for the Itemsfile passed from the Spiderfile.
You can freely write processes such as saving to DB, file output, etc. according to your purpose.

## Requirements
- `Python 3.7.0`
- Works on macOS

## Install
The quick way
'''
pip install scrapy
'''
See the install in the documentation at <https://docs.scrapy.org/en/latest/intro/install.html> for more details.

From GitHub
'''
  git clone git@github.com:tomo-cps/scrapy.git

'''


## Starter Repo

The starter repo needs to contains the following files:

- `reviews.py`
- `README.md`

'''
  cd spiders                                                           
  scrapy crawl reviews -o "保存したいファイル名".csv
'''
