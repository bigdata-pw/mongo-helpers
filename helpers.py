from pymongo.collection import Collection
from typing import Any, List, Dict


def find_duplicates(collection: Collection, field: str):
    pipeline = [
        {"$group": {"_id": f"${field}", "count": {"$count": {}}}},
        {"$match": {"count": {"$gt": 1}}},
    ]
    duplicates = list(collection.aggregate(pipeline))
    return duplicates


def query_and(queries: List[Dict[str, Any]]):
    return {"$and": queries}


def query_or(queries: List[Dict[str, Any]]):
    return {"$or": queries}


def query_exists(field: str):
    return {field: {"$exists": True}}


def query_not_exists(field: str):
    return {field: {"$exists": False}}


def query_eq(field: str, value: Any):
    return {field: {"$eq": value}}


def query_ne(field: str, value: Any):
    return {field: {"$ne": value}}


def query_gt(field: str, value: Any):
    return {field: {"$gt": value}}


def query_gte(field: str, value: Any):
    return {field: {"$gte": value}}


def query_lt(field: str, value: Any):
    return {field: {"$lt": value}}


def query_lte(field: str, value: Any):
    return {field: {"$lte": value}}


def query_in(field: str, values: List[Any]):
    return {field: {"$in": values}}


def query_sort(field: str, direction: int):
    return {"$sort": {field: direction}}


def query_project(fields: List[str]):
    projection = {field: 1 for field in fields}
    return {"$project": projection}


def query_paginate(skip: int, limit: int):
    return [{"$skip": skip}, {"$limit": limit}]
