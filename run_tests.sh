#!/bin/bash

set -e
set -x

if [ ! -d "pefile-tests" ]; then
    git clone git://github.com/viper-framework/pefile-tests.git
fi

pushd pefile-tests
git pull
popd

pytest --cov=./ -vv
