# Cramer's Rule
A Calculator to solve square matrices systems using Cramer's Rule and Laplace's Theorem. This script is designed to assist in the study and resolution of exercises in Linear Algebra classes.  

The code was inspired in this calculator in **C++** made by **RafaelGSS**: https://github.com/RafaelGSS/CramerMethod

## How it works
1. Clone this repository and start program the program by running (Python 3.7 is required):
```sh
# Python 3.7 is required. If you don't have it, read the Python docs to install.
# https://www.python.org/downloads/release/python-370/
$ python main.py # If Python 3 is default
$ python3 main.py # If you have Python 2 installed as default
```  

2. Enter the Matrix Order:
```sh
# Enter the Matrix Order:
$ 3
```

4. Enter the Matrix formatted with SPACES (for columns) and ENTERS (for lines):
```sh
# Enter the Matrix formatted with SPACES (for columns) and ENTERS (for lines):
$ 1 -2 -2
$ 1 -1 1
$ 2 1 3
```  

6. Enter the respective results for LINES separated by SPACES:  
```sh
# Enter the respective results for LINES separated by SPACES:
$ -1 -2 1
```  

7. Check if your system is mounted correctly and Enter **Y** for YES or **N** for NO (YES is default):  
```sh
# Check if your system is mounted correctly:
#
# 1.0   -2.0   -2.0   =   -1.0 
# 1.0   -1.0   1.0    =   -2.0
# 2.0   1.0    3.0    =   1.0
#
# Enter Y for YES or N for NO (YES is default):
$ Y
```  

8. The main determinant, all matrices with the substitutions and their respective determinants will be displayed.  
```sh
# Main Matrix Determinant: -8.0
#
# Matrix with replacement at COLUMN 1:
# -1.0  -2.0   -2.0 
# -2.0  -1.0   1.0
# 1.0   1.0    3.0
# Determinant of this matrix: -8.0
#
# Matrix with replacement at COLUMN 2:
# 1.0   -1.0   -2.0
# 1.0   -2.0   1.0
# 2.0   1.0    3.0
# Determinant of this matrix: -16.0
#
# Matrix with replacement at COLUMN 3:
# 1.0   -2.0   -1.0 
# 1.0   -1.0   -2.0
# 2 .0   1.0    1.0
# Determinant of this matrix: 8.0
```  

9. And finally, the solution set will also be displayed at the end of the program.  
```sh
# Solution set:
# A1 = 1.0
# A2 = 2.0
# A3 = -1.0
```  
