Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd

data=pd.read_excel(r"C:/work/data.xlsx")
print(data)
       Offset                      Description  ...  Andreea   Total
0      1043.0                           Peroni  ...      0.0    1.00
1      1046.0                        Blue Moon  ...      0.0    1.00
2      1126.0                           Pravha  ...      0.0    1.00
3      1211.0                            Madri  ...      0.0    9.00
4     20077.0  Rekorderlig Wild Berries Bottle  ...      0.0    1.00
..        ...                              ...  ...      ...     ...
58  2001002.0              Bloody Mary - Btmls  ...      1.0    1.00
59  2001007.0      Poached Pear Spritz - Btmls  ...     13.0   15.00
60  2001010.0         Raspberry Ripple - Btmls  ...      5.0   22.00
61        NaN                              NaN  ...      NaN     NaN
62        NaN                      Grand Total  ...     20.0  205.12

[63 rows x 8 columns]
ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel"]
ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
#
iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
data.loc[len(data)] = [0, 0, 0, 0, 0, 0, 0, 0]
data.loc[len(data)] = [0]* len(data.columns)
print(data.len(data))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(data.len(data))
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'len'. Did you mean: 'le'?
print(data)
       Offset                      Description  ...  Andreea   Total
0      1043.0                           Peroni  ...      0.0    1.00
1      1046.0                        Blue Moon  ...      0.0    1.00
2      1126.0                           Pravha  ...      0.0    1.00
3      1211.0                            Madri  ...      0.0    9.00
4     20077.0  Rekorderlig Wild Berries Bottle  ...      0.0    1.00
..        ...                              ...  ...      ...     ...
60  2001010.0         Raspberry Ripple - Btmls  ...      5.0   22.00
61        NaN                              NaN  ...      NaN     NaN
62        NaN                      Grand Total  ...     20.0  205.12
63        0.0                                0  ...      0.0    0.00
64        0.0                                0  ...      0.0    0.00

[65 rows x 8 columns]
for x in range(0, len(data)-1):
...     if data['Description'].values[x] in ipoint:
...         data.iloc[len(data)-1, 2:len(data.columns)-1]=data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
SyntaxError: expected an indented block after 'for' statement on line 1

KeyboardInterrupt
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1]=data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            
SyntaxError: invalid syntax
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            
SyntaxError: invalid syntax
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        
print(data.iloc[len(data)-1, 2:len(data.columns)-1])
Caitlin    1.0
Drew 2     1.0
Simona     0.0
Aidan H    0.0
Andreea    0.0
Name: 64, dtype: object
data=pd.read_excel(r"C:/work/data.xlsx")
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        
print(data.iloc[len(data)-1, 2:len(data.columns)-1])
Caitlin     28.0
Drew 2     44.12
Simona     113.0
Aidan H      2.0
Andreea     20.0
Name: 62, dtype: object
print(data)
       Offset                      Description  ...  Andreea   Total
0      1043.0                           Peroni  ...      0.0    1.00
1      1046.0                        Blue Moon  ...      0.0    1.00
2      1126.0                           Pravha  ...      0.0    1.00
3      1211.0                            Madri  ...      0.0    9.00
4     20077.0  Rekorderlig Wild Berries Bottle  ...      0.0    1.00
..        ...                              ...  ...      ...     ...
58  2001002.0              Bloody Mary - Btmls  ...      1.0    1.00
59  2001007.0      Poached Pear Spritz - Btmls  ...     13.0   15.00
60  2001010.0         Raspberry Ripple - Btmls  ...      5.0   22.00
61        NaN                              NaN  ...      NaN     NaN
62        NaN                      Grand Total  ...     20.0  205.12

[63 rows x 8 columns]
data=pd.read_excel(r"C:/work/data.xlsx")
print(data)
       Offset                      Description  ...  Andreea   Total
0      1043.0                           Peroni  ...      0.0    1.00
1      1046.0                        Blue Moon  ...      0.0    1.00
2      1126.0                           Pravha  ...      0.0    1.00
3      1211.0                            Madri  ...      0.0    9.00
4     20077.0  Rekorderlig Wild Berries Bottle  ...      0.0    1.00
..        ...                              ...  ...      ...     ...
58  2001002.0              Bloody Mary - Btmls  ...      1.0    1.00
59  2001007.0      Poached Pear Spritz - Btmls  ...     13.0   15.00
60  2001010.0         Raspberry Ripple - Btmls  ...      5.0   22.00
61        NaN                              NaN  ...      NaN     NaN
62        NaN                      Grand Total  ...     20.0  205.12

