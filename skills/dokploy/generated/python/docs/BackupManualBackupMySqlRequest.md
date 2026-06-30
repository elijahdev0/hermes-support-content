# BackupManualBackupMySqlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **str** |  | 

## Example

```python
from dokploy_client.models.backup_manual_backup_my_sql_request import BackupManualBackupMySqlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BackupManualBackupMySqlRequest from a JSON string
backup_manual_backup_my_sql_request_instance = BackupManualBackupMySqlRequest.from_json(json)
# print the JSON string representation of the object
print(BackupManualBackupMySqlRequest.to_json())

# convert the object into a dict
backup_manual_backup_my_sql_request_dict = backup_manual_backup_my_sql_request_instance.to_dict()
# create an instance of BackupManualBackupMySqlRequest from a dict
backup_manual_backup_my_sql_request_from_dict = BackupManualBackupMySqlRequest.from_dict(backup_manual_backup_my_sql_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


