def solution(book_time):
    answer = 0
    # 본격적인 계산 시작 전에 book_time은 미리 sort로 정렬해둠
    book_time.sort()
    # 가상의 호텔을 가정해 hotel_rooms 리스트를 생성
    hotel_rooms = []
    
    # 각 예약 시간 정확히 비교하기 위해 분(int)으로 바꿔주는 change_minute 제작
    def change_minute(now_time):
        new_time = int(now_time[:2]) * 60 + int(now_time[3:])
        return new_time
    
    # 당일 예약 받은(book_time) 수만큼 반복
    for now_customer in range(len(book_time)):
        # 현재 예약 book 내부 시간 값을 분 단위로 바꿔서 재지정
        book = [change_minute(book_time[now_customer][0]), change_minute(book_time[now_customer][1])+10]
        # 해당 예약자가 체크인 하는 시간을 현재 시간으로 설정
        now_time = book[0]
        # 만약 현재 손님이 첫 손님이 아니라면, 현재 시간 전에 체크아웃했거나 해야 할 손님이 있는지, 사용하고 있는 호텔 방의 수(정확히는 hotel_rooms에서 값이 담긴 리스트의 수)를 확인할 필요가 있음
        if now_customer != 0:
            # 체크아웃하지 않고 호텔에 남는 손님의 수를 담아줄 let_hotel 생성
            let_hotel = []
            # 현재 호텔 룸 수만큼 반복함
            # 만약 현재 시간과 대조해봤을 때 해당 손님이 체크아웃하거나 했던 손님일 시, pass함
            # 반면 아직 체크아웃할 시간이 아니라면, let_hotel에 담아줌
            for room_num in range(len(hotel_rooms)):
                if now_time >= hotel_rooms[room_num][1]:
                    pass
                else:
                    let_hotel.append(hotel_rooms[room_num])
            # 이후 hotel_rooms를 let_hotel로 교체해줌
            hotel_rooms = let_hotel
        
        # 현재 손님도 호텔에서 머물러야 하므로, append로 현재 예약(book)을 추가해줌
        hotel_rooms.append(book)
        
        # 이 문제는 최대 객실의 수를 구하는 것임
        # 따라서 현재 사용하고 있는 객실의 수를 나타내는 리스트인 hotel_rooms의 길이가 answer보다 크다면, 해당 값으로 교체해주면 됨
        if len(hotel_rooms) > answer:
            answer = len(hotel_rooms)
    
    # 모든 연산 끝난 후, 답 리턴함
    return answer