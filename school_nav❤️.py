def load_rooms():
    a_c = "CAFETERIA"
    a_s = "STAGE"
    a_g1 = "GYM"
    a1 = "1"
    a2 = "2"
    a3 = "3"
    a4 = "4"
    a5 = "5"
    a6 = "6"

    b7 = "7"
    b8 = "8"
    b9 = "9"
    b10 = "10"
    b11 = "11"
    b12 = "12"
    b16_1 = "16"
    b_m = "LIBRARY"

    c16_2 = "16"
    c24 = "24"
    c26 = "26"
    c27 = "27"
    c28 = "28"
    c29 = "29"

    d30 = "30"
    d31 = "31"
    d32 = "32"
    d33 = "33"
    d34 = "34"
    d35 = "35"
    d36 = "36"
    d37 = "37"
    d38 = "38"
    d_g2 = "GYM"

    a = [a_c, a_s, a_g1, a1, a2, a3, a4, a5, a6]
    a_direction_room_to_node = ["walk straight beyond the gym, to the intersection of halls",
    "take a left down to the intersection of halls",
    "take a right down to the intersection of halls",
    "take a left down to the intersection of halls",
    "take a right and go slightly forward to the intersection of halls",
    "take a right and go slightly forward to the intersection of halls",
    "take a left and go slightly forward to the intersection of halls",
    "take a right and go down to the intersection of halls",
    "take a left and go down to the intersection of halls"]
    a_direction_node_to_room = ["face south and go straight",
    "face south and go straight, then take a right at the door before the stage",
    "face south and go straight then take a left at the first doors you see",
    "face south and go straight then take a right at the first door after the boys restroom",
    "face east and go straight a small amount then take a left at the first door",
    "face north and go straight a small amount then take a left at the first door",
    "face north and go straight a small amount then take a right at the first door",
    "face north and go straight then take a left at the second door",
    "face north go straight then take a right at the second door"]
    a_b = "Face north and go forward until the intersection of halls"
    a_c = "Face east and go forward until the first intersection of halls, and then face north and go forward until the intersection of halls"
    a_d = "Face east and go forward until the first intersection of halls"

    b = [b7, b8, b9, b10, b11, b12, b16_1, b_m]
    b_direction_room_to_node = ["Exit room 7 and take a left until you reach the intersection of halls",
    "Exit room 8 and take a right until you reach the intersection of halls.",
    "Exit room 9 and take a left until you reach the intersection of halls",
    "Exit room 10 and take a right until you reach the intersection of halls",
    "Exit room 11  and take a left until you reach the intersection of halls",
    "Exit room 12 and take a right until you reach the intersection of halls",
    "Exit room 16 and take a right until you reach the intersection of halls",
    "Exit the Library and take a left until you reach the intersection of halls"
    ]
    b_direction_node_to_room = ["Turn towards the office/cafeteria (South) and room 7 is the 3rd classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 8 is the 3rd classroom on the left side",
    "Turn towards the office/cafeteria (South) and room 9 is the 2nd classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 10 is the 2nd classroom on the left side",
    "Turn towards the office/cafeteria (South) and room 11 is the 1st classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 12 is the 1st classroom on the left side",
    "Turn towards the media center (East) and room 16 is the 1st room on the left side",
    "Turn towards the media center (East) and the media center is the 1st room on the right side"
    ]
    b_c = "Turn to face towards the library (East) then go straight towards the intersection of the halls"
    b_a = "Turn towards the classroom (South) then go forward until you reach the intersection"
    b_d = "Turn towards the classroom (South) then go forward until you reach the intersections then turn towards the commons (East) and go straight"

    c = [c16_2, c24, c26, c27, c28, c29]
    c_direction_room_to_node = ["Exit room 16 and take a left until you enter the intersection of halls",
    "Exit room 24 and take a left until you enter the intersection of halls (It’s very close, and DO NOT enter the double doors)",
    "Exit room 26 and take a right until intersection of hallways before the double doors (DO NOT enter the double doors)",
    "Exit room 27 and take a left until you reach the intersection of hallways (DO NOT enter the double doors)",
    "Exit room 28 and take a right and walk until you reach the intersection of hallways (DO NOT enter the double doors)",
    "Exit room 29, take a left and walk until you reach the intersection of hallways (DO NOT enter the double doors)"]
    c_direction_node_to_room = ["Face West and walk straight, after passing the bathrooms room 16 should be on your left",
    "Face South and walk straight, and room 24 should be the first room on the right",
    "Face south and walk straight, and room 26 will be on the left",
    "Face south and walk straight, and room 27 will be the second room to the right",
    "Face south and walk straight, and room 28 will be the second room on the left",
    "Face south and walk straight, and room 29 will be the third room on the right"]
    c_b = "walk towards the bathrooms until you reach the next intersection of halls"

    c_d = "Walk towards room 24 until you reach the next intersection of halls, you should see ascending room numbers as you walk"

    c_a = "Walk towards the bathrooms until you reach the next intersection of halls, then take a left, and walk you should see rooms 11, 9 and 7 to your right. Stop when you reach the intersection of halls."

    d = [d30, d31, d32, d33, d34, d35, d36, d37, d38, d_g2]
    d_direction_room_to_node = ["After exiting the room, turn right & walk forward to the intersection of hallways.",
    "After exiting the room, turn left & walk forward to the intersection of hallways.",
    "After exiting the room, turn right & walk forward to the intersection of hallways.",
    "After exiting the room, turn right & walk forward to the intersection of hallways.",
    "After exiting the room, turn right2 & walk forward to the intersection of hallways.",
    "After exiting the room, turn left & walk forward to the intersection of hallways.",
    "Exit the room & walk forward to the intersection of hallways.",
    "Exit the room, turn left and walk forwards. Then turn left at the end of the hall and walk forwards to the intersection of hallways.",
    "Exit the room, turn left and walk forwards. Then turn left at the end of the hall and walk forwards to the intersection of hallways.",
    "Exit the doors and turn right. Continue walking forward until the end of the hall."
    ]

    d_direction_node_to_room = ["Face north, towards the science hallway. Walk forward and take the second door to your left into room 30",
    "Face north, towards the science hallway. Walk forward and take the first door to your right into room 31.",
    "Face north, towards the science hallway. Walk forward and take the first door to your left into room 32",
    "Face east, away from the commons. Walk forward and take the first door to your left into room 33",
    "Face south to the hallway facing away from room 32. Walk forward and take the first left into room 34.",
    "Face south to the hallway facing away from room 32. Walk forward and take the second left into room 35.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36. Then turn right and walk forward. Take the first left into room 37.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36. Then turn right and walk forward. Take the second left into room 38, all the way down the hall.",
    "Face west, or towards the commons. Walk forward and take the first door to your left into the gym."]
    d_c = "Face North and walk until you get to the intersection of hallways (Do not pass through the double doors."

    d_a = "Face west and walk straight until you reach the intersection of halls"

    d_b = "Face West and walk straight until you reach the intersection of halls then turn right to face N and walk straight until you reach an intersection of halls. (Do not pass through the double doors)"
    master = [a_c, a_s, a_g1, a1, a2, a3, a4, a5, a6, b7, b8, b9, b10, b11, b12, b16_1, b_m, c16_2, c24, c26, c27, c28, c29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d_g2]
    hallway_math = [3, 4, 5, 6, 7, 8, 9, 11, 12]
    hallway_science = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

    return (a, b, c, d,
            a_direction_room_to_node, a_direction_node_to_room,
            b_direction_room_to_node, b_direction_node_to_room,
            c_direction_room_to_node, c_direction_node_to_room,
            d_direction_room_to_node, d_direction_node_to_room,
            a_b, a_c, a_d, b_a, b_c, b_d, c_a, c_b, c_d, d_a, d_b, d_c,
            master, hallway_math, hallway_science)


