import boto3 as boto3
from boto3.dynamodb.conditions import Key

dynamo_client = boto3.resource(service_name='dynamodb', region_name='eu-west-1',
                               aws_access_key_id='ASIAX2KHRAJA5O6MNW5E',
                               aws_secret_access_key='xMJPDNZSFLLoM/9P/VCmMa6jmwG2u7LVXfteydq2',
                               aws_session_token='IQoJb3JpZ2luX2VjEA8aCWV1LXdlc3QtMSJHMEUCIDX3GhBraOz6SRkE0GlGLaRgqnJLEdSM2puYwHBTj581AiEA3zH3sPnqFvDIyTwTtlM7YAGdnfp3eSUrGtDb9OWYh6YqpAMIiP//////////ARADGgw1Mzc1NTc3OTUzOTMiDCoJs8Cl3BSGikL6wCr4Akwy5jBRgglostLK1Aie8gsBuV0PSOuZf64gHV+w+mdFWj1RyffxOKCdGawPyTgtQjaI//ipgNb6NMYfzV7ocUbym5TX1uj+LMFkwiWiRE4hjfqQ8K++zBSJ6hPyW/2qH/o6sM17woZ+jAlLo+RfhaaQO4axw8jIX051bmTdbQ5U0CqEebk+gzGm7KO6F1rOZTTasuhZ4NqEuv0ydNPojnG3KGs9kGiXdXd7YzXtwX//FEUtDvX0S9MLOhhraB1naFsCw/j0dY7JsLMIPfVjhUFMSxjua1kuRcyFJLqjQj+1zP6sMZYIRXnvmM2MvnMADZcfeGMXA2f09HKLg1Oy9REBApPKGESpM7a9GY2RRrQq6QquUo2QI5B3/1fkMBr6seBsHI97tsldahBC0ReW49t3ejVN2a6Xe1WpVDPFE+zt91fOz5LtrKOvYWY+Ory9M7lejeB2bbtykm/gDygx4Nut9Y+vX5760/c3C9TSzp+X4LddAkf9WMYw2cfdngY6pgF3Y2vpCjwrcqMmRzmUekRumfoje7uiCqfq8PhcTEpWVKt4iMNroJyjCCN3IX4NE6SsZpzXk9XLisH2ejYSYRjAaVJchHXrh+//Li+cjqa5IWY9TkZzZuO4g7nCvleyhewR9s05GzJWmts/Qi8+SG9Ns7Eo0LRiRUCgeOLDeMkjrHd9gm78nNXRrxRpUa8xDBClwfwpa8qynoidFq0OPTjC/cl8SBsy')
__connected_table__ = dynamo_client.Table("freshers-example")

print(__connected_table__.table_status)
print("\n")