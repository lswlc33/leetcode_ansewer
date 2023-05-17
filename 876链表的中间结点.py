# 给你单链表的头结点 head ，请你找出并返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# 例子：
# 输入：head = [1,2,3,4,5]
# 输出：[3,4,5]
# 解释：链表只有一个中间结点，值为 3 。
head = [1,2,3,4,5,6]

# 仅展示


def middleNode1(head):
    l, c = 0, head
    while c:
        c = c.next
        l += 1
    c = head
    for i in range(0,l // 2):
        c = c.next
    return c


def middleNode2(head):
    a = b = head
    while a:
        try:
            a = a.next.next
        except:
            return b
        b = b.next
    return b

def middleNode3(head):
    a = b = head
    while a and a.next:
        a = a.next.next
        b.next
    return b