[63 rows x 8 columns]
data=pd.read_excel(r"C:/work/datareal.xlsx")
print(data)
        Offset                    Description  Andreea  ... Lucy M Alex     Total
0          NaN                            NaN      Qty  ...    Qty  Qty       Qty
1          NaN                            NaN      NaN  ...    NaN  NaN       NaN
2       1006.0                    Coors Light        1  ...      0    0     106.5
3       1038.0                  Peroni Shandy        0  ...      0    0        12
4       1043.0                         Peroni        5  ...      0    0     467.5
..         ...                            ...      ...  ...    ...  ...       ...
514  2001038.0             Tonic Pint - Btmls        1  ...      0    0         1
515  2001052.0  Eager Apple Lemo Pint - Btmls        0  ...      0    0         1
516  2001058.0  Jingle Berry Highball - Btmls        3  ...      0    0        52
517        NaN                            NaN      NaN  ...    NaN  NaN       NaN
518        NaN                    Grand Total  1722.51  ...    193    1  23915.39

[519 rows x 26 columns]
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        
print(data.iloc[len(data)-1, 2:len(data.columns)-1])
Andreea           1733.51
Loic               494.38
Aidan H           2413.73
Vlad              1468.84
Ethan Cheung      1131.33
Georgia L         1888.85
Oscar J            458.82
Drew 2              987.5
Caitlin           1466.27
Cameron            401.74
Rhian              1647.7
Dan R              712.71
Jakey M           1085.19
Blessing          1304.33
Customer Sales     461.97
Simona             2927.6
Sophie H          1571.12
Scarlet            511.35
Kurtis Gm          418.45
Ben                   585
Cover                 366
Lucy M                193
Alex                    1
Name: 518, dtype: object
data=pd.read_excel(r"C:/work/datareal.xlsx")
data.loc[len(data)] = [0]* len(data.columns)
print(data)
        Offset                    Description  Andreea  ... Lucy M Alex     Total
0          NaN                            NaN      Qty  ...    Qty  Qty       Qty
1          NaN                            NaN      NaN  ...    NaN  NaN       NaN
2       1006.0                    Coors Light        1  ...      0    0     106.5
3       1038.0                  Peroni Shandy        0  ...      0    0        12
4       1043.0                         Peroni        5  ...      0    0     467.5
..         ...                            ...      ...  ...    ...  ...       ...
515  2001052.0  Eager Apple Lemo Pint - Btmls        0  ...      0    0         1
516  2001058.0  Jingle Berry Highball - Btmls        3  ...      0    0        52
517        NaN                            NaN      NaN  ...    NaN  NaN       NaN
518        NaN                    Grand Total  1722.51  ...    193    1  23915.39
519        0.0                              0        0  ...      0    0         0

[520 rows x 26 columns]
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        
print(data.iloc[len(data)-1, 2:len(data.columns)-1])
Andreea           11
Loic              10
Aidan H           11
Vlad              48
Ethan Cheung      12
Georgia L         39
Oscar J            0
Drew 2            15
Caitlin           13
Cameron            7
Rhian             15
Dan R              8
Jakey M           13
Blessing          16
Customer Sales    12
Simona            43
Sophie H          18
Scarlet            2
Kurtis Gm          5
Ben               16
Cover              1
Lucy M             0
Alex               0
Name: 519, dtype: object
data=pd.read_excel(r"C:/work/datareal.xlsx")
data.loc[len(data)] = [0]* len(data.columns)

print(data)
        Offset                    Description  Andreea  ... Lucy M Alex     Total
0          NaN                            NaN      Qty  ...    Qty  Qty       Qty
1          NaN                            NaN      NaN  ...    NaN  NaN       NaN
2       1006.0                    Coors Light        1  ...      0    0     106.5
3       1038.0                  Peroni Shandy        0  ...      0    0        12
4       1043.0                         Peroni        5  ...      0    0     467.5
..         ...                            ...      ...  ...    ...  ...       ...
515  2001052.0  Eager Apple Lemo Pint - Btmls        0  ...      0    0         1
516  2001058.0  Jingle Berry Highball - Btmls        3  ...      0    0        52
517        NaN                            NaN      NaN  ...    NaN  NaN       NaN
518        NaN                    Grand Total  1722.51  ...    193    1  23915.39
519        0.0                              0        0  ...      0    0         0

