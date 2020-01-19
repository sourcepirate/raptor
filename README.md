## Raptor

[![Build Status](https://travis-ci.org/sourcepirate/raptor.svg?branch=master)](https://travis-ci.org/sourcepirate/raptor)

[![Updates](https://pyup.io/repos/github/sourcepirate/raptor/shield.svg)](https://pyup.io/repos/github/sourcepirate/raptor/)

[![Python 3](https://pyup.io/repos/github/sourcepirate/raptor/python-3-shield.svg)](https://pyup.io/repos/github/sourcepirate/raptor/)

Raptor is a configurable html report generation tool. Based on pandas dataframe.

## Installation and Usage

```
python setup.py install

raptor config.yml > report.html

```

## Example Config file

```yaml

template: default
title: Iris Data Reports
sender: sourcepirate@codelantics.com
receivers:
  - redspectrum@codelantics.com
sections:
  - name: intro
    description: desciription text
    datasource:
      type: url
      url: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv
    transform:
      - type: groupby
        by:
        - species
  - name: intro2
    description: desciription text
    datasource:
      type: url
      url: https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv
    transform:
      - type: groupby
        by:
        - species

```

## Road Map

* Email support
* More configuration
* More customizable.


## License
MIT