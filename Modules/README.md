#### Parameters
1. alpha -> (str)
* No special character and Space *
## Ex.
``` alphaEn.toDigit([‘A’]) ```
``` alphaEn.toDigit([‘Z’, ’F’]) ```
# or
``` alphaEn.toDigit(‘A’) ```
``` alphaEn.toDigit(“ZF”) ```

1. numberCharacters -> (List of char/str)
## Ex-1
* ‘0’ to ’25’ only *
``` alphaEn.toAlpha([‘0’]) OUTPUT: A ```
``` alphaEn.toAlpha(['25', '5']) OUTPUT: ZF ```
##Ex-2
* Not recommend *
``` alphaEn.toAlpha(‘0’) OUTPUT: A ```
``` alphaEn.toAlpha(“255”) OUTPUT: CFF ```
