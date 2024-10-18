class Room():
    def __init__(self, value=None):
        self.value = value
        self.next_room_list = []
    
    def insert(self, value_list):
        new_value = value_list.pop(0)
        for next_room in self.next_room_list:
            if next_room.value == new_value:
                break
        else:
            next_room = Room(new_value)
            self.next_room_list.append(next_room)

        if value_list:
            next_room.insert(value_list)
        
    def find(self, depth):
        if self.value:
            print(f"{'--'*depth}{self.value}")
        self.next_room_list.sort(key=lambda x: x.value)
        for next_room in self.next_room_list:
            next_room.find(depth+1)
                

N = int(input())

root = Room()
for _ in range(N):
    k, *info = input().split()
    root.insert(info)

root.find(-1)