# 2. Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



- **Example 1:**

  ![img](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

  ```
  Input: l1 = [2,4,3], l2 = [5,6,4]
  Output: [7,0,8]
  Explanation: 342 + 465 = 807.
  ```

  **Example 2:**

  ```
  Input: l1 = [0], l2 = [0]
  Output: [0]
  ```

  **Example 3:**

  ```
  Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
  Output: [8,9,9,9,0,0,0,1]
  ```

   

  **Constraints:**

  - The number of nodes in each linked list is in the range `[1, 100]`.
  - `0 <= Node.val <= 9`
  - It is guaranteed that the list represents a number that does not have leading zeros.



### My Code

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 첫 노드 계산
        sum_list = ListNode((l1.val+l2.val) % 10)
        carry = int((l1.val+l2.val) / 10)
        temp = sum_list
        # 두 번째 노드 부터 계산
        while True:
            if l1.next == None and l2.next == None:
                break
            if l1.next != None:
                l1 = l1.next
            else:
                l1 = ListNode(0)
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = ListNode(0)
            temp.next = ListNode((l1.val+l2.val+carry) % 10)
            temp = temp.next
            carry = int((l1.val+l2.val+carry) / 10)
        if carry:
            temp.next = ListNode(carry)
        return sum_list
```



### Result

Runtime : 72ms ( 67.62% )

Memory Usage : 14.4MB ( 44.94% )
