#!/usr/bin/env python3
"""Module 11-school_by_topic.py documentation"""


def schools_by_topic(mongo_collection, topic):
    """Function documentation"""
    return list(mongo_collection.find({"topics": topic}))
