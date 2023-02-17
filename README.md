## mobile-app-behave-toolium

Create and activate virtual environment

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Install dependencies

```
$ pip install -r requirements.txt
```

## Running mobile tests
By default, mobile tests are configured to run against a local Appium server, so [Appium](http://appium.io/docs/en/about-appium/getting-started/?lang=en) must be installed, configured and started before executing tests.

## Appium set up on mac for Android:
1) Install [Homebrew](https://mac.install.guide/homebrew/3.html)
2) Install [NodeJS](https://nodejs.org/en/download/)
3) Install [Java JDK8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)
4) Install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac)
5) Install Appium server using npm (CLI) or Appium desktop client
7) Install [Appium Inspector](https://github.com/appium/appium-inspector/releases)
8) Set JAVA_HOME and ANDROID_HOME environment variables
9) Install [Android studio](https://developer.android.com/studio)

## Appium set up on mac for iOS:
1) Install [Homebrew](https://mac.install.guide/homebrew/3.html)
2) Install [NodeJS](https://nodejs.org/en/download/)
3) Install [Carthage](https://formulae.brew.sh/formula/carthage)
4) Install [Java JDK8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)
5) Install [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac)
6) Install Appium server using npm (CLI) or Appium desktop client
7) Install [Appium Inspector](https://github.com/appium/appium-inspector/releases)
8) Set JAVA_HOME environment variables
9) Install [Xcode ](https://developer.apple.com/xcode/)
10) Install Xcode command-line ``` $ xcode-select --install ```


## Use Appium Doctor to verify the installations
1) Install appium-doctor using command 
```
$ npm install -g appium-doctor
```

2) To view the list of available options
```
$ appium-doctor --help
```
To check Android or iOS set up 
```
$ appium-doctor --android
$ appium-doctor --ios
```












## Behave Mobile Framework using Toolium Python Wrapper Tool
Toolium is a Python wrapper tool of Selenium and Appium libraries to test web and mobile applications in a single 
project. This framework contains a behave test that could be executed either in iOS or Android depending on the 
Config_environment property.

To run the script in iOS:

```shell
$ behave mobile_behave -D Config_environment=ios
```

To run the script in Android:

```shell
$ behave mobile_behave -D Config_environment=android
```

