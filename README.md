# Study of the Lighting Conditions of a Classroom

<p>This repostory created to gather all the code used during the experimental activity for **TECNOLOGIES DEL MEDI AMBIENT I SOSTENIBILITAT - Curs 2025 - 2026**. 
<br>*Made by Francesc Ortiz Rúbies, Joan Carné Rué i Adrià Amorós Sanchez.*</p>

#### Contents

<p>Several coding languages and file have been used to perform different tasks, which are described down below:</p>

##### [IrradiationDataProcesser.py] (https://github.com/Siscos06/Class-Lighting-Analysis/blob/50222c68fe58a59c789be88eb1a01f6d828ce8cf/IrradiationDataProcesser.py)
<p>It manily uses [pandas] (https://pandas.pydata.org/about/) library to sort and perform some calculations to get significant data out of the last 7 years of irradiation data recorded in [Lleida - La Femosa] (https://www.meteo.cat/observacions/xema/dades?codi=YJ) Station.</p>

##### [OutilersRemovingSystem.py] ([https://github.com/Siscos06/Class-Lighting-Analysis/blob/50222c68fe58a59c789be88eb1a01f6d828ce8cf/IrradiationDataProcesser.py](https://github.com/Siscos06/Class-Lighting-Analysis/blob/50222c68fe58a59c789be88eb1a01f6d828ce8cf/OutilersRemovingSystem.py))
<p>It manily uses [pandas] (https://pandas.pydata.org/about/) and [numpy] (https://numpy.org/) libraries to analyse and remove outliers from a dataset using IQR and Modified Z Method.</p>
