# mongo-helpers
helper functions for pymongo

## Usage

```python
uri = ""
client = MongoClient(uri)
db = client.example
example = db["example"]

example.find_one(
    query_and([
        query_gt("count", 0),
        query_lt("count", 10),
    ])
)

example.count_documents(query_exists("test"))

duplicates = find_duplicates(example, "test")
```

Equivalent to
```python
uri = ""
client = MongoClient(uri)
db = client.example
example = db["example"]

example.find_one(
    {"$and": [
        {"count": {"$gt": 0}},
        {"count": {"$lt": 10}}
    ]}
)

example.count_documents({"test": {"$exists": True}})

pipeline = [
    {"$group": {"_id": "$test", "count": {"$count": {
    {"$match": {"count": {"$gt": 1}}},
]
duplicates = list(example.aggregate(pipeline))
```

## Why

It's just easier to use
