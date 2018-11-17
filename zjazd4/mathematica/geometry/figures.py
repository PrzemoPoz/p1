def square_area(bok):
    try: bok*1
    except: "błędna długość boku"
    pole=bok**2
    return pole

def triangle_area(podstawa, wysokość):
    pole=0.5*podstawa*wysokość
    return pole
