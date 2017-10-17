# Markov-Morse
[![Build Status](https://travis-ci.org/JLDevOps/Markov-Morse.svg?branch=master)](https://travis-ci.org/JLDevOps/Markov-Morse)

A python script that reads from either a list of text or input to generate a sentence then interpret as morse code with sound.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need 
1. Python 2.*
2. PIP (Python Install Packages) - [Link](https://pip.pypa.io/en/stable/installing/)
    1. Pygame
    2. Markovify

### Installing

A requirements.txt file has been provided for the installation of any necessary python packages onto your device.

```pip install -r requirements.txt```

## How Do I

These sections below will provide a detailed look on using the functions of the scripts.

### Morse Code Generation

There are a few functions in the morse.py file, however two functions should be utilized:

Use this to generate a markov-chain sentence from the provided file in the text_files directory:
1. ```generate_markov_morse(filename, file_format, number_of_sentences)```

Use this to provide your own input via prompt:

2. ```input_prompt()```

### To Run with Current Setup

Currently you can generate a markov-chain and run the morse code interpretation via:

```python morse.py```

## Authors

* **Jimmy Le** - [JLDevops](https://github.com/jldevops)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
