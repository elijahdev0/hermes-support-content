# VolumeBackupsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_backup_id** | **str** |  | 

## Example

```python
from dokploy_client.models.volume_backups_delete_request import VolumeBackupsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeBackupsDeleteRequest from a JSON string
volume_backups_delete_request_instance = VolumeBackupsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(VolumeBackupsDeleteRequest.to_json())

# convert the object into a dict
volume_backups_delete_request_dict = volume_backups_delete_request_instance.to_dict()
# create an instance of VolumeBackupsDeleteRequest from a dict
volume_backups_delete_request_from_dict = VolumeBackupsDeleteRequest.from_dict(volume_backups_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


