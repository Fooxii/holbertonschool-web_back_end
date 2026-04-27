#!/usr/bin/env python3
"""Module 9-insert_school.py documentation"""


def insert_school(mongo_collection, **kwargs):
    """Function documentation"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
