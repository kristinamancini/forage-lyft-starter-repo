from abc import ABC, abstractmethod
from car import Car

class Carfactory(ABC, Car):

  def __init__(self):

  def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car: 
    return self.Car()

  def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car: 
    return self.Car()

  def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car: 
    return self.Car()

  def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage -> Car:  
    return self.Car()

  def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car: 
    return self.Car()