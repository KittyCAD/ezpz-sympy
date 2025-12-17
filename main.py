import sympy as sp


def main():
    horizontal_point_line_dist()
    # vertical_point_line_dist()


def horizontal_point_line_dist():
    # Line P
    p = sp.Matrix(sp.symbols("px py", real=True))
    q = sp.Matrix(sp.symbols("qx qy", real=True))
    desired_distance = sp.symbols("d", real=True)
    px = p[0]
    py = p[1]
    qx = q[0]
    qy = q[1]

    # Point A
    a = sp.Matrix(sp.symbols("ax ay", real=True))
    ax = a[0]
    ay = a[1]

    # Slope of line PQ
    actual = ax - ((qx - px) / (qy - py) * (ay - py) + px)
    residual = actual - desired_distance
    s = sp.rust_code(residual)
    print(f"let residual = {s};")
    dpx = sp.rust_code(sp.simplify(residual.diff(px)))
    dpy = sp.rust_code(sp.simplify(residual.diff(py)))
    dqx = sp.rust_code(sp.simplify(residual.diff(qx)))
    dqy = sp.rust_code(sp.simplify(residual.diff(qy)))
    dax = sp.rust_code(sp.simplify(residual.diff(ax)))
    dax = sp.rust_code(sp.simplify(residual.diff(ax)))
    day = sp.rust_code(sp.simplify(residual.diff(ay)))

    print(f"""// Partial derivatives
let dpx = {dpx};
let dpy = {dpy};
let dqx = {dqx};
let dqy = {dqy};
let dax = {dax};
let day = {day};
""")


def vertical_point_line_dist():
    # Line P
    p = sp.Matrix(sp.symbols("px py", real=True))
    q = sp.Matrix(sp.symbols("qx qy", real=True))
    desired_distance = sp.symbols("d", real=True)
    px = p[0]
    py = p[1]
    qx = q[0]
    qy = q[1]

    # Point A
    a = sp.Matrix(sp.symbols("ax ay", real=True))
    ax = a[0]
    ay = a[1]

    # Slope of line PQ
    m = (qy - py) / (qx - px)
    actual = ay - (m * (ax - px) + py)
    residual = actual - desired_distance
    s = sp.rust_code(residual)
    print(f"let residual = {s};")

    dpx = sp.rust_code(sp.simplify(residual.diff(px)))
    dpy = sp.rust_code(sp.simplify(residual.diff(py)))
    dqx = sp.rust_code(sp.simplify(residual.diff(qx)))
    dqy = sp.rust_code(sp.simplify(residual.diff(qy)))
    dax = sp.rust_code(sp.simplify(residual.diff(ax)))
    day = sp.rust_code(sp.simplify(residual.diff(ay)))

    print(f"""// Partial derivatives
let dpx = {dpx};
let dpy = {dpy};
let dqx = {dqx};
let dqy = {dqy};
let dax = {dax};
let day = {day};
""")


if __name__ == "__main__":
    main()
