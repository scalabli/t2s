# t2s

**t2s** (*Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Compose spoken `mp3` or `m4a` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout` or simply pre-produce Google Translate Text to speech demand URLs to feed to an outside program.

<http://t2s.readthedocs.org/>

[![PyPI version](https://img.shields.io/pypi/v/t2s.svg)](https://pypi.org/project/t2s/)
[![Python versions](https://img.shields.io/pypi/pyversions/t2s.svg)](https://pypi.org/project/t2s/)
[![Tests workflow](https://github.com/secretum-inc/t2s/workflows/Tests/badge.svg)](https://github.com/secretum-inc/t2s/actions)
[![Commits Since](https://img.shields.io/github/commits-since/secretum-inc/t2s/latest.svg)](https://github.com/secretum-inc/t2s/commits/)
[![PyPi Downloads](http://pepy.tech/badge/t2s)](http://pepy.tech/project/t2s)
[![Buy me a Coffee](https://img.shields.io/badge/buy%20me%20a-coffee-orange)](https://www.buymeacoffee.com/gerrishon)

## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;

### Installation

    $ pip install t2s

### Quickstart

Command Line:

    $ t2s-cli 'hello' --output hello.mp3

Module:

    >>> from t2s import T2S
    >>> tts = T2S('hello')
    >>> tts.save('hello.mp3')

See <http://t2s.readthedocs.org/> for documentation and examples.

### Project

-   [Questions & community](https://github.com/secretum-inc/t2s/discussions)
-   [Changelog](CHANGELOG.rst)
-   [Contributing](CONTRIBUTING.rst)
