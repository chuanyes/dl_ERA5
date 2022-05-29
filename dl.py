import cdsapi
import numpy as np

years=np.arange(1979,2021) #years from 1979-2020

y1=years[:14]
y2=years[14:14+14]
y3=years[14+14:]  # span all time to 4 periods 

year2=y1

import os

if(os.path.exists(".\\url.txt")):   #check the url.txt
    os.remove(".\\url.txt")   


with open('url.txt','w') as f:
    for i in year2:
        yr=str(i)
        c = cdsapi.Client()
        r=c.retrieve(
        'reanalysis-era5-pressure-levels',
        {
            'product_type': 'reanalysis',
            'variable': 'temperature',  # NOTE change the variable
            'pressure_level': '1000',   # NOTE change the level
            'year': yr,
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
            '00:00', '02:00', '04:00',
            '06:00', '08:00', '10:00',
            '12:00', '14:00', '16:00',
            '18:00', '20:00', '22:00',
            ],
            'format': 'netcdf',
        },
        )
        url="wget -c "+r.location+" -O "+yr+".nc"
        f.write(url)
        f.write('\r\n')
