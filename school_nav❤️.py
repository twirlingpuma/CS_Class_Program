import streamlit as st

a_c = "CAFETERIA"
a_s = "STAGE"
a_g1 = "GYM"
a_o = "OFFICE"
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

a = [a_c, a_s, a_g1, a1, a2, a3, a4, a5, a6, a_o]
a_direction_room_to_node = [
    "walk straight beyond the gym, to the intersection of halls",
    "take a left down to the intersection of halls",
    "take a right down to the intersection of halls",
    "take a left down to the intersection of halls",
    "take a right and go slightly forward to the intersection of halls",
    "take a right and go slightly forward to the intersection of halls",
    "take a left and go slightly forward to the intersection of halls",
    "take a right and go down to the intersection of halls",
    "take a left and go down to the intersection of halls",
    "Exit the office and walk straight to the intersection of halls"
]
a_direction_node_to_room = [
    "face south and go straight",
    "face south and go straight, then take a right at the door before the stage",
    "face south and go straight then take a left at the first doors you see",
    "face south and go straight then take a right at the first door after the boys restroom",
    "face east and go straight a small amount then take a left at the first door",
    "face north and go straight a small amount then take a left at the first door",
    "face north and go straight a small amount then take a right at the first door",
    "face north and go straight then take a left at the second door",
    "face north go straight then take a right at the second door",
    "Face south and go straight, the office is next to the cafeteria"
]
a_to_b = "Face north and go forward until the intersection of halls"
a_to_c = "Face east and go forward until the first intersection of halls, and then face north and go forward until the intersection of halls"
a_to_d = "Face east and go forward until the first intersection of halls"

b = [b7, b8, b9, b10, b11, b12, b16_1, b_m]
b_direction_room_to_node = [
    "Exit room 7 and take a left until you reach the intersection of halls",
    "Exit room 8 and take a right until you reach the intersection of halls.",
    "Exit room 9 and take a left until you reach the intersection of halls",
    "Exit room 10 and take a right until you reach the intersection of halls",
    "Exit room 11 and take a left until you reach the intersection of halls",
    "Exit room 12 and take a right until you reach the intersection of halls",
    "Exit room 16 and take a right until you reach the intersection of halls",
    "Exit the Library and take a left until you reach the intersection of halls"
]
b_direction_node_to_room = [
    "Turn towards the office/cafeteria (South) and room 7 is the 3rd classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 8 is the 3rd classroom on the left side",
    "Turn towards the office/cafeteria (South) and room 9 is the 2nd classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 10 is the 2nd classroom on the left side",
    "Turn towards the office/cafeteria (South) and room 11 is the 1st classroom on the right side",
    "Turn towards the office/cafeteria (South) and room 12 is the 1st classroom on the left side",
    "Turn towards the media center (East) and room 16 is the 1st room on the left side",
    "Turn towards the media center (East) and the media center is the 1st room on the right side"
]
b_to_a = "Turn towards the classroom (South) then go forward until you reach the intersection"
b_to_c = "Turn to face towards the library (East) then go straight towards the intersection of the halls"
b_to_d = "Turn towards the classroom (South) then go forward until you reach the intersections then turn towards the commons (East) and go straight"

c = [c16_2, c24, c26, c27, c28, c29]
c_direction_room_to_node = [
    "Exit room 16 and take a left until you enter the intersection of halls",
    "Exit room 24 and take a left until you enter the intersection of halls (It’s very close, and DO NOT enter the double doors)",
    "Exit room 26 and take a right until intersection of hallways before the double doors (DO NOT enter the double doors)",
    "Exit room 27 and take a left until you reach the intersection of hallways (DO NOT enter the double doors)",
    "Exit room 28 and take a right and walk until you reach the intersection of hallways (DO NOT enter the double doors)",
    "Exit room 29, take a left and walk until you reach the intersection of hallways (DO NOT enter the double doors)"
]
c_direction_node_to_room = [
    "Face West and walk straight, after passing the bathrooms room 16 should be on your left",
    "Face South and walk straight, and room 24 should be the first room on the right",
    "Face south and walk straight, and room 26 will be on the left",
    "Face south and walk straight, and room 27 will be the second room to the right",
    "Face south and walk straight, and room 28 will be the second room on the left",
    "Face south and walk straight, and room 29 will be the third room on the right"
]
c_to_a = "Walk towards the bathrooms until you reach the next intersection of halls, then take a left, and walk you should see rooms 11, 9 and 7 to your right. Stop when you reach the intersection of halls."
c_to_b = "walk towards the bathrooms until you reach the next intersection of halls"
c_to_d = "Walk towards room 24 until you reach the next intersection of halls, you should see ascending room numbers as you walk"

