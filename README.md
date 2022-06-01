<img src="./logo.png" alt="Logo of the project" align="right" width="150">

# Weather Python Typing (macOS only) &middot; ![LICENSE](https://img.shields.io/badge/license-MIT-brightgreen) [![python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ss-o-furda/weather_python_typing)

> Written using python 3.10 and type hints, works only on macOS

After full installing procces you will able to type `weather` anywhere in your terminal to check what's weather outside 😍

## Installing / Getting started

To work, you need a [whereami](https://github.com/robmathers/WhereAmI) module that allows the program to obtain coordinates.
You can install it according to the instructions from the repository, or use the instructions from the contributor of the project, which you can find at [the link](https://github.com/robmathers/WhereAmI/issues/4).

Or just run the following commands:

```shell
brew tap welldan97/whereami
brew install whereami
```

If you do not have homebrew installed - follow the [instructions](https://brew.sh/).

</br>

To run the project you need:

```shell
git clone git@github.com:ss-o-furda/weather_python_typing.git
cd weather_python_typing
chmod +x weather
./weather
```

You will get the following result:

```shell
It is clouds in {city} now, the temperature is about {temp}°C.
The sun rose at {time}, and will set at {time}.
```

To be able to run this command from anywhere in the terminal - you need to make a link to the file in the directory with executable files:

```shell
sudo ln -s ${pwd}/weather /usr/local/bin
```

After that, just type `weather` anywhere in the terminal and get information about the current weather.

## Licensing

The usual MIT license is used, the full text of which can be found in the [LICENSE](/LICENSE) file.
