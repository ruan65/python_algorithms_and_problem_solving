def norm_str(s: str) -> str:
    return ' '.join(s.split())

if __name__ == '__main__':
    inp = "good       string                   ."
    print(norm_str(inp))