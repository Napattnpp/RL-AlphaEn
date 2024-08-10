# Parameters
## 1. toDigit((str)alpha)
> [!WARNING]
> **No special character and Space**
### Ex-1
``` alphaEn.toDigit([‘A’]) ```

``` alphaEn.toDigit([‘Z’, ’F’]) ```
### Ex-2
``` alphaEn.toDigit(‘A’) ```

``` alphaEn.toDigit(“ZF”) ```

## 2. toAlpha((List of char/str)numberCharacters)
### Ex-1
> [!NOTE]
> **‘0’ to ’25’ only**
  
``` alphaEn.toAlpha([‘0’]) ```
> ``` OUTPUT: A ```

``` alphaEn.toAlpha(['25', '5']) ```
> ``` OUTPUT: ZF ```

### Ex-2
> [!WARNING]
> **Not recommend**

``` alphaEn.toAlpha(‘0’) ```
> ``` OUTPUT: A ```

``` alphaEn.toAlpha(“255”) ```
> ``` OUTPUT: CFF ```
