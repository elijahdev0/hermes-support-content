# DockerStartContainerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_id** | **str** |  | 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.docker_start_container_request import DockerStartContainerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DockerStartContainerRequest from a JSON string
docker_start_container_request_instance = DockerStartContainerRequest.from_json(json)
# print the JSON string representation of the object
print(DockerStartContainerRequest.to_json())

# convert the object into a dict
docker_start_container_request_dict = docker_start_container_request_instance.to_dict()
# create an instance of DockerStartContainerRequest from a dict
docker_start_container_request_from_dict = DockerStartContainerRequest.from_dict(docker_start_container_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


