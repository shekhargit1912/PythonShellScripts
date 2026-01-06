import boto3
from datetime import date, timedelta

ce=boto3.client('ce')

#Dates
today=date.today()
start_date=str(today - timedelta(days=1))
day_before_start_date=str(today - timedelta(days=2))

def getdaily_cost(start_date, end_data):
    response= ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.isoformat(),
            'End': end_data.isoformat()
        },

        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy= [
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )
    costs= {}
    for group  in response['ResultByTime'][0]['Groups']:
        service= group['Keys'][0]
        amount= float(group['Metrics']['UnblendedCost']['Amount'])
        costs[service]= amount

    return costs

#get costs for two days
cost_yesterday= getdaily_cost(start_date, today)
cost_day_before= getdaily_daily_cost(day_before_start_date, start_date)

print("Daily AWs Cost Differance (per service):")


for service in cost_yesterday:
    prev=cost_day_before.get(service, 0)
    cost_day_before_amount= cost_yesterday[service]
    diff= cost_day_before_amount - prev

    print(f"{service}: ${diff:.2f}")
