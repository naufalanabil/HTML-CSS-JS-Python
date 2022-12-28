import statistics as st

def mean(data: list) -> float:
    return st.mean(data)

def var(data: list) -> float:
    return st.pvariance(data)

def std(data: list) -> float:
    return st.pstdev(data)

def median(data: list) -> float:
    return st.median(data)