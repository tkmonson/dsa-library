'''
Single-Threaded CPU (#1834)

You are given n tasks labeled from 0 to n - 1 represented by a 2D integer
array `tasks`, where `tasks[i] = [enqueueTime_i, processingTime_i]` means that
the task will be available to process at `enqueueTime_i` and will take
`processingTime_i` to finish processing.

You have a single-threaded CPU that can process at most one task at a time and
will act in the following way:

    * If the CPU is idle and there are no available tasks to process, the CPU
      remains idle.
    * If the CPU is idle and there are available tasks, the CPU will choose the
      one with the shortest processing time. If multiple tasks have the same
      shortest processing time, it will choose the task with the smallest
      index.
    * Once a task is started, the CPU will process the entire task without
      stopping.
    * The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

1 <= tasks.length <= 10^5
1 <= enqueueTime_i, processingTime_i <= 10^9
'''

import heapq

def get_order(tasks: list[list[int]]) -> list[int]:
    ans = []
    heap = []

    # (enqueue_time, processing_time, original_index)
    tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
    tasks.sort()

    i = 0
    current_time = tasks[0][0]
    while True:
        while i < len(tasks) and tasks[i][0] <= current_time:
            _, processing_time, task_i = tasks[i]
            heapq.heappush(heap, (processing_time, task_i))
            i += 1

        if heap:
            processing_time, task_i = heapq.heappop(heap)
            current_time += processing_time
            ans.append(task_i)
        else:
            try:
                current_time = tasks[i][0]
            except IndexError:
                break

    return ans

'''
CPU will choose available task with shortest processing time => use a heap.

At first, I thought about time incrementing by one click. At any click, you can
add available tasks to the heap, begin a task, or end a task.

But incrementing by one click is slow. Other optimizations:
    * When you begin a task, skip time forward to the end of the task and then
      add any tasks to the heap that became available during the interval.
    * If the CPU is idle and there are no available tasks, skip time forward to
      the task that will be available next.
        - To do this, you need to sort all the tasks by enqueue_time and also
          mark each item will its original index, so it can be added to the
          heap with that original index.

One could make the argument that you should just tick up if the CPU is idle and
there are no available tasks instead of taking the time to sort, but the
problem states there are at most 100K tasks and at most 1B clicks, so it is
much faster to sort the tasks and iterate over them than over all time.
'''

if __name__ == '__main__':
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    print(get_order(tasks))