[520 rows x 26 columns]
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        
print(data.iloc[len(data)-1, 2:len(data.columns)-1])
Andreea           11
Loic              10
Aidan H           11
Vlad              48
Ethan Cheung      12
Georgia L         39
Oscar J            0
Drew 2            15
Caitlin           13
Cameron            7
Rhian             15
Dan R              8
Jakey M           13
Blessing          16
Customer Sales    12
Simona            43
Sophie H          18
Scarlet            2
Kurtis Gm          5
Ben               16
Cover              1
Lucy M             0
Alex               0
Name: 519, dtype: object
Name: 519, dtype: object
SyntaxError: invalid syntax

def myinc()
SyntaxError: expected ':'
def myinc():
    file=input('Filename:')
    data=pd.read_excel(r"file")
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
        
SyntaxError: expected an indented block after 'for' statement on line 5
for x in range(0, len(data)-1):
    if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
    elif data['Description'].values[x] in iipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
    elif data['Description'].values[x] in iiipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

        

def myinc():
    file=input('Filename:')
    data=pd.read_excel(r"file")
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
        data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        
SyntaxError: expected an indented block after 'if' statement on line 6
def myinc():
    file=input('Filename:')
    data=pd.read_excel(r"file")
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])

            
def myinc(file):
    data=pd.read_excel(r"file")
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])

    
myinc(C:/work/datareal.xlsx)
SyntaxError: invalid syntax

def myinc(file):
    data=pd.read_excel(rfile)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])

    
myinc("C:/work/datareal.xlsx
      
SyntaxError: unterminated string literal (detected at line 1)
myinc("C:/work/datareal.xlsx")
      
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    myinc("C:/work/datareal.xlsx")
  File "<pyshell#79>", line 2, in myinc
    data=pd.read_excel(rfile)
NameError: name 'rfile' is not defined. Did you mean: 'file'?
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])

    
myinc(r"C:/work/datareal.xlsx")
Andreea           11
Loic              10
Aidan H           11
Vlad              48
Ethan Cheung      12
Georgia L         39
Oscar J            0
Drew 2            15
Caitlin           13
Cameron            7
Rhian             15
Dan R              8
Jakey M           13
Blessing          16
Customer Sales    12
Simona            43
Sophie H          18
Scarlet            2
Kurtis Gm          5
Ben               16
Cover              1
Lucy M             0
Alex               0
Name: 519, dtype: object
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    print(type(data.iloc[len(data)-1, 2:len(data.columns)-1]))

    
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
SyntaxError: invalid syntax

