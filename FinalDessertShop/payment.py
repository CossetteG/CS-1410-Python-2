from typing import Protocol, List, Union, runtime_checkable

@runtime_checkable
class Payable(Protocol):
  legal_values = {"CASH", "CARD", "PHONE"}
  def __init__(self, PayType:str=None in legal_values):
    self.PayType = PayType

  def get_pay_type(self):
    return self.PayType

  def set_pay_type(self, paytype):
    self.PayType = paytype