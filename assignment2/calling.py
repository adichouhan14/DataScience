
''' importing module from different directory  '''

import sys
sys.path.insert(1,"F:\\aditya data")
import mymodule as mm
ans = mm.oddSum(10)
print(ans)
mm.printSquares(20)
