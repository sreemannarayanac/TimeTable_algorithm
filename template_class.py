class Slot:
    
    def __init__(self, code, slot_type, rel_code, status):
        self.code = code
        self.slot_type = slot_type  # 0 means that the slot is Theory Type, 1 means that the slot is Practical Type
        self.rel_code = rel_code
        self.status = status  # 0 means that the slot is available, 1 means that the slot is taken
        self.subject = None
    
    def is_empty(self) -> bool:
        """Defines the status of a slot"""
        if self.status == 0:
            return True
        return False
    
    def __str__(self):
        return f"code = {self.code}\nslot_type = {self.slot_type}\nrel_code = {self.rel_code}\nstatus = {self.status}"
    
    def __repr__(self):
        return f"({self.code}, {self.slot_type}, {self.rel_code}, {self.status})"