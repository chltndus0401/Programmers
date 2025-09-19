def to_seconds(t):
    mm, ss = map(int, t.split(":"))
    return mm * 60 + ss

def to_mmss(seconds):
    mm = seconds // 60
    ss = seconds % 60
    return f"{mm:02d}:{ss:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    if op_start <= pos <= op_end:
        pos = op_end

    for cmd in commands:
        if cmd == "prev":
            pos = max(0, pos - 10)
        elif cmd == "next":
            pos = min(video_len, pos + 10)

        if op_start <= pos <= op_end:
            pos = op_end

    return to_mmss(pos)
