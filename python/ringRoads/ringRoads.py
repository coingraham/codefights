"""
Your city has two ringroads, which are concentric circles with different radiuses. There are also some roads that
connect these ringroads. These roads are segments of the radius at some angle of the outer ringroad. For example,
there are three roads in the image below: at the angle 0, at the angle 90, and at the angle 290.



You need to go from a point on the inner ringroad to a point on the outer ringroad, and you can only travel on the
ringroads and the connecting roads. Of course you want to find the shortest path!

You have the radius of the inner ringroad innerRing, the radius of the outer ringroad outerRing, an array roads that
defines the angles of the connecting roads (the ith road lies at the angle roads[i]), and an array travels, where each
element is a pair [start, finish] that defines the travel between the point in the inner ringroad with the angle start
and the point in the outer ringroad with the angle finish. Return an array in which the ith element is the length of
the shortest path of travels[i].

Example

For innerRing = 10, outerRing = 20, roads = [180] and travels = [[0, 0], [60, 300]], the output should be
ringRoads(innerRing, outerRing, roads, travels) = [104.24778, 72.83185].

You can find the path for each travel in the image below.



Input/Output

[time limit] 4000ms (py)
[input] integer innerRing

The radius of the inner ringroad.

Guaranteed constraints:
1 <= innerRing <= 999,
innerRing < outerRing.

[input] integer outerRing

The radius of the outer ringroad.

Guaranteed constraints:
2 <= outerRing <= 1000,
innerRing < outerRing.

[input] array.float roads

The angles of the roads that connect the inner and outer ringroads.

Guaranteed constraints:
0 <= roads[i] < 360,
1 <= roads.length <= 105.

[input] array.array.float travels

Each element is a pair [start, finish] that defines the travel between the point in the inner ringroad with the angle start and the point in the outer ringroad with the angle finish.

0 <= travels[i][0], travels[i][1] < 360,
1 <= travels.length <= 104.

[output] array.float

Return an array in which the ith element is the length of the shortest path of travels[i]. Your answer will be considered correct if its absolute error doesn't exceed 10-5.
"""
import math


def ring_roads(inner_ring, outer_ring, roads, travels):

    road_dist = float(outer_ring) - float(inner_ring)
    results = []

    # We're going to go through each travel and find the shortest distance
    for travel in travels:

        # Now that we have the start and end points, we need to loop through the roads and find the shortest outer dist.
        start_point = float(travel[0])
        end_point = float(travel[1])
        chosen_road = None
        shortest_outer_degrees = 180
        shortest_inner_degrees = 180

        # Getting the road closest to the outer point since that will effect total distance most (Edit: this is an
        # incorrect assumption.  There's actual edge case were the circles are very close
        for road in roads:
            test_distance = find_shortest_degrees(road, end_point)
            if test_distance <= shortest_outer_degrees:
                shortest_outer_degrees = test_distance
                chosen_road = float(road)

        # Now that we have the chosen road, get the inner distance.
        shortest_inner_degrees = find_shortest_degrees(start_point, chosen_road)

        # Now calculate the results and add it to the results array.
        outer_arc_length = (float(shortest_outer_degrees)/360) * 2 * math.pi * float(outer_ring)
        inner_arc_length = (float(shortest_inner_degrees)/360) * 2 * math.pi * float(inner_ring)

        results.append(outer_arc_length + inner_arc_length + road_dist)

    return results


