# StripeCreateCheckoutSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**product_id** | **str** |  | 
**server_quantity** | **float** |  | 
**is_annual** | **bool** |  | 

## Example

```python
from dokploy_client.models.stripe_create_checkout_session_request import StripeCreateCheckoutSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCreateCheckoutSessionRequest from a JSON string
stripe_create_checkout_session_request_instance = StripeCreateCheckoutSessionRequest.from_json(json)
# print the JSON string representation of the object
print(StripeCreateCheckoutSessionRequest.to_json())

# convert the object into a dict
stripe_create_checkout_session_request_dict = stripe_create_checkout_session_request_instance.to_dict()
# create an instance of StripeCreateCheckoutSessionRequest from a dict
stripe_create_checkout_session_request_from_dict = StripeCreateCheckoutSessionRequest.from_dict(stripe_create_checkout_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


