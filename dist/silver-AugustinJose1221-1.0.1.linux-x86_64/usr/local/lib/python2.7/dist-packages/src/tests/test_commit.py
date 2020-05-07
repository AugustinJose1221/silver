#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:35:34 2020

@author: augustinjose
"""


import pytest
import os
from ..Git import commit


def test():
    assert commit("test string") == True, "Return value should True"
    #Add more test cases