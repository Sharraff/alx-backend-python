#!/usr/bin/env python3
"""
Defines a function to measure time
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Return the average time it takes for coroutines to complete

    measure_time: run time of opperation
    Args:
        n: int
        max_delay: int
    return: float
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return float(total_time / n)
