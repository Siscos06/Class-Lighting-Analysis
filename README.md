# Study of the Lighting Conditions of a Classroom



This repository was created to gather all the code used during the experimental activity for **TECNOLOGIES DEL MEDI AMBIENT I SOSTENIBILITAT - Curs 2025 - 2026**.





### Contents

Several coding languages and files have been used to perform different tasks, which are described down below:



##### [IrradiationDataProcesser.py](https://github.com/Siscos06/Class-Lighting-Analysis/blob/50222c68fe58a59c789be88eb1a01f6d828ce8cf/IrradiationDataProcesser.py)

It mainly uses [*pandas*](https://pandas.pydata.org/about/) library to sort and perform some calculations to get significant data out of the last 7 years of irradiation data recorded in [*Lleida - La Femosa*](https://www.meteo.cat/observacions/xema/dades?codi=YJ) Station.





##### [OutilersRemovingSystem.py](https://github.com/Siscos06/Class-Lighting-Analysis/blob/50222c68fe58a59c789be88eb1a01f6d828ce8cf/OutilersRemovingSystem.py)

It mainly uses the [*pandas*](https://pandas.pydata.org/about/) and [*numpy*](https://numpy.org/) libraries to analyze and remove outliers from a dataset using IQR and the Modified Z Method.





##### [ZoneLightingQuality.m](https://github.com/Siscos06/Class-Lighting-Analysis/blob/510c2c105353326cb5443b486e49845945b87714/ZoneLightingQuality.m)

It's built around MATLAB's figure function with a specific purpose in mind: create and customize a flat chart in which the cells are colored according to the EU indoor lighting conditions requirements.





##### [*LightingPairComparison.m*](https://github.com/Siscos06/Class-Lighting-Analysis/blob/510c2c105353326cb5443b486e49845945b87714/LightingPairComparison.m)

It uses MATLAB's figure function and basic matrix operations to create a chart in which two sets of data are compared. Specifically, the graph will only represent the highest values and color them according to the dataset to which the data point belongs to.





*This code repository was solely made to perform an academic task, which means that once published it won't be updated not changed any other time.*

