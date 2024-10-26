#count total lights on

#set light state
lights = [[[0, 0, 1], [0]], [[1, 0, 0], [1]], [[1, 1, 0], [0]], [[0, 0, 1], [1]]]

#set empty list to count off red LED lights
led_count = 0

#check for LED in light type (g,y,r or white) in direction of the light state
for direction in lights :
    for light_types in direction :
        for LED in light_types : 
            if LED == 1 : #check the state of each individual LED
                led_count+=1 #update count
                print("+1 ON LED")

print(f"Amount of LEDs that are currently on : {led_count}")