d = [d30, d31, d32, d33, d34, d35, d36, d37, d38, d_g2]
d_direction_room_to_node = [
    "After exiting the room, turn right & walk forward to the intersection of hallways.",
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
d_direction_node_to_room = [
    "Face north, towards the science hallway. Walk forward and take the second door to your left into room 30",
    "Face north, towards the science hallway. Walk forward and take the first door to your right into room 31.",
    "Face north, towards the science hallway. Walk forward and take the first door to your left into room 32",
    "Face east, away from the commons. Walk forward and take the first door to your left into room 33",
    "Face south to the hallway facing away from room 32. Walk forward and take the first left into room 34.",
    "Face south to the hallway facing away from room 32. Walk forward and take the second left into room 35.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36. Then turn right and walk forward. Take the first left into room 37.",
    "Face east or the direction away from the commons. Walk forward until you reach room 36. Then turn right and walk forward. Take the second left into room 38, all the way down the hall.",
    "Face west, or towards the commons. Walk forward and take the first door to your left into the gym."
]
d_to_a = "Face west and walk straight until you reach the intersection of halls"
d_to_b = "Face West and walk straight until you reach the intersection of halls then turn right to face N and walk straight until you reach an intersection of halls. (Do not pass through the double doors)"
d_to_c = "Face North and walk until you get to the intersection of hallways (Do not pass through the double doors."

master = [
    a_c, a_s, a_g1, a_o, a1, a2, a3, a4, a5, a6,
    b7, b8, b9, b10, b11, b12, b16_1, b_m,
    c16_2, c24, c26, c27, c28, c29,
    d30, d31, d32, d33, d34, d35, d36, d37, d38, d_g2
]

hallway_math = ["3", "4", "5", "6", "7", "8", "9", "11", "12"]
hallway_science = ["24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]

st.title("School Directions")

with st.form("nav"):
    start = st.selectbox("Enter your current room number (For rooms without the number, enter the name in all caps):", master)
    end = st.selectbox("Enter the room you want to go to:", master)
    submitted = st.form_submit_button("Get Directions")

if submitted:
    if start not in master:
        st.error("Invalid, try again (try LIBRARY, GYM, STAGE, or OFFICE)")
    elif end not in master:
        st.error("Invalid, try again (try LIBRARY, GYM, STAGE, or OFFICE)")
    else:
        special = ["CAFETERIA", "STAGE", "LIBRARY", "GYM", "OFFICE"]

        if start not in special and end not in special:
            start1 = int(start)
            end1 = int(end)

            if start in hallway_math and end in hallway_math:
                if start1 > end1:
                    if start1 % 2 == 0:
                        st.write("Go to your left and look around the hallway.")
                    else:
                        st.write("Go to your right and look around the hallway.")
                else:
                    if start1 % 2 == 0:
                        st.write("Go to your right and look around the hallway.")
                    else:
                        st.write("Go to your left and look around the hallway.")
                st.stop()

            if start in hallway_science and end in hallway_science:
                pass

        start_index = 0
        end_index = 0
        nodetoroom = ""

        if start in a:
            for i in range(len(a)):
                if a[i] == start:
                    st.write(a_direction_room_to_node[i])
            start_index = 0
        elif start in b:
            for i in range(len(b)):
                if b[i] == start:
                    st.write(b_direction_room_to_node[i])
            start_index = 1
        elif start in c:
            for i in range(len(c)):
                if c[i] == start:
                    st.write(c_direction_room_to_node[i])
            start_index = 2
        elif start in d:
            for i in range(len(d)):
                if d[i] == start:
                    st.write(d_direction_room_to_node[i])
            start_index = 3

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
        node_node = [
            [z, a_to_b, a_to_c, a_to_d],
            [b_to_a, z, b_to_c, b_to_d],
            [c_to_a, c_to_b, z, c_to_d],
            [d_to_a, d_to_b, d_to_c, z]
        ]

        st.write(node_node[start_index][end_index])
        st.write(nodetoroom)