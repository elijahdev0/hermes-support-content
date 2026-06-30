# VolumeBackupsRunManuallyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_backup_id** | **str** |  | 

## Example

```python
from dokploy_client.models.volume_backups_run_manually_request import VolumeBackupsRunManuallyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeBackupsRunManuallyRequest from a JSON string
volume_backups_run_manually_request_instance = VolumeBackupsRunManuallyRequest.from_json(json)
# print the JSON string representation of the object
print(VolumeBackupsRunManuallyRequest.to_json())

# convert the object into a dict
volume_backups_run_manually_request_dict = volume_backups_run_manually_request_instance.to_dict()
# create an instance of VolumeBackupsRunManuallyRequest from a dict
volume_backups_run_manually_request_from_dict = VolumeBackupsRunManuallyRequest.from_dict(volume_backups_run_manually_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


