
import signal
import time

import g
import config
import logger

from MasterData import MasterData
from Player import Player
from Area import AREA_LOBBY, AREA_TOWN, AREA_DUNGEON, AREA_ARENA, Area

from play_handle_message_no_1 import handle_message_no_1

PLAYER_CREATE = -1
PLAYER_DELETE = -2

class PlayLoop:
    def __init__(self, phase, server_seq):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.phase = phase
        self.server_seq = server_seq

        self.is_running = True
        self.get_max = 1000
        self.players = {}
        self.area_id = 0
        self.areas = {}
        self.areas[self.area_id] = Area(AREA_LOBBY)
        self.area_id += 1

        self.curr_time = 0
        self.delta_time = 0
        self.last_time = 0

    def run(self, incoming, internal, outgoing):
        g.PHASE = self.phase
        g.SERVER_SEQ = self.server_seq

        config.load()
        logger.init('play')

        g.MST = MasterData()
        g.MST.load()

        while self.is_running:
            time.sleep(0.001)

            self.curr_time = time.time()
            self.delta_time = (self.curr_time - self.last_time) * 1000

            i = 0
            while i < self.get_max and not incoming.empty():
                i += 1

                print('incoming_get')
                (conn_id, req_msg_type, req_msg_body) = incoming.get()
                print(conn_id)
                print(req_msg_type)
                print(req_msg_body)
                if req_msg_type == PLAYER_CREATE:
                    print('add_player')
                    area_id = 0
                    self.players[conn_id] = Player(area_id)
                    self.areas[area_id].player_conn_ids.append(conn_id)

                elif req_msg_type == PLAYER_DELETE:
                    print('remove_player')
                    area_id = self.players[conn_id].area_id
                    self.areas[area_id].player_conn_ids.remove(conn_id)
                    del self.players[conn_id]

                elif req_msg_type in g.PLAY_HANDLERS:
                    (conn_id, ack_msg_type, ack_msg_body, rcpt) = \
                        g.PLAY_HANDLERS[req_msg_type](conn_id, req_msg_type, req_msg_body)

                    if rcpt == g.TO_ME:
                        outgoing.put([conn_id, ack_msg_type, ack_msg_body])

                    if rcpt == g.TO_ALL:
                        area_id = self.players[conn_id].area_id
                        for player_conn_id in self.areas[area_id].player_conn_ids:
                            outgoing.put([player_conn_id, ack_msg_type, ack_msg_body])

                    elif rcpt == g.TO_DATA:
                        internal.put([player_conn_id, ack_msg_type, ack_msg_body])

            for player in self.players.values():
                player.run(self.delta_time)

            for area in self.areas.values():
                area.run(self.delta_time)

            self.last_time = self.curr_time

    def stop(self, signal_num, frame_obj):
        self.is_running = False

