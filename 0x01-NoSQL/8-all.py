#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""

def list_all(mongo_collection):
    """List all doc in a collection"""
    return [doc for doc in mongo_collection.find()]
