# check that N/S and W/E are not green at the same time

#set light state where there WON'T be accidents
no_accident = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[0, 0, 1], [0]], [[1, 0, 0], [1]]]
#set light state where there WILL be accidents
accident = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[1, 1, 0], [0]], [[0, 0, 1], [1]]]

def check_green_lights(light_setting) :
    if ((light_setting[0][0][0] or light_setting[2][0][0]) == 1) and ((light_setting[1][0][0] or light_setting[3][0][0]) == 1) :
        print("Oh no!! A North/South green light and a East/West green light is on at the same time. This could cause and accident!")
    else :
        print("No problemo, a North/South and East/West green light aren't on at the same time. Circulation should be safe.")

check_green_lights(accident)
check_green_lights(no_accident)