# aws-dns-update
update route 53 for DDNS

## prepare

1. install boto3
1. activate boto3 for your aws account
1. create zone settings for your own domain


## usage

### set current global ip to test.hogehoge.com

```
$ python3 aws-dns-update.py test hogehoge.com
```

### set `123.123.123.123` to test.hogehoge.com

```
$ python3 aws-dns-update.py test hogehoge.com 123.123.123.123
```
