#!/bin/python
import random

class Temperature:
    def __init__(self):
        from zeus import ZeusSession
        self._session = ZeusSession()

    def save(self):
        VALUE_MIN = 0.0
        VALUE_MAX = 37.5

        value = random.randrange(360, 370, 1)/10 # set random range 36.0 ~ 37.0

        if value < VALUE_MIN or value >= VALUE_MAX:
            raise Exception(f'Invalid value: {value}')

        self._session.save(
            path='/amc/amcDailyTempRegE/save.do',
            pg_name='AmcDailyTempRegE',
            temp=value,
            sympt_1=False,
            sympt_2=False,
            sympt_3=False,
            sympt_4=False,
            sympt_5=False,
            sympt_6=False,
            spc_ctnt='',
            gubun='AA',
        )


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    Temperature().save()

    print("Checked successfully!")
