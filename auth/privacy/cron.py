import logging
logger=logging.getLogger(__name__)
from .models import Test


def print_hello():
   print("Hello ")
   logger.info("cron job was called")



def my_job():
    Test.objects.create(name='test')
  