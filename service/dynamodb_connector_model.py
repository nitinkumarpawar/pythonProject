import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJAXYR74NPE',
                               aws_secret_access_key='g+O+2tSrT0VqwmvNd0Z3LNLpvyVz+g2ZMtzpMb91',
                               aws_session_token='IQoJb3JpZ2luX2VjEKf//////////wEaCWV1LXdlc3QtMSJHMEUCIQDTgV16Yq/KRNq8JLI7Ak8jxmPa6/1ucKSJDQYk971jDgIga93HZ1xUrFPdOLs/4TfLso/Fu/SlwUxYOHRJRkF7IZkqmwMIMBAEGgw1Mzc1NTc3OTUzOTMiDP1Xog1FQ0/6P8s+wCr4Akz1tJzhfMuxjlOoPKsgZf+9RQoQCVVH+8/Psn9LxMoPEc/YxNGHoXQpn67y/RNmpUdP8oONXu6NOiy5OEUYzvkGulAUfx9Tf2mFIvqITTk23c5RhETD3tB+ccdj3qBuYeHMjsrKQChkH6HZlVvtKMiG6zBUhgmRY3Ahh+xHv68p6VV0CnKsj1O9bc5koaND7k7TShIyiBwKI3/T6CngtOfNzqqX88sUdQuqbtwZ/b+xLDrJl7FyYHls4KVQCmhe8gTa+kqwasAbqnhHtPdrJyqrCwodRQTUAqpDd1QuL7I3kX+4ORvXJ51ncIg2uRmDSuoh06HSlu4tN4tBgKGMMjS+SSnCCfUtGjpuvgqKqId9n4QqYkY0a+y09d0THDecTtmCrufx0ILYrp6u5ESQLotG/PidEAbIysRcliviFTERsZKL4b1BE6A5VwApLd655pLmeFeOoJ+eZCI5o01KUh9Ul7fP6gkiWqtx/JAAXJT5rS/uaQtJhmUwzYj/ngY6pgFVjsXQdgTAM3TDjGP0urzfVgYQqhC54IKLu4UcDbLp6FMOBdMOVf6hSmStseR7sYVi4TEH9gk/OUOwBntAH6QqyFoeEipgEKVXEhtdzHUxZALDwUpRGL8VTkMZ7VRYwFzPSegEv8eRYRTmMAOGMPe1DsWZPr/7eGVzoblpZYDwEU8XXPNDgEHJyT3jE5sg6mM3mws+fR1yk1V2sD4hnbqZAHL82YUE')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")
