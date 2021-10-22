#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="t2s",
    install_requires=[
        "quo; platform_system == 'Windows'",
        "six; python_version < '3.8'",
    ],
)
