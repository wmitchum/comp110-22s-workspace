def favorite_color(dic: dict[str, str]) -> str:
    """Returns the most common favorite color in a dictionary of names and asociated favorite colors."""
    colors: list = []
    for name in dic:
        colors.append(dic[name])
    i = 1
    x = 0
    while i < len(colors):
        if colors[i] == colors[x]:
            