def get_start_room(master):
    start = str(input("Enter your current room number (For rooms without the number, enter the name in all caps): "))
    while start not in master:
        start = str(input("Invalid, try again (try LIBRARY,GYM, or, STAGE)"))
    return start


def get_end_room(master):
    end = str(input("Enter the room you want to go to: "))
    while end not in master:
        end = str(input("Invalid, try again (try LIBRARY,GYM, or, STAGE)"))
    return end


def handle_same_hallway_case(start, end, hallway_math):
    #THIS IS THE CODE FOR THE MISCELLANEOUS CASES
    start1 = int(start)
    end1 = int(end)
    if start and end in hallway_math:
        if start1 > end1:
            if start1 % 2 == 0:
                print("Go to your left and look around the hallway.")
            else:
                print("Go to your right and look around the hallway.")
        else:
            if start1 % 2 == 0:
                print("Go to your right and look around the hallway.")
            else:
                print("Go to your left and look around the hallway.")
    #need to a add end condition


def handle_cross_hallway_case(start, end, hallway_science,
                               a, b, c, d,
                               a_direction_room_to_node, a_direction_node_to_room,
                               b_direction_room_to_node, b_direction_node_to_room,
                               c_direction_room_to_node, c_direction_node_to_room,
                               d_direction_room_to_node, d_direction_node_to_room,
                               a_b, a_c, a_d, b_a, b_c, b_d, c_a, c_b, c_d, d_a, d_b, d_c):
    if start and end in hallway_science:

        start_index = 0
        end_index = 0
        ''' def start_to_node(a,a_direction_room_to_node,b,b_direction_room_to_node,c,c_direction_room_to_node,d,d_direction_room_to_node):
        if start in a:
        for i in range(len(a)):
        if a[i]==start:
        print(a_direction_room_to_node[i])
        elif start in b:
        for i in range(len(b)):
        if b[i]==start:
        print(b_direction_room_to_node[i])
        elif start in c:
        for i in range(len(c)):
        if c[i]==start:
        print(c_direction_room_to_node[i])
        elif start in d:
        for i in range(len(d)):
        if d[i]==start:
        print(d_direction_room_to_node[i])
        else:
        print("Invalid, try again (try LIBRARY,GYM, or, STAGE)")
        def node_to_node(a_b,a_c,a_d, b_a, b_c, b_d, c_a, c_b, c_d, d_a, d_b, d_c) '''

        nodetoroom = ""

        if start in a:
            for i in range(len(a)):
                if a[i] == start:
                    print(a_direction_room_to_node[i])
                    start_index = 0
        elif start in b:
            for i in range(len(b)):
                if b[i] == start:
                    print(b_direction_room_to_node[i])
                    start_index = 1
        elif start in c:
            for i in range(len(c)):
                if c[i] == start:
                    print(c_direction_room_to_node[i])
                    start_index = 2
        elif start in d:
            for i in range(len(d)):
                if d[i] == start:
                    print(d_direction_room_to_node[i])
                    start_index = 3

        #going to final room
        if end in a:
            for i in range(len(a)):
                if a[i] == end:
                    nodetoroom = a_direction_node_to_room[i]
                    end_index = 0
        elif end in b:
            for i in range(len(b)):
                if b[i] == end:
                    nodetoroom = b_direction_node_to_room[i]
                    end_index = 1
        elif end in c:
            for i in range(len(c)):
                if c[i] == end:
                    nodetoroom = c_direction_node_to_room[i]
                    end_index = 2
        elif end in d:
            for i in range(len(d)):
                if d[i] == end:
                    nodetoroom = d_direction_node_to_room[i]
                    end_index = 3

        z = "then,"
        node_node = [[z, a_b, a_c, a_d], [b_a, z, b_c, b_d], [c_a, c_b, z, c_d], [d_a, d_b, d_c, z]]

        print(node_node[start_index][end_index])
        print(nodetoroom)


