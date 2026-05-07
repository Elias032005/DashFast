SELECT
    pt.name AS producto,
    sol.product_uom_qty AS cantidad,
    sol.price_unit AS precio_unitario,
    sol.price_subtotal AS total_venta,
    so.date_order AS fecha_venta
FROM sale_order_line sol
JOIN sale_order so
    ON so.id = sol.order_id
JOIN product_product pp
    ON pp.id = sol.product_id
JOIN product_template pt
    ON pt.id = pp.product_tmpl_id
JOIN product_supplierinfo psi
    ON psi.product_tmpl_id = pt.id
   AND (psi.product_id IS NULL OR psi.product_id = pp.id)
JOIN res_partner rp
    ON rp.id = psi.partner_id
WHERE rp.id = 31
  AND so.date_order::date >= '2026-01-01'
  AND so.date_order::date <= '2026-05-22'
ORDER BY so.date_order DESC;