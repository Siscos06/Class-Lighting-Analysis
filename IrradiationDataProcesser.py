import pandas as pd
import xlrd
import openpyxl
import xlsxwriter


def dateSort(df, monthlyData, hourlyData):
    """     Extracció de dades

        Entrades:
            - df: Totes les dades
            - montlyData: Dataframe per les dades dels mesos
            - hourlyData: Dataframe per les dades de les hores

        Sortides:
            - hourlyData: Dataframe amb les dades d'un any afegides
            - monthlyData: Dataframe amb les dades d'un any afegides
    """

    df['Irradiància solar global'] = pd.to_numeric(df['Irradiància solar global'], errors='coerce')
    df.loc[df['Irradiància solar global'] < 0,'Irradiància solar global'] = 0

    #Convertir dates i hores a un format correcte
        #Dates
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    df['Month'] = df['Data'].dt.month

        #Hores
    df['Hora'] = df['Hora'].replace('24:00', '00:00')
    df['Hora'] = pd.to_datetime(df['Hora'], format='%H:%M', errors='coerce')
    df['Hour'] = df['Hora'].dt.hour

    #Treure dades per mesos
    monthlyData = pd.concat([monthlyData, df[['Month', 'Irradiància solar global']]])

    #Treure dades per les hores de sol
    hourly_filtered = df[df['Hour'].isin([7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])]
    hourlyData = pd.concat([hourlyData, hourly_filtered[['Hour', 'Irradiància solar global']]])
   
    return hourlyData, monthlyData


def meanIngFul(hourlyData, monthlyData):
    """     Procesament de totes les dades: 
                - Treure mitjana per hores
                - Treure mitjana per mesos
                - Treure mitjanes per estacions
        
        Entrades:
            - hourlyData: Dades classificades per cada hora
            - monthlyData: Dades classificades per cada mes
        
        Sortides:
            - hourlyMean: Mitjana de les hores de sol
            - montlyMean: Mitjana de cada mes
            - monthlyMeanSeason: Mitjana de cada estació
    """
    
    #Calcular la mitjana
    hourlyMean = hourlyData.groupby('Hour')['Irradiància solar global'].mean().reset_index()
    monthlyMean = monthlyData.groupby('Month')['Irradiància solar global'].mean().reset_index()

    #Dividir per estacions i calcular la mitjana
    monthMeanSeasonTemp = []
    monthsSeason={'Spring': [3,4,5], 'Summer': [6,7,8], 'Autumn': [9,10,11], 'Winter': [12,1,2]}
    for season, months in monthsSeason.items():
        monthMean = monthlyMean[monthlyMean['Month'].isin(months)]['Irradiància solar global'].mean()

        monthMeanSeasonTemp.append({'Season': season, 'Irradiància solar global': monthMean})
    
    monthlyMeanSeason=pd.DataFrame(monthMeanSeasonTemp)


    return hourlyMean, monthlyMean, monthlyMeanSeason


def exporter(hourlyMean, monthlyMean, monthlyMeanSeason, excelOutput):
    with pd.ExcelWriter(excelOutput) as writer:
        hourlyMean.to_excel(writer, sheet_name='Mitjana per hores', index='False')
        monthlyMean.to_excel(writer, sheet_name='Mitjanes mensuals', index='False')
        monthlyMeanSeason.to_excel(writer, sheet_name='Mitjanes per estacions', index='False')

#Iniciar variables
any=[2018, 2019, 2020, 2021, 2022, 2023, 2024]
excelOutput="C:/Users/Usuari/Desktop/Dades Procesades.xlsx"
monthlyData=pd.DataFrame()
hourlyData=pd.DataFrame()

#Obrir fitxers i extreure les dades
for year in any:
    df=pd.read_excel(f"C:/Users/Usuari/Downloads/Lleida - la Femosa - estacio {year}.xls")
    
    hourlyData, monthlyData = dateSort(df, monthlyData, hourlyData)

#Procesar les dades
hourlyMean, monthlyMean, monthlyMeanSeason = meanIngFul(hourlyData, monthlyData)

#Exportar dades en un fitxer excel
exporter(hourlyMean, monthlyMean, monthlyMeanSeason, excelOutput)
