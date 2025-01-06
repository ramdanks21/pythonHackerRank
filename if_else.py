#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('Weird')
        #jika n nya genap dan nilainya termasuk rentang 2 - 5z
    elif n % 2 == 0 and 2 <= n <= 5: 
        print('Not Weird')
        #jika n nya genap dan nilainya termasuk rentang 6 - 20
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
        #jika n nya genap dan nilainya termasuk rentang 0 - 20
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
