import boto3
import requests
import time
import sys


def get_my_ip():
    response = requests.get('http://httpbin.org/ip')
    ip = response.json()['origin']

    return ip


def update_dns(record_name, zone_name, ip=None, check=True):

    if not ip:
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

    # pprint.pprint(response)
    print('Set %s: %s' % (record_name + '.' + zone_name, ip))

    # check update
    while check:
        time.sleep(2)
        response = route53.get_change(Id=response['ChangeInfo']['Id'])
        if response['ChangeInfo']['Status'] == 'INSYNC':
            print('OK')
            break


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python %s [record name] [zone name] (IP address)')

    record_name = sys.argv[1]
    zone_name = sys.argv[2]
    
    if len(sys.argv) == 4:
        ip_address = sys.argv[3]
    else:
        ip_address = None
        
    update_dns(record_name=record_name, zone_name=zone_name, ip=ip_address)

