from template_class import Slot

def set_subject(code_dic, code, subject, freq):
    i = 0
    if freq <= len(code_dic[code]):
        while i < freq:
            if code_dic[code][i].is_empty():
                code_dic[code][i].subject = subject
                code_dic[code][i].status = 1
                i += 1
            else:
                i += 1
                raise Exception("Slot is already taken")
    elif freq > len(code_dic[code]):
        raise Exception (f"There are only {len(code_dic[code])} slots but you want to set {freq}")

def makeTemplate():
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
    dic["Monday"]["L"].append(Slot("J1", 0, ["L21"], 2))      # 3 Means that the slot is should be taken in worst case scenario
    dic["Monday"]["P"].append(Slot("L1", 1, ["A1", "B1"], 0))
    dic["Monday"]["P"].append(Slot("L2", 1, ["C1", "D1"], 0))
    dic["Monday"]["P"].append(Slot("L3", 1, ["E1", "F1"], 0))
    dic["Monday"]["P"].append(Slot("L4", 1, ["G1", "TH12"], 0))
    dic["Monday"]["P"].append(Slot("L21", 1, ["TD12", "J1"], 2))  # 2 means thatt the slo can not be used
    
    # Objects of Tuesday class are created with the following parameters:
    dic["Tuesday"]["L"].append(Slot("I1", 0, ["L5"], 0))
    dic["Tuesday"]["L"].append(Slot("H1", 0, ["L5"], 0))
    dic["Tuesday"]["L"].append(Slot("B1", 0, ["L6"], 0))
    dic["Tuesday"]["L"].append(Slot("A1", 0, ["L6"], 0))
    dic["Tuesday"]["L"].append(Slot("G1", 0, ["L7"], 0))
    dic["Tuesday"]["L"].append(Slot("TE12", 0, ["L7"], 0))
    dic["Tuesday"]["L"].append(Slot("TD11", 0, ["L8"], 0))
    dic["Tuesday"]["L"].append(Slot("TC11", 0, ["L8"], 0))
    dic["Tuesday"]["L"].append(Slot("Student Life", None, ["L22"], 2))
    dic["Tuesday"]["L"].append(Slot("TJ12", 0, ["L22"], 2))
    dic["Tuesday"]["P"].append(Slot("L5", 1, ["I1", "H1"], 0))
    dic["Tuesday"]["P"].append(Slot("L6", 1, ["B1", "A1"], 0))
    dic["Tuesday"]["P"].append(Slot("L7", 1, ["G1", "TE12"], 0))
    dic["Tuesday"]["P"].append(Slot("L8", 1, ["TD11", "TC11"], 0))
    dic["Tuesday"]["P"].append(Slot("L22", 1, ["Student Life", "TJ12"], 2))
    
    # Objects of Wednesday class are created with the following parameters:
    dic["Wednesday"]["L"].append(Slot("B1", 0, ["L9"], 0))
    dic["Wednesday"]["L"].append(Slot("A1", 0, ["L9"], 0))
    dic["Wednesday"]["L"].append(Slot("C1", 0, ["L10"], 0))
    dic["Wednesday"]["L"].append(Slot("D1", 0, ["L10"], 0))
    dic["Wednesday"]["L"].append(Slot("E1", 0, ["L11"], 0))
    dic["Wednesday"]["L"].append(Slot("F1", 0, ["L11"], 0))
    dic["Wednesday"]["L"].append(Slot("TH11", 0, ["L12"], 0))
    dic["Wednesday"]["L"].append(Slot("TI11", 0, ["L12"], 0))
    dic["Wednesday"]["L"].append(Slot("Student Life", 0, ["L23"], 2))
    dic["Wednesday"]["L"].append(Slot("J1", 0, ["L23"], 2))
    dic["Wednesday"]["P"].append(Slot("L9", 1, ["B1", "A1"], 0))
    dic["Wednesday"]["P"].append(Slot("L10", 1, ["C1", "D1"], 0))
    dic["Wednesday"]["P"].append(Slot("L11", 1, ["E1", "F1"], 0))
    dic["Wednesday"]["P"].append(Slot("L12", 1, ["TH11", "TI11"], 0))
    dic["Wednesday"]["P"].append(Slot("L23", 1, ["Student Life", "J1"], 2))
    
    # Objects of Thursday class are created with the following parameters:
    dic["Thursday"]["L"].append(Slot("H1", 0, ["L13"], 0))
    dic["Thursday"]["L"].append(Slot("I1", 0, ["L13"], 0))
    dic["Thursday"]["L"].append(Slot("G1", 0, ["L14"], 0))
    dic["Thursday"]["L"].append(Slot("TC12", 0, ["L14"], 0))
    dic["Thursday"]["L"].append(Slot("TE11", 0, ["L15"], 0))
    dic["Thursday"]["L"].append(Slot("TF11", 0, ["L15"], 0))
    dic["Thursday"]["L"].append(Slot("TB12", 0, ["L16"], 0))
    dic["Thursday"]["L"].append(Slot("TA12", 0, ["L16"], 0))
    dic["Thursday"]["L"].append(Slot("Student Life", 0, ["L24"], 2))
    dic["Thursday"]["L"].append(Slot("TJ11", 0, ["L24"], 2))
    dic["Thursday"]["P"].append(Slot("L13", 1, ["H1", "I1"], 0))
    dic["Thursday"]["P"].append(Slot("L14", 1, ["G1", "TC12"], 0))
    dic["Thursday"]["P"].append(Slot("L15", 1, ["TE11", "TF11"], 0))
    dic["Thursday"]["P"].append(Slot("L16", 1, ["TB12", "TA12"], 0))
    dic["Thursday"]["P"].append(Slot("L24", 1, ["Student Life", "TJ11"], 2))
    
    # Objects of Friday class are created with the following parameters:
    dic["Friday"]["L"].append(Slot("H1", 0, ["L17"], 0))
    dic["Friday"]["L"].append(Slot("I1", 0, ["L17"], 0))
    dic["Friday"]["L"].append(Slot("D1", 0, ["L18"], 0))
    dic["Friday"]["L"].append(Slot("C1", 0, ["L18"], 0))
    dic["Friday"]["L"].append(Slot("E1", 0, ["L19"], 0))
    dic["Friday"]["L"].append(Slot("F1", 0, ["L19"], 0))
    dic["Friday"]["L"].append(Slot("TA11", 0, ["L20"], 0))
    dic["Friday"]["L"].append(Slot("TB11", 0, ["L20"], 0))
    dic["Friday"]["L"].append(Slot("Student Life", 0, ["L25"], 2))
    dic["Friday"]["L"].append(Slot("J1", 0, ["L25"], 2))
    dic["Friday"]["P"].append(Slot("L17", 1, ["H1", "I1"], 0))
    dic["Friday"]["P"].append(Slot("L18", 1, ["D1", "C1"], 0))
    dic["Friday"]["P"].append(Slot("L19", 1, ["E1", "F1"], 0))
    dic["Friday"]["P"].append(Slot("L20", 1, ["TA11", "TB11"], 0))
    dic["Friday"]["P"].append(Slot("L25", 1, ["Student Life", "J1"], 2))
    
    code_dic = {
        # Theory
        "A1":(dic["Monday"]["L"][0], dic["Tuesday"]["L"][3], dic["Wednesday"]["L"][1]),
        "B1":(dic["Monday"]["L"][1], dic["Tuesday"]["L"][2], dic["Wednesday"]["L"][0]),
        "C1":(dic["Monday"]["L"][2], dic["Wednesday"]["L"][2], dic["Friday"]["L"][3]),
        "D1":(dic["Monday"]["L"][3], dic["Wednesday"]["L"][3], dic["Friday"]["L"][2]),
        "E1":(dic["Monday"]["L"][4], dic["Wednesday"]["L"][4], dic["Friday"]["L"][4]),
        "F1":(dic["Monday"]["L"][5], dic["Wednesday"]["L"][5], dic["Friday"]["L"][5]),
        "G1":(dic["Monday"]["L"][6], dic["Tuesday"]["L"][4], dic["Thursday"]["L"][2]),
        
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
    
    return (dic, code_dic)