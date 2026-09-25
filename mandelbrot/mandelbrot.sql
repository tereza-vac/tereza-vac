-- The Mandelbrot set in one recursive CTE.
-- Plain SQLite, no extensions: every pixel and every iteration is a row.
-- Returns one row per pixel: the iteration at which z escaped (or :max_iter) and |z|^2 there.
WITH RECURSIVE
  params(w, h, x0, x1, y0, y1, max_iter) AS (
    SELECT :w, :h, :x0, :x1, :y0, :y1, :max_iter
  ),
  px(i) AS (SELECT 0 UNION ALL SELECT i + 1 FROM px, params WHERE i + 1 < w),
  py(j) AS (SELECT 0 UNION ALL SELECT j + 1 FROM py, params WHERE j + 1 < h),
  z(i, j, cx, cy, x, y, n) AS (
    SELECT i, j,
           x0 + (x1 - x0) * i / (w - 1.0),
           y0 + (y1 - y0) * j / (h - 1.0),
           0.0, 0.0, 0
    FROM px, py, params
    UNION ALL
    -- z_{n+1} = z_n^2 + c
    SELECT i, j, cx, cy, x * x - y * y + cx, 2.0 * x * y + cy, n + 1
    FROM z, params
    WHERE x * x + y * y < 256.0 AND n < max_iter
  )
SELECT i, j, n, x * x + y * y AS r2
FROM z, params
WHERE x * x + y * y >= 256.0 OR n = max_iter;
