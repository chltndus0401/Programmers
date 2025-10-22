def solution(data, ext, val_ext, sort_by):
    idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext_idx = idx[ext]
    sort_idx = idx[sort_by]
    
    filtered = [d for d in data if d[ext_idx] < val_ext]
    filtered.sort(key=lambda x: x[sort_idx])
    
    return filtered
