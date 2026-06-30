# StripeUpgradeSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**server_quantity** | **float** |  | 
**is_annual** | **bool** |  | 

## Example

```python
from dokploy_client.models.stripe_upgrade_subscription_request import StripeUpgradeSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeUpgradeSubscriptionRequest from a JSON string
stripe_upgrade_subscription_request_instance = StripeUpgradeSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(StripeUpgradeSubscriptionRequest.to_json())

# convert the object into a dict
stripe_upgrade_subscription_request_dict = stripe_upgrade_subscription_request_instance.to_dict()
# create an instance of StripeUpgradeSubscriptionRequest from a dict
stripe_upgrade_subscription_request_from_dict = StripeUpgradeSubscriptionRequest.from_dict(stripe_upgrade_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


