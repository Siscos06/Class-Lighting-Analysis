import pandas as pd
import numpy as np
import openpyxl

dataSheets=['Pt & Lt', 'Pt & Lo', 'Po & Lo', 'Po & Lt']
excelOutput="C:/Users/Usuari/Desktop/Blank Procesades.xlsx"

with pd.ExcelWriter(excelOutput) as writer:
    for data in dataSheets:
        dataSets = pd.read_excel("C:/Users/Usuari/Desktop/Blank.xlsx", sheet_name=data)

        for i in range(1,21):
            Q3=dataSets[f'Situació {i}'].quantile(0.75)
            Q1=dataSets[f'Situació {i}'].quantile(0.25)
            IQR=Q3-Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            #lower_array = np.where(dataSets[f'Situació {i}'] <= lower)[0]
            #upper_array = np.where(dataSets[f'Situació {i}'] >= upper)[0]

            median=np.median(dataSets[f'Situació {i}'])
            MAD=np.median(np.abs(dataSets[f'Situació {i}'] - median))
            y=((dataSets[f'Situació {i}'] - median) / MAD) * 0.6745

            iqr_outlier= (dataSets[f'Situació {i}'] < lower) | (dataSets[f'Situació {i}'] > upper)
            z_outlier= (y < -3.5) | (y > 3.5)

            dataSets.loc[iqr_outlier | z_outlier, f'Situació {i}'] = np.nan


        print(dataSets)
        dataSets.to_excel(writer, sheet_name=f"{data}", index=False)