Series.sort_values(*, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    print(type(data.iloc[len(data)-1, 2:len(data.columns)-1]))def myinc(file):
        data=pd.read_excel(file)
        data.loc[len(data)] = [0]* len(data.columns)
        for x in range(0, len(data)-1):
            if data['Description'].values[x] in ipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
            elif data['Description'].values[x] in iipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
            elif data['Description'].values[x] in iiipoint:
                data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
        print(data.iloc[len(data)-1, 2:len(data.columns)-1])
        print(type(data.iloc[len(data)-1, 2:len(data.columns)-1]))
        
SyntaxError: Invalid star expression

def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    data.sort_values(*, axis=1, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
    
SyntaxError: Invalid star expression

def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    data.sort_values(ascending=False)

    
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#97>", line 12, in myinc
    data.sort_values(ascending=False)
TypeError: DataFrame.sort_values() missing 1 required positional argument: 'by'
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    data.sort_values(axis=1, ascending=False)

    
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#100>", line 12, in myinc
    data.sort_values(axis=1, ascending=False)
TypeError: DataFrame.sort_values() missing 1 required positional argument: 'by'
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])

    
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    print(data.iloc[len(data)-1, 2:len(data.columns)-1])
    data.iloc[len(data)-1, 2:len(data.columns)-1].to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#106>", line 12, in myinc
    data.iloc[len(data)-1, 2:len(data.columns)-1].to_excel(r"C:/work/result240225.xlsx")
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 2417, in to_excel
    formatter.write(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\formats\excel.py", line 943, in write
    writer = ExcelWriter(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 61, in __init__
    super().__init__(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1246, in __init__
    self._handles = get_handle(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'C:/work/result240225.xlsx'
myinc(r"C:/work/Incentive240225.xlsx")
  
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    print(result)
    print(result['Loic'])
    result.to_excel(r"C:/work/result240225.xlsx")

    

myinc(r"C:/work/Incentive240225.xlsx")
Andreea           42
Loic               7
Aidan H           19
Vlad               7
Ethan Cheung       5
Georgia L         49
Oscar J            8
Drew 2             3
Caitlin            9
Cameron           16
Rhian              5
Dan R             14
Scarlet           39
Jakey M           17
Blessing          16
Customer Sales    15
Simona            42
Kurtis Gm          4
Sophie H          19
Damien             0
Ben               27
Cover              1
Lucy M             0
Georgina           0
Loic.1             0
Alex               0
Name: 522, dtype: object
7
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#111>", line 14, in myinc
    result.to_excel(r"C:/work/result240225.xlsx")
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 2417, in to_excel
    formatter.write(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\formats\excel.py", line 943, in write
    writer = ExcelWriter(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 61, in __init__
    super().__init__(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1246, in __init__
    self._handles = get_handle(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'C:/work/result240225.xlsx'
floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
  
bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
  
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.iloc[result.index in bar]
    fresult=result.iloc[result.index in floor]
    print(bresult)
    print(fresult)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#117>", line 17, in myinc
    bresult=result.iloc[result.index in bar]
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.iloc[result.any in bar]
    fresult=result.iloc[result.any in floor]
    print(bresult)
    print(fresult)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#120>", line 17, in myinc
    bresult=result.iloc[result.any in bar]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py", line 1191, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexing.py", line 1749, in _getitem_axis
    raise TypeError("Cannot index by location index with a non-integer key")
TypeError: Cannot index by location index with a non-integer key
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.isin(bar)
    fresult=result.isin(floor)
    print(bresult)
    print(fresult)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Andreea           False
Loic              False
Aidan H           False
Vlad              False
Ethan Cheung      False
Georgia L         False
Oscar J           False
Drew 2            False
Caitlin           False
Cameron           False
Rhian             False
Dan R             False
Scarlet           False
Jakey M           False
Blessing          False
Customer Sales    False
Simona            False
Kurtis Gm         False
Sophie H          False
Damien            False
Ben               False
Cover             False
Lucy M            False
Georgina          False
Loic.1            False
Alex              False
Name: 522, dtype: bool
Andreea           False
Loic              False
Aidan H           False
Vlad              False
Ethan Cheung      False
Georgia L         False
Oscar J           False
Drew 2            False
Caitlin           False
Cameron           False
Rhian             False
Dan R             False
Scarlet           False
Jakey M           False
Blessing          False
Customer Sales    False
Simona            False
Kurtis Gm         False
Sophie H          False
Damien            False
Ben               False
Cover             False
Lucy M            False
Georgina          False
Loic.1            False
Alex              False
Name: 522, dtype: bool
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#123>", line 21, in myinc
    result.to_excel(r"C:/work/result240225.xlsx")
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 2417, in to_excel
    formatter.write(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\formats\excel.py", line 943, in write
    writer = ExcelWriter(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 61, in __init__
    super().__init__(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1246, in __init__
    self._handles = get_handle(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'C:/work/result240225.xlsx'
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.isin(bar)
    barseries=series[bresult]
    fresult=result.isin(floor)
    floorseries=series[fresult]
    print(barseries)
    print(floorseries)
    result.to_excel(r"C:/work/result240225.xlsx")


myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#126>", line 18, in myinc
    barseries=series[bresult]
NameError: name 'series' is not defined
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.isin(bar)
    barseries=result[bresult]
    fresult=result.isin(floor)
    floorseries=result[fresult]
    print(barseries)
    print(floorseries)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Series([], Name: 522, dtype: object)
Series([], Name: 522, dtype: object)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#130>", line 23, in myinc
    result.to_excel(r"C:/work/result240225.xlsx")
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\generic.py", line 2417, in to_excel
    formatter.write(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\formats\excel.py", line 943, in write
    writer = ExcelWriter(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 61, in __init__
    super().__init__(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1246, in __init__
    self._handles = get_handle(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
PermissionError: [Errno 13] Permission denied: 'C:/work/result240225.xlsx'
myinc(r"C:/work/Incentive240225.xlsx")
  
Series([], Name: 522, dtype: object)
Series([], Name: 522, dtype: object)

myinc(r"C:/work/Incentive240225.xlsx")
  
Series([], Name: 522, dtype: object)
Series([], Name: 522, dtype: object)
print(barseries)
  
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    print(barseries)
NameError: name 'barseries' is not defined
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult]
    fresult=result.index.isin(floor)
    floorseries=result[fresult]
    print(barseries)
    print(floorseries)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Oscar J      8
Drew 2       3
Caitlin      9
Cameron     16
Rhian        5
Dan R       14
Scarlet     39
Jakey M     17
Blessing    16
Name: 522, dtype: object
Andreea      42
Georgia L    49
Simona       42
Sophie H     19
Damien        0
Ben          27
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=false)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=false)
    print(barseries)
    print(floorseries)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#140>", line 18, in myinc
    barseries=result[bresult].sort_values(ascending=false)
NameError: name 'false' is not defined. Did you mean: 'False'?
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    print(barseries)
    print(floorseries)
    result.to_excel(r"C:/work/result240225.xlsx")

    
myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    print(barseries)
    print(floorseries)
    barseries.to_excel(r"C:/work/result240225.xlsx")
    floorseries.to_excel(r"C:/work/result240225.xlsx")

    

myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    print(barseries)
    print(floorseries)

    
pip install pandas openpyxl
SyntaxError: invalid syntax
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    print(barseries)
    print(floorseries)

    
myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Value')
    plt.xticks(barseries.index, barseries.values)
    plt.show()
    print(barseries)
    print(floorseries)

    
myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#156>", line 21, in myinc
    plt.figure(figsize=(10, 5))
NameError: name 'plt' is not defined


KeyboardInterrupt

myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#156>", line 21, in myinc
    plt.figure(figsize=(10, 5))
NameError: name 'plt' is not defined
import matplotlib.pyplot as plt
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Value')
    plt.xticks(barseries.index, barseries.values)
    plt.show()
    print(barseries)
    print(floorseries)

    
myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Value')
    plt.xticks(barseries.index)
    plt.show()
    print(barseries)
    print(floorseries)

    
myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Value')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()
    print(barseries)
    print(floorseries)

    
myinc(r"C:/work/Incentive240225.xlsx")
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    myinc(r"C:/work/Incentive240225.xlsx")
  File "<pyshell#168>", line 27, in myinc
    for bar in bars:
NameError: name 'bars' is not defined. Did you mean: 'bar'?
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Value')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()
    print(barseries)
    print(floorseries)

    
KeyboardInterrupt
myinc(r"C:/work/Incentive240225.xlsx")
myinc(r"C:/work/Incentive240225.xlsx")
Scarlet     39
Jakey M     17
Cameron     16
Blessing    16
Dan R       14
Caitlin      9
Oscar J      8
Rhian        5
Drew 2       3
Name: 522, dtype: object
Georgia L    49
Andreea      42
Simona       42
Ben          27
Sophie H     19
Damien        0
Name: 522, dtype: object
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()

    
myinc(r"C:/work/Incentive240225.xlsx")

def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()
    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.show()

    
myinc(r"C:/work/Incentive240225.xlsx")

def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    
    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive240225.xlsx")
myinc(r"C:/work/Incentive270225.xlsx")
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    myinc(r"C:/work/Incentive270225.xlsx")
  File "<pyshell#183>", line 2, in myinc
    data=pd.read_excel(file)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 495, in read_excel
    io = ExcelFile(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1550, in __init__
    ext = inspect_excel_format(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\excel\_base.py", line 1402, in inspect_excel_format
    with get_handle(
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 882, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'C:/work/Incentive270225.xlsx'
myinc(r"C:/work/Incentive240225.xlsx")
  
myinc(r"C:/work/Incentive270225.xlsx")
  
myinc(r"C:/work/Incentive020325.xlsx")
  
Traceback (most recent call last):
  
SyntaxError: invalid syntax. Perhaps you forgot a comma?

def add_points(series, index_name, points):
    if index_name in result.index:
        result[index_name] += points
    else:
        print(f"Index {index_name} not found in the Series.")

        
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    while True:
    index_name = int(input("Enter the index to add points to (or -1 to stop): "))
    if index_name == -1:
        break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()
    
SyntaxError: expected an indented block after 'while' statement on line 17
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    while True:
        index_name = int(input("Enter the index to add points to (or -1 to stop): "))
    if index_name == -1:
        break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()
    
SyntaxError: 'break' outside loop
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    while True:
        index_name = int(input("Enter the index to add points to (or -1 to stop): "))
        if index_name == -1:
            break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or -1 to stop): Georgia
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx")
  File "<pyshell#196>", line 18, in myinc
    index_name = int(input("Enter the index to add points to (or -1 to stop): "))
ValueError: invalid literal for int() with base 10: 'Georgia'
def add_points(series, index_name, points):
    if index_name in result.index:
        result[index_name] += ' +' + str(points)  # Append points as a string
    else:
        print(f"Index {index_name} not found in the Series.")

        
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
   while True:
    index_name = input("Enter the index to add points to (or 'stop' to end): ")
    if index_name.lower() == 'stop':
        break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()
    
SyntaxError: unindent does not match any outer indentation level
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia
Enter the index to add points to (or 'stop' to end): stop
Enter the number of points to add: 9
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx")
  File "<pyshell#202>", line 22, in myinc
    add_points(result, index_name, points)
  File "<pyshell#199>", line 2, in add_points
    if index_name in result.index:
NameError: name 'result' is not defined
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += ' +' + str(points)  # Append points as a string
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
    points = int(input("Enter the number of points to add: "))
    add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia
Enter the index to add points to (or 'stop' to end): stop
Enter the number of points to add: 9
Index stop not found in the Series.
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia
Enter the index to add points to (or 'stop' to end): 'stop'
Enter the index to add points to (or 'stop' to end): stop
Enter the number of points to add: 9
Index stop not found in the Series.
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += ' +' + str(points)  # Append points as a string
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia
Enter the number of points to add: stop
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx")
  File "<pyshell#209>", line 27, in myinc
    points = int(input("Enter the number of points to add: "))
ValueError: invalid literal for int() with base 10: 'stop'
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia
Enter the number of points to add: 9
Index Georgia not found in the Series.
Enter the index to add points to (or 'stop' to end): stop
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia L
Enter the number of points to add: 9
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx")
  File "<pyshell#209>", line 28, in myinc
    add_points(result, index_name, points)
  File "<pyshell#209>", line 19, in add_points
    result[index_name] += ' +' + str(points)  # Append points as a string
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
def myinc(file):
    data=pd.read_excel(file)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    ipoint = ["Grey Goose", "Havana 7yr", "Tanquaray 10", "Thai Chicken Curry", "Alpine Chicken Schnitzel", "Banyan Bott Martini Upgrade"]
    iipoint = ["Hennessy", "Patron Silver", "Patron Anejo", "Nikka From The Barrel", "Tacos Your Way", "Crispy Duck Pancakes", "Pan-Asian Chicken Trio"]
    iiipoint = ["Bottle Grey Goose", "Bottle Woodford Reserve", "Bottle Ciroc", "Bottle Ciroc Red Berry", "Bottle Ciroc Apple", "Bottle Gentleman Jack", "Bottle Jamesons", "Bottle Hendricks"]
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia L
Enter the number of points to add: 9
Enter the index to add points to (or 'stop' to end): stop
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): stop
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia L
Enter the number of points to add: 9
Enter the index to add points to (or 'stop' to end): stop
myinc(r"C:/work/Incentive020325.xlsx")
Enter the index to add points to (or 'stop' to end): Georgia L
Enter the number of points to add: 12
Enter the index to add points to (or 'stop' to end): Simona
Enter the number of points to add: 3
Enter the index to add points to (or 'stop' to end): stop
def myinc(file1, file2):
    data=pd.read_excel(file1)
    ind=pd.read_excel(file2)
    ipoint = df['ipoint'].tolist()
    iipoint = df['iipoint'].tolist()
    iiipoint = df['iiipoint'].tolist()
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
  File "<pyshell#220>", line 4, in myinc
    ipoint = df['ipoint'].tolist()
NameError: name 'df' is not defined
def myinc(file1, file2):
    data=pd.read_excel(file1)
    ind=pd.read_excel(file2)
    ipoint = ind['ipoint'].tolist()
    iipoint = ind['iipoint'].tolist()
    iiipoint = ind['iiipoint'].tolist()
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
Traceback (most recent call last):
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 218, in _na_arithmetic_op
    result = func(left, right)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\computation\expressions.py", line 242, in evaluate
    return _evaluate(op, op_str, a, b)  # type: ignore[misc]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\computation\expressions.py", line 73, in _evaluate_standard
    return op(a, b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
  File "<pyshell#223>", line 12, in myinc
    data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\common.py", line 76, in new_method
    return method(self, other)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\arraylike.py", line 186, in __add__
    return self._arith_method(other, operator.add)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\series.py", line 6135, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\base.py", line 1382, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 283, in arithmetic_op
    res_values = _na_arithmetic_op(left, right, op)  # type: ignore[arg-type]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 227, in _na_arithmetic_op
    result = _masked_arith_op(left, right, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 163, in _masked_arith_op
    result[mask] = op(xrav[mask], yrav[mask])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
def myinc(file1, file2):
    data=pd.read_excel(file1)
    ind=pd.read_excel(file2)
    ipoint = ind['ipoint'].tolist()
    iipoint = ind['iipoint'].tolist()
    iiipoint = ind['iiipoint'].tolist()
    print(ipoint)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
['Grey Goose', 'Havana 7yr', 'Tanquaray 10', 'Thai Chicken Curry', 'Alpine Chicken Schnitzel', 'Banyan Bott Martini Upgrade', 'Black Angus Beef Roast', 'Herb Roasted Chicken Breast', 'Plant Mince, Onion, Stout Pie', 'Vegan Mince, Onion, Stout Pie', nan, nan]
Traceback (most recent call last):
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 218, in _na_arithmetic_op
    result = func(left, right)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\computation\expressions.py", line 242, in evaluate
    return _evaluate(op, op_str, a, b)  # type: ignore[misc]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\computation\expressions.py", line 73, in _evaluate_standard
    return op(a, b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
  File "<pyshell#226>", line 13, in myinc
    data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\common.py", line 76, in new_method
    return method(self, other)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\arraylike.py", line 186, in __add__
    return self._arith_method(other, operator.add)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\series.py", line 6135, in _arith_method
    return base.IndexOpsMixin._arith_method(self, other, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\base.py", line 1382, in _arith_method
    result = ops.arithmetic_op(lvalues, rvalues, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 283, in arithmetic_op
    res_values = _na_arithmetic_op(left, right, op)  # type: ignore[arg-type]
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 227, in _na_arithmetic_op
    result = _masked_arith_op(left, right, op)
  File "C:\Users\echeu\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\ops\array_ops.py", line 163, in _masked_arith_op
    result[mask] = op(xrav[mask], yrav[mask])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
def myinc(file1, file2):
    data=pd.read_excel(file1)
    ind=pd.read_excel(file2)
    ipoint = [x for x in ind['ipoint'].astype(str).tolist() if pd.notna(x)]
    iipoint = [x for x in ind['iipoint'].astype(str).tolist() if pd.notna(x)]
    iiipoint = [x for x in ind['iiipoint'].astype(str).tolist() if pd.notna(x)]
    print(ipoint)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
['Grey Goose', 'Havana 7yr', 'Tanquaray 10', 'Thai Chicken Curry', 'Alpine Chicken Schnitzel', 'Banyan Bott Martini Upgrade', 'Black Angus Beef Roast', 'Herb Roasted Chicken Breast', 'Plant Mince, Onion, Stout Pie', 'Vegan Mince, Onion, Stout Pie', 'nan', 'nan']
Enter the index to add points to (or 'stop' to end): stop
def myinc(file1, file2):
    data=pd.read_excel(file1)
    ind=pd.read_excel(file2)
    ipoint = [x for x in ind['ipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
    iipoint = [x for x in ind['iipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
    iiipoint = [x for x in ind['iiipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
    print(ipoint)
    data.loc[len(data)] = [0]* len(data.columns)
    bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
    floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
    for x in range(0, len(data)-1):
        if data['Description'].values[x] in ipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
        elif data['Description'].values[x] in iipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
        elif data['Description'].values[x] in iiipoint:
            data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
    result=data.iloc[len(data)-1, 2:len(data.columns)-1]
    def add_points(series, index_name, points):
        if index_name in result.index:
            result[index_name] += points
        else:
            print(f"Index {index_name} not found in the Series.")

    while True:
        index_name = input("Enter the index to add points to (or 'stop' to end): ")
        if index_name.lower() == 'stop':
            break
        points = int(input("Enter the number of points to add: "))
        add_points(result, index_name, points)
    bresult=result.index.isin(bar)
    barseries=result[bresult].sort_values(ascending=False)
    fresult=result.index.isin(floor)
    floorseries=result[fresult].sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    bars = plt.bar(barseries.index, barseries.values, color='blue')
    plt.bar(barseries.index, barseries.values, color='blue')
    plt.title('Bartender Incentive')
    plt.xlabel('Bartender')
    plt.ylabel('Score')
    plt.xticks(barseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')

    plt.figure(figsize=(10, 5))
    bars = plt.bar(floorseries.index, floorseries.values, color='green')
    plt.bar(floorseries.index, floorseries.values, color='green')
    plt.title('Floortender Incentive')
    plt.xlabel('Floortender')
    plt.ylabel('Score')
    plt.xticks(floorseries.index)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
    plt.tight_layout()
    plt.show()

    
myinc(r"C:/work/Incentive020325.xlsx",r"C:/work/PointSystem.xlsx")
['Grey Goose', 'Havana 7yr', 'Tanquaray 10', 'Thai Chicken Curry', 'Alpine Chicken Schnitzel', 'Banyan Bott Martini Upgrade', 'Black Angus Beef Roast', 'Herb Roasted Chicken Breast', 'Plant Mince, Onion, Stout Pie', 'Vegan Mince, Onion, Stout Pie']
Enter the index to add points to (or 'stop' to end): stop
>>> def myinc(file1, file2):
...     data=pd.read_excel(file1)
...     ind=pd.read_excel(file2)
...     ipoint = [x for x in ind['ipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
...     iipoint = [x for x in ind['iipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
...     iiipoint = [x for x in ind['iiipoint'].astype(str).tolist() if pd.notna(x) and x != 'nan']
...     data.loc[len(data)] = [0]* len(data.columns)
...     bar = ['Oscar J', 'Drew 2', 'Caitlin', 'Cameron', 'Rhian', 'Dan R', 'Scarlet', 'Jakey M', 'Blessing']
...     floor = ['Andreea', 'Georgia L', 'Simona', 'Damien', 'Sophie H', 'Ben', 'Halima']
...     for x in range(0, len(data)-1):
...         if data['Description'].values[x] in ipoint:
...             data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + data.iloc[x, 2:len(data.columns)-1]
...         elif data['Description'].values[x] in iipoint:
...             data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 2*(data.iloc[x, 2:len(data.columns)-1])
...         elif data['Description'].values[x] in iiipoint:
...             data.iloc[len(data)-1, 2:len(data.columns)-1] = data.iloc[len(data)-1, 2:len(data.columns)-1] + 3*(data.iloc[x, 2:len(data.columns)-1])
...     result=data.iloc[len(data)-1, 2:len(data.columns)-1]
...     def add_points(series, index_name, points):
...         if index_name in result.index:
...             result[index_name] += points
...         else:
...             print(f"Index {index_name} not found in the Series.")
... 
...     while True:
...         index_name = input("Enter the index to add points to (or 'stop' to end): ")
...         if index_name.lower() == 'stop':
...             break
...         points = int(input("Enter the number of points to add: "))
...         add_points(result, index_name, points)
...     bresult=result.index.isin(bar)
...     barseries=result[bresult].sort_values(ascending=False)
...     fresult=result.index.isin(floor)
...     floorseries=result[fresult].sort_values(ascending=False)
...     plt.figure(figsize=(10, 5))
...     bars = plt.bar(barseries.index, barseries.values, color='blue')
...     plt.bar(barseries.index, barseries.values, color='blue')
...     plt.title('Bartender Incentive')
...     plt.xlabel('Bartender')
...     plt.ylabel('Score')
...     plt.xticks(barseries.index)
...     for bar in bars:
...         yval = bar.get_height()
...         plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
... 
...     plt.figure(figsize=(10, 5))
...     bars = plt.bar(floorseries.index, floorseries.values, color='green')
...     plt.bar(floorseries.index, floorseries.values, color='green')
...     plt.title('Floortender Incentive')
...     plt.xlabel('Floortender')
...     plt.ylabel('Score')
...     plt.xticks(floorseries.index)
...     for bar in bars:
...         yval = bar.get_height()
...         plt.text(bar.get_x() + bar.get_width()/2.0, yval, yval, va='bottom')
...     plt.tight_layout()
