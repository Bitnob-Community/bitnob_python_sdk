class LNURL:
    def __init__(self,         
        id, 
        tld, 
        identifier, 
        identifier_type, 
        ln_url, 
        ln_url_QR,
        sat_min_sendable,
        sat_max_sendable) -> None:
        self.id = id
        self.tld = tld
        self.identifier = identifier
        self.identifier_type = identifier_type
        self.ln_url = ln_url
        self.ln_url_QR = ln_url_QR
        self.sat_min_sendable = sat_min_sendable
        self.sat_max_sendable = sat_max_sendable