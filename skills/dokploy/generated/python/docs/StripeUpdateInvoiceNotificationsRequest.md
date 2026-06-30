# StripeUpdateInvoiceNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 

## Example

```python
from dokploy_client.models.stripe_update_invoice_notifications_request import StripeUpdateInvoiceNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StripeUpdateInvoiceNotificationsRequest from a JSON string
stripe_update_invoice_notifications_request_instance = StripeUpdateInvoiceNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(StripeUpdateInvoiceNotificationsRequest.to_json())

# convert the object into a dict
stripe_update_invoice_notifications_request_dict = stripe_update_invoice_notifications_request_instance.to_dict()
# create an instance of StripeUpdateInvoiceNotificationsRequest from a dict
stripe_update_invoice_notifications_request_from_dict = StripeUpdateInvoiceNotificationsRequest.from_dict(stripe_update_invoice_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


