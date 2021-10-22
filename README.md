# t2s

**t2s** (*Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Write spoken `mp3` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout`. Or simply pre-generate Google Translate TTS request URLs to feed to an external program.
<http://t2s.readthedocs.org/>

[![PyPI version](https://img.shields.io/pypi/v/t2s.svg)](https://pypi.org/project/t2s/)
[![Python versions](https://img.shields.io/pypi/pyversions/t2s.svg)](https://pypi.org/project/gTTS/)
[![Tests workflow](https://github.com/secretum-inc/t2s/workflows/Tests/badge.svg)](https://github.com/secretum-inc/t2s/actions)
[![codecov](https://codecov.io/gh/pndurette/gTTS/branch/master/graph/badge.svg)](https://codecov.io/gh/pndurette/gTTS)
[![Commits Since](https://img.shields.io/github/commits-since/secretum-inc/t2s/latest.svg)](https://github.com/secretum-inc/t2s/commits/)
[![PyPi Downloads](http://pepy.tech/badge/t2s)](http://pepy.tech/project/t2s)
[![Buy me a Coffee](https://img.shields.io/badge/buy%20me%20a-coffee-orange)](https://www.buymeacoffee.com/pndurette)

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

### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *different* from [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

### Project

-   [Questions & community](https://github.com/secretum-inc/t2s/discussions)
-   [Changelog](CHANGELOG.rst)
-   [Contributing](CONTRIBUTING.rst)

### Licence

[The MIT License (MIT)](LICENSE) Copyright © 2014-2021 Pierre Nicolas Durette & [Contributors](https://github.com/pndurette/gTTS/graphs/contributors)
