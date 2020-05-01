""" ecommerce is considered a package here"""

from ecommerce.shopping.sales import calc_shipping, calc_tax

import ecommerce.shopping.sales
import sys


calc_tax()
calc_shipping()

print(sys.path)
