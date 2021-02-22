import json
import xml.etree.ElementTree as ET


# Rubbish function LOL
def parse_seatmap1(file):
    tree = ET.parse(file)
    root = tree.getroot()

    result = []
    # Looping through body
    for seat_map in root[0]:
        seat_map_obj = {}

        # Looping through AirSeatMaps responses
        for response in seat_map[1]:
            res_obj = {'FlightInfo': response[0].attrib}
            # print(res_obj)
            cabins = []
            # Looping through SeatMap Cabins
            for cabin in response[1]:
                cabin_obj = cabin.attrib

                rows = []
                for row in cabin:
                    row_obj = row.attrib

                    for seat in row:
                        seat_obj = seat.attrib

                    rows.append(row_obj)

                cabin_obj['rows'] = rows
                cabins.append(cabin_obj)

            res_obj['Cabins'] = cabins

            seat_map_obj['Response'] = res_obj

        result.append(seat_map_obj)

    with open('%s_parsed.json' % file[:-4], 'w') as outfile:
        json.dump(result, outfile, indent=2)
    print('$ END: Finished SeatMap 1 successfully!')
