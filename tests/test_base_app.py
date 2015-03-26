# -*- coding: utf-8 -*-#

from game_of_life import base_app


class TestBaseClass:
    def test_calculate_cell_survive(self):
        App = base_app.BaseApp()

        live = App.LIVE_CELL_SYMBOL
        dead = App.DEAD_CELL_SYMBOL

        assert App.calculate_cell_state_for_next_round(live) == dead
        assert App.calculate_cell_state_for_next_round(live, live) == dead
        assert App.calculate_cell_state_for_next_round(live, live, live) == live
        assert App.calculate_cell_state_for_next_round(live, live, live, live) == live
        assert App.calculate_cell_state_for_next_round(live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(live, live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(live, live, live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(live, live, live, live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead) == dead
        assert App.calculate_cell_state_for_next_round(dead, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live, live) == live
        assert App.calculate_cell_state_for_next_round(dead, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live, live, live, live, live, live) == dead
        assert App.calculate_cell_state_for_next_round(dead, live, live, live, live, live, live, live, live) == dead