def ring_roads_slow(inner_ring, outer_ring, roads, travels):

    road_dist = float(outer_ring) - float(inner_ring)
    results = []

    # We're going to go through each travel and find the shortest distance
    for travel in travels:
        # print "\ntravel: {}".format(travel)
        # Now that we have the start and end points, we need to loop through the roads and find the shortest outer dist.
        start_point = float(travel[0])
        end_point = float(travel[1])
        shortest_distance = 2 * math.pi * float(outer_ring) + road_dist

        if len(roads) > 4:
            new_roads = whittle_down_roads(roads, start_point, end_point)
            print "reduced_roads: {}".format(new_roads)
        else:
            new_roads = roads

        # Brute force check the distance for each road
        right_road = None
        for road in new_roads:
            test_outer_distance = float(find_shortest_degrees(float(road), end_point, False))/360 * 2 * math.pi * float(outer_ring)
            test_inner_distance = float(find_shortest_degrees(float(road), start_point, False))/360 * 2 * math.pi * float(inner_ring)
            if test_inner_distance + test_outer_distance + road_dist < shortest_distance:
                shortest_distance = test_inner_distance + test_outer_distance + road_dist
                right_road = road

        print "right road: {}".format(right_road)

        if right_road not in new_roads:
            print "ERROR HERE!!!"

        results.append(shortest_distance)
        print(str.format('{0:.6f}', shortest_distance))

    return results


def ring_roads_fast(inner_ring, outer_ring, roads, travels):

    road_dist = float(outer_ring) - float(inner_ring)
    results = []
    roads = sorted(roads)

    # We're going to go through each travel and find the shortest distance
    for travel in travels:
        # print "\ntravel: {}".format(travel)
        # Now that we have the start and end points, we need to loop through the roads and find the shortest outer dist.
        start_point = float(travel[0])
        end_point = float(travel[1])
        shortest_distance = 2 * math.pi * float(outer_ring) + road_dist

        if len(roads) > 40:
            temp_roads = list(roads)
            new_roads = whittle_down_roads_updated(temp_roads, start_point, end_point)
            # print "reduced_roads: {}".format(new_roads)
        else:
            new_roads = roads

        # Brute force check the distance for each road
        right_road = None
        for road in new_roads:
            test_outer_distance = float(find_shortest_degrees(road, end_point, False))/360 * 2 * math.pi * float(outer_ring)
            test_inner_distance = float(find_shortest_degrees(road, start_point, False))/360 * 2 * math.pi * float(inner_ring)
            if test_inner_distance + test_outer_distance + road_dist < shortest_distance:
                shortest_distance = test_inner_distance + test_outer_distance + road_dist
                right_road = road

        # print "right road: {}".format(right_road)
        #
        # if right_road not in new_roads:
        #     print "ERROR HERE!!!"

        results.append(shortest_distance)
        # print(str.format('{0:.6f}', shortest_distance))

    return results


def whittle_down_roads_updated(local_roads, inner_point, outer_point):
    try:

        filtered_roads = [None, None, None, None]

        if inner_point not in local_roads:
            local_roads.append(inner_point)
        else:
            filtered_roads[0] = inner_point
            filtered_roads[1] = inner_point

        if outer_point not in local_roads:
            local_roads.append(outer_point)
        else:
            filtered_roads[2] = outer_point
            filtered_roads[3] = outer_point

        local_roads = sorted(local_roads)

        inner_location = local_roads.index(inner_point)
        outer_location = local_roads.index(outer_point)

        if inner_location - outer_location == 0:
            if filtered_roads[0] is None:
                if inner_location == len(local_roads):
                    return [local_roads[(len(local_roads) - 1)], local_roads[0]]
                else:
                    return [local_roads[inner_location - 1], local_roads[inner_location + 1]]
            else:
                return [inner_point]

        if outer_location - inner_location == 1:
            if filtered_roads[0] is None and filtered_roads[2] is None:
                if outer_location == len(local_roads):
                    return [local_roads[inner_location - 1], local_roads[0]]
                else:
                    return [local_roads[inner_location - 1], local_roads[outer_location + 1]]

            elif filtered_roads[0] is not None and filtered_roads[2] is not None:
                return [inner_point, outer_point]

            elif filtered_roads[0] is None:
                if outer_location == len(local_roads):
                    return [inner_point, local_roads[0]]
                else:
                    return [inner_point, local_roads[outer_location + 1]]

            else:
                return [local_roads[inner_location - 1], outer_point]

        if inner_location - outer_location == 1:
            if filtered_roads[0] is None and filtered_roads[2] is None:
                if inner_location == len(local_roads):
                    return [local_roads[outer_location - 1], local_roads[0]]
                else:
                    return [local_roads[outer_location - 1], local_roads[inner_location + 1]]

            elif filtered_roads[0] is not None and filtered_roads[2] is not None:
                return [inner_point, outer_point]

            elif filtered_roads[0] is None:
                return [inner_point, local_roads[outer_location - 1]]

            else:
                if inner_location == len(local_roads):
                    return [outer_point, local_roads[0]]
                else:
                    return [outer_point, local_roads[inner_location + 1]]

        if filtered_roads[0] is None:
            filtered_roads[0] = local_roads[inner_location - 1]
            if inner_location == len(local_roads):
                filtered_roads[1] = local_roads[0]
            else:
                filtered_roads[1] = local_roads[inner_location + 1]

        if filtered_roads[2] is None:
            outer_location = local_roads.index(outer_point)
            filtered_roads[2] = local_roads[outer_location - 1]
            if outer_point == len(local_roads):
                filtered_roads[3] = local_roads[0]
            else:
                filtered_roads[3] = local_roads[outer_location + 1]

        return filtered_roads
    except:
        return local_roads


