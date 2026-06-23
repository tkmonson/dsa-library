'''
Online Stock Span (#901)

Design an algorithm that collects daily price quotes for some stock and returns
the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive
days (starting from that day and going backward) for which the stock price was
less than or equal to the price of that day.

e.g. prev = [7, 2, 1, 2], curr = 2 => span = 4

Implement the StockSpanner class:
    - StockSpanner(): Initializes the object of the class.
    - int next(int price): Returns the span of the stock's price given that
                           today's price is `price`.
'''

# Time: O(n)
# Auxiliary space: O(n)
class StockSpanner:
    def __init__(self):
        self.monotonic_stack = []  # price, span

    def next(self, price: int) -> int:
        stack = self.monotonic_stack
        curr_span = 1

        while stack and stack[-1][0] <= price:
            _, prev_span = stack.pop()
            curr_span += prev_span

        stack.append([price, curr_span])
        return curr_span
    
'''
curr < prev: curr_span == 1
curr == prev: curr_span == prev_span + 1
curr > prev: curr_span == prev_span + 1 + potentially other spans

You are looking for the left side of the span, which is curr's previous greater
element. This suggests the use of a monotonic stack.

Put decreasing elements onto the stack. When curr is greater than the top of
the stack, pop elements off of the stack until curr can be put on the stack
while maintaining decreasing order (until the top of the stack is curr's
previous greater element). Store span info in the same stack. The current span
aggregates the spans of previous non-greater elements.
'''

# Time: O(n)
# Auxiliary space: O(n)
class StockSpanner2:
    def __init__(self):
        self.prices = [float('inf')]
        self.spans = [0]
    
    def next(self, price: int) -> int:
        span = 1
        i = len(self.prices) - 1
        while self.prices[i] <= price:
            span += self.spans[i]
            i -= self.spans[i]
        
        self.prices.append(price)
        self.spans.append(span)
        return span
 

if __name__ == '__main__':
    s = StockSpanner()
    s.next(100)
    s.next(80)
    s.next(60)
    s.next(70)
    s.next(60)
    s.next(75)
    s.next(85)
