# aws-dns-update
update route 53 for DDNS

## prepare

1. install boto3
1. activate boto3 for your aws account
1. create zone settings for your own domain


## usage

### set current global ip to test.hogehoge.com

```
update_dns(record_name='test', zone_name='hogehoge.com')
```

### set ip address to test.hogehoge.com

```
update_dns(record_name='test', zone_name='hogehoge.com', ip='123.123.123.123')
```
