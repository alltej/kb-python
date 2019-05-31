SENDING_MORNING_BEGIN = 9
SENDING_EVENING_END = 20


class WorkingHours(object):

    @staticmethod
    def is_working_hours(hour):
        return SENDING_MORNING_BEGIN <= hour < SENDING_EVENING_END

    def is_non_working_hours(self, hour):
        return not self.is_working_hours(hour)
