from template_class import Slot

def check_slot(code_dic: dict, slot: object):
    """Takes in two arguments code_dic and slot.\n"""
    #? This function is used to check weather the related slot is free, if free returns True and sets status of related slot to 1
    res = None
    for rel_code in slot.rel_code:
        for slot in code_dic[rel_code]:
            if slot.is_empty():
                res = True
                slot.status = 1
            else:
                res = False
                break
    return res

def set_subject(code_dic: dict, code: str, subject: str, freq: int):
    """Takes in four arguments code_dic, code, subject and frequency(no. of slots required).\n
    code_dic is the code dictionary from the template.\n
    code is the code in which you want to set the subject.\n
    subject is the subject you want to set.\n
    freq is the frequency of the subject you want to set.
    """
    i = 0
    if freq <= len(code_dic[code]):
        while i < freq:
            if code_dic[code][i].is_empty():
                if check_slot(code_dic, code_dic[code][i]):
                    code_dic[code][i].subject = subject
                    code_dic[code][i].status = 1
                    i += 1
                else:
                    i += 1
                    raise Exception("Related Slot is not empty")
            else:
                i += 1
                raise Exception("Slot is already taken")
    elif freq > len(code_dic[code]):
        raise Exception (f"There are only {len(code_dic[code])} slots but you want to set {freq}")

def set_lunch(code_dic: dict, option: int):   #todo: add security layer by ensuring that there is only one lunch slot chosen
    """Takes in two arguments code_dic and option.\n
    Option is of int type and takes in either 1 or 2 as input.\n
    1 is for lunch time 12:00 to 12:50 and 
    2 is for lunch time 13:00 to 13:50"""
    if option == 1 or option == 2:
        if option == 1:
            for slot in code_dic["E1"]:
                slot.subject = "Lunch"
                slot.status = 1
            code_dic["G1"][1].subject, code_dic["G1"][1].status = "Lunch", 1
            code_dic["TE"][1].subject, code_dic["TE"][1].status = "Lunch", 1
        elif option == 2:
            for slot in code_dic["F1"]:
                slot.subject = "Lunch"
                slot.status = 1
            code_dic["TE"][0].subject, code_dic["TE"][0].status = "Lunch", 1
            code_dic["TF"][0].subject, code_dic["TF"][0].status = "Lunch", 1
        code_dic["L3"][0].status = 1
        code_dic["L7"][0].status = 1
        code_dic["L11"][0].status = 1
        code_dic["L15"][0].status = 1
        code_dic["L19"][0].status = 1
    else:
        raise Exception("Invalid option")

