## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case 1 : 하필 찾는 애가 head 인 경우 (다현 ,화사)
    if (findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 찾는 애가 중간에 있는 경우(사나, 솔라)
    current = head
    while(current.link != None):
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return

    # Case 3 : 없는 노드 앞에 삽입(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # Case 1 : head 삭제(다현)
    if (head.data == deleteData):
        current = head
        head = head.link
        del(current)
        return

    # Case 2 : 지울애가 중간 인 경우(쯔위)
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            del(current)
            return

    # Case 3 : 지울 애가 없는 경우(재남)
    return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if (current.data == findData):
        return current
    while (current.link != None):
        current = current.link
        if (current.data == findData):
            return current
    return Node()

## 변수
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
#* 연결 리스트 생성
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 안 중요(생략 가능)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)


printNodes(head)

#* 데이터 삽입
# insertNode('다현', '화사') # 찾을 데이터, 삽입할 데이터
# insertNode('사나', '솔라')
# insertNode('재남', '문별')
# printNodes(head)


# deleteNode('다현') # 삭제할 데이터
# deleteNode('쯔위')
# deleteNode('재남')
# printNodes(head)

returnNode = findNode('사나')
print(returnNode.data, '뮤비가 나옵니다. 쿵짝쿵짝')
