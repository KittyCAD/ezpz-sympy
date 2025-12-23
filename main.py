import sympy as sp
from sympy.plotting import plot


def main():
    arc_len()
    # point_arc_coincident_ang()
    # horizontal_point_line_dist()
    # vertical_point_line_dist()


def arc_len():
    # Start of arc
    a = sp.Matrix(sp.symbols("ax ay", real=True))
    # End of arc
    b = sp.Matrix(sp.symbols("bx by", real=True))
    # Center of arc
    c = sp.Matrix(sp.symbols("cx cy", real=True))
    # Desired arc length distance
    d = sp.symbols("d", real=True)

    u = a - c
    v = b - c
    ux = u[0]
    uy = u[1]
    vx = v[0]
    vy = v[1]

    r = u.norm()
    r2 = r**2

    cos_theta = u.dot(v) / r2
    sin_theta = (ux * vy - uy * vx) / r2
    # Target angle
    alpha = d / r

    # Residuals
    res0 = cos_theta - sp.cos(alpha)
    res1 = sin_theta - sp.sin(alpha)

    test_rad = 5
    test_satisfied = res0.subs(
        {
            # theta = 0
            a[0]: test_rad,
            a[1]: 0,
            # theta = 90deg
            b[0]: 0,
            b[1]: test_rad,
            # center = origin
            c[0]: 0,
            c[1]: 0,
            # distance = 1/4 circle
            d: 2 * sp.pi * test_rad / 4,
        }
    )

    # print("test_satisfied:", test_satisfied)
    # print("test_satisfied:", test_satisfied.evalf())
    assert test_satisfied.evalf() == 0

    # print(f"let res0 = {sp.rust_code(res0)};")
    # print(f"let res1 = {sp.rust_code(res1)};")
    print(f"let r0dax = {sp.rust_code(sp.simplify(res0.diff(a[0])))};")
    print(f"let r0day = {sp.rust_code(sp.simplify(res0.diff(a[1])))};")
    print(f"let r0dbx = {sp.rust_code(sp.simplify(res0.diff(b[0])))};")
    print(f"let r0dby = {sp.rust_code(sp.simplify(res0.diff(b[1])))};")
    print(f"let r0dcx = {sp.rust_code(sp.simplify(res0.diff(c[0])))};")
    print(f"let r0dcy = {sp.rust_code(sp.simplify(res0.diff(c[1])))};")
    print(f"let r1dax = {sp.rust_code(sp.simplify(res1.diff(a[0])))};")
    print(f"let r1day = {sp.rust_code(sp.simplify(res1.diff(a[1])))};")
    print(f"let r1dbx = {sp.rust_code(sp.simplify(res1.diff(b[0])))};")
    print(f"let r1dby = {sp.rust_code(sp.simplify(res1.diff(b[1])))};")
    print(f"let r1dcx = {sp.rust_code(sp.simplify(res1.diff(c[0])))};")
    print(f"let r1dcy = {sp.rust_code(sp.simplify(res1.diff(c[1])))};")


def cross2(u, v):
    """Return the scalar z-component of the 2D cross product."""
    return u[0] * v[1] - u[1] * v[0]


def point_arc_coincident_ang():
    # The arc (a = start, b = end, counterclockwise from A to B)
    c = sp.Matrix(sp.symbols("cx cy", real=True))
    a = sp.Matrix(sp.symbols("ax ay", real=True))
    b = sp.Matrix(sp.symbols("bx by", real=True))

    p = sp.Matrix(sp.symbols("px py", real=True))
    px = p[0]
    py = p[1]
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    cx = c[0]
    cy = c[1]

    ua = a - c
    ub = b - c
    up = p - c

    res1 = sp.Min(0, cross2(ua, up))
    res2 = sp.Min(0, cross2(up, ub))

    r1dpx = sp.rust_code(sp.simplify(res1.diff(px)))
    r1dpy = sp.rust_code(sp.simplify(res1.diff(py)))
    r1dax = sp.rust_code(sp.simplify(res1.diff(ax)))
    r1day = sp.rust_code(sp.simplify(res1.diff(ay)))
    r1dbx = sp.rust_code(sp.simplify(res1.diff(bx)))
    r1dby = sp.rust_code(sp.simplify(res1.diff(by)))
    r1dcx = sp.rust_code(sp.simplify(res1.diff(cx)))
    r1dcy = sp.rust_code(sp.simplify(res1.diff(cy)))
    print(f"let residual1 = {sp.rust_code(res1)}")
    print(f"""// Partial derivatives, res1
let r1dpx = {r1dpx};
let r1dpy = {r1dpy};
let r1dax = {r1dax};
let r1day = {r1day};
let r1dbx = {r1dbx};
let r1dby = {r1dby};
let r1dcx = {r1dcx};
let r1dcy = {r1dcy};
""")
    print("\n\n\n\n\n")
    r2dpx = sp.rust_code(sp.simplify(res2.diff(px)))
    r2dpy = sp.rust_code(sp.simplify(res2.diff(py)))
    r2dax = sp.rust_code(sp.simplify(res2.diff(ax)))
    r2day = sp.rust_code(sp.simplify(res2.diff(ay)))
    r2dbx = sp.rust_code(sp.simplify(res2.diff(bx)))
    r2dby = sp.rust_code(sp.simplify(res2.diff(by)))
    r2dcx = sp.rust_code(sp.simplify(res2.diff(cx)))
    r2dcy = sp.rust_code(sp.simplify(res2.diff(cy)))
    print(f"let residual2 = {sp.rust_code(res2)}")
    print(f"""// Partial derivatives, res2
let r2dpx = {r2dpx};
let r2dpy = {r2dpy};
let _r2dax = {r2dax};
let _r2day = {r2day};
let r2dbx = {r2dbx};
let r2dby = {r2dby};
let r2dcx = {r2dcx};
let r2dcy = {r2dcy};
""")

    # print("residual 2: ", sp.rust_code(res2))


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
