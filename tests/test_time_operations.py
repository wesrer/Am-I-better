from src.operations import TimeOperations
import datetime

time_operations = TimeOperations.TimeOperations()
jan_31_2019 = datetime.datetime(2019, 1, 31)


class TestTimeOperations:
    def aliases_helper(self,
                       date_value,
                       alias_list):
        condition = True
        for x in alias_list:
            condition = condition and date_value.date() == \
                        time_operations.decode_relative_time_strings(start_time=jan_31_2019,
                                                                     relative_time_string=x).date()
            print(x, condition)

        return condition

    def test_one_month_from_jan(self):
        returnval = time_operations.decode_relative_time_strings(start_time=jan_31_2019,
                                                                 relative_time_string="next_month")

        assert returnval.date() == datetime.datetime(2019, 2, 28).date()

    def test_reference_strings(self):
        assert datetime.datetime(2019, 2, 7).date() == \
               time_operations.decode_relative_time_strings(start_time=jan_31_2019,
                                                            relative_time_string="next_week").date()

        assert datetime.datetime(2019, 2, 1).date() == \
               time_operations.decode_relative_time_strings(start_time=jan_31_2019,
                                                            relative_time_string="tomorrow").date()

        assert datetime.datetime(2019, 1, 30).date() == \
               time_operations.decode_relative_time_strings(start_time=jan_31_2019,
                                                            relative_time_string="yesterday").date()

    def test_tomorrow_aliases(self):
        assert self.aliases_helper(date_value=datetime.datetime(2019, 2, 1),
                                   alias_list=["the_day_after", "day_after", "day_after_today", "the_next_day",
                                               "next_day"])

    def test_yesterday_aliases(self):
        assert self.aliases_helper(date_value=datetime.datetime(2019, 1, 30),
                                   alias_list=["the_day_before", "day_before", "day_before_today", "the_previous_day",
                                               "previous_day"])

