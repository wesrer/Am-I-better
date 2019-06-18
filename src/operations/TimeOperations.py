from datetime import datetime, timedelta
from dateutil import relativedelta
import json


class TimeOperations:

    def datetime_to_string(self,
                           date_time_value: datetime):
        date_time_value.strftime("%c")

    @staticmethod
    def __get_aliases(relative_time_string: str):
        aliases = {
            "tomorrow": ["the_day_after", "day_after", "day_after_today", "the_next_day", "next_day"],
            "yesterday": ["the_day_before", "day_before", "day_before_today", "the_previous_day", "previous_day"],
        }

        for x in ["week", "month", "year"]:
            aliases[f"next_{x}"] = [f"the_{x}_after",
                                    f"the_{x}_after_this",
                                    f"the_next_{x}",
                                    f"coming_{x}",
                                    f"upcoming_{x}"]

            aliases[f"last_{x}"] = [f"the_{x}_before",
                                    f"the_{x}_before_this",
                                    f"the_last_{x}",
                                    f"previous_{x}",
                                    f"the_previous_{x}"]

        return False if (relative_time_string not in list(aliases)) else aliases[relative_time_string]

    def decode_relative_time_strings(self,
                                     start_time: datetime,
                                     relative_time_string: str):

        # TODO: add more relative time strings
        reference_dict = {
            "today": start_time,
            "tomorrow": start_time + timedelta(days=1),
            "yesterday": start_time + timedelta(days=-1),
            "day_after_tomorrow": start_time + timedelta(days=2),
            "next_hour": start_time + timedelta(hours=1),
            "next_week": start_time + timedelta(days=7),
            "next_month": start_time + relativedelta.relativedelta(months=1),
            "next_year": start_time + relativedelta.relativedelta(year=1),
        }

        # adding aliases:
        for key, value in reference_dict.copy().items():
            aliases = self.__get_aliases(key)

            if aliases:
                for x in aliases:
                    reference_dict[x] = reference_dict[key]

        if relative_time_string not in reference_dict:
            raise ValueError("relative time string is not valid")
        else:
            return reference_dict[relative_time_string]

    @staticmethod
    def is_still_valid(last_completed_on: str,
                       refresh_rate: int) -> bool:
        last_completed_on = datetime.strptime(last_completed_on, "%c")

        refresh_after = 24 // refresh_rate # integer division

        return last_completed_on + timedelta(hours=refresh_after) >= datetime.now()