def makeTemplate():
    """This function needs zero arguments and creates two template dictionary.\n
    one template is day wise and the other is code wise.\n
    this function returns both the template dictionary.\n
    output: (template_dic, code_dic)"""
    
    # Default structure 
    dic = {"Monday":{"L":[], "P":[]}, "Tuesday":{"L":[], "P":[]}, "Wednesday":{"L":[], "P":[]}, "Thursday":{"L":[], "P":[]}, "Friday":{"L":[], "P":[]}}
    
    # Objects of Monday class are created with the following parameters:
    dic["Monday"]["L"].append(Slot("A1", 0, ["L1"], 0))  
    dic["Monday"]["L"].append(Slot("B1", 0, ["L1"], 0))
    dic["Monday"]["L"].append(Slot("C1", 0, ["L2"], 0))
    dic["Monday"]["L"].append(Slot("D1", 0, ["L2"], 0))
    dic["Monday"]["L"].append(Slot("E1", 0, ["L3"], 0))
    dic["Monday"]["L"].append(Slot("F1", 0, ["L3"], 0))
    dic["Monday"]["L"].append(Slot("G1", 0, ["L4"], 0))
    dic["Monday"]["L"].append(Slot("TH12", 0, ["L4"], 0))
    dic["Monday"]["L"].append(Slot("TD12", 0, ["L21"], 0))
    dic["Monday"]["L"].append(Slot("J1", 0, ["L21"], 0))      
    dic["Monday"]["P"].append(Slot("L1", 1, ["A1", "B1"], 0))
    dic["Monday"]["P"].append(Slot("L2", 1, ["C1", "D1"], 0))
    dic["Monday"]["P"].append(Slot("L3", 1, ["E1", "F1"], 0))
    dic["Monday"]["P"].append(Slot("L4", 1, ["G1", "TH12"], 0))
    dic["Monday"]["P"].append(Slot("L21", 1, ["TD12", "J1"], 0))  
    
    # Objects of Tuesday class are created with the following parameters:
    dic["Tuesday"]["L"].append(Slot("I1", 0, ["L5"], 0))
    dic["Tuesday"]["L"].append(Slot("H1", 0, ["L5"], 0))
    dic["Tuesday"]["L"].append(Slot("B1", 0, ["L6"], 0))
    dic["Tuesday"]["L"].append(Slot("A1", 0, ["L6"], 0))
    dic["Tuesday"]["L"].append(Slot("G1", 0, ["L7"], 0))
    dic["Tuesday"]["L"].append(Slot("TE12", 0, ["L7"], 0))
    dic["Tuesday"]["L"].append(Slot("TD11", 0, ["L8"], 0))
    dic["Tuesday"]["L"].append(Slot("TC11", 0, ["L8"], 0))
    dic["Tuesday"]["L"].append(Slot("Student Life", None, ["L22"], 0))
    dic["Tuesday"]["L"].append(Slot("TJ12", 0, ["L22"], 0))
    dic["Tuesday"]["P"].append(Slot("L5", 1, ["I1", "H1"], 0))
    dic["Tuesday"]["P"].append(Slot("L6", 1, ["B1", "A1"], 0))
    dic["Tuesday"]["P"].append(Slot("L7", 1, ["G1", "TE12"], 0))
    dic["Tuesday"]["P"].append(Slot("L8", 1, ["TD11", "TC11"], 0))
    dic["Tuesday"]["P"].append(Slot("L22", 1, ["Student Life", "TJ12"], 0))
    
    # Objects of Wednesday class are created with the following parameters:
    dic["Wednesday"]["L"].append(Slot("B1", 0, ["L9"], 0))
    dic["Wednesday"]["L"].append(Slot("A1", 0, ["L9"], 0))
    dic["Wednesday"]["L"].append(Slot("C1", 0, ["L10"], 0))
    dic["Wednesday"]["L"].append(Slot("D1", 0, ["L10"], 0))
    dic["Wednesday"]["L"].append(Slot("E1", 0, ["L11"], 0))
    dic["Wednesday"]["L"].append(Slot("F1", 0, ["L11"], 0))
    dic["Wednesday"]["L"].append(Slot("TH11", 0, ["L12"], 0))
    dic["Wednesday"]["L"].append(Slot("TI11", 0, ["L12"], 0))
    dic["Wednesday"]["L"].append(Slot("Student Life", None, ["L23"], 0))
    dic["Wednesday"]["L"].append(Slot("J1", 0, ["L23"], 0))
    dic["Wednesday"]["P"].append(Slot("L9", 1, ["B1", "A1"], 0))
    dic["Wednesday"]["P"].append(Slot("L10", 1, ["C1", "D1"], 0))
    dic["Wednesday"]["P"].append(Slot("L11", 1, ["E1", "F1"], 0))
    dic["Wednesday"]["P"].append(Slot("L12", 1, ["TH11", "TI11"], 0))
    dic["Wednesday"]["P"].append(Slot("L23", 1, ["Student Life", "J1"], 0))
    
    # Objects of Thursday class are created with the following parameters:
    dic["Thursday"]["L"].append(Slot("H1", 0, ["L13"], 0))
    dic["Thursday"]["L"].append(Slot("I1", 0, ["L13"], 0))
    dic["Thursday"]["L"].append(Slot("G1", 0, ["L14"], 0))
    dic["Thursday"]["L"].append(Slot("TC12", 0, ["L14"], 0))
    dic["Thursday"]["L"].append(Slot("TE11", 0, ["L15"], 0))
    dic["Thursday"]["L"].append(Slot("TF11", 0, ["L15"], 0))
    dic["Thursday"]["L"].append(Slot("TB12", 0, ["L16"], 0))
    dic["Thursday"]["L"].append(Slot("TA12", 0, ["L16"], 0))
    dic["Thursday"]["L"].append(Slot("Student Life", None, ["L24"], 0))
    dic["Thursday"]["L"].append(Slot("TJ11", 0, ["L24"], 0))
    dic["Thursday"]["P"].append(Slot("L13", 1, ["H1", "I1"], 0))
    dic["Thursday"]["P"].append(Slot("L14", 1, ["G1", "TC12"], 0))
    dic["Thursday"]["P"].append(Slot("L15", 1, ["TE11", "TF11"], 0))
    dic["Thursday"]["P"].append(Slot("L16", 1, ["TB12", "TA12"], 0))
    dic["Thursday"]["P"].append(Slot("L24", 1, ["Student Life", "TJ11"], 0))
    
    # Objects of Friday class are created with the following parameters:
    dic["Friday"]["L"].append(Slot("H1", 0, ["L17"], 0))
    dic["Friday"]["L"].append(Slot("I1", 0, ["L17"], 0))
    dic["Friday"]["L"].append(Slot("D1", 0, ["L18"], 0))
    dic["Friday"]["L"].append(Slot("C1", 0, ["L18"], 0))
    dic["Friday"]["L"].append(Slot("E1", 0, ["L19"], 0))
    dic["Friday"]["L"].append(Slot("F1", 0, ["L19"], 0))
    dic["Friday"]["L"].append(Slot("TA11", 0, ["L20"], 0))
    dic["Friday"]["L"].append(Slot("TB11", 0, ["L20"], 0))
    dic["Friday"]["L"].append(Slot("Student Life", None, ["L25"], 0))
    dic["Friday"]["L"].append(Slot("J1", 0, ["L25"], 0))
    dic["Friday"]["P"].append(Slot("L17", 1, ["H1", "I1"], 0))
    dic["Friday"]["P"].append(Slot("L18", 1, ["D1", "C1"], 0))
    dic["Friday"]["P"].append(Slot("L19", 1, ["E1", "F1"], 0))
    dic["Friday"]["P"].append(Slot("L20", 1, ["TA11", "TB11"], 0))
    dic["Friday"]["P"].append(Slot("L25", 1, ["Student Life", "J1"], 0))
    
    code_dic = {
        # Theory
        "A1":(dic["Monday"]["L"][0], dic["Tuesday"]["L"][3], dic["Wednesday"]["L"][1]),
        "B1":(dic["Monday"]["L"][1], dic["Tuesday"]["L"][2], dic["Wednesday"]["L"][0]),
        "C1":(dic["Monday"]["L"][2], dic["Wednesday"]["L"][2], dic["Friday"]["L"][3]),
        "D1":(dic["Monday"]["L"][3], dic["Wednesday"]["L"][3], dic["Friday"]["L"][2]),
        "E1":(dic["Monday"]["L"][4], dic["Wednesday"]["L"][4], dic["Friday"]["L"][4]),
        "F1":(dic["Monday"]["L"][5], dic["Wednesday"]["L"][5], dic["Friday"]["L"][5]),
        "G1":(dic["Monday"]["L"][6], dic["Tuesday"]["L"][4], dic["Thursday"]["L"][2]),
        "H1":(dic["Tuesday"]["L"][1], dic["Thursday"]["L"][0], dic["Friday"]["L"][0]),
        "I1":(dic["Tuesday"]["L"][0], dic["Thursday"]["L"][1], dic["Friday"]["L"][1]),
        
        "TA":(dic["Thursday"]["L"][7], dic["Friday"]["L"][6]),
        "TB":(dic["Thursday"]["L"][6], dic["Friday"]["L"][7]),
        "TC":(dic["Tuesday"]["L"][7], dic["Thursday"]["L"][3]),
        "TD":(dic["Monday"]["L"][8], dic["Tuesday"]["L"][6]),
        "TE":(dic["Tuesday"]["L"][5], dic["Thursday"]["L"][4]),
        "TF":(dic["Thursday"]["L"][5], ),
        "TH":(dic["Monday"]["L"][7], dic["Wednesday"]["L"][6]),
        "TI":(dic["Wednesday"]["L"][7], ),
        #Labs
        "L1":(dic["Monday"]["P"][0], ),
        "L2":(dic["Monday"]["P"][1], ),
        "L3":(dic["Monday"]["P"][2], ),
        "L4":(dic["Monday"]["P"][3], ),
        "L21":(dic["Monday"]["P"][4], ),
        
        "L5":(dic["Tuesday"]["P"][0], ),
        "L6":(dic["Tuesday"]["P"][1], ),
        "L7":(dic["Tuesday"]["P"][2], ),
        "L8":(dic["Tuesday"]["P"][3], ),
        "L22":(dic["Tuesday"]["P"][4], ),
        
        "L9":(dic["Wednesday"]["P"][0], ),
        "L10":(dic["Wednesday"]["P"][1], ),
        "L11":(dic["Wednesday"]["P"][2], ),
        "L12":(dic["Wednesday"]["P"][3], ),
        "L23":(dic["Wednesday"]["P"][4], ),
        
        "L13":(dic["Thursday"]["P"][0], ),
        "L14":(dic["Thursday"]["P"][1], ),
        "L15":(dic["Thursday"]["P"][2], ),
        "L16":(dic["Thursday"]["P"][3], ),
        "L24":(dic["Thursday"]["P"][4], ),
        
        "L17":(dic["Friday"]["P"][0], ),
        "L18":(dic["Friday"]["P"][1], ),
        "L19":(dic["Friday"]["P"][2], ),
        "L20":(dic["Friday"]["P"][3], ),
        "L25":(dic["Friday"]["P"][4], ),
        }
    
    filled_codes = {
        "A1":(),
        "B1":(),
        "C1":(),
        "D1":(),
        "E1":(),
        "F1":(),
        "G1":(),
        "H1":(),
        "I1":(),
        
        "TA":(),
        "TB":(),
        "TC":(),
        "TD":(),
        "TE":(),
        "TF":(),
        "TH":(),
        "TI":(),
        #Labs
        "L1":(),
        "L2":(),
        "L3":(),
        "L4":(),
        "L21":(),
        
        "L5":(),
        "L6":(),
        "L7":(),
        "L8":(),
        "L22":(),
        
        "L9":(),
        "L10":(),
        "L11":(),
        "L12":(),
        "L23":(),
        
        "L13":(),
        "L14":(),
        "L15":(),
        "L16":(),
        "L24":(),
        
        "L17":(),
        "L18":(),
        "L19":(),
        "L20":(),
        "L25":(),
    }
    
    return (dic, code_dic, filled_codes)