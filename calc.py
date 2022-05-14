def selectScore(file_id):
    diya10 = 'AAJzIwABS-8-TM_e_0odJAQ'
    diya10_ = 'AC3xYAAnMjAAFL7z5Mz97_Sh0kBA'
    diya_10 = 'AAjUaAALA5gFLwQgAAfYKD5E3JAQ'
    diya_10_ = 'AAI1GgACwOYBS8EIAAH2Cg-RNyQE'
    diya50 = 'AAuoaAALtCQABS6Saypb4VxtBJAQ'
    diya50_ = 'AC6hoAAu0JAAFLpJrKlvhXG0EkBA'
    diya_50 = 'AAp0aAALlSQhL1IMSch6huYckBA'
    diya_50_ = 'RoAAuVJCEvUgxJyHqG5hyQE'
    diya100 = 'AAogZAAL4uAABS9XM19IputVDJAQ'
    diya100_ = 'AAKIGQAC-LgAAUvVzNfSKbrVQyQE'
    diya_100 = 'AArAcAAKerAABSyRS4t1TZgE5JAQ'
    diya_100_ = 'ACsBwAAp6sAAFLJFLi3VNmATkkBA'
    if file_id.count(diya10) or file_id.count(diya10_) != 0:
        return 10
    elif file_id.count(diya_10) or file_id.count(diya_10_) != 0:
        return -10
    elif file_id.count(diya50) or file_id.count(diya50_) != 0:
        return 50
    elif file_id.count(diya_50) or file_id.count(diya_50_) != 0:
        return -50
    elif file_id.count(diya100) or file_id.count(diya100_) != 0:
        return 100
    elif file_id.count(diya_100) or file_id.count(diya_100_) != 0:
        return -100
