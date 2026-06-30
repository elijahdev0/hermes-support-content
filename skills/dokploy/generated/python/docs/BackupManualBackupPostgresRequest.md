# BackupManualBackupPostgresRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** |  | 

## Example

```python
from dokploy_client.models.backup_manual_backup_postgres_request import BackupManualBackupPostgresRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BackupManualBackupPostgresRequest from a JSON string
backup_manual_backup_postgres_request_instance = BackupManualBackupPostgresRequest.from_json(json)
# print the JSON string representation of the object
print(BackupManualBackupPostgresRequest.to_json())

# convert the object into a dict
backup_manual_backup_postgres_request_dict = backup_manual_backup_postgres_request_instance.to_dict()
# create an instance of BackupManualBackupPostgresRequest from a dict
backup_manual_backup_postgres_request_from_dict = BackupManualBackupPostgresRequest.from_dict(backup_manual_backup_postgres_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


