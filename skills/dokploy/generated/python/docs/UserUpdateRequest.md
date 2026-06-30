# UserUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**is_registered** | **bool** |  | [optional] 
**expiration_date** | **str** |  | [optional] 
**created_at2** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**two_factor_enabled** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**banned** | **bool** |  | [optional] 
**ban_reason** | **str** |  | [optional] 
**ban_expires** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**enable_paid_features** | **bool** |  | [optional] 
**allow_impersonation** | **bool** |  | [optional] 
**enable_enterprise_features** | **bool** |  | [optional] 
**license_key** | **str** |  | [optional] 
**stripe_customer_id** | **str** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**servers_quantity** | **float** |  | [optional] 
**send_invoice_notifications** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**current_password** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.user_update_request import UserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateRequest from a JSON string
user_update_request_instance = UserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UserUpdateRequest.to_json())

# convert the object into a dict
user_update_request_dict = user_update_request_instance.to_dict()
# create an instance of UserUpdateRequest from a dict
user_update_request_from_dict = UserUpdateRequest.from_dict(user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


