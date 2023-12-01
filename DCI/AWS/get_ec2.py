import boto3

ec2 = boto3.resource('ec2')

# for instance in ec2.instances.all():
#     print(instance.id, instance.state)


## Task 2.
## *Discover All Regions*:
## Use Boto3 to find all available AWS regions that support EC2 service.

def list_ec2_instances_and_volumes():
    session = boto3.Session()
    ec2_client = session.client('ec2')

    regions = ec2_client.describe_regions()['Regions']
    list_regions = [region['RegionName'] for region in regions]

    for region in list_regions:
        print(f'Region: {region}')

        region_client = session.client('ec2', region_name=region)
        instances = region_client.describe_instances()
        
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                print(f'Instance: {instance["InstanceId"]}, '
                      f'InstanceType: {instance["InstanceType"]}, '
                      f'State: {instance["State"]["Name"]}, '
                      f'InstanceName: {instance["Tags"][0]["Value"]}')

        volumes = region_client.describe_volumes()
        for volume in volumes['Volumes']:
            print(f'Volume: {volume["VolumeId"]}, '
                  f'Size: {volume["Size"]}, '
                  f'State: {volume["State"]}, '
                  f'VolumeType: {volume["VolumeType"]}, ')



list_ec2_instances_and_volumes()
