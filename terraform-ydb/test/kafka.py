import rpc

rpc Get (GetDiskRequest) returns (Disk) {
    option (google.api.http) = {
        get: "/compute/v1/disks/{disk_id}"
    };
    }

def kafka(event, context):
    name = event['queryStringParameters']['clusterId']

    message GetDiskRequest {
        string disk_id = 1;
    }

    
    if ...:
        return False
    return True