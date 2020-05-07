#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:07:31 2020

@author: augustinjose
"""


import pytest
import os
from ..Git import add


def test():
    assert add(str(os.getcwd())) == True, "Return value should True"
    #Add more test cases
    