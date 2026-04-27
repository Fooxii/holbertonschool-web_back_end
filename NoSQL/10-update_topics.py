#!/usr/bin/env python3
"""Module 10-update_topics.py documentation"""


def update_topics(mongo_collection, name, topics):
    """Function documentation"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