def main():
    (a, b, c, d,
     a_direction_room_to_node, a_direction_node_to_room,
     b_direction_room_to_node, b_direction_node_to_room,
     c_direction_room_to_node, c_direction_node_to_room,
     d_direction_room_to_node, d_direction_node_to_room,
     a_b, a_c, a_d, b_a, b_c, b_d, c_a, c_b, c_d, d_a, d_b, d_c,
     master, hallway_math, hallway_science) = load_rooms()

    start = get_start_room(master)
    end = get_end_room(master)

    if start and end not in ["CAFETERIA", "STAGE", "LIBRARY", "GYM"]:
        handle_same_hallway_case(start, end, hallway_math)
        handle_cross_hallway_case(start, end, hallway_science,
                                   a, b, c, d,
                                   a_direction_room_to_node, a_direction_node_to_room,
                                   b_direction_room_to_node, b_direction_node_to_room,
                                   c_direction_room_to_node, c_direction_node_to_room,
                                   d_direction_room_to_node, d_direction_node_to_room,
                                   a_b, a_c, a_d, b_a, b_c, b_d, c_a, c_b, c_d, d_a, d_b, d_c)


main()

import streamlit as st
from campus_nav_functions import build_data, handle_same_hallway_case, handle_cross_hallway_case

data = build_data()
start = st.text_input("Current room")
end = st.text_input("Destination room")

if st.button("Get directions") and start in data["master"] and end in data["master"]:
    if start and end not in ["CAFETERIA", "STAGE", "LIBRARY", "GYM"]:
        handle_same_hallway_case(start, end, data["hallway_math"])
        handle_cross_hallway_case(start, end, data["hallway_science"], data)
