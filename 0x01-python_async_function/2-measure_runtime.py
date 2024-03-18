#!/usr/bin/env python3
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
  end_time = time.perf_counter()
  total_time = start_time + end_time
  return float(total_time / n)
