#!/usr/bin/env python3
# ===================================================================================
#  ملف: setup.py (إعداد حزمة Python)
# ===================================================================================

from setuptools import setup, find_packages
import os

# قراءة محتوى ملف README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# قراءة المتطلبات من ملف requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bassera-platform",
    version="1.0.0",
    author="Bassera Team",
    author_email="info@bassera.ai",
    description="منصة بصيرة - مساعد ذكي باللغة العربية مبني على OVOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bassera-platform/bassera-app",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: Arabic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.2.0",
            "black>=22.10.0",
            "flake8>=5.0.0",
            "mypy>=0.991",
        ],
        "docs": [
            "sphinx>=5.3.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "bassera=start_basseera:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt", "*.md"],
    },
    keywords="voice assistant, arabic, ovos, ai, speech recognition, text to speech",
    project_urls={
        "Bug Reports": "https://github.com/bassera-platform/bassera-app/issues",
        "Source": "https://github.com/bassera-platform/bassera-app",
        "Documentation": "https://docs.bassera.ai",
    },
)