def find_shortest_degrees(point1, point2, direction):
    # Given two points on a circle find the shortest path in degrees.
    # Will be used for both outer and inner computations.

    if 0 <= float(point1) - float(point2) <= 180:
        if direction:
            return [float(point1) - float(point2), "right"]
        else:
            return float(point1) - float(point2)

    if 0 < float(point2) - float(point1) <= 180:
        if direction:
            return [float(point2) - float(point1), "left"]
        else:
            return float(point2) - float(point1)

    if float(point1) - float(point2) > 180:
        if direction:
            return [360 - float(point1) + float(point2), "left"]
        else:
            return 360 - float(point1) + float(point2)

    if float(point2) - float(point1) > 180:
        if direction:
            return [360 - float(point2) + float(point1), "right"]
        else:
            return 360 - float(point2) + float(point1)


def whittle_down_roads(roads, inner_point, outer_point):
    inner_right_shortest = None
    inner_right_shortest_road = None
    inner_left_shortest = None
    inner_left_shortest_road = None
    outer_right_shortest = None
    outer_right_shortest_road = None
    outer_left_shortest = None
    outer_left_shortest_road = None
    new_roads = []

    for road in roads:
        inner_current, inner_direction = find_shortest_degrees(inner_point, float(road), True)
        if inner_direction == "left":
            if inner_left_shortest is None:
                inner_left_shortest = inner_current
                inner_left_shortest_road = road

            if inner_current < inner_left_shortest:
                inner_left_shortest = inner_current
                inner_left_shortest_road = road
        else:
            if inner_right_shortest is None:
                inner_right_shortest = inner_current
                inner_right_shortest_road = road

            if inner_current < inner_right_shortest:
                inner_right_shortest = inner_current
                inner_right_shortest_road = road

        outer_current, outer_direction = find_shortest_degrees(outer_point, float(road), True)
        if outer_direction == "left":
            if outer_left_shortest is None:
                outer_left_shortest = outer_current
                outer_left_shortest_road = road

            if outer_current < outer_left_shortest:
                outer_left_shortest = outer_current
                outer_left_shortest_road = road
        else:
            if outer_right_shortest is None:
                outer_right_shortest = outer_current
                outer_right_shortest_road = road

            if outer_current < outer_right_shortest:
                outer_right_shortest = outer_current
                outer_right_shortest_road = road

    if inner_right_shortest_road is not None:
        new_roads.append(float(inner_right_shortest_road))

    if inner_left_shortest_road is not None:
        new_roads.append(float(inner_left_shortest_road))

    if outer_right_shortest_road is not None:
        new_roads.append(float(outer_right_shortest_road))

    if outer_left_shortest_road is not None:
        new_roads.append(float(outer_left_shortest_road))

    return new_roads


