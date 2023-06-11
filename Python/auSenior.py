import requests
from datetime import datetime, timedelta
import mysql.connector

connection = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

today = datetime.now().date()
yesterday = today - timedelta(days=3)
search_date = yesterday.strftime("%Y-%m-%d")

employees = ['', '', '']

### --- Get marcação de ponto from Senior API

token = ''

for names in employees:
    payload = {

        'filter': {
            'nameSearch': names,
            'period': {
                'initialDate': search_date,
                'finalDate': search_date,
                'initialTime': '00:00:01',
                'finalTime': '23:59:59'
            },
        'sort': {
        'order': 'DESC'
            }
        }
    }

    headers = {
        'client_id': '',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    url = ''
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        cursor = connection.cursor()

        isql = "INSERT INTO clock (name, first, second, third, fourth, fifth, sixth, dateEvent, workedHours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(isql, ((names, '00:00', '00:00', '00:00', '00:00', '00:00', '00:00', search_date, 0)))
        connection.commit()
    
        i = 0
        count = 0
        ClockEvent = []
        hours = []
        minutes = []

        for item in data["result"]:
            if "timeEvent" in item:
                clockEvent = data["result"][i]["timeEvent"][:5]
                clockTime = [clockEvent]
                times = sorted(clockTime)
                x = 0
                
                hours.append(int(times[x][:2]))
                minutes.append(int(times[x][3:5]))

                db_date = search_date

                i += 1
                x += 1
                
            if i == 1:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                first = datetime.strptime(first_clock_time, "%H:%M").time()
                
                cursor = connection.cursor()
                cursor.execute(sql, (first, '00:00', '00:00', '00:00', '00:00', '00:00', search_date, 0, db_date, names))
                connection.commit()
                count = 1
                
            elif i == 2:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                second_clock_time = data["result"][1]["timeEvent"][:5]

                first = datetime.strptime(first_clock_time, "%H:%M").time()
                second = datetime.strptime(second_clock_time, "%H:%M").time()
                
                events = [first, second]
                order = sorted(events)
                
                cursor = connection.cursor()
                cursor.execute(sql, (order[0], order[1], '00:00', '00:00', '00:00', '00:00', search_date, 0, db_date, names))
                connection.commit()
                count = 2

            elif i == 3:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                second_clock_time = data["result"][1]["timeEvent"][:5]
                third_clock_time = data["result"][2]["timeEvent"][:5]

                first = datetime.strptime(first_clock_time, "%H:%M").time()
                second = datetime.strptime(second_clock_time, "%H:%M").time()
                third = datetime.strptime(third_clock_time, "%H:%M").time()
                
                events = [first, second, third]
                order = sorted(events)
                
                cursor = connection.cursor()
                cursor.execute(sql, (events[0], events[1], events[2], '00:00', '00:00', '00:00', search_date, 0, db_date, names))
                connection.commit()
                count = 3

            elif i == 4:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                second_clock_time = data["result"][1]["timeEvent"][:5]
                third_clock_time = data["result"][2]["timeEvent"][:5]
                fourth_clock_time = data["result"][3]["timeEvent"][:5]

                first = datetime.strptime(first_clock_time, "%H:%M").time()
                second = datetime.strptime(second_clock_time, "%H:%M").time()
                third = datetime.strptime(third_clock_time, "%H:%M").time()
                fourth = datetime.strptime(fourth_clock_time, "%H:%M").time()
                
                events = [first, second, third, fourth]
                order = sorted(events)
                
                cursor = connection.cursor()
                cursor.execute(sql, (order[0], order[1], order[2], order[3], '00:00', '00:00', search_date, 0, db_date, names))
                connection.commit()
                count = 4

            elif i == 5:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                second_clock_time = data["result"][1]["timeEvent"][:5]
                third_clock_time = data["result"][2]["timeEvent"][:5]
                fourth_clock_time = data["result"][3]["timeEvent"][:5]
                fifth_clock_time = data["result"][4]["timeEvent"][:5]

                first = datetime.strptime(first_clock_time, "%H:%M").time()
                second = datetime.strptime(second_clock_time, "%H:%M").time()
                third = datetime.strptime(third_clock_time, "%H:%M").time()
                fourth = datetime.strptime(fourth_clock_time, "%H:%M").time()
                fifth = datetime.strptime(fifth_clock_time, "%H:%M").time()
                
                events = [first, second, third, fourth, fifth]
                order = sorted(events)
                
                cursor = connection.cursor()
                cursor.execute(sql, (order[0], order[1], order[2], order[3], order[4], '00:00', search_date, 0, db_date, names))
                connection.commit()
                count = 5

            elif i == 6:

                sql = "UPDATE clock SET first = %s, second = %s, third = %s, fourth = %s, fifth = %s, sixth = %s, dateEvent = %s, workedHours = %s WHERE dateEvent = %s AND name = %s"
                    
                first_clock_time = data["result"][0]["timeEvent"][:5]
                second_clock_time = data["result"][1]["timeEvent"][:5]
                third_clock_time = data["result"][2]["timeEvent"][:5]
                fourth_clock_time = data["result"][3]["timeEvent"][:5]
                fifth_clock_time = data["result"][4]["timeEvent"][:5]
                sixth_clock_time = data["result"][5]["timeEvent"][:5]

                first = datetime.strptime(first_clock_time, "%H:%M").time()
                second = datetime.strptime(second_clock_time, "%H:%M").time()
                third = datetime.strptime(third_clock_time, "%H:%M").time()
                fourth = datetime.strptime(fourth_clock_time, "%H:%M").time()
                fifth = datetime.strptime(fifth_clock_time, "%H:%M").time()
                sixth = datetime.strptime(sixth_clock_time, "%H:%M").time()
                
                events = [first, second, third, fourth, fifth, sixth]
                order = sorted(events)
                
                cursor = connection.cursor()
                cursor.execute(sql, (order[0], order[1], order[2], order[3], order[4], order[5], search_date, 0, db_date, names))
                connection.commit()
                count = 6

        if count == 4:
            f_hours = hours[0] - hours[1]
            s_hours = hours[2] - hours[3]
            t_hours = 0

            f_mins = minutes[0] - minutes[1] 
            s_mins = minutes[2] - minutes[3]
            t_mins = 0

        elif count == 2:
            f_hours = hours[0] - hours[1]
            s_hours = 0
            t_hours = 0
            f_mins = minutes[0] - minutes[1] 
            s_mins = 0
            t_mins = 0
        
        elif count == 6:
            f_hours = hours[0] - hours[1]
            s_hours = hours[2] - hours[3]
            t_hours = hours[4] - hours[5]

            f_mins = minutes[0] - minutes[1] 
            s_mins = minutes[2] - minutes[3]
            t_mins = minutes[4] - minutes[5]

        elif count == 1:
            f_hours = 0
            s_hours = 0
            t_hours = 0
            f_mins = 0
            s_mins = 0
            t_mins = 0

        elif count == 3:
            f_hours = 0
            s_hours = 0
            t_hours = 0
            f_mins = 0
            s_mins = 0
            t_mins = 0

        elif count == 5:
            f_hours = 0
            s_hours = 0
            t_hours = 0
            f_mins = 0
            s_mins = 0
            t_mins = 0
        
        else:
            clockFlag = "não identificado"   

        #print(names)
    

        final_hours = f_hours + s_hours + t_hours
        final_minutes = f_mins + s_mins + t_mins

        toDecimal = final_hours + final_minutes / 60
        formatted_hours = format(abs(toDecimal), ".2f")
        wh = formatted_hours
        

        cursor = connection.cursor()
        sql = "UPDATE clock SET workedHours = %s WHERE dateEvent = %s AND name = %s"

        cursor.execute(sql, (wh, search_date, names))
        connection.commit()

cursor.close()
connection.close()
