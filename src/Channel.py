
import time
import signal

from Area import AREA_LOBBY, AREA_TOWN, AREA_DUNGEON, AREA_ARENA, Area
from Player import Player

CHANNEL_ADD_PLAYER = 1
CHANNEL_REMOVE_PLAYER = 2

class Channel:
    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.mst = {}
        self.is_running = True
        self.process_incoming_max = 100
        self.area_idx = 0
        self.areas = {}
        self.areas[self.area_idx] = Area(AREA_LOBBY)

    def run(self, incoming, outgoing):
        print('channel_run')

        process_incoming = False
        while self.is_running:
            if process_incoming:
                #print('incoming')
                i = 0
                less_than_max = i < self.process_incoming_max
                not_empty = not incoming.empty()
                while less_than_max and not_empty:
                    i += 1

                    (msg_type, msg_body) = incoming.get()
                    if msg_type == CHANNEL_ADD_PLAYER:
                        self.areas[0][msg_body] = Player(msg_body)

                print('process_incoming')
                time.sleep(1)
                process_incoming = False

            else:
                for area in self.areas.values():
                    area.run()
                print('loop')
                time.sleep(1)
                process_incoming = True

    def stop(self, signal_num, frame_obj):
        print('stop_called')
        self.is_running = False

