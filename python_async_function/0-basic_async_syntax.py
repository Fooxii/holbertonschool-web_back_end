#!/usr/bin/env python3
"""Module 0-basic_async_syntax documentation"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous function documentation"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
