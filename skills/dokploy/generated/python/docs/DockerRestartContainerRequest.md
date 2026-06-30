# DockerRestartContainerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** |  | 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.docker_restart_container_request import DockerRestartContainerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DockerRestartContainerRequest from a JSON string
docker_restart_container_request_instance = DockerRestartContainerRequest.from_json(json)
# print the JSON string representation of the object
print(DockerRestartContainerRequest.to_json())

# convert the object into a dict
docker_restart_container_request_dict = docker_restart_container_request_instance.to_dict()
# create an instance of DockerRestartContainerRequest from a dict
docker_restart_container_request_from_dict = DockerRestartContainerRequest.from_dict(docker_restart_container_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