if __name__ == '__main__':
    print "\nRing Roads Fast"
    print ring_roads_fast(999, 1000,
                          [209.253983, 38.969013, 178.467116, 137.531902, 181.993079, 129.885195, 178.516437,
                           283.597115, 147.611906, 70.972958, 30.68365, 287.241272, 327.252872, 320.581891, 207.981467,
                           230.251322, 57.999991, 175.158868, 218.254257, 276.207182, 74.387357, 42.690989, 311.780595,
                           219.341251, 82.990768, 121.382704, 341.861433, 223.908523, 89.413574, 91.510786, 63.453949,
                           281.596767, 7.812061, 89.234636, 155.427805, 146.770936, 334.669652, 359.928379, 84.990235,
                           205.403351, 353.127536, 288.703872, 292.191005, 48.789789, 143.825368, 82.991824, 7.082733,
                           220.705587, 135.904538, 229.574117, 102.247097, 116.28474, 232.236324, 28.565627, 309.324372,
                           247.603646, 309.936331, 38.6685, 245.371316, 15.799253, 278.360391, 123.745333, 1.93573,
                           146.333184, 148.875957, 43.006822, 173.749581, 96.635514, 272.695444, 56.108854, 349.687975,
                           48.880578, 315.660873, 187.702005, 307.663622, 9.174811, 281.815963, 356.598521, 157.795476,
                           274.792717, 98.406199, 0.904473, 188.436128, 306.709474, 249.287469, 273.368373, 77.922331,
                           289.508906, 195.037041, 96.526764, 288.353308, 265.453368, 306.190427, 27.456484, 324.509789,
                           77.683106, 224.602919, 145.821893, 223.176635, 279.00666],
                          [
                           # [6.285942, 3.727166],
                           # [155.372217, 247.97651],
                           # [178.647243, 205.404351],
                           # [351.132158, 224.999026],
                           [292.092687, 266.296254],
                           [161.908434, 268.033799],
                           # [231.819534, 17.644594],
                           # [104.155045, 149.642857],
                           # [241.788408, 83.596315],
                           # [359.020681, 322.335046],
                           # [288.977633, 124.183544],
                           # [344.593331, 139.31701],
                           # [317.512, 31.423823],
                           # [187.705853, 58.75674],
                           # [246.697332, 315.419944],
                           # [72.870759, 104.922135],
                           # [275.11225, 280.752786],
                           # [168.83957, 183.110794],
                           # [35.717176, 173.372701],
                           # [31.701571, 325.986656],
                           # [40.94527, 285.945695],
                           # [230.76503, 329.818465],
                           # [289.776864, 258.59928],
                           # [79.846921, 147.212055],
                           # [161.077189, 166.101357],
                           # [332.00278, 327.203154],
                           # [350.938459, 131.327992],
                           # [61.475, 61.313957],
                           # [252.84716, 352.92383],
                           # [122.650773, 85.909734],
                           # [138.048986, 72.67912],
                           # [45.218962, 149.15269],
                           # [205.471521, 343.267699],
                           # [64.310129, 77.40439],
                           # [319.25832, 122.218576],
                           # [258.362391, 259.566119],
                           # [16.979471, 342.86646],
                           # [359.777809, 159.500379],
                           # [186.74302, 271.371537],
                           # [69.659658, 109.555246],
                           # [177.269461, 299.677035],
                           # [288.674902, 258.33691],
                           # [273.809695, 208.208877],
                           # [26.405739, 150.257456],
                           # [293.135747, 4.682841],
                           # [79.59101, 325.087497],
                           # [147.479707, 242.302459],
                           # [111.21753, 287.811797],
                           # [135.467626, 273.322527],
                           # [315.009174, 12.647315],
                           # [275.717329, 275.339414],
                           # [125.280698, 46.022406],
                           # [52.263963, 348.006966],
                           # [210.308497, 274.823734],
                           # [289.02181, 132.548439],
                           # [272.762858, 207.944173],
                           # [115.423591, 334.010966],
                           # [67.177526, 49.622331],
                           # [290.407534, 357.947413],
                           # [329.725964, 199.996915],
                           # [266.128735, 95.437945],
                           # [196.882854, 353.620267],
                           # [41.729527, 85.903083],
                           # [54.692961, 198.83104],
                           # [27.375445, 19.956952],
                           # [187.091265, 237.674191],
                           # [192.463997, 358.327345],
                           # [212.508522, 98.142781],
                           # [69.894872, 290.658796],
                           # [149.37156, 223.726385],
                           # [357.595826, 142.732929],
                           # [38.688744, 171.509909],
                           # [259.575739, 191.049837],
                           # [331.085757, 19.827096],
                           # [61.892487, 54.613682],
                           # [274.661596, 100.739118],
                           # [30.787086, 191.247701],
                           # [151.792288, 225.06587],
                           # [200.299052, 120.993247],
                           # [197.907847, 239.413427],
                           # [186.856994, 320.768989],
                           # [56.16837, 338.498269],
                           # [238.543891, 258.66992],
                           # [30.795113, 344.615437],
                           # [275.62612, 262.279038],
                           # [355.876757, 117.049228],
                           # [49.555693, 222.427855],
                           # [104.870469, 195.61994],
                           # [28.879377, 329.341936],
                           # [241.814314, 163.008997],
                           # [44.655786, 76.662788],
                           # [145.039386, 353.804834],
                           # [19.191247, 75.060526],
                           # [118.104976, 206.450801],
                           # [77.153148, 118.936344],
                           # [70.022954, 316.408303],
                           # [126.897425, 52.844399],
                           # [355.33009, 156.273658],
                           # [58.142163, 275.123812],
                           # [122.584566, 156.204725]
                           ])


    print "\nRing Roads Slow"
    print ring_roads_slow(999, 1000,
                          [209.253983, 38.969013, 178.467116, 137.531902, 181.993079, 129.885195, 178.516437,
                           283.597115, 147.611906, 70.972958, 30.68365, 287.241272, 327.252872, 320.581891, 207.981467,
                           230.251322, 57.999991, 175.158868, 218.254257, 276.207182, 74.387357, 42.690989, 311.780595,
                           219.341251, 82.990768, 121.382704, 341.861433, 223.908523, 89.413574, 91.510786, 63.453949,
                           281.596767, 7.812061, 89.234636, 155.427805, 146.770936, 334.669652, 359.928379, 84.990235,
                           205.403351, 353.127536, 288.703872, 292.191005, 48.789789, 143.825368, 82.991824, 7.082733,
                           220.705587, 135.904538, 229.574117, 102.247097, 116.28474, 232.236324, 28.565627, 309.324372,
                           247.603646, 309.936331, 38.6685, 245.371316, 15.799253, 278.360391, 123.745333, 1.93573,
                           146.333184, 148.875957, 43.006822, 173.749581, 96.635514, 272.695444, 56.108854, 349.687975,
                           48.880578, 315.660873, 187.702005, 307.663622, 9.174811, 281.815963, 356.598521, 157.795476,
                           274.792717, 98.406199, 0.904473, 188.436128, 306.709474, 249.287469, 273.368373, 77.922331,
                           289.508906, 195.037041, 96.526764, 288.353308, 265.453368, 306.190427, 27.456484, 324.509789,
                           77.683106, 224.602919, 145.821893, 223.176635, 279.00666],
                          [
                           [6.285942, 3.727166],
                           [155.372217, 247.97651],
                           [178.647243, 205.404351],
                           [351.132158, 224.999026],
                           [292.092687, 266.296254],
                           [161.908434, 268.033799],
                           # [231.819534, 17.644594],
                           # [104.155045, 149.642857],
                           # [241.788408, 83.596315],
                           # [359.020681, 322.335046],
                           # [288.977633, 124.183544],
                           # [344.593331, 139.31701],
                           # [317.512, 31.423823],
                           # [187.705853, 58.75674],
                           # [246.697332, 315.419944],
                           # [72.870759, 104.922135],
                           # [275.11225, 280.752786],
                           # [168.83957, 183.110794],
                           # [35.717176, 173.372701],
                           # [31.701571, 325.986656],
                           # [40.94527, 285.945695],
                           # [230.76503, 329.818465],
                           # [289.776864, 258.59928],
                           # [79.846921, 147.212055],
                           # [161.077189, 166.101357],
                           # [332.00278, 327.203154],
                           # [350.938459, 131.327992],
                           # [61.475, 61.313957],
                           # [252.84716, 352.92383],
                           # [122.650773, 85.909734],
                           # [138.048986, 72.67912],
                           # [45.218962, 149.15269],
                           # [205.471521, 343.267699],
                           # [64.310129, 77.40439],
                           # [319.25832, 122.218576],
                           # [258.362391, 259.566119],
                           # [16.979471, 342.86646],
                           # [359.777809, 159.500379],
                           # [186.74302, 271.371537],
                           # [69.659658, 109.555246],
                           # [177.269461, 299.677035],
                           # [288.674902, 258.33691],
                           # [273.809695, 208.208877],
                           # [26.405739, 150.257456],
                           # [293.135747, 4.682841],
                           # [79.59101, 325.087497],
                           # [147.479707, 242.302459],
                           # [111.21753, 287.811797],
                           # [135.467626, 273.322527],
                           # [315.009174, 12.647315],
                           # [275.717329, 275.339414],
                           # [125.280698, 46.022406],
                           # [52.263963, 348.006966],
                           # [210.308497, 274.823734],
                           # [289.02181, 132.548439],
                           # [272.762858, 207.944173],
                           # [115.423591, 334.010966],
                           # [67.177526, 49.622331],
                           # [290.407534, 357.947413],
                           # [329.725964, 199.996915],
                           # [266.128735, 95.437945],
                           # [196.882854, 353.620267],
                           # [41.729527, 85.903083],
                           # [54.692961, 198.83104],
                           # [27.375445, 19.956952],
                           # [187.091265, 237.674191],
                           # [192.463997, 358.327345],
                           # [212.508522, 98.142781],
                           # [69.894872, 290.658796],
                           # [149.37156, 223.726385],
                           # [357.595826, 142.732929],
                           # [38.688744, 171.509909],
                           # [259.575739, 191.049837],
                           # [331.085757, 19.827096],
                           # [61.892487, 54.613682],
                           # [274.661596, 100.739118],
                           # [30.787086, 191.247701],
                           # [151.792288, 225.06587],
                           # [200.299052, 120.993247],
                           # [197.907847, 239.413427],
                           # [186.856994, 320.768989],
                           # [56.16837, 338.498269],
                           # [238.543891, 258.66992],
                           # [30.795113, 344.615437],
                           # [275.62612, 262.279038],
                           # [355.876757, 117.049228],
                           # [49.555693, 222.427855],
                           # [104.870469, 195.61994],
                           # [28.879377, 329.341936],
                           # [241.814314, 163.008997],
                           # [44.655786, 76.662788],
                           # [145.039386, 353.804834],
                           # [19.191247, 75.060526],
                           # [118.104976, 206.450801],
                           # [77.153148, 118.936344],
                           # [70.022954, 316.408303],
                           # [126.897425, 52.844399],
                           # [355.33009, 156.273658],
                           # [58.142163, 275.123812],
                           # [122.584566, 156.204725]
                           ])