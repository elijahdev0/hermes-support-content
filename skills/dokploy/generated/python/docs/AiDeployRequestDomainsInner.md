# AiDeployRequestDomainsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**port** | **float** |  | 
**service_name** | **str** |  | 

## Example

```python
from dokploy_client.models.ai_deploy_request_domains_inner import AiDeployRequestDomainsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiDeployRequestDomainsInner from a JSON string
ai_deploy_request_domains_inner_instance = AiDeployRequestDomainsInner.from_json(json)
# print the JSON string representation of the object
print(AiDeployRequestDomainsInner.to_json())

# convert the object into a dict
ai_deploy_request_domains_inner_dict = ai_deploy_request_domains_inner_instance.to_dict()
# create an instance of AiDeployRequestDomainsInner from a dict
ai_deploy_request_domains_inner_from_dict = AiDeployRequestDomainsInner.from_dict(ai_deploy_request_domains_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


