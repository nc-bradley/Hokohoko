# Generated by generate_tests (from the Hokohoko project).
import unittest as ut


class TestPeriod(ut.TestCase):
    def test_get_last_close_at_minute_raises_an_error_if_the_data_source_does_not_inherit_hokohokoentitiesData(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_raises_an_error_if_minute_is_negative(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_raises_an_error_if_past_minutes_is_negative(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_raises_an_error_if_minute_is_past_end_of_source(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_returns_a_List_of_Bars(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_the_order_of_the_Bars_in_the_list_dont_change_between_calls(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_last_close_at_minute_if_minute_is_zero_all_fields_should_be_the_datas_open_value(self):
        """Auto-generated from _period.py:74"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_raises_an_error_if_the_data_source_does_not_inherit_hokohokoentitiesData(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_raises_an_error_if_minute_is_not_N(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_raises_an_error_if_minute_is_past_end_of_source(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_returns_a_list_of_Bars(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_the_order_of_the_Bars_in_the_list_dont_change_between_calls(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minute_if_minute_is_1_should_match_the_data(self):
        """Auto-generated from _period.py:114"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_raises_an_error_if_the_data_source_does_not_inherit_hokohokoentitiesData(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_raises_an_error_if_start_is_negative(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_raises_an_error_if_start_is_past_end_of_source(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_raises_an_error_if_end_is_less_than_start(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_raises_an_error_if_end_is_past_end_of_source(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_returns_a_list_of_Bars(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_the_order_of_the_Bars_in_the_list_dont_change_between_calls(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_high_values_are_highest_from_the_data(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_low_values_are_lowest_from_the_data(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_volumes_are_sum_of_data_volumes(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_open_matches_first_value_open(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_close_matches_last_value_close(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_get_past_minutes_end_timestamp_is_greater_than_start_timestamp(self):
        """Auto-generated from _period.py:143"""
        self.fail('TODO: Implement me!')

    def test_init_sets_internal_locks_correctly(self):
        """Auto-generated from _period.py:62"""
        self.fail('TODO: Implement me!')


if __name__ == '__main__':
    ut.main()