import boto3
import json
import requests
import pprint

# curl httpbin.org/ip


def get_my_ip():
    response = requests.get(
        'http://httpbin.org/ip'
    )
    # pprint.pprint(response.json())
    ip = response.json()['origin']

    return ip


def update_dns(record_name, zone_name):

    ip = get_my_ip()

    route53 = boto3.client('route53')

    # get zone Id
    response = route53.list_hosted_zones_by_name(DNSName=zone_name)
    zone_id = response['HostedZones'][0]['Id']

    # update record
    response = route53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': record_name + '.' + zone_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': ip
                            }
                        ]
                    }
                }
            ]
        }
    )

    pprint.pprint(response)

    # check update


if __name__== '__main__':
    update_dns('test', 'brain.sc')

