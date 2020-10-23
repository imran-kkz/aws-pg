# notepad

## create ddb table in cli
```
aws dynamodb create-table \
--table-name Starships \
--attribute-definitions \
AttributeName=ShipClass,AttributeType=S \
AttributeName=Registry,AttributeType=S \
--key-schema \
AttributeName=ShipClass,KeyType=HASH \
AttributeName=Registry,KeyType=RANGE \
--provisioned-throughput \
ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region ca-central-1
```
