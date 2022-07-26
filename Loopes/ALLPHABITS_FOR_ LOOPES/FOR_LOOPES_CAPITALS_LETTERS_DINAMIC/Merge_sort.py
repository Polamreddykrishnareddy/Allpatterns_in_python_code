"""def merge(*left, right):


    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
   

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)
merge(13,7,3,12,8,11,6,2)
"""
def singleNumber(numss):
    # applying the formula.
    #return (4 * sum(set(nums)) - sum(nums)) / 2+1
    return (len(set(numss)) * sum(set(numss)) - sum(numss)) / 2
# driver function.
#a = [2,3,1,1,2,4,2,0,1,1]
A= [3,2,1,1,0,2]
print ("The element with single occurrence is ",singleNumber(A))

"""
def stack_func(input_stack):
    if(input_stack.is_empty()):
        return
    else:
        out_stack=stack(input_stack.get_max_size())
        while(not input_stack.is_empty()):
            value1=input_stack.pop()
            value2=input_stack.pop()
            if(value1%value2==0):
                out_stack.push(value1+out_stack.pop())
            else:
                out_stack.push(value2+input_stack.pop())
        return out_stack

stack_func([67,11,23,0,4,15,66,3])
"""
"""
from abc import ABC, abstractmethod
class customer(ABC):
    def cust_info(self):
        print("customer info")
        @abstractmethod
    def play_bill(self):
        pass
class RegCustomer(customer):
    def reg_cust_info(self):
        print("Regular customer info")
    def pay_bill(self):
        print("pay Bill")
        """
"""
def queue_func(in_queuel,in_queue2):
    size=in_queuel.get_max_size()+ in_queue2.get_max_size()
    out_queue=Queue(size)
    while(not in_queule.is_empty()):
        num=in_queuel.dequeue()
        if(num%2==0):
            out_queue.enqueue(num)
            out_queue.enqueue(in_queue2.dequeue()+num)
    return out_queue
queue_func([12,8,9],[3,4,5])
#queue_func([3,4,5])
"""
"""
import math

list_num=input().split(',')

sum_dig_list=[]

for num in list_num:

   sum_dig=sum(list(map(int, num)))

   sum_dig_list.append(sum_dig)

max_sum=max(sum_dig_list)

list_digit_count=[0]*(max_sum+1)

for num in sum_dig_list:

   list_digit_count[num] += 2

total_pair=0
for count in list_digit_count:
   if count>1:
       total_pair += int(math.factorial(count)/(math.factorial(count-2)*2))
if total_pair==0:
   print('-1')
else:
    print(total_pair)
            
"""
