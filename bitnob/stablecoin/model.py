class Receipt:
    def __init__(self, id, reference, description, amount, fees, action, receipt_type, status) -> None:
        self.reference =reference
        self.description = description
        self.amount = amount
        self.fees = fees
        self.action = action
        self.receipt_type = receipt_type
        self.status = status
        self.id=id
    
    @property
    def cent_amount(self):
        self.amount * 100
    
    @property
    def cent_fees(self):
        self.fees * 100
    
    @property
    def total_amount(self):
        """
        Total amount debited from user
        """
        return self.amount + self.fees
    
    @property
    def total_cents(self):
        """
        Total cents debited from user
        """
        return self.centAmount + self.centFees