# for build
from setuptools import setup, find_packages


with open('README.md', 'r') as f:
	long_description = f.read()


with open('requirements.txt') as f:
	requirements = [l for l in f.read().splitlines() if l]


setup(name="FreeProxy",
	  version="0.1.0",
	  description="Get free proxies.",
	  long_description=long_description,
	  long_description_content_type="text/markdown",
	  license="MIT",
	  install_requires=requirements,
	  author="Charles",
	  author_email="Charlesjzc@qq.com",
	  url="https://github.com/CharlesPikachu/FreeProxy",
	  download_url="https://github.com/CharlesPikachu/FreeProxy/archive/master.zip",
	  packages=find_packages(),
	  keywords=["proxy", "free"],
	  zip_safe=True)