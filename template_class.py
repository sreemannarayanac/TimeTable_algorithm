class Slot:
    
    def __init__(self, code, slot_type, rel_code, status):
        self.code = code
        self.slot_type = slot_type  # zero means that the slot is Theory Type and one means that the slot is Practical Type
        self.rel_code = rel_code
        self.status = status  # zero means that the slot is available and one means that the slot is taken
        self.subject = None
    
    def is_empty(self):
        if self.status == 0:
            return True
        return False
    
    def __str__(self):
        return f"code = {self.code}\nslot_type = {self.slot_type}\nrel_code = {self.rel_code}\nstatus = {self.status}"
    
    def __repr__(self):
        return f"({self.code}, {self.slot_type}, {self.rel_code}, {self.status})"